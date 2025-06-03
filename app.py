import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import os

# Load model (update path if needed)
MODEL_PATH = os.path.join(os.path.dirname(__file__), "model_1_03333330.h5")
model = tf.keras.models.load_model(MODEL_PATH, compile=False)

# Update this list with your actual class names in the order your model predicts them
class_names = [
    'Bacterial Blight',
    'Curl Virus',
    'Fusarium Wilt',
    'Healthy',
    'Leaf Spot',
    'Root Rot'
]

st.set_page_config(page_title="Cotton Plant Disease Checker", page_icon="🌱", layout="centered")
st.title("🌱 Cotton Plant Disease Checker")
st.write("Upload a cotton plant leaf image to detect disease using deep learning.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_column_width=True)
    img = image.resize((256, 256))
    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction[0])]
    confidence = np.max(prediction[0]) * 100
    st.success(f"Prediction: {predicted_class} ({confidence:.2f}%)")
    st.progress(int(confidence))
else:
    st.info("Please upload a cotton plant leaf image.")
