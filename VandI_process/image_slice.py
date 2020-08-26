import cv2
import os

x = 0
for root, dirs, files in os.walk(r'C:\Users\Administrator\Desktop\stapler\video_frames\VID_20200710_134553'):
    for d in dirs:
        # 打印资料夹个数
        print(d)
    for file in files:
        print(file)

        # 读入图像
        img_path = root + '/' + file
        img = cv2.imread(img_path, 1)
        print(img_path, img.shape)
        cv2.namedWindow('colorModeOpen', cv2.WINDOW_NORMAL)
        cv2.imshow('colorModeOpen', img)
        cv2.waitKey(1)

        # 图像处理：改变分辨率'
        img = cv2.resize(img, (608, 608))

        # 保存图像
        x = x + 1
        img_saving_path = img_path.replace('.png', str(x) + '.png')
        print(img_saving_path)
        cv2.imwrite(img_saving_path, img)