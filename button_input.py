from gpiozero import Button
from time import sleep

# Define buttons using Broadcom (BCM) numbering
start_button = Button(18, pull_up=True)  # GPIO18 corresponds to physical pin 12
stop_button = Button(23, pull_up=True)   # GPIO23 corresponds to physical pin 16

print("Button Control Program")
print("Press START button to see a message")
print("Press STOP button to see a different message")
print("Press BOTH buttons together to exit")
print("Press Ctrl+C to quit\n")

end = False

try:
    while not end:
        # Check if both buttons pressed (exit condition)
        if start_button.is_pressed and stop_button.is_pressed:
            print('Both buttons pressed - Make up your mind!')
            print('Exiting program...')
            end = True
        # Check individual button presses
        elif start_button.is_pressed:
            print('START button was pressed')
            sleep(0.5)  # Prevent rapid repeated messages
        elif stop_button.is_pressed:
            print('STOP button was pressed')
            sleep(0.5)  # Prevent rapid repeated messages
        
        sleep(0.1)  # Small delay to prevent excessive CPU usage
        
except KeyboardInterrupt:
    print("\nProgram stopped by user (Ctrl+C)")

print("Button monitoring ended.")
