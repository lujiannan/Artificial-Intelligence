"""

Given a set of specific objects, use trained model to predict the labels for object 'a' and object 'b'

variables needs to be set before run:
'savedFile': refers to the number of frames within a video, and refers to the names of the labelled and saved frames
'framesFrequency': refers to how frequently taking frames of the video is
'outPutDirName': refers to what directory you want to save your snipped frames into
'****'(cap = cv2.VideoCapture('****')): refers to where your unprocessed video located

"""


# coding: utf-8
import base64
import json
import time
import os
import io
import PIL.Image
from labelme.logger import logger
from labelme import PY2
from labelme import QT4
from labelme import utils
import os.path as osp
from yolo import YOLO
from PIL import Image
import cv2
import numpy as np

yolo = YOLO()


outPutDirName = r"C:\Users\Administrator\Desktop\new_frames_labelled\\"
# 计帧
savedFile = 33000
# 多少帧写入一次图片
framesFrequency = 15
# label坐标集
coord_set = []
# label名集me
label_set = ['a', 'b']


if not os.path.exists(outPutDirName):
    # 如果文件目录不存在则创建目录
    os.makedirs(outPutDirName)


cap = cv2.VideoCapture('./model_data/test_nails_0728_3.mp4')

while cap.isOpened():
    # 计帧
    savedFile += 1
    normal_list = []
    # image是numpy.ndarray類型
    ret, image = cap.read()
    if not ret:
        break

    if (savedFile - 20000) % framesFrequency == 0:
        # 预设
        label_json = {}
        savedJsonName = str(savedFile) + '.json'
        savedImgName = str(savedFile) + '.jpg'

        # 输出图片
        cv2.imwrite(outPutDirName + savedImgName, image)

        # 输出binding box坐标
        image_yo = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_yo = Image.fromarray(image_yo)
        r_image, coord_set, _ = yolo.detect_image(image_yo, normal_list)
        print(coord_set)

        # 如果输入的图片没有预测出物体，不生成json文件并开始处理下一个图片
        if not coord_set:
            continue

        # 输出json打标文件，f.read可以用imgbytearray.getvalue代替
        with open(outPutDirName + savedImgName, "rb") as f:  # 转为二进制格式
            image_data = base64.b64encode(f.read()).decode("utf-8")  # 使用base64进行加密
            # print(image_data)
        label_json = {"version": "4.5.5", "flags": {}, "shapes": [],
                      "imagePath": savedImgName, "imageData": image_data,
                      "imageHeight": 720, "imageWidth": 720}
        points1 = []
        points2 = []
        points1.clear()
        points2.clear()
        if coord_set[0][4] == 'a':
            for i in range(2):
                points1.append([float(coord_set[0][2 * i]), float(coord_set[0][2 * i + 1])])
            shape1 = {"label": label_set[0], "points": points1, "group_id": None, "shape_type": "rectangle",
                      "flags": {}}
            label_json["shapes"].append(shape1)
            if len(coord_set) != 1 and coord_set[1][4] == 'b':
                for i in range(2):
                    points2.append([float(coord_set[1][2 * i]), float(coord_set[1][2 * i + 1])])
                shape2 = {"label": label_set[1], "points": points2, "group_id": None, "shape_type": "rectangle",
                          "flags": {}}
                label_json["shapes"].append(shape2)

        if coord_set[0][4] == 'b':
            for i in range(2):
                points2.append([float(coord_set[0][2 * i]), float(coord_set[0][2 * i + 1])])
            shape2 = {"label": label_set[1], "points": points2, "group_id": None, "shape_type": "rectangle",
                      "flags": {}}
            label_json["shapes"].append(shape2)

        with open(os.path.join(outPutDirName, savedJsonName), 'w') as fd:
            json.dump(label_json, fd)
        label_json.clear()
        print(savedJsonName)

        img = cv2.cvtColor(np.asarray(r_image), cv2.COLOR_BGR2RGB)
        cv2.namedWindow("video", flags=False)
        cv2.imshow("video", img)
        cv2.waitKey(1)
yolo.close_session()
