"""
realize reading data from json file
"""



# -*- coding: utf-8 -*-
import json, os
from PIL import Image

label_path = r"C:\Users\RoseC\Desktop\picture"

save_path = "save_img"

with open("./label.txt", "w+") as f: # 打开文件
    for filename in os.listdir(label_path):
        # 定义特征点
        x1 ,y1 = 0, 0   # 框左上  x: 距左，y:距上
        x2, y2 = 0, 0   # 框右下
        mark_x1, mark_y1 = 0, 0    # 左上点
        mark_x2, mark_y2 = 0, 0    # 右上点
        mark_x3, mark_y3 = 0, 0    # 左下点
        mark_x4, mark_y4 = 0, 0    # 右下点
        if filename.endswith(".json"):
            json_path = os.path.join(label_path, filename)
            data = json.load(open(json_path, 'r'))

            img_name = data['imagePath'] # 拿到图像的名字

            for obj in data['shapes']:
                if obj['label'] == "box":   # 框
                    x1 = int(obj['points'][0][0])
                    y1 = int(obj['points'][0][1])
                    x2 = int(obj['points'][1][0])
                    y2 = int(obj['points'][1][1])
                if obj['label'] == "left_up":   # 左上点
                    mark_x1 = int(obj['points'][0][0])
                    mark_y1 = int(obj['points'][0][1])
                if obj['label'] == "right_up":   # 右上点
                    mark_x2 = int(obj['points'][0][0])
                    mark_y2 = int(obj['points'][0][1])
                if obj['label'] == "left_down":   # 左下点
                    mark_x3 = int(obj['points'][0][0])
                    mark_y3 = int(obj['points'][0][1])
                if obj['label'] == "right_down":  # 右下点
                    mark_x4 = int(obj['points'][0][0])
                    mark_y4 = int(obj['points'][0][1])

            # 保存图片
            img = Image.open(os.path.join(label_path, img_name))
            img_save_path = os.path.join(save_path, img_name)
            img.save(img_save_path)

            # 写入文件
            line = "{0} {1} {2} {3} {4} " \
                       "{5} {6} {7} {8} " \
                       "{9} {10} {11} {12}\n".format(img_save_path, x1, y1, x2, y2,
                                        mark_x1, mark_y1, mark_x2, mark_y2,
                                        mark_x3, mark_y3, mark_x4, mark_y4)
            f.write(line)

"""
{
  "version": "3.16.7",
  "flags": {},
  "shapes": [
    {
      "label": "box",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          121.16666666666669,
          89.75
        ],
        [
          1230.5416666666667,
          815.7916666666667
        ]
      ],
      "shape_type": "rectangle",
      "flags": {}
    },
    {
      "label": "left_up",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          184.70833333333337,
          127.25
        ]
      ],
      "shape_type": "point",
      "flags": {}
    },
    {
      "label": "right_up",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          1175.3333333333335,
          152.25
        ]
      ],
      "shape_type": "point",
      "flags": {}
    },
    {
      "label": "left_down",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          159.70833333333337,
          752.25
        ]
      ],
      "shape_type": "point",
      "flags": {}
    },
    {
      "label": "right_down",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          1174.2916666666667,
          768.9166666666667
        ]
      ],
      "shape_type": "point",
      "flags": {}
    },
    {
      "label": "height_middle_left",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          161.79166666666669,
          424.125
        ]
      ],
      "shape_type": "point",
      "flags": {}
    },
    {
      "label": "height_middle_right",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          1185.75,
          451.20833333333337
        ]
      ],
      "shape_type": "point",
      "flags": {}
    },
    {
      "label": "width_middle_up",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          699.2916666666667,
          132.45833333333334
        ]
      ],
      "shape_type": "point",
      "flags": {}
    },
    {
      "label": "width_middle_down",
      "line_color": null,
      "fill_color": null,
      "points": [
        [
          703.4583333333334,
          774.125
        ]
      ],
      "shape_type": "point",
      "flags": {}
    }
  ],
  "lineColor": [
    0,
    255,
    0,
    128
  ],
  "fillColor": [
    255,
    0,
    0,
    128
  ],
  "imagePath": "15665254962320480618.jpg",
  "imageData": "很多值，不重要，省略，只要文件名和框和点的坐标",
  "imageHeight": 1001,
  "imageWidth": 1334
}
"""