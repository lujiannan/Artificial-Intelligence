import coremltools as ct
import numpy as np
import tensorflow as tf

path = r"C:\Users\Administrator\Desktop\yolov4-keras_stapler\pb\saved_model.pb"

# Load the protobuf file from the disk and parse it to retrieve the
# graph_def
with tf.io.gfile.GFile(path, "rb") as f:
    graph_def = tf.compat.v1.GraphDef()
    graph_def.ParseFromString(f.read())

# Import the graph_def into a new Graph
with tf.Graph().as_default() as graph:
    tf.import_graph_def(graph_def, name="")

ops = graph.get_operations()
N = len(ops)
# print all the placeholder ops, these would be the inputs
print("Inputs ops: ")
for op in ops:
    if op.type == "Placeholder":
        print("op name: {}, output shape : {}".
              format(op.name, op.outputs[0].get_shape()))


# print all the tensors that are the first output of an op
# and do not feed into any other op
# these are prospective outputs
print("\nProspective output tensor(s): ", )
sink_ops = []
input_tensors = set()
for op in ops:
    for x in op.inputs:
        if x.name not in input_tensors:
            input_tensors.add(x.name)
for op in ops:
    if len(op.outputs) > 0:
        x = op.outputs[0]
        if x.name not in input_tensors:
            print("tensor name: {}, tensor shape : {}, parent op type: {}"
                  .format(x.name, x.get_shape(), op.type))

x = np.random.rand(1, 224, 224, 3)

with tf.Session(graph = graph) as sess:
    tf_out = sess.run('MobilenetV2/Predictions/Reshape_1:0',
                      feed_dict={'input:0': x})
mlmodel = ct.convert(graph,
                     inputs=[ct.TensorType(shape=x.shape)])

# Core ML model prediction
coreml_out_dict = mlmodel.predict({"input" : x}, useCPUOnly=True)
coreml_out = list(coreml_out_dict.values())[0]
np.testing.assert_allclose(tf_out, coreml_out, rtol=1e-3, atol=1e-2)