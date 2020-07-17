from tensorflow import keras
import time
import cv2

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