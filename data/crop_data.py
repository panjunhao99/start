import pandas as pd
import os
from shutil import copyfile
import shutil
from PIL import Image, ImageDraw
import numpy as np
import cv2
import pandas as pd
from sklearn.model_selection import train_test_split
import os
import cv2
import json



# df = pd.read_csv(r'D:\Achollege\QT\QTdemo_modeltest\图片虫子位置详情表.csv', encoding="GBK", usecols=["文件名", "虫子编号"])
df = pd.read_csv(r'D:\Achollege\QT\QTdemo_modeltest\图片虫子位置详情表.csv', encoding="GBK")
# df = pd.read_csv(r'D:\Achollege\QT\QTdemo_modeltest\无位置信息的图片汇总表.csv', encoding="GBK", usecols=["文件名"])
# height,width = df.shape
# print(height,width,type(df))
# print(df)
start_bbox_id = 1
categories = {"大螟": 6, "二化螟": 7, "稻纵卷叶螟": 8, "白背飞虱": 9, "褐飞虱属": 10, "地老虎": 25, "蝼蛄": 41, "粘虫": 105, "草地螟": 110, "甜菜夜蛾": 115, "黄足猎蝽": 148,
              "八点灰灯蛾": 156, "棉铃虫": 222, "二点委夜蛾": 228, "甘蓝夜蛾": 235, "蟋蟀": 256, "黄毒蛾": 280, "稻螟蛉": 310, "紫条尺蛾": 387, "水螟蛾": 392,
              "线委夜蛾": 394, "甜菜白带野螟": 398, "歧角螟": 401, "瓜绢野螟": 402, "豆野螟": 430, "石蛾": 480, "大黑鳃金龟": 485, "干纹冬夜蛾": 673}
json_dict = {"images": [], "type": "instances", "annotations": [], "categories": []}
image_id = 0
bnd_id = 0
json_file = "train.json"

for cls in categories:
    cat = {"id": categories[cls], "name": cls}
    json_dict["categories"].append(cat)


print(json_dict["categories"])




