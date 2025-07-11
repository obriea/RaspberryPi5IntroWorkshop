from gpiozero import LED
from time import sleep

led = LED(17)  # GPIO17 corresponds to physical pin 11
led.on()
sleep(10)
led.off()
