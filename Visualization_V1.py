import json
import cv2
import matplotlib.pyplot as plt
import os

json_path = "data/annotations/instances_train2017.json"
train_path = 'data/train2017/'

with open(json_path, 'r') as f:
    coco_data = json.load(f)

annotations = coco_data["annotations"]
images = coco_data["images"]
image_id_to_filename = {img["id"]: img["file_name"] for img in images}
image_to_bboxes = {}

for ann in annotations:
    image_id = ann["image_id"]
    bbox = ann["bbox"] 
    
    filename = image_id_to_filename.get(image_id)
    if filename:
        image_path = os.path.join(train_path, filename)
        if image_path not in image_to_bboxes:
            image_to_bboxes[image_path] = []
        image_to_bboxes[image_path].append(bbox)

for image_path, bboxes in image_to_bboxes.items():
    if not os.path.exists(image_path):
        print(f"Image not found: {image_path}")
        continue
    
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    for bbox in bboxes:
        x, y, w, h = bbox
        cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (255, 0, 0), 2)

    plt.figure(figsize=(8, 8))
    plt.imshow(image)
    plt.axis("off")
    plt.show()
