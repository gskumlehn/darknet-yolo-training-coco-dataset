import os
import json
from pycocotools.coco import COCO
from tqdm import tqdm

def coco_to_yolo(coco_json, output_dir, image_dir):
    coco = COCO(coco_json)
    os.makedirs(output_dir, exist_ok=True)

    categories = {cat['id']: cat['name'] for cat in coco.loadCats(coco.getCatIds())}

    for img_id in tqdm(coco.getImgIds(), desc="Converting Annotations"):
        img = coco.loadImgs(img_id)[0]
        img_filename = img['file_name']
        img_width = img['width']
        img_height = img['height']

        annotation_file = os.path.join(output_dir, os.path.splitext(img_filename)[0] + ".txt")

        ann_ids = coco.getAnnIds(imgIds=img_id)
        anns = coco.loadAnns(ann_ids)

        with open(annotation_file, "w") as f:
            for ann in anns:
                cat_id = ann['category_id']
                bbox = ann['bbox']

                x_center = (bbox[0] + bbox[2] / 2) / img_width
                y_center = (bbox[1] + bbox[3] / 2) / img_height
                width = bbox[2] / img_width
                height = bbox[3] / img_height

                f.write(f"{cat_id - 1} {x_center} {y_center} {width} {height}\n")

coco_json_path = "annotations/instances_val2017.json"
yolo_output_dir = "labels/val2017"
image_dir = "images/val2017"

coco_to_yolo(coco_json=coco_json_path, output_dir=yolo_output_dir, image_dir=image_dir)

coco_json_path = "annotations/instances_train2017.json"
yolo_output_dir = "labels/train2017"
image_dir = "images/train2017"

coco_to_yolo(coco_json=coco_json_path, output_dir=yolo_output_dir, image_dir=image_dir)
