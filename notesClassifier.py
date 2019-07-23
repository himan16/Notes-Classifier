# -*- coding: utf-8 -*-
"""
Created on Sun Jun 30 00:29:34 2019

@author: Himanshu
"""

from keras.models import Sequential
from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout

def cnn_model():
    
    classifier = Sequential()

    classifier.add(Convolution2D(24, 3, 3, input_shape = (124, 124, 3), activation = 'relu'))
    
    classifier.add(MaxPooling2D(pool_size=(2, 2)))

    classifier.add(Convolution2D(24, 3, 3, activation = 'relu'))
    
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    
    classifier.add(Convolution2D(34, 3, 3, activation = 'relu'))
    
    classifier.add(MaxPooling2D(pool_size=(2, 2)))
    
    classifier.add(Flatten())
    
    classifier.add(Dense(output_dim = 40, activation = 'relu'))
    
    classifier.add(Dropout(0.2))
    
    classifier.add(Dense(output_dim = 1, activation = 'sigmoid')) 
    
    classifier.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    
    return classifier