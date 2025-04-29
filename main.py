import streamlit as st
import cv2
import numpy as np
from PIL import Image
from analysis import analyze_brightness, analyze_sharpness, analyze_contrast, analyze_saturation
from suggestions import generate_suggestions

# Set Streamlit page configuration with a wide layout and a custom icon
st.set_page_config(page_title="Basic Photo Analyzer", layout="wide", page_icon="📷")

# Custom CSS for better styling with dark theme and attractive colors
st.markdown(
    """
    <style>
    body {
        background-color: #121212;
        color: #e0e0e0;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    .stApp {
        background-color: #121212;
    }
    .stButton>button {
        background-color: #1e88e5;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 24px;
        transition: background-color 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #1565c0;
        color: white;
    }
    .stSidebar {
        background-color: #1f1f1f;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 0 15px rgba(30, 136, 229, 0.5);
        color: #e0e0e0;
    }
    h1, h2, h3 {
        color: #90caf9;
    }
    .metric {
        background-color: #1e1e1e;
        padding: 1rem;
        border-radius: 10px;
        box-shadow: 0 0 10px rgba(30, 136, 229, 0.7);
        margin-bottom: 1rem;
        color: #bbdefb;
    }
    .suggestion {
        background-color: #263238;
        padding: 0.75rem 1rem;
        border-radius: 8px;
        margin-bottom: 0.5rem;
        color: #cfd8dc;
        box-shadow: 0 0 8px rgba(38, 50, 56, 0.8);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Sidebar for analysis options
st.sidebar.header("Analysis Options")
analyze_brightness_opt = st.sidebar.checkbox("Brightness", value=True)
analyze_sharpness_opt = st.sidebar.checkbox("Sharpness", value=True)
analyze_contrast_opt = st.sidebar.checkbox("Contrast", value=True)
analyze_saturation_opt = st.sidebar.checkbox("Saturation", value=True)

# Main header with icon
st.markdown("## 📷 Basic Photo Analyzer")
st.markdown("Analyze your photos for Brightness, Sharpness, Contrast, and Saturation with suggestions to improve.")

# File uploader for image
uploaded_file = st.file_uploader("Upload an image to analyze", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Convert to OpenCV format
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)

    brightness = analyze_brightness(image_cv) if analyze_brightness_opt else None
    sharpness = analyze_sharpness(image_cv) if analyze_sharpness_opt else None
    contrast = analyze_contrast(image_cv) if analyze_contrast_opt else None
    saturation = analyze_saturation(image_cv) if analyze_saturation_opt else None

    metrics = {}
    if brightness is not None:
        metrics["Brightness"] = brightness
    if sharpness is not None:
        metrics["Sharpness"] = sharpness
    if contrast is not None:
        metrics["Contrast"] = contrast
    if saturation is not None:
        metrics["Saturation"] = saturation

    # Display metrics in columns with styled boxes
    cols = st.columns(len(metrics))
    for idx, (metric, value) in enumerate(metrics.items()):
        with cols[idx]:
            st.markdown(f"<div class='metric'><h3>{metric}</h3><p style='font-size:24px; font-weight:bold;'>{value:.2f}</p></div>", unsafe_allow_html=True)

    suggestions = generate_suggestions(
        brightness if brightness is not None else 0,
        sharpness if sharpness is not None else 0,
        contrast if contrast is not None else 0,
        saturation if saturation is not None else 0,
    )

    st.markdown("### Suggestions")
    for suggestion in suggestions:
        st.markdown(f"<div class='suggestion'>{suggestion}</div>", unsafe_allow_html=True)

else:
    st.info("Please upload an image to analyze.")
