# -*- coding: utf-8 -*-
"""
Created on Mon Jul  1 15:45:44 2019

@author: Himanshu
"""
'''from keras.preprocessing.image import ImageDataGenerator
import notesClassifier 
classifier = notesClassifier.cnn_model()
# Data Augumentation
train_datagen = ImageDataGenerator(
                                    rescale=1./255,    
                                    rotation_range=40,
                                    width_shift_range=0.2,
                                    height_shift_range=0.2,
                                    shear_range=0.2,
                                    zoom_range=0.2,
                                    horizontal_flip=True,
                                    fill_mode='nearest')

test_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
        'training_set', # this is the target data directory
        target_size=(124, 124), # all images will be resized to 124 x 124
        batch_size=4,
        class_mode='binary')  # since we use binary_crossentropy loss, we need binary labels

test_set = test_datagen.flow_from_directory(
        'test_set',
        target_size=(124, 124),
        batch_size=4,
        class_mode='binary')

x, y = next(train_generator)
print(x.shape)
print(y.shape)

# Train the model
from PIL import ImageFile
ImageFile.LOAD_TRUNCATED_IMAGES = True
classifier.fit_generator(
        train_generator,
        steps_per_epoch=1999,
        epochs=5,
        validation_data=test_set,
        validation_steps=32)


classifier.save_weights('notesClassifier.h5')

from glob import glob
import random
from keras.preprocessing.image import*
import numpy as np
img_path = random.choice(glob('others/*'))
img = load_img(img_path, target_size = (124, 124))
x = img_to_array(img)/255.0
print(x.shape)
y = classifier.predict(np.expand_dims(x, axis = 0))
print(y)
y.shape
print(np.squeeze(y) > 0.5)
                                  '''
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
    
if not os.path.exists('notes'):
    os.mkdir('notes')
    

# extract notes image from whatsapp image folder
    #This PC\Galaxy J2\Phone\WhatsApp\Media\WhatsApp Images
from glob import glob
files  =  glob('C:\Users\Himanshu\Desktop\test image\*.*')    
 
#C:\Windows\System32\cmd.exe