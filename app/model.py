import numpy as np 
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from PIL import Image, ImageOps
from tempfile import NamedTemporaryFile
import io
import tensorflow_addons as tfa

def runModel(img):
    # preprocessing the image
    img_data = np.ndarray(shape = (1,256,256,3), dtype = np.float64 )
    img = img.resize((256,256), Image.ANTIALIAS)
    img_array = np.asarray(img)
    img_data[0] = (img_array.astype(np.float64) / 255.0)

    model = load_model('melanoma_model4.h5',custom_objects={'SigmoidFocalCrossEntropy': tfa.losses.SigmoidFocalCrossEntropy()})
    result = model.predict(img_data)
    print("It works")

    percentage_malignant = str(result*100)
    percentage_benign = str(100-(result*100))

    print(result)
    
    if result >= 0.5:
        return 'Dermo Prediction:  ' + percentage_malignant + '%  Malignant'
    else:
        return 'Dermo Prediction:  ' + percentage_benign + '%  Benign'
