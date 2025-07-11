from gpiozero import Button, LED
from signal import pause
from datetime import datetime

# Hardware setup
button = Button(18, pull_up=True)  # GPIO18 corresponds to physical pin 12
led = LED(17)  # GPIO17 corresponds to physical pin 11

# Button press counter
press_count = 0

def button_pressed():
    """Function called when button is pressed"""
    global press_count
    press_count += 1
    current_time = datetime.now().strftime("%H:%M:%S")
    
    print(f"[{current_time}] Button pressed! Count: {press_count}")
    
    # Flash LED when button is pressed
    led.on()
    
def button_released():
    """Function called when button is released"""
    current_time = datetime.now().strftime("%H:%M:%S")
    print(f"[{current_time}] Button released")
    
    # Turn off LED when button is released
    led.off()

# Set up event handlers
button.when_pressed = button_pressed
button.when_released = button_released

print("=== Event-Driven Button Example ===")
print("Press the button to see events in real-time")
print("Press Ctrl+C to exit")
print()

try:
    # Wait indefinitely for button events
    pause()
except KeyboardInterrupt:
    print(f"\nExiting... Total button presses: {press_count}")
    led.off()  # Ensure LED is off when exiting
    print("Program ended.")