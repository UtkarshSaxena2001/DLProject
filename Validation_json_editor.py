import json

def get_img_name(id:int):
    for i in data['images']:
        if i["id"]==id:
            return i["file_name"]

def get_category_name(id:int):
    for i in data['categories']:
        if i['id']== id:
            return i["name"]
        
def get_image_size(id:int):
    for i in data['images']:
        if i["id"]==id:
            return (i["width"], i["height"])
        
def get_largest_bounding_box(id:int):
    area_list,bbox_list,cat_list = [0],[0],[0]
    
    for i in data['annotations']:
        if i['image_id']==id:
            area_list.append(i["area"])
            bbox_list.append(i["bbox"])
            cat_list.append(i["category_id"])
            
        else:
            continue
        
    if len(area_list) != 0: 
        max_area = max(area_list)
        bbox = bbox_list[area_list.index(max_area)]
        cat = cat_list[area_list.index(max_area)]
        return bbox,cat

# Open and read the JSON file
with open("/home/utkarsh/Desktop/Sem-2/Deep Learning/2024PGCSDS14_Utkarsh Saxena_DeepLearning/coco_dataset/annotations/instances_val2017.json", "r") as file:
    data = json.load(file)  # Parses JSON into a Python dictionary

# Output the JSON content as a Python dictionary
l = []
for i in data['images']:
    img = {}
    img["img_id"] = i
    img['size'] = get_image_size(i["id"])
    img["bbox"],img["category_id"] = get_largest_bounding_box(i["id"])
    if img["bbox"] != 0:
        l.append(img)

with open("Max_Area_BB_validation.json",'w+') as file:
    json.dump(l, file, indent=4)