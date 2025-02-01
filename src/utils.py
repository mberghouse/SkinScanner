import os
import cv2
import pandas as pd
import numpy as np
import streamlit as st
from PIL import Image
from models import (
    image_quality_model,
    cancer_binary_model,
    cancer_multiclass_model,
    skin_disease_model,
    oily_dry_model,
    skin_type_model
)

def upload_image():
    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)
        return image
    return None
    
def check_image_quality(image):
    quality_score = image_quality_model.predict(image)
    if quality_score < 0.75:
        retake = st.button("Retake Picture")
        if retake:
            return upload_image()
        else:
            st.button("Continue Anyway")
    return image
    
def classify_cancer(image):
    cancer_prob = cancer_binary_model.predict(image)
    if cancer_prob > 0.75:
        cancer_type = cancer_multiclass_model.predict(image)
        return cancer_prob, cancer_type
    return cancer_prob, None
    
def classify_skin(image):
    skin_diseases = skin_disease_model.predict(image, threshold=0.2)
    oily_dry = oily_dry_model.predict(image)
    skin_type = skin_type_model.predict(image)
    return skin_diseases, oily_dry, skin_type
    
def interpret_results(cancer_prob, cancer_type, skin_diseases, oily_dry, skin_type):
    interpretation = f"Cancer probability: {cancer_prob}\n"
    if cancer_type:
        interpretation += f"Predicted cancer type: {cancer_type}\n"
        interpretation += "Please follow up with a doctor for further evaluation.\n"
    interpretation += f"Skin diseases detected: {', '.join(skin_diseases)}\n"
    interpretation += f"Skin type: {oily_dry}, {skin_type}"
    return interpretation
    
def display_results(interpretation):
    st.subheader("Results")
    st.write(interpretation)
    
def handle_followup():
    question = st.text_input("Ask a follow-up question")
    if question:
        response = conversation.predict(input=question)
        st.write(response)
        
def store_results(cancer_prob, cancer_type, skin_diseases, oily_dry, skin_type):
    # Store the results in a database or file
    # You can use libraries like pandas, SQLAlchemy, or CSV for this purpose
    pass
    
 