import streamlit as st
import joblib

# Load pre-trained model
model = joblib.load("text_classifier.joblib")

# Streamlit GUI
st.title("Text Classifier")

user_input = st.text_input("Enter some text:")

if user_input:
    prediction = model.predict([user_input])[0]
    st.write(f"### Prediction: {prediction}")
