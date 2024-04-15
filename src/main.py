def main():
    st.title("Skin Classification App")
    
    image = upload_image()
    if image:
        image = check_image_quality(image)
        cancer_prob, cancer_type = classify_cancer(image)
        skin_diseases, oily_dry, skin_type = classify_skin(image)
        interpretation = interpret_results(cancer_prob, cancer_type, skin_diseases, oily_dry, skin_type)
        display_results(interpretation)
        handle_followup()
        store_results(cancer_prob, cancer_type, skin_diseases, oily_dry, skin_type)