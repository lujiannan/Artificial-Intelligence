"""

The purpose for this file is to constantly display the labels in each frames within a video or a live show based on the
trained model

variables needs to be altered before running:
'***'(cap = cv2.VideoCapture('***')): should be the address of the source video or live show

"""

import time

from yolo import YOLO
from PIL import Image
import cv2
import numpy as np
yolo = YOLO()

# cap = cv2.VideoCapture("http://admin:admin@192.168.90.40:8081/video")
cap = cv2.VideoCapture('./V&I_process/test_nails_0817_1.mp4')
normal_list = []
overall_bool = ''
b_dis_count = 0
while cap.isOpened():
    ret, frame = cap.read()

    frame = cv2.rotate(frame, 0)
    # if not ret:
    #     cap = cv2.VideoCapture("http://admin:admin@192.168.90.40:8081/video")
    #     continue

    image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image = Image.fromarray(image)
    # start_ = time.time()
    r_image, _, normal_list, overall_bool, b_dis_count = yolo.detect_image(image, normal_list, overall_bool, b_dis_count)
    # print("runtime:", time.time() - start_)
    img = cv2.cvtColor(np.asarray(r_image), cv2.COLOR_BGR2RGB)
    cv2.namedWindow("video", flags=0)
    cv2.imshow("video", img)
    cv2.waitKey(1)
cv2.waitKey(0)
yolo.close_session()