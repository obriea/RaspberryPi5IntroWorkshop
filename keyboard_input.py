from gpiozero import LED
from time import sleep

led = LED(17)  # GPIO17 corresponds to physical pin 11

try:
    # Get user input for the number of blinks with validation
    while True:
        try:
            blink_num = int(input('How many times do you want to blink? '))
            if blink_num < 0:
                print("Please enter a positive number.")
                continue
            if blink_num > 100:
                print("That's too many! Please enter a number less than 100.")
                continue
            break
        except ValueError:
            print("Please enter a valid number.")
    
    print(f"Blinking LED {blink_num} times...")
    
    # Blink the LED as many times as specified by the user
    for i in range(blink_num):
        led.on()   # Turn the LED on
        sleep(1)   # Wait for 1 second
        led.off()  # Turn the LED off
        sleep(1)   # Wait for 1 second
        print(f"Blink {i+1} of {blink_num} complete")
    
    print("Blinking sequence completed!")
    
except KeyboardInterrupt:
    print("\nProgram stopped by user")
    led.off()  # Ensure LED is off
