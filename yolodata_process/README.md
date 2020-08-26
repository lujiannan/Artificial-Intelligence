Info:
The files included in this directory is used to create datas that yolo4 train needs.
-kmeans data
-yolo: train data
-anchor data

Tools:
Pycharm

Instruction:
cocoapi folder must be included and used, make sure you see this folder in yolov4-keras!!!!
-use labelme to label and get json files, store both images and their jason(annotated) files in folder 'A'
-change the annotations' name in labels.txt
-windows+R, type in cmd
 enter the 'yolodata_process' directory
 type in 'python (address of 'labelme2coco.py') (address of images and annotated files(folder 'B')) (address of saving
	converted coco_datas) --labels (address of labels.txt)
-correct and run create_anchor.py
-based on numbers of annotations, run coco2kmeans_xcategs.py, and coco2yolo_xcategs.py
-finally there should be (5)'train.txt', 'kmeansdata.txt', 'saved_anchor.txt', 'annotations.json', and folder 'JPEGImages'
 in folder 'B'