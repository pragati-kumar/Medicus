from flask import Flask, request, jsonify
from scipy.misc import imread, imresize, imsave
import numpy as np
import tensorflow.keras.models
import re
from werkzeug.utils import secure_filename
import sys
import os
import base64
import os
import numpy as np
import pandas as pd
import random
import cv2
import matplotlib.pyplot as plt
import calendar
import time

import tensorflow as tf
import tensorflow.keras.backend as K
from tensorflow.keras.models import Model, Sequential
from tensorflow.keras.layers import Input, Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.layers import Conv2D, SeparableConv2D, MaxPool2D, LeakyReLU, Activation
from tensorflow.keras.optimizers import Adam
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.callbacks import ModelCheckpoint, ReduceLROnPlateau, EarlyStopping

from os import listdir
from os.path import isfile, join
from PIL import Image
import glob
# sys.path.append(os.path.abspath("./model"))
#from load import *
img_dims = 224
model_path = 'pneumonia_full_model.h5'


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
        f = request.files['the_file']
        filename = f.filename
        epoch = str(calendar.timegm(time.strptime(
            'Jul 9, 2009 @ 20:02:58 UTC', '%b %d, %Y @ %H:%M:%S UTC')))
        f.save(os.getcwd() + '/uploads/' + filename + '-'+epoch)
        img = preprocess_uploaded_image(
            os.getcwd() + '/uploads/' + filename+'-'+epoch)
        prediction_result = prediction(model_path, img)
        return prediction_result
