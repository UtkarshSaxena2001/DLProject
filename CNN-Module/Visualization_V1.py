import json as js
import cv2
import matplotlib.pyplot as plt
import os

with open("config_CNN.json",'r') as file:
    paths = js.load(file)

json_path = paths["Preprocessed_Train_json"]
train_path = paths["Train_resized"]

with open(json_path, 'r') as f:
    coco_data = js.load(f)

for img in coco_data:
    img_path = os.path.join(train_path, img["img_id"])
    if not os.path.exists(img_path):
        print(f"Image not found: {img_path}")
        continue
    
    image = cv2.imread(img_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    
    x, y, w, h = img["bbox"]
    cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (255, 0, 0), 2)

    plt.figure(figsize=(8, 8))
    plt.imshow(image)
    plt.axis("off")
    plt.show()
