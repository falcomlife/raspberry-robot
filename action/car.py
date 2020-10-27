import RPi.GPIO as GPIO

leftFront1 = 11
leftFront2 = 12
rightFront1 = 13
rightFront2 = 15
leftBack1 = 16
leftBack2 = 18
rightBack1 = 22
rightBack2 = 7

action = ""
class Car:
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(leftFront1, GPIO.OUT)
        GPIO.setup(leftFront2, GPIO.OUT)
        GPIO.setup(rightFront1, GPIO.OUT)
        GPIO.setup(rightFront2, GPIO.OUT)
        GPIO.setup(leftBack1, GPIO.OUT)
        GPIO.setup(leftBack2, GPIO.OUT)
        GPIO.setup(rightBack1, GPIO.OUT)
        GPIO.setup(rightBack2, GPIO.OUT)

    def forward(self):
        print("forward")
        GPIO.output(leftFront1, GPIO.HIGH)
        GPIO.output(leftFront2, GPIO.LOW)
        GPIO.output(rightFront1, GPIO.HIGH)
        GPIO.output(rightFront2, GPIO.LOW)
        GPIO.output(leftBack1, GPIO.HIGH)
        GPIO.output(leftBack2, GPIO.LOW)
        GPIO.output(rightBack1, GPIO.HIGH)
        GPIO.output(rightBack2, GPIO.LOW)

    def backward(self):
        print("backward")
        GPIO.output(leftFront1, GPIO.LOW)
        GPIO.output(leftFront2, GPIO.HIGH)
        GPIO.output(rightFront1, GPIO.LOW)
        GPIO.output(rightFront2, GPIO.HIGH)
        GPIO.output(leftBack1, GPIO.LOW)
        GPIO.output(leftBack2, GPIO.HIGH)
        GPIO.output(rightBack1, GPIO.LOW)
        GPIO.output(rightBack2, GPIO.HIGH)

    def left(self):
        print("left")
        GPIO.output(leftFront1, GPIO.LOW)
        GPIO.output(leftFront2, GPIO.HIGH)
        GPIO.output(rightFront1, GPIO.HIGH)
        GPIO.output(rightFront2, GPIO.LOW)
        GPIO.output(leftBack1, GPIO.LOW)
        GPIO.output(leftBack2, GPIO.HIGH)
        GPIO.output(rightBack1, GPIO.HIGH)
        GPIO.output(rightBack2, GPIO.LOW)

    def right(self):
        print("right")
        GPIO.output(leftFront1, GPIO.HIGH)
        GPIO.output(leftFront2, GPIO.LOW)
        GPIO.output(rightFront1, GPIO.LOW)
        GPIO.output(rightFront2, GPIO.HIGH)
        GPIO.output(leftBack1, GPIO.HIGH)
        GPIO.output(leftBack2, GPIO.LOW)
        GPIO.output(rightBack1, GPIO.LOW)
        GPIO.output(rightBack2, GPIO.HIGH)

    def stop(self):
        print("stop")
        GPIO.output(leftFront1, GPIO.LOW)
        GPIO.output(leftFront2, GPIO.LOW)
        GPIO.output(rightFront1, GPIO.LOW)
        GPIO.output(rightFront2, GPIO.LOW)
        GPIO.output(leftBack1, GPIO.LOW)
        GPIO.output(leftBack2, GPIO.LOW)
        GPIO.output(rightBack1, GPIO.LOW)
        GPIO.output(rightBack2, GPIO.LOW)

car=Car()