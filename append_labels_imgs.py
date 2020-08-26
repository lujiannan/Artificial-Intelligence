"""

justify the default values, especially model in yolo.py, do not try to modify this file!!!!
if you need the appending label to be x, then modify model loaded in yolo.py, let it be x

This file mainly process the condition that you only have two labels for an image in a json file, and you have the model
trained for the third and only the third label, you have to append the third label to the json file

variable that needs to be altered before running:
'outer_path': where you want to save your processed image and labelled(json) file
'label_set': should be exactly the same as the labels used in train.py/trained models

if you changed names in label_set, make sure all the same ones below are changed too

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

outer_path = r"C:\Users\Administrator\Desktop\stapler_total_tmp\\"
imgtype = '.jpg'
labeltype = '.json'


def get_filename(outer_path, imgtype, labeltype):
    imgname = []
    labelname = []
    for root, dirs, files in os.walk(outer_path):
        for i in files:
            if imgtype in i:
                imgname.append(i.replace(imgtype, ''))  # 生成不带后缀的文件名组成的列表
            elif labeltype in i:
                labelname.append(i.replace(labeltype, ''))
    final_imgs = [item + imgtype for item in imgname]  # 生成后缀的文件名组成的列表
    final_labels = [item + labeltype for item in labelname]
    return imgname, labelname, final_imgs, final_labels  # 输出由有后缀的文件名组成的列表


# label坐标集
coord_set = []

# label名集me
label_set = ['a', 'b', 't']


normal_list = []
# list of all specific type of files in the given directory

img_names = []
label_names = []
simple_img_names, simple_label_names, img_names, label_names = get_filename(outer_path, imgtype, labeltype)
num_of_imgs = len(img_names)

for i in range(len(simple_img_names)):
    if simple_img_names[i] not in simple_label_names:
        simple_label_names.insert(i, "")
        label_names.insert(i, simple_img_names[i] + labeltype)

# count
count = 0

normal_list = []
overall_bool = ''
b_dis_count = 0
while count < num_of_imgs:
    # 读取图片并转换为numpy.ndarray的形式
    image = cv2.imread(outer_path + img_names[count])

    # 输出binding box坐标
    image_yo = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    image_yo = Image.fromarray(image_yo)
    r_image, coord_set, normal_list, overall_bool, b_dis_count = yolo.detect_image(image_yo, normal_list, overall_bool, b_dis_count)
    print(coord_set)

    # 如果输入的图片没有预测出物体，不生成json文件并开始处理下一个图片
    if not coord_set:
        count += 1
        continue

    # 输出json打标文件，f.read可以用imgbytearray.getvalue代替
    with open(outer_path + img_names[count], "rb") as f:  # 转为二进制格式
        image_data = base64.b64encode(f.read()).decode("utf-8")  # 使用base64进行加密
        # print(image_data)

    points1 = []
    points2 = []
    points3 = []
    points1.clear()
    points2.clear()
    points3.clear()

    if simple_label_names[count] == "":
        # 预设
        if coord_set[0][4] == 't':
            label_json = {}
            label_json = {"version": "4.5.5", "flags": {}, "shapes": [],
                          "imagePath": img_names[count], "imageData": image_data,
                          "imageHeight": 720, "imageWidth": 720}
            for i in range(2):
                points3.append([float(coord_set[0][2 * i]), float(coord_set[0][2 * i + 1])])
            shape3 = {"label": label_set[2], "points": points3, "group_id": None, "shape_type": "rectangle",
                      "flags": {}}
            label_json["shapes"].append(shape3)

            with open(os.path.join(outer_path, label_names[count]), 'w') as fd:
                json.dump(label_json, fd)
            label_json.clear()
            print(label_names[count])
            count += 1
        continue

    if coord_set[0][4] == 'a':
        for i in range(2):
            points1.append([float(coord_set[0][2 * i]), float(coord_set[0][2 * i + 1])])
        shape1 = {"label": label_set[0], "points": points1, "group_id": None, "shape_type": "rectangle",
                  "flags": {}}
        with open(os.path.join(outer_path, label_names[count]), 'r') as fr:
            jsonload = json.load(fr)
            jsonload["shapes"].append(shape1)
        with open(os.path.join(outer_path, label_names[count]), 'w') as fr:
            json.dump(jsonload, fr)
        print(label_names[count])
        if len(coord_set) != 1 and coord_set[1][4] == 'b':
            for i in range(2):
                points2.append([float(coord_set[1][2 * i]), float(coord_set[1][2 * i + 1])])
            shape2 = {"label": label_set[1], "points": points2, "group_id": None, "shape_type": "rectangle",
                      "flags": {}}
            with open(os.path.join(outer_path, label_names[count]), 'r') as fr:
                jsonload = json.load(fr)
                jsonload["shapes"].append(shape2)
            with open(os.path.join(outer_path, label_names[count]), 'w') as fr:
                json.dump(jsonload, fr)
            print(label_names[count])

    if coord_set[0][4] == 'b':
        for i in range(2):
            points2.append([float(coord_set[0][2 * i]), float(coord_set[0][2 * i + 1])])
        shape2 = {"label": label_set[1], "points": points2, "group_id": None, "shape_type": "rectangle",
                  "flags": {}}
        with open(os.path.join(outer_path, label_names[count]), 'r') as fr:
            jsonload = json.load(fr)
            jsonload["shapes"].append(shape2)
        with open(os.path.join(outer_path, label_names[count]), 'w') as fr:
            json.dump(jsonload, fr)
        print(label_names[count])
        if len(coord_set) != 1 and coord_set[1][4] == 'a':
            for i in range(2):
                points1.append([float(coord_set[1][2 * i]), float(coord_set[1][2 * i + 1])])
            shape1 = {"label": label_set[1], "points": points1, "group_id": None, "shape_type": "rectangle",
                      "flags": {}}
            with open(os.path.join(outer_path, label_names[count]), 'r') as fr:
                jsonload = json.load(fr)
                jsonload["shapes"].append(shape1)
            with open(os.path.join(outer_path, label_names[count]), 'w') as fr:
                json.dump(jsonload, fr)
            print(label_names[count])

    if coord_set[0][4] == 't':
        for i in range(2):
            points3.append([float(coord_set[0][2 * i]), float(coord_set[0][2 * i + 1])])
        shape3 = {"label": label_set[2], "points": points3, "group_id": None, "shape_type": "rectangle",
                  "flags": {}}
        with open(os.path.join(outer_path, label_names[count]), 'r') as fr:
            jsonload = json.load(fr)
            jsonload["shapes"].append(shape3)
        with open(os.path.join(outer_path, label_names[count]), 'w') as fr:
            json.dump(jsonload, fr)
        print(label_names[count])

    # img = cv2.cvtColor(np.asarray(r_image), cv2.COLOR_BGR2RGB)
    # cv2.namedWindow("video", flags=False)
    # cv2.imshow("video", img)
    # cv2.waitKey(1)

    count += 1
yolo.close_session()