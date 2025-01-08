import json

annotation_file = "annotations/instances_train2017.json"
coco_names_file = "coco.names"

with open(annotation_file, 'r') as f:
    coco_data = json.load(f)

class_names = [category['name'] for category in coco_data['categories']]

with open(coco_names_file, 'w') as f:
    for class_name in class_names:
        f.write(class_name + '\n')