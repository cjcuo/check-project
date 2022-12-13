# UI Library
import streamlit as st 
from streamlit_option_menu import option_menu

# Base Libraries
import pandas as pd
import joblib

import time


############# Data and Saved model ##############
data = pd.read_csv("Bigmartsalesdata.csv")
model = joblib.load("bigmart.pkl")


########## UI Background ###################

def add_bg_from_url():
    st.markdown(
         f"""
         <style>
         .stApp {{
             background-image: url("https://cdn.wallpapersafari.com/6/34/9zypSX.jpg");
             background-attachment: fixed;
             background-size: cover
         }}
         </style>
         """,
         unsafe_allow_html=True
     )


add_bg_from_url()


########################################### UI ##########################
with st.sidebar:
    choose = option_menu("BigMart Sales Data Analysis", ["Project Info", "Data Studied", "Predictions"],
                         icons=['house', 'table', "tags-fill", 'tags-fill'],
                         menu_icon="app-indicator", default_index=0,
                         styles={
        "container": {"padding": "5!important", "background-color": "#fafafa"},
        "icon": {"color": "black", "font-size": "25px"}, 
        "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
    )

if choose == "Project Info":
    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">About the Project:</p>', unsafe_allow_html=True)    

    st.markdown(""" <style> .para {
        font-size:20px ; font-family: 'Calibri'; color: black; text-align: 'justify'}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="para">Bigmart sales data have been analyzed using Statistical and Machine Learning</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .para {
        font-size:20px ; font-family: 'Calibri'; color: black; text-align: 'justify'}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="para">In This Project we had analyzed big mart sales for the both outlet info and item info.</p>', unsafe_allow_html=True)

elif choose == "Data Studied":
    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">Data Info:</p>', unsafe_allow_html=True)    

    st.markdown(""" <style> .para {
        font-size:20px ; font-family: 'Calibri'; color: black; text-align: 'justify'}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="para">Data is taken from open-source.</p>', unsafe_allow_html=True)

    st.markdown(""" <style> .para {
        font-size:20px ; font-family: 'Calibri'; color: black; text-align: 'justify'}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="para">Collected data is huge and having duplicates, unwanted columns for the analysis. These were handled</p>', unsafe_allow_html=True)
    
    st.markdown(""" <style> .para {
        font-size:20px ; font-family: 'Calibri'; color: black; text-align: 'justify'}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="para"><b>Sample of Raw Data Collected:</b></p>', unsafe_allow_html=True)
    st.dataframe(data.head())
    st.markdown(""" <style> .para {
        font-size:20px ; font-family: 'Calibri'; color: black; text-align: 'justify'}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="para"><b>From the above data Item_Outlet_Sales is our Output column for analysis and prediction. We can predict the sales by giving other columsn data.</b></p>', unsafe_allow_html=True)

elif choose == "Predictions":
    st.markdown(""" <style> .font {
        font-size:30px ; font-family: 'Cooper Black'; color: #FF9633;}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="font">We can estimate the sales value for the mentioned features in data.</p>', unsafe_allow_html=True) 

    ########### Predictions on CSV  Data###########
    st.markdown(""" <style> .para {
        font-size:20px ; font-family: 'Calibri'; color: black; text-align: 'justify'}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="para"><b>Predict Sales on New data</b></p>', unsafe_allow_html=True)

#### Predictions on Test Data #######    
    testdata = st.file_uploader("Upload data for prediction without sales column with the other columns mentioned:")
    if testdata is not None:
        df = pd.read_csv(testdata)
        st.write("First 5 rows of Uploaded Data:")
        st.write(df)
    else:
        st.write("No Data Given")
    
    if st.button("Predict"):
        with st.spinner("Predicting......"):
            predictions = model.predict(df)
            time.sleep(5)
            st.success("Done!.")
            df['Item_Outlet_Sales'] = predictions
            st.write("**Generated Predictions.....**")
            st.dataframe(df)
    
    ##### Prediction on Single review Code #####

    st.markdown(""" <style> .para {
        font-size:20px ; font-family: 'Calibri'; color: black; text-align: 'justify'}
        </style> """, unsafe_allow_html=True)
    st.markdown('<p class="para"><b>Prediction on a Single Input row:</b></p>', unsafe_allow_html=True)

    st.write("Fill out the form values to get input row")

    col1, col2 = st.columns(2)
    with col1:
        weight = st.number_input("Enter Item_Weight")
    with col2:
        fat = st.selectbox("Select Fat_Type", data.Item_Fat_Content.unique())
    
    col3, col4 = st.columns(2)
    with col3:
        visibility = st.number_input("Enter Item_Visibility Percentage")
    with col4:
        type = st.selectbox("Select Item_Type",data.Item_Type.unique())
    
    col5, col6 = st.columns(2)
    with col5:
        mrp = st.number_input("Enter Item_MRP")
    with col6:
        outyears = st.number_input("Enter Number of Years Outltet Established")

    col7, col8 = st.columns(2)
    with col7:
        outsize = st.selectbox("Select Outlet_Size", data.Outlet_Size.unique())
    with col8:
        outlocation = st.selectbox("Select Outlet_Location_Type",data.Outlet_Location_Type.unique())

    col9, col10 = st.columns(2)
    with col9:
        outtype = st.selectbox("Select Outlet_Type",data.Outlet_Type.unique())


    if st.button("Estimate Price"):
        values = [[weight,fat,visibility,type,mrp,outyears,outsize,outlocation,outtype]]
        check = pd.DataFrame(values, columns = data.columns[0:9])
        st.write("Given Data")
        st.dataframe(check)
        st.write("**Estimated Sales Value:**")
        price = round(model.predict(check)[0])
        price = str(price)+"$"
        st.subheader(price)