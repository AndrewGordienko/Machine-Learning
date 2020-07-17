import tensorflow as tf
from tensorflow import keras
import os
import zipfile
from keras_preprocessing.image import ImageDataGenerator
import time
import cv2

local_zip = '/tmp/rps.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp/')
zip_ref.close()

local_zip = '/tmp/rps-test-set.zip'
zip_ref = zipfile.ZipFile(local_zip, 'r')
zip_ref.extractall('/tmp/')
zip_ref.close()

rock_dir = os.path.join('/tmp/rps/rock')
paper_dir = os.path.join('/tmp/rps/paper')
scissors_dir = os.path.join('/tmp/rps/scissors')
rock_files = os.listdir(rock_dir)
paper_files = os.listdir(paper_dir)
scissors_files = os.listdir(scissors_dir)

TRAINING_DIR = "/tmp/rps/"
training_generator = ImageDataGenerator(
    rescale=1./255,
    rotation_range=40,
    width_shift_range=0.2,
    height_shift_range=0.2)
train_generator = training_generator.flow_from_directory(
    TRAINING_DIR,
    target_size=(150, 150),
    class_mode='categorical',
    batch_size=150)

VALIDATION_DIR = "/tmp/rps-test-set/"
validation_generator = ImageDataGenerator(
    rescale=1./255)
validation_generator = validation_generator.flow_from_directory(
    VALIDATION_DIR,
    target_size=(150, 150),
    class_mode='categorical',
    batch_size=150)

model = tf.keras.models.Sequential([
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu', input_shape=(150, 150, 3)),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(64, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(128, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(256, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Conv2D(512, (3, 3), activation='relu'),
    tf.keras.layers.MaxPooling2D(2, 2),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dropout(0.5),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(3, activation='softmax')
])

model.compile(loss='categorical_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
history = model.fit(train_generator, epochs=50, steps_per_epoch=20, validation_data=validation_generator, verbose=1,
                    validation_steps=3)
model.save('C:/Users/andrew/Desktop/All Code/lilo')


stitch = keras.models.load_model('C:/Users/andrew/Desktop/All Code/lilo')

cap = cv2.VideoCapture(0)
cap.set(3, 240)
cap.set(4, 240)

dictionary = {'rock': 0, 'paper': 1, 'scissors': 2}


def getting_value(dictionary):
    for key, value in dictionary.items():
        if value == prediction:
            temp = key
    return temp


val = "Y"

while val == "Y":
    print("__________________________")
    print("Welcome to a game of rock-paper-scissors!")
    time.sleep(0.5)
    print("Let's play!")
    time.sleep(1)
    print("__________________________")
    print("Rock")
    time.sleep(1)
    print("Paper")
    time.sleep(1)
    print("Scissors")
    time.sleep(1)
    print("Shoot")
    time.sleep(1)
    success, img = cap.read()
    cv2.imshow("video", img)
    img = cv2.resize(img, (150, 150))
    img = img / 255.0
    prediction = stitch.predict_classes(img.reshape(1, 150, 150, 3))
    if getting_value(dictionary) == "rock":
        print("Paper")
    if getting_value(dictionary) == "paper":
        print("Scissors")
    if getting_value(dictionary) == "scissors":
        print("Rock")
    print("Good Game!")
    val = input("Would you like to play again?(Y or N): ")

print("Please play again sometime!")