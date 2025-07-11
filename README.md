# RaspberryPi5IntroWorkshop

Welcome to this **RaspberryPi5 Introduction Workshop**! This workshop is designed to provide comprehensive, step-by-step guidance on getting started with Raspberry Pi 5, focusing on GPIO (General Purpose Input/Output), audio playback, and hardware interfacing using Python programming.

## 📋 Prerequisites and Requirements

Before starting this workshop, ensure you have:

### Hardware Requirements
- **Raspberry Pi 5 board** (any RAM variant)
- **MicroSD card** (32GB or larger recommended, Class 10 for better performance)
- **Raspberry Pi OS** pre-installed on the SD card
- **USB-C power supply** (official Raspberry Pi 5V/5A power supply recommended)
- **HDMI cable** and compatible monitor/TV
- **USB keyboard and mouse**
- **Breadboard** (half-size or full-size)
- **Jumper wires** (male-to-male and male-to-female)
- **LEDs** (5mm, any color - red recommended for visibility)
- **Resistors** (1kΩ, 220Ω for LED current limiting)
- **Push buttons** (2x momentary tactile switches)
- **Speaker or headphones** (3.5mm jack or USB)

### Software Requirements
- **Raspberry Pi OS** (latest version recommended)
- **Python 3** (pre-installed with Raspberry Pi OS)
- **Thonny IDE** (pre-installed with Raspberry Pi OS)
- **GPIO Zero library** (pre-installed with Raspberry Pi OS)

### Safety Warnings ⚠️
- **Always power off** your Raspberry Pi before making circuit connections
- **Double-check wiring** before applying power to prevent damage
- **Use appropriate resistors** with LEDs to prevent burnout
- **Handle components gently** to avoid static damage
- **Never exceed 3.3V** on GPIO pins (Raspberry Pi uses 3.3V logic)

---

## 🚀 Getting Started

### Step 1: Setting Up Your Raspberry Pi 5

