"""

The purpose for this file is to  display the labels in an specific image at a specific directory

variables needs to be altered before running:
when inpur window pops up, enter the address of the image which needs to be predicted

"""

from yolo import YOLO
from PIL import Image

yolo = YOLO()

normal_list = []
overall_bool = ''
b_dis_count = 0
while True:
    img = input('Input image filename:')
    try:
        image = Image.open(img)
    except:
        print('Open Error! Try again!')
        continue
    else:
        r_image, _, normal_list, overall_bool, b_dis_count = yolo.detect_image(image, normal_list, overall_bool, b_dis_count)
        # print(coord_set)
        r_image.show()
yolo.close_session()
