import streamlit as st
import numpy as np
import sys

sys.path.append("Users/bxrdxs/Desktop/SkinCancerApp/app_copy")

from model import runModel
from PIL import Image

#Application heading
st.title("Dermoverse Skin Cancer Detector")

#Brief summary of what the application does
st.header("This application can classify potential skin cancer images into two classes, whether they are benign or malignant")
st.subheader("Note that only self-made pictures (not zoom, not perfect light, not high definition) are allowed ")

#Information of what kind of images should be uploaded.
st.subheader("The images uploaded should be a close up of the suspect skin anomoly ")

# code, to enable users to upload the file.
image = st.file_uploader(label = "Users can uplaod their images here. Note multiple files are not accepted and files types are limited to PNG and JPEG", type = ['png', 'jpeg'], accept_multiple_files=False,label_visibility="visible")

if image is None:
    st.warning("Please Upload a Image")
    st.stop()
else:
    uploadedImageData = Image.open(image)
    
    st.image(image, caption = image.name, output_format = "auto" )
    modelBtn = st.button("Run Model")

if modelBtn:
    answer = runModel(uploadedImageData)
    st.success(answer);


        
