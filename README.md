# SkinScanner

SkinScanner is a Python-based application designed to analyze skin images for cancer presence, skin type, and overall skin health. This innovative tool leverages deep learning models to provide immediate insights based on images you either upload or capture using your webcam. The application also features an integrated chat interface powered by OpenAI's o3-mini, allowing you to ask detailed follow-up questions about your analysis results.

## Features

- **Image Analysis**: Upload or capture a skin image using your webcam.
- **Advanced Insights**: 
  - Detect signs of skin cancer.
  - Identify common skin diseases.
  - Evaluate skin type and condition.
- **Interactive Chat**: Ask follow-up questions and receive detailed responses from a dermatology assistant powered by OpenAI.
- **User-Friendly Navigation**: Enjoy a welcoming landing page along with a dedicated analysis page for a seamless experience.

## How It Works

1. **Landing Page**:  
   A friendly and informative landing page introduces the app and its features. You can easily navigate to the analysis page by clicking the "Proceed to Analysis" button.

2. **Image Input**:  
   Choose your preferred method to submit an image:
   - **Upload Image**: Select an image from your device.
   - **Webcam Capture**: Use your webcam to take a picture.

3. **Image Analysis**:  
   - The app first checks the image quality.  
   - It then processes the image using pre-trained deep learning models from the `weights` folder to assess cancer probability, identify skin diseases, and determine your skin type.

4. **Results & Chat Interface**:  
   - Analysis results are displayed along with an interpretation.  
   - The integrated chat interface allows you to ask questions about your results, providing further insights to help you understand your skin health better.

## Installation

Ensure you have Python 3.7+ installed. From the project's root directory, install the required packages using pip:

```bash
pip install -r requirements.txt
```

## Usage

Launch the application using Streamlit by running the following command in your terminal (from the project's root directory):

```bash
streamlit run src/index.py
```

This will open the app in your default web browser. Start on the landing page and click "Proceed to Analysis" to begin uploading or capturing images and exploring the analysis and chat features.

## File Structure

```
.
├── README.md                  # Project documentation
├── requirements.txt           # List of required Python packages
└── src
    ├── app.py                 # Landing page implementation
    ├── index.py               # Main entry point for multipage routing
    ├── main.py                # Analysis page implementation (image analysis & chat interface)
    ├── models.py              # Model definitions and initialization using weights from the 'weights' folder
    └── utils.py               # Utility functions for image upload, quality check, analysis, and result interpretation
```

## Weights & Trained Models

Ensure that the `weights` folder contains your trained model weights:
- `weights/image_quality_model.pth`
- `weights/cancer_binary_model.pth`
- `weights/cancer_multiclass_model.pth`
- `weights/skin_disease_model.pth`
- `weights/oily_dry_model.pth`
- `weights/skin_type_model.pth`

These weights are loaded by the models defined in `src/models.py` to perform the required predictions.

## Disclaimer

SkinScanner is intended for informational purposes only and is not a substitute for professional medical advice. Always consult a qualified healthcare provider for any concerns regarding your health.


