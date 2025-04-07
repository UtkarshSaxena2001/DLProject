import json as js

with open("config.json",'r') as file:
    paths = js.load(file)
    
og_train_json = paths["Instance_Train"]
og_val_json = paths["Instance_Validation"]

with open(og_train_json, "r") as file:
    train_json = js.load(file)
    
with open(og_val_json, "r") as file:
    val_json = js.load(file)
    
print(f"unique labels in train set: {len(train_json["categories"])}")
print(f"unique labels in validation set: {len(val_json["categories"])}")