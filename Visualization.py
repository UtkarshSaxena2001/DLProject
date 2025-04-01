import json
import cv2
import matplotlib.pyplot as plt
import os

json_path = "/home/utkarsh/Desktop/Sem-2/Deep Learning/2024PGCSDS14_Utkarsh Saxena_DeepLearning/coco_dataset/annotations/instances_train2017.json"
train_path = '/home/utkarsh/Downloads/train2017/'

# Load COCO annotations
with open(json_path, 'r') as f:
    coco_data = json.load(f)

annotations = coco_data["annotations"]
images = coco_data["images"]

# Create a mapping from image_id to filename
image_id_to_filename = {img["id"]: img["file_name"] for img in images}

# Create a mapping from image filename to bounding boxes
image_to_bboxes = {}

for ann in annotations:
    image_id = ann["image_id"]
    bbox = ann["bbox"]  # [x, y, width, height]
    
    filename = image_id_to_filename.get(image_id)
    if filename:
        image_path = os.path.join(train_path, filename)
        if image_path not in image_to_bboxes:
            image_to_bboxes[image_path] = []
        image_to_bboxes[image_path].append(bbox)

# Loop through images and draw bounding boxes
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
