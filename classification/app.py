
import os 
import streamlit as st
from joblib import load

MODEL_LOCATION=['models/nb_model.joblib','nb_model.joblib'] #path and filename of the model
VECTORIZER_LOCATION=['models/count_vectorizer.joblib','count_vectorizer.joblib'] #path and filename of the vectorizer

#goes thropugh the list of path 
def find_first(paths):
    for path in paths:
        if os.path.exists (path):
            return path
    raise FileNotFoundError ("No valid path found in the list.")

#streamlit page configuration 
st.set_page_config(page_title="spam classifier",layout="centered")
st.title ("Spam Classifier")

model_path=find_first (MODEL_LOCATION)
vect_path=find_first (VECTORIZER_LOCATION)

if model_path and vect_path:
    try:
        model=load (model_path)
        vectorizer=load (vect_path)
        st.sidebar.success (f"Model and Vectorizer loaded successfully!'{os.path.basename (model_path)}'and'{os.path.basename (vect_path)}'")
    except Exception as e:
        st.sidebar.error (f"Error loading model or vectorizer: {e}")
        st.stop()
else:
    st.sidebar.error ("Model or Vectorizer file not found.")
    st.stop()