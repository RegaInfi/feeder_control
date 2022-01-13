from gpiozero import MotionSensor
from gpiozero import Servo
from time import sleep

servo = Servo(17)
pir = MotionSensor(4)
while True:
	pir.wait_for_motion()
	print("Motion detected!")
	servo.max()
	sleep(5)
	servo.min()
