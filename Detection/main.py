#user defined modules
import plot
import train_model as tm
import image_preprocess

#pre-defined modules
import os
import sys
import numpy as np
import tensorflow as tf
from tensorflow import keras
from tensorflow.keras.models import Model
from tensorflow.keras.applications.resnet50 import decode_predictions

#available Error types in this file
Error1 = '\nError: model not found make sure the model is present inside the current working directory'
Error2 = '\nError: Courrupt image or size is not 300x300x3'
Error3 = '\nError: unable to fetch images'

def start_predictions(model):
  path = input('/Users/ayushraj/Desktop/Demo')
  if os.path.isdir(path) == True:
    for image_Path in range(len(os.listdir(path))):
      image_instance = image_preprocess.resize_(image_Path) #resize_ function is defined in image_resize.py
      try:
        predictions = model.predict(image_instance)
        predictions.append(predictions)
      except:
        print(Error3)
        
  else:
    image_instance = image_preprocess.resize_(path)
    try:
      predictions = model.predict(image_instance)
    except:
      print(Error2)

  plot.plot_predictions(predictions) #plot_ function is defined in plot.py

def start():
  if len(sys.argv) > 3:
    sys.exit("\nError: main.py except only 1 argument 'train_model'")
  elif len(sys.argv) == 2 and sys.argv[1] == 'train_model':
    tm.load_data()
    tm.create_data()
    tm.create_generator()
    if len(sys.argv) == 3 and sys.argv[2] == 'existing':
      model = tm.load_existing_model()
    else:
      model = tm.create_model_ResNet50()
      model = tm.compile_model(model)

    if model == False:
      sys.exit(Error1)
    else:
      tm.fit_model(model)
      model.save('trained_model_GlaucomaDetecton.h5')
    return model

  elif len(sys.argv) == 1 or sys.argv[1] == 'make_predictions':
    model = tm.load_existing_model()
    if model == False:
      sys.exit(Error1)
    return model

model = start()
if input("\npress 'P' for making predictions: ") == 'P':
  start_predictions(model)