1. **Prepare your SD card:**
   - If not already done, flash Raspberry Pi OS to your MicroSD card using the [Raspberry Pi Imager](https://www.raspberrypi.com/software/)
   - Enable SSH and configure WiFi if needed during the imaging process

2. **Physical setup:**
   - Insert the MicroSD card into the Raspberry Pi 5
   - Connect your monitor using the HDMI cable (use HDMI0 port)
   - Connect USB keyboard and mouse
   - Connect your speaker or headphones to the 3.5mm audio jack
   - **Important:** Connect the power supply last to avoid power surges

3. **Initial boot and configuration:**
   - Power on the Raspberry Pi by connecting the USB-C power supply
   - Follow the on-screen setup wizard to:
     - Set your country, language, and timezone
     - Create a user account and password
     - Configure WiFi network
     - Update the system (this may take several minutes)

4. **Accessing Thonny IDE:**
   - Click on the Raspberry Pi icon (top-left corner)
   - Navigate to: **Programming → Thonny Python IDE**
   - Thonny is a beginner-friendly Python IDE that's perfect for this workshop

![Open ThonnyIDE](thonny_ide_start.png)

### Step 2: Understanding GPIO Basics

**GPIO (General Purpose Input/Output)** pins allow your Raspberry Pi to communicate with external hardware components like LEDs, buttons, sensors, and motors.

#### GPIO Numbering Systems
The Raspberry Pi has two numbering systems:
- **Physical numbering:** Pin numbers 1-40 based on physical position
- **BCM (Broadcom) numbering:** GPIO numbers used by the processor

**Important:** This workshop uses **BCM numbering** (the default for GPIO Zero library).

#### Key GPIO Concepts:
- **Digital Output:** Send HIGH (3.3V) or LOW (0V) signals to control devices
- **Digital Input:** Read HIGH or LOW signals from sensors/buttons
- **Pull-up/Pull-down resistors:** Ensure reliable reading of button states
- **Current limiting:** Use resistors to protect LEDs and GPIO pins

For reference: [Raspberry Pi GPIO Pinout](https://pinout.xyz/)

---

## 🌿 Module 1: Working with GPIO Pins

### Understanding LEDs and Current Limiting

Before we start, it's important to understand why we need resistors with LEDs:
- **LEDs are current-sensitive devices** that can burn out if too much current flows through them
- **Raspberry Pi GPIO pins** output 3.3V and can provide up to 16mA safely
- **1kΩ resistors** limit current to safe levels (~3mA) while keeping the LED bright enough to see
- **Always use resistors** with LEDs to protect both the LED and your Raspberry Pi

### Circuit Building Best Practices
1. **Always power off** your Raspberry Pi before building circuits
2. **Plan your circuit** on paper before building
3. **Use the breadboard** for temporary connections
4. **Keep wires short** and organized
5. **Double-check connections** before powering on

### Example 1: Turning On an LED

This example demonstrates basic digital output by controlling an LED.

#### Building the Circuit:
1. **Power off** your Raspberry Pi
2. **Gather components:**
   - 1x LED (any color, 5mm recommended)
   - 1x 1kΩ resistor ([Color code: Brown-Black-Red-Gold](https://www.electronics-tutorials.ws/resistor/res_2.html))
   - 2x jumper wires
   - Breadboard

3. **Wire the circuit:**
   - Connect **GPIO17 (Physical pin 11)** to one end of the 1kΩ resistor
   - Connect the **other end of the resistor** to the **positive (longer) leg** of the LED
   - Connect the **negative (shorter) leg** of the LED to **Ground (Physical pin 6)**
   
   **Wiring Reference:**
   - [Raspberry Pi GPIO Pinout](https://pinout.xyz/)
   - [Resistor Color Code Guide](https://www.electronics-tutorials.ws/resistor/res_2.html)

![CONNECT Blink Circuit](Blink.png)

#### Understanding the Code:
```python
from gpiozero import LED    # Import LED class from GPIO Zero library
from time import sleep     # Import sleep function for timing

led = LED(17)  # Create LED object on GPIO17 (BCM numbering)
led.on()       # Turn LED on (set GPIO17 to HIGH/3.3V)
sleep(10)      # Wait for 10 seconds
led.off()      # Turn LED off (set GPIO17 to LOW/0V)
```

#### Running the Script:
1. **Create the file:** In Thonny, create a new file and save it as `LED.py`
2. **Copy the code** from the example above
3. **Run the script:** Press F5 or click the "Run" button
4. **Expected result:** LED should turn on for 10 seconds, then turn off

```bash
# Alternative: Run from terminal
python3 LED.py
```

### Example 2: Blinking an LED

This example creates a continuous blinking pattern using a loop.

#### Understanding the Enhanced Code:
```python
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
```

#### Key Programming Concepts:
- **Infinite loop:** `while True:` creates a continuous cycle
- **Error handling:** `try/except` allows graceful program termination
- **KeyboardInterrupt:** Catches Ctrl+C to stop the program cleanly
- **Cleanup:** Always turn off outputs when the program ends

#### Running the Script:
1. **Save as** `blink.py`
2. **Run the script**
3. **Stop the program:** Press Ctrl+C in the terminal or click "Stop" in Thonny
4. **Expected result:** LED blinks on/off every second until stopped

```bash
python3 blink.py
```

#### Troubleshooting LED Issues:
- **LED not lighting up?**
  - Check all connections are secure
  - Verify LED polarity (longer leg = positive)
  - Ensure resistor is connected properly
  - Check GPIO pin number in code matches your wiring

- **LED very dim?**
  - Try a smaller resistor (220Ω instead of 1kΩ)
  - Check for loose connections

- **Program won't stop?**
  - Press Ctrl+C in terminal
  - Click "Stop" button in Thonny
  - If stuck, close terminal/Thonny and reopen

---

## 👉 Module 2: Working with Input

Input is just as important as output! This module covers how to get information into your Raspberry Pi programs from both keyboard input and physical buttons.

### Example 1: Getting Input from the Terminal

This example combines user input with LED control, demonstrating how to make interactive programs.

#### Understanding User Input:
- **`input()` function** pauses the program and waits for user keyboard input
- **`int()` function** converts text input to a number
- **Error handling** prevents crashes from invalid input

#### Enhanced Code with Error Handling:
```python
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
```

#### Running the Script:
1. **Save as** `keyboard_input.py`
2. **Run the program**
3. **Enter a number** when prompted (try different inputs like letters to see error handling)
4. **Expected result:** LED blinks the specified number of times with progress updates

```bash
python3 keyboard_input.py
```

### Example 2: Getting Input from Physical Buttons

Physical buttons allow for real-time interaction without a keyboard. This example demonstrates digital input reading.

#### Understanding Pull-up Resistors:
- **Pull-up resistors** ensure buttons read correctly when not pressed
- **GPIO Zero** has built-in pull-up support with `pull_up=True`
- **Button pressed** = LOW signal (0V) due to connection to ground
- **Button released** = HIGH signal (3.3V) due to pull-up resistor

#### Building the Button Circuit:
1. **Power off** your Raspberry Pi
2. **Gather components:**
   - 2x momentary push buttons (tactile switches)
   - 4x jumper wires
   - Breadboard

3. **Wire the circuit:**
   - **Button 1:**
     - One leg to **GPIO18 (Physical pin 12)**
     - Other leg to **Ground (Physical pin 14)**
   - **Button 2:**
     - One leg to **GPIO23 (Physical pin 16)**
     - Other leg to **Ground (Physical pin 20)**

![Connect Buttons Circuit](Buttons.png)

#### Understanding the Enhanced Code:
```python
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
```

#### Key Programming Concepts:
- **Button debouncing:** Small delays prevent rapid repeated readings
- **Logical operators:** `and` checks if both conditions are true
- **Polling loop:** Continuously checks button states
- **CPU efficiency:** Small sleep prevents 100% CPU usage

#### Running the Script:
1. **Save as** `button_input.py`
2. **Run the program**
3. **Test the buttons:**
   - Press each button individually
   - Press both buttons together to exit
   - Use Ctrl+C as alternative exit method

```bash
python3 button_input.py
```

#### Troubleshooting Button Issues:
- **Buttons not responding?**
  - Check all connections are secure
  - Verify GPIO pin numbers in code match your wiring
  - Ensure buttons are properly seated in breadboard

- **Buttons always showing as pressed?**
  - Check for short circuits between GPIO and Ground
  - Verify `pull_up=True` is set in code

- **Multiple rapid messages when pressing once?**
  - This is normal "bounce" - the sleep delays help minimize it
  - For more precise control, consider using button event handlers

#### Advanced Button Techniques:
You can also use **event-driven programming** instead of polling:
```python
from gpiozero import Button
from signal import pause

def button_pressed():
    print("Button was pressed!")

button = Button(18)
button.when_pressed = button_pressed

print("Waiting for button press...")
pause()  # Wait indefinitely for events
```

---

## 🎵 Module 3: Audio Playback with Raspberry Pi

### Setup Audio
1. Install required packages:
   ```bash
   sudo apt-get update
   sudo apt-get install alsa-utils mpg123
   ```
2. download Mystery_Song.mp3

   
### Play an MP3 File
1. Create a Python script to play audio:
   ```python
   import os
   from time import sleep
   
   # Song filename
   song_file_name = 'Mystery_Song.mp3'
   
   # Construct the command for playing the song
   song_command = f'mpg123 -q {song_file_name} &'
   
   # Print files in the current directory (optional)
   print(os.system("ls"))
   
   # Play the song
   os.system(song_command)
   print(f"Now playing: {song_file_name}")
   
   # Wait while the song plays (adjust sleep duration as needed)
   sleep(30)
   
   # Stop the song playback by killing the mpg123 process
   os.system('pkill mpg123')
   ```
2. Place your MP3 file in the same directory as the script and run it:
   ```bash
   python3 play_audio.py
   ```

---
---

## 🔧 Additional Commands

### Check Raspberry Pi OS Version
```bash
cat /etc/os-release
```

### Update Your System
```bash
sudo apt update && sudo apt upgrade -y
```

### Monitor CPU Temperature
```bash
vcgencmd measure_temp
```

---

## 📚 Resources

- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- [Raspberry Pi GPIO Pinout](https://pinout.xyz/)

---

Feel free to copy and paste the commands and code snippets above into your terminal or editor to follow along. Happy tinkering with Raspberry Pi 5! 🤖

