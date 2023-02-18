import numpy as np 
from tensorflow.keras.models import load_model
from tesnorflow.keras.preprocessing import image
from PIL import Image, ImageOps
from tempfile import NamedTemporaryFile
import io

def runModel(img):
    # preprocessing the image
    img_data = np.ndarray(shape = (1,256,256,3), dtype = np.float64 )
    img = img.resize((256,256), Image.ANTIALIAS)
    img_array = np.asarray(img)
    img_data[0] = (img_array.astype(np.float64) / 255.0)

    model = load_model('melanoma_model4.h5')
    result = model.predict(img_data)

    if result >= 0.5:
        return 'Malignant'
    else:
        return 'Benign'

