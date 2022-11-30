#import packages
import streamlit as st
import pandas as pd
import joblib
from sklearn.model_selection import GridSearchCV

#set web page
st.set_page_config(
    page_title='Prediksi Harga Rumah', 
    page_icon=':house:',
    layout="centered", 
    initial_sidebar_state="auto", 
    menu_items=None)
st.write("""
# Prediksi Harga Rumah
Aplikasi ini akan memprediksi harga rumah berdasarkan dataset yang tersedia di kaggle
""")
st.sidebar.header('Silahkan unggah file CSV sesuai dengan contoh!')
st.sidebar.markdown("""
*Informasi dalam file CSV yang diunggah akan digunakan sebagai parameter prediksi!*
""")
st.sidebar.markdown("""
[Contoh file CSV](https://github.com/maulanaibrohim/house-price-predictor/blob/main/contoh_input_file.csv)
""")

#set upload file for user (type:csv)
uploaded_file = st.sidebar.file_uploader("Silahkan unggah file CSV anda di sini!", type=["csv"])
if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    st.sidebar.write('Silahkan unggah file CSV anda!')
    df = pd.read_csv('https://raw.githubusercontent.com/maulanaibrohim/house-price-predictor/main/contoh_input_file.csv')

#set main page
st.subheader ('File masukkan pengguna')
if uploaded_file is not None:
    st.write(df)
else:
    st.write('Silahkan unggah file csv anda! Saat ini mnggunakan contoh input file')
    st.write(df)

#load model machine learning
load_model = joblib.load('house_predict.pkl')
#make prediction
prediction = load_model.predict(df).round(decimals=3)
#show prediction
st.header('Perkiraan harga rumah berdasar input yang anda masukkan')
st.subheader(f'{prediction} USD')