from gpiozero import Button
from time import sleep

# Define buttons using Broadcom (BCM) numbering
start_button = Button(21, pull_up=True, bounce_time = 0.05) 
stop_button = Button(20, pull_up=True, bounce_time = 0.05)   

def pressed():
    if start_button.is_pressed and stop_button.is_pressed:
        print('Make up your mind!')
    elif start_button.is_pressed:
        print('Start was pressed')
    elif stop_button.is_pressed:
        print('Stop was pressed')

start_button.when_pressed = pressed
stop_button.when_pressed = pressed
print("Ready.... Press buttons!")
while True:
    sleep(1)
