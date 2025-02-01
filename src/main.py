import streamlit as st
from openai import OpenAI
from PIL import Image
import cv2
from utils import (
    upload_image,
    check_image_quality,
    classify_cancer,
    classify_skin,
    interpret_results,
    display_results,
    store_results
)

# Initialize OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def capture_from_webcam():
    img_file_buffer = st.camera_input("Take a picture")
    if img_file_buffer is not None:
        image = Image.open(img_file_buffer)
        return image
    return None

def main():
    st.title("Skin Classification App")
    
    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []
    
    # Image input selection
    input_method = st.radio("Choose input method:", ["Upload Image", "Use Webcam"])
    
    image = None
    if input_method == "Upload Image":
        image = upload_image()
    else:
        image = capture_from_webcam()
    
    if image:
        image = check_image_quality(image)
        cancer_prob, cancer_type = classify_cancer(image)
        skin_diseases, oily_dry, skin_type = classify_skin(image)
        interpretation = interpret_results(cancer_prob, cancer_type, skin_diseases, oily_dry, skin_type)
        display_results(interpretation)
        
        # Chat interface
        st.subheader("Ask follow-up questions")
        
        # Display chat history
        for message in st.session_state.messages:
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
        
        # Chat input
        if prompt := st.chat_input("Ask a question about your results"):
            # Prepare context for the AI
            context = f"Context: {interpretation}\nUser question: {prompt}"
            
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)
            
            with st.chat_message("assistant"):
                stream = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": "You are a helpful dermatology assistant. Use the provided context to answer questions about the skin analysis results."},
                        *[{"role": m["role"], "content": m["content"]} for m in st.session_state.messages],
                        {"role": "user", "content": context}
                    ],
                    stream=True,
                )
                response = st.write_stream(stream)
            st.session_state.messages.append({"role": "assistant", "content": response})
        
        store_results(cancer_prob, cancer_type, skin_diseases, oily_dry, skin_type)

if __name__ == "__main__":
    main()