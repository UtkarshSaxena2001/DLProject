import json
from collections import Counter

def most_common(lst):
    return Counter(lst).most_common(1)[0][0] if lst else None

train_anno = '/home/utkarsh/Desktop/Sem-2/Deep Learning/2024PGCSDS14_Utkarsh Saxena_DeepLearning/DLProject/combined_pos_train.json'
val_anno = '/home/utkarsh/Desktop/Sem-2/Deep Learning/2024PGCSDS14_Utkarsh Saxena_DeepLearning/DLProject/combined_pos_val.json'

with open(train_anno, "r") as f:
    train_data = json.load(f)

with open(val_anno, "r") as f:
    val_data = json.load(f)

def process_data(data):
    image_nouns = {}

    for item in data:
        image_id = item["image_id"]
        nouns = item.get("nouns", [])  

        if image_id not in image_nouns:
            image_nouns[image_id] = []
        image_nouns[image_id].extend(nouns)
    return {image_id: most_common(nouns) for image_id, nouns in image_nouns.items()}

train_dict = process_data(train_data)
val_dict = process_data(val_data)

with open("train_most_common.json", "w") as f:
    json.dump(train_dict, f, indent=4)

with open("val_most_common.json", "w") as f:
    json.dump(val_dict, f, indent=4)

