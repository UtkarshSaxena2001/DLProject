import os
import cv2
import matplotlib.pyplot as plt
from collections import Counter

train_path = "data/train2017/"
image_files = [os.path.join(train_path, f) for f in os.listdir(train_path) if f.endswith(('.jpg', '.png', '.jpeg'))]
image_sizes = []

for img_path in image_files:
    image = cv2.imread(img_path)
    if image is not None:
        h, w, _ = image.shape  
        image_sizes.append((w, h))

size_counts = Counter(image_sizes)
sizes = [f"{w}x{h}" for w, h in size_counts.keys()]
counts = list(size_counts.values())
plt.figure(figsize=(12, 12))
plt.bar(sizes, counts, color="skyblue")
plt.xlabel("Image Size (Width x Height)")
plt.ylabel("Frequency")
plt.title("Distribution of Image Sizes in Dataset (Direct from Images)")
plt.xticks(rotation=90)  
plt.show()