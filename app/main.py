import streamlit as st
import numpy as np
#from model import runModel
from PIL import Image
#Application heading
st.title("Dermoverse Skin Cancer Detector (V1)")

#Brief summary of what the application does
st.header("by dermoverse.org)")
st.subheader("This application can classify potential skin cancer images into two classes, whether they are benign or malignant")

#Information of what kind of images should be uploaded.
st.subheader("The images uploaded should be a close up of the suspect skin anomaly ")

# code, to enable users to upload the file.
image = st.file_uploader(label = "Users can uplaod their images here. Note multiple files are not accepted and file type is limited to PNG", type = ['png', 'jpeg'], accept_multiple_files=False,label_visibility="visible")

if image is None:
    st.warning("Please Upload a Image")
    st.stop()
else:
    uploadedImageData = Image.open(image)
    
    st.image(image, caption = image.name, output_format = "auto" )
    modelBtn = st.button("Run Model")
    
    
 finresult = result * 100

    st.write("Dermoverse Console: ", finresult, "%")
    
    if result >= 0,5:
        st.write("Potentially Malignant")
    else:
        st.write("Potentially Benign")
            

#if modelBtn:
    #answer = runModel(image)
    #st.success(answer);
