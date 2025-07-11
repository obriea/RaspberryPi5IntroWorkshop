from gpiozero import LED
from time import sleep

led = LED(17)  # GPIO17 corresponds to physical pin 11

try:  # Error handling for clean exit
    while True:
        led.on()    # Turn the LED on
        sleep(1)    # Wait for 1 second
        led.off()   # Turn the LED off
        sleep(1)    # Wait for 1 second
except KeyboardInterrupt:  # Handle Ctrl+C gracefully
    print("\nBlinking stopped by user")
    led.off()  # Ensure LED is off when program ends
    print("LED turned off. Program ended.")
