import json
import cv2
import matplotlib.pyplot as plt
import os

def visualize_coco_annotations(json_path, image_folder):
    with open(json_path, 'r') as f:
        coco_data = json.load(f)
    
    image_id_to_filename = {img['id']: img['file_name'] for img in coco_data['images']}
    
    for ann in coco_data['annotations']:
        image_id = ann['image_id']
        bbox = ann['bbox']  
        
        if image_id not in image_id_to_filename:
            continue
        
        image_path = os.path.join(image_folder, image_id_to_filename[image_id])
        image = cv2.imread(image_path)
        if image is None:
            continue
        
        image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        x, y, w, h = bbox
        cv2.rectangle(image, (int(x), int(y)), (int(x + w), int(y + h)), (255, 0, 0), 2)
        plt.figure(figsize=(8, 6))
        plt.imshow(image)
        plt.axis("off")
        plt.show()
        
json_path = "/home/utkarsh/Desktop/Sem-2/Deep Learning/2024PGCSDS14_Utkarsh Saxena_DeepLearning/coco_dataset/annotations/bb_train2017.json"
image_folder = "/home/utkarsh/Desktop/Sem-2/Deep Learning/2024PGCSDS14_Utkarsh Saxena_DeepLearning/coco_dataset"
visualize_coco_annotations(json_path, image_folder)
