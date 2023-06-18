# Import libraries
import streamlit as st
import pickle
import joblib
import pandas as pd
import numpy as np 

# Configuration Page
st.set_page_config(page_title = "Fradulent Credit Card Detection")
st.markdown("\n")

# Title Style 

st.markdown(
    """
    <h1 style="text-align: center; font-family: 'Arial', sans-serif; color: #336699;">
        Fradulent Credit Card Detection
    </h1>
    """,
    unsafe_allow_html=True)
st.markdown("""<style>p {font-size: 24px;}</style>""",unsafe_allow_html=True)
st.markdown("---")


# File selection
pickle_file = 'C://Users//Honey//Desktop//xgb_model.pkl'
with open(pickle_file, "rb") as f:
    try:
        data = pickle.load(f)
    except pickle.UnpicklingError as e:
        st.error("Error loading pickle file.")
        st.error(str(e))

def load_pickle_file(pickle_file):
    with open(pickle_file, "rb") as f:
        data = pickle.load(f)
    return data

if pickle_file is not None:
    try:
        data = load_pickle_file(pickle_file)
    except pickle.UnpicklingError as e:
        st.error("Error loading pickle file.")
        st.error(str(e))


#Display Page
st.subheader("Enter all required Features")
X_validation = st.text_input("")
X_validation_splited = X_validation.split(",")
print(X_validation)

submit = st.button("Submit")
if submit :
    features  = np.asarray(X_validation_splited , dtype = np.float64)
    prediction = data.predict(features.reshape(1,-1)) 
    if prediction[0] == 0:
        st.write("Legitimate")
    elif prediction[0] == 1:
        st.write("Fruadulent")
     


