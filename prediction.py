from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import cv2 
import numpy as np
def prediction(saved_image):
    index = ["no","yes"]
    model = load_model("BTD2.h5")
    img = image.load_img("./static/TI/"+saved_image,target_size = (64,64))
    x = image.img_to_array(img)
    x = np.expand_dims(x,axis=0)
    pred = model.predict_classes(x) 
    print(index[pred[0]])
    return index[pred[0]]