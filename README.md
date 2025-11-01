# RaspberryPi5IntroWorkshop

Welcome to this **RaspberryPi5 Introduction Workshop**! This workshop is designed to provide step-by-step guidance on getting started with Raspberry Pi 5, focusing on GPIO, audio playback, and analog-to-digital conversion (ADC) using the Raspberry Pi. 

---

## 🚀 Getting Started

### Step 1: Setting Up Your Raspberry Pi 5
1. Ensure you have the following items:
   - Raspberry Pi 5 board
   - MicroSD card (16GB or larger, with Raspberry Pi OS pre-installed)
   - Power supply (USB-C)
   - HDMI cable and monitor
   - Keyboard and mouse
2. Insert the MicroSD card into the Raspberry Pi.
3. Connect the monitor, keyboard, and mouse to the Raspberry Pi.
4. Power on the Raspberry Pi by connecting the power supply.
5. Follow the on-screen instructions to complete the initial setup.
6. We will be using Thonny IDE, (Click on the top left icon representing a raspberry > Programming > Thonny Python IDE)
![Open ThonnyIDE](thonny_ide_start.png)

---

## 🌿 Module 1: Working with GPIO Pins

### Example 1: Turning On an LED
1. Build the circuit:
   - Connect the positive lead of the LED to pin 11 via a 1kΩ resistor.
   - Connect the ground leg of the LED to a ground pin.
     [Raspberry Pi GPIO Pinout](https://pinout.xyz/)
   - [1K colour code] (https://sjaeng.wordpress.com/wp-content/uploads/2010/10/resistor-color-codes1.jpg?w=584)
![CONNECT Blink Circuit](Blink.png)

2. Write the Python script `LED.py`:
   ```python
   from gpiozero import LED
   from time import sleep
   
   led = LED(17)  # GPIO17 corresponds to physical pin 11
   led.on()
   sleep(10)
   led.off()
   ```
3. Run the script:
   ```bash
   python3 LED.py
   ```

### Example 2: Blinking an LED
1. Modify the script to blink the LED. Save as `blink.py`:
   ```python
   from gpiozero import LED
   from time import sleep
   
   led = LED(17)  # GPIO17 corresponds to physical pin 11
   
   while True:
       led.on()    # Turn the LED on
       sleep(1)    # Wait for 1 second
       led.off()   # Turn the LED off
       sleep(1)    # Wait for 1 second
   ```
2. Run the script:
   ```bash
   python3 blink.py
   ```

---

## 👉 Module 2: Working with Input

### Example 1: Getting Input from the Terminal
1. Write the Python script `keyboard_input.py`:
   ```python
   from gpiozero import LED
   from time import sleep

   led = LED(17)  # GPIO17 corresponds to physical pin 11

   # Get user input for the number of blinks
   blink_num = int(input('How many times do you want to blink? '))

   # Blink the LED as many times as specified by the user
   for _ in range(blink_num):
       led.on()   # Turn the LED on
       sleep(1)   # Wait for 1 second
       led.off()  # Turn the LED off
       sleep(1)   # Wait for 1 second
   ```
2. Run the script and specify the blink count:
   ```bash
   python3 keyboard_input.py
   ```

### Example 2: Getting Input from Two Buttons
1. Build the circuit:
   - Connect one button to GPIO18 (physical pin 12) and ground.
   - Connect the second button to GPIO23 (physical pin 16) and ground.
![Connect Buttons Circuit](Buttons.png)

2. Write the Python script `button_input.py`:
   ```python
   from gpiozero import Button
   from time import sleep
   
   # Define buttons using Broadcom (BCM) numbering
   start_button = Button(18, pull_up=True)  # GPIO18 corresponds to physical pin 12
   stop_button = Button(23, pull_up=True)   # GPIO23 corresponds to physical pin 16
   
   end = False
   
   while not end:
      if start_button.is_pressed and stop_button.is_pressed:
           print('Make up your mind!')
           end = True
       if start_button.is_pressed:
           print('Start was pressed')
           sleep(0.5)
       if stop_button.is_pressed:
           print('Stop was pressed')
           sleep(0.5)
   ```
3. Run the script:
   ```bash
   python3 button_input.py
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

