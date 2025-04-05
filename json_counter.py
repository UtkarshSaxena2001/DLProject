import json as js

with open("config.json",'r') as file:
    paths = js.load(file)
    
# Add "Train_Label_Frequency" and "Validation_Label_Frequency" in your config file
train_json_path = paths["Preprocessed_Train_json"]
val_json_path = paths["Preprocessed_Validation_json"]
Train_Label_Frequency = paths["Train_Label_Frequency"]
Validation_Label_Frequency = paths["Validation_Label_Frequency"]


with open(train_json_path, "r") as file:
    train_json = js.load(file)
    
with open(val_json_path, "r") as file:
    val_json = js.load(file)
    
train_label_freq = {}
val_label_freq = {}

for ann in train_json:
    if ann["label"] not in train_label_freq.keys():
        train_label_freq[ann["label"]] = 1
    else:
        train_label_freq[ann["label"]] += 1
        
print(f"Unique labels in Train: {len(train_label_freq.keys())}")
with open(Train_Label_Frequency, "w") as f:
    js.dump(train_label_freq, f)
    
for ann in val_json:
    if ann["label"] not in val_label_freq.keys():
        val_label_freq[ann["label"]] = 1
    else:
        val_label_freq[ann["label"]] += 1
        
print(f"Unique labels in Validation: {len(val_label_freq.keys())}")
with open(Validation_Label_Frequency, "w") as f:
    js.dump(val_label_freq, f)