import gradio as gr
from tensorflow.keras.models import load_model
from PIL import Image
import numpy as np
import os
import requests
import gdown
model_path = "pneumonia_densenet121.h5"

# Eğer model yoksa indir
if not os.path.exists(model_path):
    print("📥 Model indiriliyor...")

model_url = "https://drive.google.com/uc?id=1bnymkLz41lUlEiV5IYIxgnI1K8wkw10q"
if not os.path.exists(model_path):
    print("📥 Model indiriliyor (gdown)...")
    gdown.download(model_url, model_path, quiet=False)
    print("✅ Model indirildi.")

# Modeli yükle
model = load_model(model_path)

def predict(img):
    img = img.resize((224, 224))
    img = np.array(img) / 255.0
    img = np.expand_dims(img, axis=0)
    pred = model.predict(img)[0][0]
    return "🫁 Zatürre Var" if pred > 0.5 else "✅ Zatürre Yok"

app = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="pil"),
    outputs="text",
    title="Zatürre Tespit Uygulaması",
    description="Göğüs röntgeni yükleyin, model zatürre olup olmadığını tahmin etsin."
)

app.launch()
