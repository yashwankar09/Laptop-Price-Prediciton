import streamlit as st
import pandas as pd
import numpy as np
import pickle
import json
import warnings
warnings.filterwarnings("ignore")

#import model
with open('../Models/model_v1.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("Laptop Price Prediciton")

# @st.cache_data
def get_list():
    # get company name
    global company_json,cpu_brand_json,Display_type_json,GPU_json,OS_json,Primary_type_json,Secondary_type_json,type_nm_json
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\Company.json', 'r') as file:
        company_json = json.load(file)

    # get cpu brand name
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\CPU_Brand.json', 'r') as file:
        cpu_brand_json = json.load(file)

    # get Display_type
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\Display_type.json', 'r') as file:
        Display_type_json = json.load(file)

    # get GPU
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\GPU.json', 'r') as file:
        GPU_json = json.load(file)

    # get OS
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\OS.json', 'r') as file:
        OS_json = json.load(file)

    # get Primary_type
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\Primary_type.json', 'r') as file:
        Primary_type_json = json.load(file)

    # get Secondary_type
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\Secondary_type.json', 'r') as file:
        Secondary_type_json = json.load(file)

    # get TypeName
    with open(r'C:\Users\yashw\DataSets\Laptop Price\2025\JSON Files\TypeName.json', 'r') as file:
        type_nm_json = json.load(file)

    return list(company_json),list(cpu_brand_json),list(Display_type_json),list(GPU_json),list(OS_json),list(Primary_type_json),list(Secondary_type_json),list(type_nm_json)



company_list,cpu_brand_list,Display_type_list,GPU_list,OSjson,Primary_type_list,Secondary_type_list,type_nm_list = get_list()

def calculate_megapixel(h_pixel,v_pixel):
    mp = (h_pixel*v_pixel) / 1000000
    return round(mp,2)

resolutions = ["1920x1080", "1366x768", "3840x2160", "3200x1800", "2560x1440", "1600x900", "2560x1600", "2304x1440", "2256x1504", 
               "1920x1200", "1440x900", "2880x1800", "2400x1600", "2160x1440", "2736x1824"]


company = st.selectbox("Select Company",company_list)
model_typ = st.selectbox("Select Model Type",type_nm_list)
cpu = st.selectbox("Select CPU Brand",cpu_brand_list)
res = st.selectbox("Provide Resolution",resolutions)
display_type = st.selectbox("Select Display Type",Display_type_list)
ram = st.selectbox("Select RAM",[8, 4, 16, 6, 12, 2, 32, 24, 64])
gpu = st.selectbox("Select GPU",GPU_list)
ops = st.selectbox("Select Operating System",OSjson)
wt = st.text_input("Enter Weight [0 to 3 g]")
inch = st.text_input("Enter Inches [Normal range 11 to 17 inch]")
prim_stg = st.selectbox("Select Primary Storage",[128, 256, 512, 1024, 2048, 3072, 4096, 500, 6, 10, 12, 16])
prim_stg_typ = st.selectbox("Select Primary Storage Type",Primary_type_list)
scnd_stg = st.selectbox("Select Secondary Storage",[0,128, 256, 512, 1024, 2048, 3072, 4096, 500, 6, 10, 12, 16])
scnd_stg_typ = st.selectbox("Select Secondary Storage Type",Secondary_type_list)


megapixel = calculate_megapixel(int(res.split('x')[0]),int(res.split('x')[-1]))

def get_predictions():
    final_data = []
    if wt != '' or inch != '':
        final_data = [[company_json[company], type_nm_json[model_typ], OS_json[ops], Display_type_json[display_type], cpu_brand_json[cpu],
                    Primary_type_json[prim_stg_typ], Secondary_type_json[scnd_stg_typ],GPU_json[gpu],float(wt),float(inch),megapixel,ram,prim_stg,scnd_stg ]]
    else:
        st.write("Please enter Weight & Inches.")

    predicted = model.predict(final_data)
    st.write(f"Predicted price is : ₹{np.round(np.exp(predicted.item()),2)}")

if st.button('Get Predicitons'):
    get_predictions()
