import cv2
import os

# 要提取视频的文件名，隐藏后缀
sourceFileName = 'VID_20200716_112229'
# 在这里把后缀接上
video_path = os.path.join("", "", sourceFileName + '.mp4')
times = 13000
# 提取视频的频率，每25帧提取一个
frameFrequency = 15
# 输出图片到当前目录vedio文件夹下
outPutDirName = 'video_frames/' + sourceFileName + '/'
if not os.path.exists(outPutDirName):
    # 如果文件目录不存在则创建目录
    os.makedirs(outPutDirName)
camera = cv2.VideoCapture(video_path)
while True:
    times += 1
    res, image = camera.read()
    image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
    image = image[200:-360, :, :]
    if not res:
        print('not res , not image')
        break
    cv2.imshow("t", image)
    cv2.waitKey(25)
    if times % frameFrequency == 0:
        cv2.imwrite(outPutDirName + str(times) + '.jpg', image)
        print(outPutDirName + str(times) + '.jpg')
print('图片提取结束')
camera.release()
