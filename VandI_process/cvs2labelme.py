import json

import cv2
import base64
import io
import os.path as osp
import re
import PIL.Image
from labelme.logger import logger
from labelme import PY2
from labelme import QT4
from labelme import utils
import os

file_path = "/home/george/baidunetdiskdownload/SpaceNet/spacenet/train/SummaryData/SN6_Train_AOI_11_Rotterdam_Buildings.csv"


def load_image_file(filename):
    try:
        image_pil = PIL.Image.open(filename)
    except IOError:
        logger.error('Failed opening image file: {}'.format(filename))
        return

    # apply orientation to image according to exif
    image_pil = utils.apply_exif_orientation(image_pil)

    with io.BytesIO() as f:
        ext = osp.splitext(filename)[1].lower()
        if PY2 and QT4:
            format = 'PNG'
        elif ext in ['.jpg', '.jpeg']:
            format = 'JPEG'
        else:
            format = 'PNG'
        image_pil.save(f, format=format)
        f.seek(0)
        return f.read()


def cvs2labelme(images_path, new_dataset_path):
    p = re.compile("POLYGON [(][(](.*)[)][)]")
    with open(file_path) as fd:
        label_json = {}
        current_fid = ""
        for i, line in enumerate(fd):
            if i == 0:
                continue
            fid = line.split(",")[0]
            fid_num = line.split(",")[1]
            if fid != current_fid:
                save_img_file_name = "SN6_Train_AOI_11_Rotterdam_PS-RGB_" + current_fid + ".jpg"
                save_json_file_name = save_img_file_name.replace(".jpg", ".json")
                if current_fid != "":
                    with open(os.path.join(new_dataset_path, save_json_file_name), "w") as fd:
                        json.dump(label_json, fd)
                        print(save_json_file_name)
                label_json.clear()

                img_file_name = "SN6_Train_AOI_11_Rotterdam_PS-RGB_" + fid + ".jpg"
                img = load_image_file(os.path.join(images_path, img_file_name))
                image_data = base64.b64encode(img).decode('utf-8')
                label_json = {"version": "4.2.9", "flags": {}, "shapes": [],
                              "imagePath": img_file_name, "imageHeight": 900, "imageWidth": 900,
                              "imageData": image_data}
            current_fid = fid

            ret = re.findall(p, line)
            if len(ret) <= 0:
                continue
            coords = ret[0].split(", ")
            points = []
            for j in coords:
                tmp = j.split(" ")
                tmp[0] = tmp[0].replace("(", "")
                tmp[1] = tmp[1].replace(")", "")
                x, y = float(tmp[0]), float(tmp[1])
                points.append([x, y])
            shape = {"label": "building", "points": points, "group_id": None, "shape_type": "polygon", "flags": {}}
            label_json["shapes"].append(shape)


cvs2labelme("/home/george/baidunetdiskdownload/SpaceNet/spacenet/train/PS-RGB_JPG",
            "/home/george/baidunetdiskdownload/SpaceNet/spacenet/train/PS-RGB_JPG"
            )
