# 🧘 Yoga Pose Prediction Web App

Welcome to the **Yoga Pose Prediction App**—an interactive Streamlit web tool powered by Deep Learning! This project uses TensorFlow and computer vision to automatically identify popular yoga poses from user-uploaded images.

***

## 🚀 Features

- **Fast Predictions:** Instantly identify yoga poses in any photo
- **Simple Interface:** Drag & drop your image—get results in seconds!
- **Model Confidence:** See how sure the AI is in its prediction
- **Supported Poses:**  
  - Downward Dog 🐕  
  - Goddess 🙆  
  - Plank 💪  
  - Tree 🌳  
  - Warrior II 🏹

***

## 🖥️ Preview

![App Screenshot](<img width="1409" height="615" alt="image" src="https://github.com/user-attachments/assets/defb24a9-3331-413c-b085-62712a7c32de" />
)*

***

## 🛠️ Installation

### 1. **Clone the repository**
```bash
git clone https://github.com/distroagnostic/yoga-pose-prediction.git
cd yoga-pose-prediction
```
### 2. **Setup your Python environment**
It's best to use Python 3.10 or 3.11 for TensorFlow compatibility.
```bash
python -m venv yogaenv
source yogaenv/bin/activate       # For Linux/Mac
yogaenv\Scripts\activate.bat      # For Windows
```

### 3. **Install dependencies**
```bash
pip install -r requirement.txt
```

### 4. **Add your trained model**
Place `yoga_model.h5` in the project root.

### 5. **Run the app**
```bash
streamlit run YogaUI.py
```

***

## 📦 Files

- `YogaUI.py` — Streamlit app source code  
- `yoga.ipynb` — Model training Jupyter notebook  
- `yoga_model.h5` — Saved Keras/TensorFlow yoga pose model  
- `requirement.txt` — List of dependencies

***

## 🎯 Demo

Try uploading an image of yourself doing a yoga pose—see instant, AI-powered feedback!

***

## 🤝 Contributing

Pull requests are welcome! Please open issues for feature requests, bugs, or suggestions.

***

## 💡 How it Works

1. User uploads a yoga pose image.
2. The app preprocesses the image and passes it to a trained CNN model.
3. The model outputs the predicted pose label and confidence score.
4. Results are dynamically displayed in the Streamlit UI.

***

## 📚 Credits

Created by [DistroAgnostic](https://github.com/distroagnostic)  
Model trained and app built using TensorFlow, Streamlit & PIL.

***

## 📄 License

[MIT License](LICENSE)

***

**Namaste & Happy Posing! 🧘**

***
