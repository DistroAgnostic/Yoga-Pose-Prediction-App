import streamlit as st
try:
    import tensorflow as tf
except ImportError as e:
    st.error(f"TensorFlow failed to import: {e}")
    st.stop()
import numpy as np
from PIL import Image

class PatchedInput(tf.keras.layers.InputLayer):
    def __init__(self, *args, **kwargs):
        if 'batch_shape' in kwargs and 'batch_input_shape' not in kwargs:
            kwargs['batch_input_shape'] = kwargs.pop('batch_shape')
        super().__init__(*args, **kwargs)

@st.cache_resource(show_spinner=True)
def load_model():
    try:
        return tf.keras.models.load_model(
            "yoga_model.h5",
            compile=False,
            custom_objects={"InputLayer": PatchedInput},
        )
    except Exception as e:
        st.error(f"Failed to load model: {e}")
        st.stop()
        
model = load_model()

LABELS = ['downdog', 'goddess', 'plank', 'tree', 'warrior2']
IMGSIZE = (160 ,160)

def prepare_image(img):
    img = img.convert("RGB").resize(IMGSIZE)
    arr = np.array(img, dtype=np.float32) / 255.0
    return np.expand_dims(arr, axis=0)

def predict_pose(img):
    arr = prepare_image(img)
    pred = model.predict(arr)[0]
    pred_idx = np.argmax(pred)
    return LABELS[pred_idx], float(pred[pred_idx])

st.title("Yoga Pose Prediction App")
st.write("Upload a yoga pose image to get the predicted pose and confidence.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=True)
    st.write("Predicting...")
    pose, confidence = predict_pose(image)
    st.success(f"**Predicted Pose:** {pose}")
    st.info(f"**Confidence:** {confidence:.2f}")
