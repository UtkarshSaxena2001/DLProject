import os
from collections import Counter
from PIL import Image

def get_image_dimensions(folder_path):
    dimensions = []
    
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        
        try:
            with Image.open(file_path) as img:
                dimensions.append(img.size)  # (width, height)
        except Exception as e:
            print(f"Skipping {filename}: {e}")
    
    if not dimensions:
        print("No valid images found in the folder.")
        return None, None
    
    # Find the maximum dimensions
    max_dimensions = max(dimensions, key=lambda x: x[0] * x[1])
    
    # Find the most frequent dimensions
    most_common_dimensions, _ = Counter(dimensions).most_common(1)[0]
    
    return max_dimensions, most_common_dimensions

if __name__ == "__main__":
    folder_path="data/val2017/"
    maxm, mode = get_image_dimensions(folder_path)
    print("Maximum size= ", maxm)
    print("Most frequent size= ", mode)
