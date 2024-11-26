import streamlit as st
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow_hub import KerasLayer


# Load model and define target size
def run():
    st.title ('Expression Detection ')
    # Horizontal line 
    st.write('---')

    # input banner 
    st.image('https://idseducation.com/wp-content/uploads/2022/11/Thumbnail-Program-Kemang-12730_In-Your-Face.jpg')
    file = st.file_uploader("Upload an image", type=["jpg", "png"])

    # Load the pre-trained model
    model = load_model('best_model.h5', custom_objects={'KerasLayer': KerasLayer})
    target_size = (224, 224)
    
    def import_and_predict(image_data, model):
        # Load image from uploaded file
        image = load_img(image_data, target_size=target_size)
        img_array = img_to_array(image)
        img_array = tf.expand_dims(img_array, 0)  # Add batch dimension

        # Normalize the image to [0, 1] range
        img_array = img_array / 255.0

        # Make prediction
        predictions = model.predict(img_array)

        # Determine the class index
        idx = np.argmax(predictions, axis=1)[0]  # Get the index of the highest probability

        # Define class labels
        class_name = ['Ahegao', 'Happy', 'Neutral', 'Sad', 'Surprise', 'Angry']
        result = f"Expression Prediction: {class_name[idx]}"

        return result

    # Check if a file is uploaded
    if file is None:
        st.text("Please upload an image file")
    else:
        # Display the image
        st.image(file)

        # Predict the class of the image
        result = import_and_predict(file, model)
        st.write(result)

if __name__ == "__main__":
    run()
