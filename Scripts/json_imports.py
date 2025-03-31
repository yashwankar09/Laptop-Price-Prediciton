import os
import json

# def extract_keys(obj, keys_set):
#     if isinstance(obj, dict):
#         for key, value in obj.items():
#             keys_set.add(key) 
#             extract_keys(value, keys_set) 
#     elif isinstance(obj, list):
#         for item in obj:
#             extract_keys(item, keys_set) 

def import_json(self):
# get company name
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\Company.json', 'r') as file:
        self.company_json = json.load(file)

    # get cpu brand name
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\CPU_Brand.json', 'r') as file:
        self.cpu_brand_json = json.load(file)

    # get Display_type
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\Display_type.json', 'r') as file:
        self.Display_type_json = json.load(file)

    # get GPU
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\GPU.json', 'r') as file:
        self.GPU_json = json.load(file)

    # get OS
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\OS.json', 'r') as file:
        self.OSjson = json.load(file)

    # get Primary_type
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\Primary_type.json', 'r') as file:
        self.Primary_type_json = json.load(file)

    # get Secondary_type
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\Secondary_type.json', 'r') as file:
        self.Secondary_type_json = json.load(file)

    # get TypeName
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\TypeName.json', 'r') as file:
        self.type_nm_json = json.load(file)


# 1920x1080    
# 1366x768   
# 3840x2160    
# 3200x1800    
# 2560x1440     
# 1600x900      
# 2560x1600      
# 2304x1440      
# 2256x1504      
# 1920x1200      
# 1440x900       
# 2880x1800      
# 2400x1600      
# 2160x1440      
# 2736x1824 