import os
from PIL import Image
from tqdm import tqdm
import json as js

with open("config_CNN.json",'r') as file:
    paths = js.load(file)

def resize_images(input_folder, output_folder, size=(256, 256)):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in tqdm(os.listdir(input_folder)):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        try:
            with Image.open(input_path) as img:
                img = img.resize(size, Image.LANCZOS)
                img.save(output_path)
        except Exception as e:
            print(f"Skipping {filename}: {e}")


input_folder_train = paths["Train_folder"] 
output_folder_train = paths["Train_resized"]
input_folder_Val = paths["Validation_folder"] 
output_folder_Val = paths["Validation_resized"]

if os.path.exists(input_folder_train):
    resize_images(input_folder_train, output_folder_train)
else: 
    print("Wrong path")

if os.path.exists(input_folder_Val):
    resize_images(input_folder_Val, output_folder_Val)
else: 
    print("Wrong path")
