import os
from PIL import Image
from tqdm import tqdm

def resize_images(input_folder, output_folder, size=(256, 256)):
    """
    Resizes all images in the input folder to the specified size and saves them to the output folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in tqdm(os.listdir(input_folder)):
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)
        
        try:
            with Image.open(input_path) as img:
                img = img.resize(size, Image.LANCZOS)
                img.save(output_path)
                # print(f"Resized and saved: {output_path}")
        except Exception as e:
            print(f"Skipping {filename}: {e}")

if __name__ == "__main__":
    fol = input("which folder to resize: ")
    input_folder = f"data/{fol}/"  # Change this to your input folder
    output_folder = f"data/resized_{fol}"  # Change this to your output folder
    if os.path.exists(input_folder):
        resize_images(input_folder, output_folder)
    else: 
        print("Wrong path")
