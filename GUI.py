# import streamlit as st
# import joblib


# model = joblib.load("text_classifier.joblib")


# st.title("Text Classifier")

# user_input = st.text_input("Enter some text:")

# if user_input:
#     prediction = model.predict([user_input])[0]
#     st.write(f"### Prediction: {prediction}")

import streamlit as st
import joblib

# Load pre-trained model
model = joblib.load("text_classifier.joblib")

# Page configuration
st.set_page_config(page_title="News Classifier", page_icon="📰")

# Title with newspaper emoji
st.markdown("<h1 style='text-align: center;'>📰 News Text Classifier</h1>", unsafe_allow_html=True)

# Large text input
user_input = st.text_area("Enter news/article text here:", height=200)

# Large button
predict_button = st.button("🔍 Predict", use_container_width=True)

# Predict on button click
if predict_button and user_input.strip():
    prediction = model.predict([user_input])[0]
    st.success(f"### 🧠 Prediction: {prediction}")
