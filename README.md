# DL-Project
Creating Captions from Images

# .gitegnore
/data/* (for linux) <br />
your_location_to_project\\data\\* (for windows) <br />
config_CNN.json (Common for all) <br />
config_RNN.json (Common for all)
best_model_bbox.keras

# Config_CNN

Create this config file in the CNN-Module named as 'config_CNN.json'

{ <br />
    "Train_folder" : "", <br />
    "Validation_folder" : "", <br />
    "Train_resized" : "", <br />
    "Validation_resized" : "", <br />
    "Max_Area_Train_Json" : "", <br />
    "Max_Area_Val_Json" : "", <br />
    "Preprocessed_Train_json" : "", <br />
    "Preprocessed_Validation_json" : "", <br />
    "Instance_Train" : "", <br />
    "Instance_Validation" : "", <br />
    "Train_Label_Frequency" : "", <br />
    "Validation_Label_Frequency" : "", <br />
    "Trained_model" : "" <br />
}

# Config_RNN

create this config file in the RNN-Module name as 'Config_RNN.json'

{ <br />
    "Caption_Train" : "", <br />
    "Caption_Val" : "", <br /> 
    "Corpus" : "", <br /> 
    "Preprocessed_Corpus" : "", <br />
    "Nouned_Corpus" : "", <br />
    "Preprocessed_data" : "", <br />
    "Padded_preprocessed_data" : "" <br />
}