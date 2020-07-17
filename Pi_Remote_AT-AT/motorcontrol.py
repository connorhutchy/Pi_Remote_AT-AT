import RPi.GPIO as GPIO          
from time import sleep


class MotorControl:

    def start(self):
        in1 = 24
        in2 = 23
        en = 25
        forward=True

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(in1,GPIO.OUT)
        GPIO.setup(in2,GPIO.OUT)
        GPIO.setup(en,GPIO.OUT)
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.LOW)
        p=GPIO.PWM(en,1000)

        p.start(100)
        print("\n")
        print("q - start \t e - stop\nw - forward \t s - backward\nm - medium \t h - high\nr - exit")
        print("\n")    

        while True:

            x=input()
            
            if x=='q':
                print("start")
                if(forward):
                    GPIO.output(in1,GPIO.LOW)
                    GPIO.output(in2,GPIO.HIGH)
                    print("forward")
                    x='z'
                else:
                    GPIO.output(in1,GPIO.HIGH)
                    GPIO.output(in2,GPIO.LOW)
                    print("backward")
                    x='z'


            elif x=='e':
                print("stop")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.LOW)
                x='z'

            elif x=='w':
                print("forward")
                GPIO.output(in1,GPIO.HIGH)
                GPIO.output(in2,GPIO.LOW)
                temp1=1
                x='z'

            elif x=='s':
                print("backward")
                GPIO.output(in1,GPIO.LOW)
                GPIO.output(in2,GPIO.HIGH)
                forward = False
                x='z'

            elif x=='m':
                print("medium")
                p.ChangeDutyCycle(75)
                x='z'

            elif x=='h':
                print("high")
                p.ChangeDutyCycle(100)
                x='z'
            
            elif x=='r':
                GPIO.cleanup()
                print("exit")
                break