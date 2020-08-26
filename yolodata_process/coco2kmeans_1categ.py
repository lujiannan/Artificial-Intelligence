import json

category_id = [1]


class COCO:
    def __init__(self, root_path):
        self.root_path = root_path

    def parse(self, json_path):
        json_data = json.load(open(json_path))
        old = None
        line = []
        with open(r"C:\Users\Administrator\Desktop\yolodata_process\stapler_coco\kmeansdata.txt", "w") as fd:
            for anno in json_data["annotations"]:
                if anno["category_id"] in category_id:
                    image_id = anno["image_id"]
                    file_name = json_data["images"][image_id]["file_name"]
                    file_name = file_name[11:]
                    if old != image_id and old is not None:
                        tmp = " ".join(line) + "\n"
                        fd.write(tmp)
                        line.clear()
                        print(tmp)
                    if old != image_id:
                        line.append(str(image_id))
                        line.append(file_name)

                    cls_id = str(anno["category_id"] - 1)
                    line.append(cls_id)
                    x, y = str(int(anno["bbox"][0])), str(int(anno["bbox"][1]))
                    line.append(x)
                    line.append(y)
                    x1 = str(int(anno["bbox"][0] + anno["bbox"][2]))
                    y1 = str(int(anno["bbox"][1] + anno["bbox"][3]))
                    line.append(x1)
                    line.append(y1)

                    old = image_id


if __name__ == '__main__':
    coco = COCO(r"C:\Users\Administrator\Desktop\yolodata_process\stapler_coco\JPEGImages")
    coco.parse(r"C:\Users\Administrator\Desktop\yolodata_process\stapler_coco\annotations.json")
