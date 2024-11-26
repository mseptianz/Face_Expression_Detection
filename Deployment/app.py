# import libraries 
import streamlit as st
import eda
import prediction

# Navigation Section
navigation = st.sidebar.selectbox('Pilih Halaman ',('Predictor','Eda'))

# Page
if navigation == 'Predictor':
    prediction.run()
elif navigation == 'Eda':
    eda.run()