import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)

#set score
score = 0

#set question number
question = 1

#setup A B and C buttons
GPIO.setup(23, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
GPIO.setup(24, GPIO.IN, pull_up_down = GPIO.PUD_UP)
GPIO.setup(25, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

#main text that appears on screen for user
print("You find a wallet, do you...")
print("A. Find who it belongs to")
print("B. Keep it and spend it on yourself")
print("C. Give it to the police and let them handle it")
print("A, B or C?")

#while loop to run code if button is pressed
#Question 1
while question == 1:
    if(GPIO.input(23) == 1):
        print("You chose, A. Find who it belongs to")
        time.sleep(1)
        question = question +1
    elif(GPIO.input(24) == 0):
        print("You chose, B. Keep it and spend it on yourself")
        time.sleep(1)
        question = question +1
    elif(GPIO.input(25) == 1):
        print("You chose, C. Give it to the police and let them handle it")
        time.sleep(1)
        score = score +1
        question = question +1
print("Your score is ", + score)

#Question 2
print("Choose A, B, or C")
while question == 2:
    if(GPIO.input(23)== 1):
        print("A is a letter")
        time.sleep(1)
        question = question +1
    elif(GPIO.input(24)== 0):
        print("B is a letter")
        time.sleep(1)
        question = question +1
    elif(GPIO.input(25) == 1):
        print("C is a letter")
        time.sleep(1)
        question = question +1

print("Your score is ", + score)

#Question 3
print("Choose A, B, or C")
while question == 3:
    if(GPIO.input(23)== 1):
        print("A is a letter")
        time.sleep(1)
        question = question +1
    elif(GPIO.input(24)== 0):
        print("B is a letter")
        time.sleep(1)
        question = question +1
    elif(GPIO.input(25) == 1):
        print("C is a letter")
        time.sleep(1)
        question = question +1

print("Your score is ", + score)

#Question 4
print("Choose A, B, or C")
while question == 4:
    if(GPIO.input(23)== 1):
        print("A is a letter")
        time.sleep(1)
        question = question +1
    elif(GPIO.input(24)== 0):
        print("B is a letter")
        time.sleep(1)
        question = question +1
    elif(GPIO.input(25) == 1):
        print("C is a letter")
        time.sleep(1)
        question = question +1

print("Your score is ", + score)
GPIO.cleanup()
