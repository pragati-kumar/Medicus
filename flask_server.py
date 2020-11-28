from flask import Flask, request, jsonify
import numpy as np
import tensorflow.keras.models
import re
import sys
import os
import base64
import random
import cv2
import matplotlib.pyplot as plt
import calendar
import time

import tensorflow as tf
import tensorflow.keras.backend as K

# sys.path.append(os.path.abspath("./model"))
#from load import *
img_dims = 224
model_path = 'model/pneumonia_full_model.h5'


def preprocess_uploaded_image(path):
    img = plt.imread(path)
    img = cv2.resize(img, (img_dims, img_dims))
    img = np.dstack([img, img, img])
    img = img.astype('float32') / 255
    img = img.reshape([1, 224, 224, 3])
    return img


def prediction(model_path, test_image):
    model = tf.keras.models.load_model(model_path)
    a = model.predict(test_image)
    perc = 0.0
    if a >= 0.5:
        predict_string = "Ohh no, you might have Pneumonia."
        perc = a
    else:
        predict_string = "Congrats, you're safe."
        perc = 1.0-a
    prediction = {'prediction_key': predict_string, 'conf': float(perc)}
    # print(predict_string)
    return prediction


app = Flask(__name__)


@app.route('/')
def hello_world():

    return 'Welcome to our Medicus Flask Server!'


@app.route('/detect', methods=['GET', 'POST'])
def detect():

    if(request.method == 'GET'):
        return 'This is a post request test, use post method'

    if(request.method == 'POST'):
        f = request.files['xray']
        filename = f.filename
        epoch = str(calendar.timegm(time.strptime(
            'Jul 9, 2009 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC')))
        f.save(os.getcwd() + '/uploads/' + filename + '-'+epoch)
        img = preprocess_uploaded_image(
            os.getcwd() + '/uploads/' + filename+'-'+epoch)
        prediction_result = prediction(model_path, img)
        return prediction_result
