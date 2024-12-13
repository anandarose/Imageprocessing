import streamlit as st
import cv2
import numpy as np
from PIL import Image, ImageEnhance

# App title
st.title("Advanced Image Processing App")
st.write("Upload an image and apply various transformations.")

# File uploader
uploaded_file = st.file_uploader("Upload your image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    # Load the image
    image = Image.open(uploaded_file)
    st.image(image, caption="Original Image", use_column_width=True)
    
    # Convert to NumPy array for OpenCV processing
    img_array = np.array(image)

    # Sidebar options
    st.sidebar.title("Processing Options")
    
    # Apply blur
    blur_amount = st.sidebar.slider("Blur", 0, 50, 0)
    if blur_amount > 0:
        img_array = cv2.GaussianBlur(img_array, (blur_amount * 2 + 1, blur_amount * 2 + 1), 0)

    # Rotate image
    rotate_angle = st.sidebar.slider("Rotate (degrees)", 0, 360, 0)
    if rotate_angle > 0:
        (h, w) = img_array.shape[:2]
        center = (w // 2, h // 2)
        matrix = cv2.getRotationMatrix2D(center, rotate_angle, 1.0)
        img_array = cv2.warpAffine(img_array, matrix, (w, h))

    # Adjust contrast
    contrast_factor = st.sidebar.slider("Contrast", 0.5, 3.0, 1.0)
    if contrast_factor != 1.0:
        enhancer = ImageEnhance.Contrast(Image.fromarray(img_array))
        img_array = np.array(enhancer.enhance(contrast_factor))

    # Display the processed image
    st.image(img_array, caption="Processed Image", use_column_width=True)
