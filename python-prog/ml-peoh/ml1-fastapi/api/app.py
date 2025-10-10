from fastapi import FastAPI, UploadFile, File, HTTPException
import tensorflow as tf 
import numpy as np
from PIL import Image


# initialize the FASTAPI App 
app = FastAPI()
path = "models/cifar10_model.h5"
model = tf.keras.models.load_model(path)
class_name = ["airplane", "automobile", "bird", "cat", "deer", "dog", "frog", "horse", "ship", "truck"]

@app.post("/predict/")
async def predict(file: UploadFile = File(...)): 
    if not file: 
        raise HTTPException(status_code=400, detail="No file upload")
    
    try: 
        img = Image.open(file.file).resize((32, 32))
        img_array = np.array(img).astype("float32") / 255.0
        img_array = np.expand_dims(img_array, axis=0)


        # make the prediction 
        predictions = model.predict(img_array)
        class_idx = np.argmax(predictions)
        class_label = class_name[class_idx]


        return {
            "class": class_label, 
            "confidence": float(predictions[0][class_idx])
        }
    
    except Exception as e: 
        raise HTTPException(status_code=500, detail=f"Prediction Failed: {str(e)}")
    


@app.get("/")
def read_root(): 
    return {
        "message": "welcome to the CIFAR-10 image classification API"
    }

