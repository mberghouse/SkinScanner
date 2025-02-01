import streamlit as st
#from models import image_quality_model, cancer_binary_model, cancer_multiclass_model, skin_disease_model, oily_dry_model, skin_type_model

def main():
    st.set_page_config(page_title="SkinScanner", page_icon="🩺", layout="wide")
    
    # Landing page header
    st.title("Welcome to SkinScanner")
    st.write("A comfortable and innovative solution for analyzing your skin conditions!")
    
    # Display an image (update the URL to your own logo or relevant image)
    st.image("https://via.placeholder.com/800x400.png?text=Skin+Scanner", use_column_width=True)
    
    # Landing page description and features
    st.markdown("""
    **SkinScanner** is an all-in-one application for skin analysis:
    
    - Detect signs of skin cancer
    - Identify common skin diseases 
    - Evaluate skin type and condition
    
    Use our tool to upload an image or capture one using your webcam. Our advanced models provide immediate
    insights and interpretations of your skin health.
    """)
    
    st.markdown("""
    ### How It Works:
    1. **Image Input:** Upload an image or capture one using your webcam.
    2. **Analysis:** The app processes your image with pre-trained deep learning models.
    3. **Results & Insights:** Receive detailed results and have follow-up questions answered.
    
    *Disclaimer: This application is for informational purposes only and is not a substitute for professional 
    medical advice. Always consult with a healthcare professional for any concerns.*
    """)
    
    # Navigation to the analysis page
    if st.button("Proceed to Analysis"):
        st.session_state.page = "analysis"

if __name__ == "__main__":
    main()