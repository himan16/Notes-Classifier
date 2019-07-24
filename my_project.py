# -*- coding: utf-8 -*-

from keras.preprocessing.image import *
import numpy as np
import matplotlib as plt
import os
import random
from glob import glob
from notesClassifier import cnn_model                               

# Model

classifer = cnn_model()
classifier.load_weights('notesClassifier.h5')

#check model performance on random images

img_path = random.choice(glob('notes/*'))
img = load_img(img_path, target_size = (124, 124, 3)) # this is an PIL image
x = img_to_array(img)/255.0
y = classifier.predict(np.expand_dims(x, axis = 0))
print(np.squeeze(y) < 0.5)

# PREDICTION

def prediction(file_path):
    img = load_img(file_path, target_size = (124, 124, 3))
    x = img_to_array(img)/255.0
    y = classifier.predict(np.expand_dims(x, axis = 0))
    return np.squeeze(y) < 0.5



# create 'notes' folder to store extracted notes image
    
if not os.path.exists(r'C:\Users\Himanshu\Desktop\testDataSet\notes'):
    os.mkdir(r'C:\Users\Himanshu\Desktop\testDataSet\notes')
    
# get filepaths

files = glob(r'C:\Users\Himanshu\Desktop\testDataSet/*.*')

for file_path in files:
    if prediction(file_path):
        file_name = ( file_path.split("testDataSet")[1])
        file_name = file_name[1:]
        print(file_name)
        os.rename(file_path,r'C:\Users\Himanshu\Desktop\testDataSet\notes/' + file_name)
        
        
        