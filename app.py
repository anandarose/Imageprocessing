import streamlit as st
from PIL import Image, ImageEnhance
import cv2  # Optional, for OpenCV functions
from io import BytesIO
st.title("Image Processing App")

# Image Upload Section
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)

    # Add Processing Options (e.g., sliders, checkboxes)
    brightness_factor = st.slider("Adjust Brightness", 0.5, 2.0, 1.0)
    contrast_factor = st.slider("Adjust Contrast", 0.5, 2.0, 1.0)

    # Apply Image Processing (example: brightness and contrast adjustment)
    enhanced_image = ImageEnhance.Brightness(image).enhance(brightness_factor)
    enhanced_image = ImageEnhance.Contrast(enhanced_image).enhance(contrast_factor)

    # Display Processed Image
    st.image(enhanced_image, caption="Processed Image", use_column_width=True)

    # Optional: Download Button
    download_button = st.button("Download Processed Image")
    if download_button:
        with BytesIO() as buffer:
            enhanced_image.save(buffer, format="JPEG")
            btn_txt = st.download_button(label="Download", data=buffer.getvalue(), file_name="processed_image.jpg", mime="image/jpeg")
