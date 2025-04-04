import json as js

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

with open("config.json",'r') as file:
    paths = js.load(file)

with open(paths["Max_Area_Val_Json"], "r") as file:
    data = js.load(file)  

l = []
for i in data['images']:
    img = {}
    img["img_id"] = i["file_name"]
    img['size'] = get_image_size(i["id"])
    img["bbox"],img["category_id"] = get_largest_bounding_box(i["id"])
    img["label"] = get_category_name(img["category_id"])
    if img["bbox"] != 0:
        l.append(img)

with open(paths["Preprocessed_Validation"],'w+') as file:
    js.dump(l, file, indent=4)