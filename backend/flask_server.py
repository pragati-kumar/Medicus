from flask import Flask, request
from scipy.misc import imsave, imread, imresize
import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
import keras.models
import re
import sys
import os
import base64
import cv2

app = Flask(__name__)

# img_dims = 224
# model_path =
# image path =


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

    if a >= 0.5:
        predict_string = "Ohh no, you might have Pneumonia."
    else:
        predict_string = "Congrats, you're safe."
    prediction = {'prediction_key': predict_string}
    # print(predict_string)
    return prediction


@app.route('/')
def hello_world():

    return 'The Flask Server has started successfully on port 5000!'


@app.route('/query/<int:post_data>')
def query_test(post_data):

    return 'Query Returned: %d' % post_data


@app.route('/post_test', methods=['GET', 'POST'])
def post_test():

    if(request.method == 'GET'):
        return 'This is a post request test, use post method'

    if(request.method == 'POST'):
        return request.data


@app.route('/detect', methods=['POST'])
def detect():

    if(request.method == 'POST'):

        f = request.files['xray']
        print(f)
        return 'Image Received'
