import json

category_id = [1, 2]


class COCO:
    def __init__(self, root_path):
        self.root_path = root_path

    def parse(self, json_path):
        json_data = json.load(open(json_path))
        old = None
        line = []
        line_tmp = []
        with open(r"C:\Users\Administrator\Desktop\yolodata_process\nails_coco\kmeansdata.txt", "w") as fd:
            for anno in json_data["annotations"]:
                if anno["category_id"] in category_id:
                    image_id = anno["image_id"]
                    file_name = json_data["images"][image_id]["file_name"]
                    file_name = file_name[11:]

                    if old != image_id and old is not None:
                        if len(line) == 4:
                            tmp = line[0] + " " + line[1] + " " + line[2] + " " + line[3] + "\n"
                        elif len(line) == 3:
                            tmp = line[0] + " " + line[1] + " " + line[2] + "\n"
                        else:
                            tmp = "" + "\n"
                        fd.write(tmp)
                        line.clear()
                        print(tmp, end=' ')
                    if old != image_id:
                        line.append(str(image_id))
                        line.append(file_name)

                    cls_id = str(anno["category_id"] - 1)
                    line_tmp.append(cls_id)
                    x, y = str(int(anno["bbox"][0])), str(int(anno["bbox"][1]))
                    line_tmp.append(x)
                    line_tmp.append(y)
                    x1 = str(int(anno["bbox"][0] + anno["bbox"][2]))
                    y1 = str(int(anno["bbox"][1] + anno["bbox"][3]))
                    line_tmp.append(x1)
                    line_tmp.append(y1)

                    tmp_line = " ".join(line_tmp)  # binding box coordinates + class id, separated by comma
                    line.append(tmp_line)
                    line_tmp.clear()

                    old = image_id


if __name__ == '__main__':
    coco = COCO(r"C:\Users\Administrator\Desktop\yolodata_process\nails_coco\JPEGImages")
    coco.parse(r"C:\Users\Administrator\Desktop\yolodata_process\nails_coco\annotations.json")