wide_max = 0
count = 0
path = r'D:\Achollege\竞赛\正式数据\附件1'  # 源文件夹
save_path = r'D:\Achollege\竞赛\附件2'  # 保存文件夹
hmin = 0
wmin = 0
hmax = 960
wmax = 960
for index, row in df.iterrows():
    if row['虫子编号'] != 0:  # 这里条件按需要任意改
        image_origin_path = os.path.join(path, row['文件名'])
        images_save_path = os.path.join(save_path, row['文件名'])

        img_org = np.array(Image.open(image_origin_path))

        id_name = row['文件名']

        wide = row['右下角x坐标'] - row['左上角x坐标']
        height = row['右下角y坐标'] - row['左上角y坐标']
        xmin = row['左上角x坐标']
        ymin = row['左上角y坐标']
        xmax = row['右下角x坐标']
        ymax = row['右下角y坐标']
        label = row['虫子编号']
        # if wide < 960 and height < 960:
        #     w_edge_left = xmin
        #     w_edge_right = 5472 - xmax
        #     h_edge_top = ymin
        #     h_edge_down = 3648 - ymax
        #     # if w_edge_left > w_edge_right:
        #     if (xmin + xmax) / 2 + 480 > 5472:
        #         wmax = 5472
        #         wmin = 5472 - 960
        #         xmax = xmax - wmin
        #         xmin = xmin - wmin
        #     elif (xmin + xmax) / 2 - 480 < 0:
        #         wmax = 960
        #         wmin = 0
        #         xmax = xmax - wmin
        #         xmin = xmin - wmin
        #     else:
        #         wmax = (xmin + xmax) / 2 + 480
        #         wmin = (xmin + xmax) / 2 - 480
        #         xmax = xmax - wmin
        #         xmin = xmin - wmin
        #     # else:
        #     #     if (xmin+xmax)/2 - 480 < 0:
        #     #         wmax = 960
        #     #         wmin = 0
        #     #         xmax = xmax - wmin
        #     #         xmin = xmin - wmin
        #     #     else:
        #     #         wmax = (xmin + xmax) / 2 + 480
        #     #         wmin = (xmin + xmax) / 2 - 480
        #     #         xmax = xmax - wmin
        #     #         xmin = xmin - wmin
        #
        #     if (ymin + ymax) / 2 + 480 > 3648:
        #         hmax = 3648
        #         hmin = 3648 - 960
        #         ymax = ymax - hmin
        #         ymin = ymin - hmin
        #     elif (ymin + ymax) / 2 - 480 < 0:
        #         hmax = 960
        #         hmin = 0
        #         ymax = ymax - hmin
        #         ymin = ymin - hmin
        #     else:
        #         hmax = (ymin + ymax) / 2 + 480
        #         hmin = (ymin + ymax) / 2 - 480
        #         ymax = ymax - hmin
        #         ymin = ymin - hmin
        #     #
        #     # else:
        #     #     if (xmin+xmax)/2 - 480 < 0:
        #     #         hmax = 960
        #     #         hmin = 0
        #     #         ymax = ymax - hmin
        #     #         ymin = ymin - hmin
        #     #     else:
        #     #         hmax = (ymin + ymax) / 2 + 480
        #     #         hmin = (ymin + ymax) / 2 - 480
        #     #         ymax = ymax - hmin
        #     #         ymin = ymin - hmin
        #
        # if wide > 960 or height > 960:
        #     w_edge_left = xmin
        #     w_edge_right = 5472 - xmax
        #     h_edge_top = ymin
        #     h_edge_down = 3648 - ymax
        #
        #     if (xmin + xmax) / 2 + 660 > 5472:
        #         wmax = 5472
        #         wmin = 5472 - 1320
        #         xmax = xmax - wmin
        #         xmin = xmin - wmin
        #     elif (xmin + xmax) / 2 - 660 < 0:
        #         wmax = 1320
        #         wmin = 0
        #         xmax = xmax - wmin
        #         xmin = xmin - wmin
        #     else:
        #         wmax = (xmin + xmax) / 2 + 660
        #         wmin = (xmin + xmax) / 2 - 660
        #         xmax = xmax - wmin
        #         xmin = xmin - wmin
        #     # else:
        #     #     if (xmin+xmax)/2 - 660 < 0:
        #     #         wmax = 1320
        #     #         wmin = 0
        #     #         xmax = xmax - wmin
        #     #         xmin = xmin - wmin
        #     #     else:
        #     #         wmax = (xmin + xmax) / 2 + 660
        #     #         wmin = (xmin + xmax) / 2 - 660
        #     #         xmax = xmax - wmin
        #     #         xmin = xmin - wmin
        #
        #     # if h_edge_top > h_edge_down:
        #     if (ymin + ymax) / 2 + 660 > 3648:
        #         hmax = 3648
        #         hmin = 3648 - 660
        #         ymax = ymax - hmin
        #         ymin = ymin - hmin
        #     elif (ymin + ymax) / 2 - 660 < 0:
        #         hmax = 1320
        #         hmin = 0
        #         ymax = ymax - hmin
        #         ymin = ymin - hmin
        #     else:
        #         hmax = (ymin + ymax) / 2 + 660
        #         hmin = (ymin + ymax) / 2 - 660
        #         ymax = ymax - hmin
        #         ymin = ymin - hmin
        #     # else:
        #     #     if (xmin+xmax)/2 - 660 < 0:
        #     #         hmax = 1320
        #     #         hmin = 0
        #     #         ymax = ymax - hmin
        #     #         ymin = ymin - hmin
        #     #     else:
        #     #         hmax = (ymin + ymax) / 2 + 660
        #     #         hmin = (ymin + ymax) / 2 - 660
        #     #         ymax = ymax - hmin
        #     #         ymin = ymin - hmin
        #     xmin = int(xmin * 960 / 1320)
        #     ymin = int(ymin * 960 / 1320)
        #     xmax = int(xmax * 960 / 1320)
        #     ymax = int(ymax * 960 / 1320)

        print(index, row['文件名'], row['虫子编号'])
        # image_origin_path = os.path.join(path, row['文件名'])
        # images_copy = os.path.join(save_path, row['文件名'])
        # print(image_origin_path)
        # shutil.copyfile(image_origin_path,images_copy)
        # os.remove(image_origin_path)   # 删除源文件，可选

        # 保存

        # print(img_org.shape)
        # img_patch = img_org[int(hmin):int(hmax), int(wmin):int(wmax), :]
        # img = cv2.cvtColor(np.asarray(img_patch), cv2.COLOR_RGB2BGR)
        # img = cv2.resize(img, (960, 960))
        # result = Image.fromarray(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        # result = np.asarray(result)
        #
        # print(hmin, hmax, wmin, wmax, id_name)
        # images_save_path = os.path.join(save_path, str(id_name) + '.jpg')
        # Image.fromarray(result.astype(np.uint8)).save(images_save_path)


        image_id = image_id + 1
        img_name = str(id_name) + '.jpg'
        flag_same = 0

        # 检测是否有同一张图片
        for file_list in json_dict["images"]:
            if img_name in file_list["file_name"]:
                print(img_name)
                image_id = image_id - 1
                image_id = file_list["id"]
                print(image_id)
                flag_same = 1





        if flag_same == 0:
            image = {"coco_url": "", "date_captured": "", "file_name": img_name,  "flickr_url": "", "id": image_id, "license": 0, "width": 5472, "height": 3648}
            json_dict["images"].append(image)

        category = row['虫子名称']
        category_id = categories[category]



        xmin = int(xmin)
        ymin = int(ymin)
        xmax = int(xmax)
        ymax = int(ymax)
        o_width = abs(xmax - xmin)
        o_height = abs(ymax - ymin)
        area = o_height * o_width
        bnd_id += 1
        anno = {"area": area, "iscrowd": 0, "image_id": image_id, "bbox": [xmin, ymin, o_width, o_height],
                "category_id": category_id, "id": bnd_id, "ignore": 0, "segmentation": []}


        json_dict["annotations"].append(anno)

        #
        # cat = {"id": category_id, "name": str(category)}
        # json_dict["categories"].append(cat)

json_fp = open(json_file, "w")
json_str = json.dumps(json_dict, indent=4)
json_fp.write(json_str)
json_fp.close()
print("Done!")


# test
# image_origin_path = os.path.join(path, '00004.jpg')
# images_copy = os.path.join(save_path, '00004.jpg')
# shutil.copyfile(image_origin_path,images_copy)         # 复制文件
# os.remove(image_origin_path)                         #   删除源文件，可选



#
# if __name__ == "__main__":
#     # files_path = "train_label_fix.csv"
#     # images_path = "/home/airu1314/competition/Train_fix"
#     # train_val(files_path, images_path)
#     files_path = "train_annotation.csv"
#     json_file = "train.json"
#     convert(files_path, json_file)
#
#     files_path = "val_annotation.csv"
#     json_file = "val.json"
#     convert(files_path, json_file)
