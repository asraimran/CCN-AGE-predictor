import streamlit as st
import tensorflow as tf
from PIL import Image

def main():
    st.header("How old are you?")
    st.write("Upload an image of yourself below to find out! (preferably a squared image and containing only your face)")
    file = st.file_uploader("Upload Photo")
    if file is not None:
        st.image(file, width=300)
        image = Image.open(file)
        image = tf.image.resize(image, [224,224]) 
        image = tf.keras.preprocessing.image.img_to_array(image)
        image = image / 255.0      
        image = tf.expand_dims(image, axis=0)
        
        model = tf.keras.models.load_model("C:/Users/asrai/age-prediction-master/my_model1.h5")
        age = model.predict(image)
        st.markdown("## You're %i years old according to our model!" %age[0][0])
        st.write("Happy Aging")
    
if __name__ == '__main__':
	main()