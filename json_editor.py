import json

def img_namer(id:int, size:int, suffix:str):
    t= str(id)
    l = len(t)
    r = "0"*(size-l)+t+"."+suffix
    return r

def get_category_name(id:int):
    for i in data['categories']:
        if i['id']== id:
            return i["name"]
        
def get_image_size(id:int):
    for i in data['images']:
        if i["id"]==id:
            pass

# Open and read the JSON file
with open("data/annotations_trainval2017/annotations/instances_val2017.json", "r") as file:
    data = json.load(file)  # Parses JSON into a Python dictionary

print(data['annotations'])  # Output the JSON content as a Python dictionary
for i in data['annotaions']:
    img = {}
    img["img_id"] = img_namer(i['image_id'],12,"jpg")
    img["category"] = get_category_name(i['category_id'])
# print(data.keys())