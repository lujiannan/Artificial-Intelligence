import cv2
import os

# 提取视频的文件名，隐藏后缀
sourceFileName = 'VID_20200817_115042'
# 视频保存的文件名，隐藏后缀
saveFileName = 'test_nails_0817_1'
# 在这里把后缀接上
source_path = os.path.join("", "", sourceFileName + '.mp4')
save_path = os.path.join("", "", saveFileName + '.mp4')

# 在此只用于计数
times = 0
# 提取视频的频率，每x帧提取一个 == fps
frameFrequency = 1

camera = cv2.VideoCapture(source_path)
fourcc = cv2.VideoWriter_fourcc('m','p','4','v')
out = cv2.VideoWriter(save_path, fourcc, 30, (720,720), True)

while camera.isOpened():
    times += 1
    res, image = camera.read()
    if res:
        image = cv2.rotate(image, cv2.ROTATE_90_CLOCKWISE)
        # 图片裁剪
        image = image[200:-360, :, :]
        cv2.imshow("img", image)
        cv2.waitKey(25)
        if times % frameFrequency == 0:
            out.write(image)
        if cv2.waitKey(10) & 0xFF == ord('q'):
            break
    else:
        print('res not true')
        break

print('图片提取结束')
camera.release()
out.release()
cv2.destroyAllWindows()