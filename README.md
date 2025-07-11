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

Audio playback is an exciting way to add sound effects, music, or voice feedback to your Raspberry Pi projects. This module covers the basics of audio setup and playback using Python.

### Understanding Raspberry Pi Audio

The Raspberry Pi 5 has several audio output options:
- **3.5mm audio jack** (analog output)
- **HDMI audio** (digital output through monitor/TV)
- **USB audio devices** (external sound cards, speakers)
- **Bluetooth audio** (wireless speakers/headphones)

### Audio Setup and Configuration

#### Step 1: Install Required Audio Packages
These packages provide command-line audio tools and MP3 playback capability:

```bash
# Update package list
sudo apt-get update

# Install audio utilities and MP3 player
sudo apt-get install alsa-utils mpg123

# Optional: Install additional audio tools
sudo apt-get install pulseaudio pavucontrol
```

#### Step 2: Configure Audio Output
Check and configure your audio output device:

```bash
# List available audio devices
aplay -l

# Test audio output with a test sound
speaker-test -t wav -c 2

# Set audio output to 3.5mm jack (if needed)
sudo raspi-config
# Navigate to: Advanced Options > Audio > Force 3.5mm jack
```

#### Step 3: Test Audio Levels
```bash
# Open audio mixer (adjust volume)
alsamixer

# Test with a simple beep
echo -e "\a"
```

### Example 1: Basic Audio Playback

This example demonstrates how to play audio files using Python and system commands.

#### Preparing Your Audio File:
1. **Download or transfer** an MP3 file to your Raspberry Pi
2. **Rename it** to `Mystery_Song.mp3` or update the filename in the code
3. **Place it** in the same directory as your Python script
4. **Verify the file** exists and is readable

#### Understanding the Enhanced Code:
```python
import os
import subprocess
from time import sleep
from pathlib import Path

def play_audio_file(filename, duration=30):
    """
    Play an audio file for a specified duration
    
    Args:
        filename (str): Name of the audio file to play
        duration (int): How long to play in seconds
    """
    
    # Check if file exists
    if not Path(filename).exists():
        print(f"Error: Audio file '{filename}' not found!")
        print("Available files in current directory:")
        for file in Path(".").glob("*"):
            if file.is_file():
                print(f"  - {file.name}")
        return False
    
    print(f"Playing: {filename}")
    print(f"Duration: {duration} seconds")
    
    try:
        # Start playing the audio file in background
        # -q flag makes mpg123 quiet (less output)
        process = subprocess.Popen(['mpg123', '-q', filename])
        
        print("Audio playback started...")
        print("Press Ctrl+C to stop early")
        
        # Wait for specified duration
        sleep(duration)
        
        # Stop the audio playback
        process.terminate()
        process.wait()  # Wait for process to fully terminate
        
        print("Audio playback stopped.")
        return True
        
    except FileNotFoundError:
        print("Error: mpg123 not installed!")
        print("Install it with: sudo apt-get install mpg123")
        return False
    except KeyboardInterrupt:
        print("\nPlayback stopped by user")
        process.terminate()
        process.wait()
        return True
    except Exception as e:
        print(f"Error playing audio: {e}")
        return False

# Main program
if __name__ == "__main__":
    # Song filename
    song_file_name = 'Mystery_Song.mp3'
    
    print("=== Raspberry Pi Audio Player ===")
    print()
    
    # List files in current directory
    print("Files in current directory:")
    for file in Path(".").glob("*"):
        if file.is_file() and file.suffix.lower() in ['.mp3', '.wav', '.ogg']:
            print(f"  🎵 {file.name}")
    print()
    
    # Play the audio file
    success = play_audio_file(song_file_name, duration=30)
    
    if success:
        print("Audio playback completed successfully!")
    else:
        print("Audio playback failed. Check the troubleshooting guide below.")
```

#### Running the Audio Script:
1. **Save as** `play_audio.py`
2. **Ensure your audio file** is in the same directory
3. **Check audio output** is connected (speakers/headphones)
4. **Run the script:**

```bash
python3 play_audio.py
```

### Example 2: Interactive Audio Player

Create a more advanced audio player with user controls:

```python
import os
import subprocess
from time import sleep
from pathlib import Path

class SimpleAudioPlayer:
    def __init__(self):
        self.current_process = None
        self.audio_files = self.find_audio_files()
    
    def find_audio_files(self):
        """Find all audio files in current directory"""
        audio_extensions = ['.mp3', '.wav', '.ogg', '.m4a']
        files = []
        for ext in audio_extensions:
            files.extend(list(Path(".").glob(f"*{ext}")))
        return [f.name for f in files]
    
    def list_files(self):
        """List available audio files"""
        if not self.audio_files:
            print("No audio files found in current directory!")
            return
        
        print("Available audio files:")
        for i, file in enumerate(self.audio_files, 1):
            print(f"  {i}. {file}")
    
    def play_file(self, filename):
        """Play an audio file"""
        if filename not in self.audio_files:
            print(f"File '{filename}' not found!")
            return False
        
        try:
            self.current_process = subprocess.Popen(['mpg123', '-q', filename])
            print(f"Playing: {filename}")
            return True
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def stop_playback(self):
        """Stop current playback"""
        if self.current_process:
            self.current_process.terminate()
            self.current_process = None
            print("Playback stopped.")
    
    def run(self):
        """Main interactive loop"""
        print("=== Interactive Audio Player ===")
        print("Commands: list, play <filename>, stop, quit")
        
        while True:
            try:
                command = input("\n> ").strip().lower()
                
                if command == "quit" or command == "exit":
                    self.stop_playback()
                    print("Goodbye!")
                    break
                elif command == "list":
                    self.list_files()
                elif command == "stop":
                    self.stop_playback()
                elif command.startswith("play "):
                    filename = command[5:]  # Remove "play " prefix
                    self.play_file(filename)
                else:
                    print("Commands: list, play <filename>, stop, quit")
                    
            except KeyboardInterrupt:
                self.stop_playback()
                print("\nGoodbye!")
                break

# Run the interactive player
if __name__ == "__main__":
    player = SimpleAudioPlayer()
    player.run()
```

### Audio Troubleshooting Guide

#### No Sound Output:
- **Check connections:** Ensure speakers/headphones are properly connected
- **Test audio device:** Run `speaker-test -t wav -c 2`
- **Check volume:** Use `alsamixer` to adjust volume levels
- **Verify output device:** Use `aplay -l` to list audio devices

#### File Not Found Errors:
- **Check file path:** Ensure audio file is in the correct directory
- **Verify filename:** Check spelling and file extension
- **File permissions:** Ensure file is readable (`ls -la filename.mp3`)

#### mpg123 Not Found:
- **Install mpg123:** `sudo apt-get install mpg123`
- **Alternative players:** Try `omxplayer` or `vlc`

#### Audio Quality Issues:
- **Check file format:** MP3, WAV, and OGG are well-supported
- **Sample rate:** 44.1kHz is standard for most audio
- **Bit rate:** Higher bit rates may need more processing power

#### Performance Issues:
- **Large files:** Consider compressing audio files
- **Background processes:** Close unnecessary programs
- **SD card speed:** Use Class 10 or better SD cards

### Supported Audio Formats

| Format | Extension | Quality | Notes |
|--------|-----------|---------|-------|
| MP3 | .mp3 | Good | Most common, smaller files |
| WAV | .wav | Excellent | Uncompressed, larger files |
| OGG | .ogg | Good | Open source alternative |
| FLAC | .flac | Excellent | Lossless compression |

---

## 🔧 Useful Raspberry Pi Commands

### System Information and Monitoring

#### Check Raspberry Pi OS Version and Details
```bash
# Operating system information
cat /etc/os-release

# Raspberry Pi model and revision
cat /proc/cpuinfo | grep Model

# Kernel version
uname -a

# Disk space usage
df -h

# Memory usage
free -h
```

#### System Updates and Maintenance
```bash
# Update package list and upgrade system
sudo apt update && sudo apt upgrade -y

# Clean up unnecessary packages
sudo apt autoremove -y
sudo apt autoclean

# Reboot system
sudo reboot

# Shutdown system
sudo shutdown -h now
```

#### Hardware Monitoring
```bash
# CPU temperature
vcgencmd measure_temp

# CPU frequency
vcgencmd measure_clock arm

# GPU memory split
vcgencmd get_mem gpu

# Voltage levels
vcgencmd measure_volts

# Check for throttling
vcgencmd get_throttled
```

#### GPIO and Hardware Tools
```bash
# List GPIO pin states
gpio readall

# Check I2C devices
sudo i2cdetect -y 1

# Test camera (if connected)
libcamera-hello

# List USB devices
lsusb

# List connected hardware
lshw
```

---

## 🚨 Comprehensive Troubleshooting Guide

### Hardware Issues

#### LED Not Working
**Symptoms:** LED doesn't light up or very dim
**Solutions:**
1. **Check wiring connections:**
   ```bash
   # Power off Pi first
   sudo shutdown -h now
   # Verify all connections are secure
   ```
2. **Verify LED polarity:** Longer leg = positive (anode)
3. **Test LED separately:** Connect directly to 3.3V and GND with resistor
4. **Check resistor value:** 220Ω-1kΩ works best for standard LEDs
5. **Verify GPIO pin:** Use `gpio readall` to check pin states

#### Buttons Not Responding
**Symptoms:** Button presses not detected
**Solutions:**
1. **Check pull-up settings:** Ensure `pull_up=True` in code
2. **Test button continuity:** Use multimeter to test button function
3. **Verify wiring:** Button should connect GPIO to GND when pressed
4. **Check debouncing:** Add small delays to prevent rapid triggering

#### Audio Problems
**Symptoms:** No sound or poor audio quality
**Solutions:**
1. **Test audio output:**
   ```bash
   speaker-test -t wav -c 2
   aplay /usr/share/sounds/alsa/Front_Left.wav
   ```
2. **Check audio configuration:**
   ```bash
   # List audio devices
   aplay -l
   
   # Configure audio output
   sudo raspi-config
   # Advanced Options > Audio
   ```
3. **Adjust volume:**
   ```bash
   alsamixer
   amixer set Master 70%
   ```

### Software Issues

#### Python Import Errors
**Symptoms:** `ModuleNotFoundError` or import failures
**Solutions:**
1. **Install missing packages:**
   ```bash
   # For GPIO Zero
   sudo apt install python3-gpiozero
   
   # For general packages
   pip3 install package_name
   ```
2. **Check Python version:**
   ```bash
   python3 --version
   which python3
   ```

#### Permission Errors
**Symptoms:** Permission denied when accessing GPIO
**Solutions:**
1. **Add user to gpio group:**
   ```bash
   sudo usermod -a -G gpio $USER
   # Logout and login again
   ```
2. **Run with sudo (if needed):**
   ```bash
   sudo python3 script.py
   ```

#### Program Won't Stop
**Symptoms:** Infinite loops or unresponsive programs
**Solutions:**
1. **Keyboard interrupt:** Press `Ctrl+C`
2. **Force kill process:**
   ```bash
   # Find process ID
   ps aux | grep python
   
   # Kill specific process
   kill -9 <process_id>
   
   # Kill all Python processes (use carefully)
   sudo pkill python3
   ```

### Network and Connectivity Issues

#### SSH Connection Problems
```bash
# Enable SSH
sudo systemctl enable ssh
sudo systemctl start ssh

# Check SSH status
sudo systemctl status ssh

# Find Pi IP address
hostname -I
```

#### WiFi Issues
```bash
# Scan for networks
sudo iwlist wlan0 scan | grep ESSID

# Configure WiFi
sudo raspi-config
# Network Options > WiFi

# Check connection
iwconfig
ping google.com
```

### Performance Issues

#### System Running Slowly
**Symptoms:** Laggy interface, slow program execution
**Solutions:**
1. **Check system resources:**
   ```bash
   htop  # Install with: sudo apt install htop
   ```
2. **Free up disk space:**
   ```bash
   sudo apt autoremove -y
   sudo apt autoclean
   ```
3. **Check temperature:**
   ```bash
   vcgencmd measure_temp
   # If >70°C, improve cooling
   ```

#### SD Card Issues
**Symptoms:** Slow performance, corruption errors
**Solutions:**
1. **Check SD card health:**
   ```bash
   sudo fsck /dev/mmcblk0p2
   ```
2. **Use high-quality SD card:** Class 10 or better
3. **Regular backups:** Clone SD card periodically

### Emergency Recovery

#### System Won't Boot
1. **Check power supply:** Ensure 5V/3A minimum
2. **Try different SD card:** Test with known good card
3. **Check connections:** Reseat all cables
4. **Recovery mode:** Hold SHIFT during boot

#### Factory Reset
```bash
# Reset to defaults (keep files)
sudo raspi-config
# Advanced Options > Reset

# Complete reinstall: Use Raspberry Pi Imager
```

### Getting Help

#### Official Resources
- [Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)
- [GPIO Zero Documentation](https://gpiozero.readthedocs.io/)
- [Raspberry Pi Forums](https://www.raspberrypi.org/forums/)

#### Command Line Help
```bash
# Python help
python3 -c "help('modules')"

# Man pages
man gpio
man python3

# Command help
gpio -h
python3 --help
```

#### Diagnostic Commands
```bash
# System information
sudo rpi-eeprom-update
dmesg | tail -20
journalctl -xe
lsmod
```

---

## 📚 Learning Resources and References

### Official Documentation
- **[Raspberry Pi Documentation](https://www.raspberrypi.com/documentation/)** - Complete official guide
- **[Raspberry Pi GPIO Pinout](https://pinout.xyz/)** - Interactive GPIO reference
- **[GPIO Zero Documentation](https://gpiozero.readthedocs.io/)** - Python GPIO library guide
- **[Raspberry Pi OS Guide](https://www.raspberrypi.com/software/)** - Operating system information

### Hardware References
- **[Raspberry Pi 5 Specifications](https://www.raspberrypi.com/products/raspberry-pi-5/)** - Technical specifications
- **[GPIO Pin Layout](https://pinout.xyz/#)** - Detailed pin functions and alternatives
- **[Electronic Components Guide](https://www.electronics-tutorials.ws/)** - Learn about resistors, LEDs, buttons
- **[Breadboard Tutorial](https://learn.sparkfun.com/tutorials/how-to-use-a-breadboard)** - Circuit building basics

### Programming Resources
- **[Python.org Tutorial](https://docs.python.org/3/tutorial/)** - Official Python documentation
- **[GPIO Zero Recipes](https://gpiozero.readthedocs.io/en/stable/recipes.html)** - Code examples and patterns
- **[MagPi Magazine](https://magpi.raspberrypi.com/)** - Free monthly Raspberry Pi magazine
- **[Raspberry Pi Press Books](https://www.raspberrypi.com/news/category/books/)** - Free programming books

### Community and Support
- **[Raspberry Pi Forums](https://www.raspberrypi.org/forums/)** - Community discussion and help
- **[Reddit r/raspberry_pi](https://www.reddit.com/r/raspberry_pi/)** - Active community with projects and help
- **[Stack Overflow](https://stackoverflow.com/questions/tagged/raspberry-pi)** - Programming questions and answers
- **[GitHub Raspberry Pi](https://github.com/raspberrypi)** - Source code and examples

### Project Ideas and Inspiration
- **[Raspberry Pi Foundation Projects](https://projects.raspberrypi.org/)** - Step-by-step project tutorials
- **[Adafruit Learning](https://learn.adafruit.com/category/raspberry-pi)** - Hardware projects and tutorials
- **[SparkFun Tutorials](https://learn.sparkfun.com/tutorials/tags/raspberry-pi)** - Electronic project guides
- **[Hackster.io](https://www.hackster.io/raspberry-pi)** - Community-shared projects

### Advanced Topics
- **[I2C and SPI Communication](https://learn.sparkfun.com/tutorials/raspberry-pi-spi-and-i2c-tutorial)** - Hardware protocols
- **[Camera Module Guide](https://www.raspberrypi.com/documentation/accessories/camera.html)** - Working with camera
- **[IoT with Raspberry Pi](https://www.raspberrypi.com/news/iot-python-libraries/)** - Internet of Things projects
- **[Real-time Programming](https://www.raspberrypi.com/documentation/computers/linux_kernel.html)** - Advanced system programming

### Tools and Software
- **[Thonny IDE](https://thonny.org/)** - Beginner-friendly Python editor
- **[VS Code](https://code.visualstudio.com/)** - Advanced code editor with Pi support
- **[Raspberry Pi Imager](https://www.raspberrypi.com/software/)** - SD card imaging tool
- **[VNC Viewer](https://www.realvnc.com/en/connect/download/viewer/)** - Remote desktop access

### Shopping and Components
- **[Official Raspberry Pi Store](https://www.raspberrypi.com/products/)** - Authentic hardware
- **[Adafruit](https://www.adafruit.com/)** - Electronics components and kits
- **[SparkFun](https://www.sparkfun.com/)** - Educational electronics
- **[Amazon/Local Electronics Stores](https://amazon.com)** - General components

### Next Steps
After completing this workshop, consider exploring:
1. **Camera projects** - Time-lapse, security systems, computer vision
2. **Sensor integration** - Temperature, humidity, motion detection
3. **Motor control** - Robotics, servo motors, stepper motors
4. **Communication protocols** - I2C, SPI, UART devices
5. **Web interfaces** - Control your Pi through a web browser
6. **IoT projects** - Connect to cloud services and APIs
7. **Machine learning** - TensorFlow Lite, object detection
8. **Home automation** - Smart home control systems

---

## 🎉 Conclusion

Congratulations on completing the Raspberry Pi 5 Introduction Workshop! You've learned:

- ✅ **GPIO basics** and digital output control
- ✅ **LED circuits** with proper current limiting
- ✅ **User input** from keyboard and physical buttons
- ✅ **Audio playback** with Python programming
- ✅ **Error handling** and best practices
- ✅ **Troubleshooting** common issues
- ✅ **Safety practices** for electronics work

### What You Can Build Next:
- **Smart alarm clock** with LED indicators and audio alerts
- **Interactive game controller** using buttons and LEDs
- **Sound-reactive light show** combining audio and visual effects
- **Home automation controller** with sensors and actuators
- **Robot control system** with motors and sensors

### Keep Learning:
The Raspberry Pi ecosystem is vast and constantly growing. Join the community, share your projects, and don't hesitate to ask questions. Every expert was once a beginner!

**Happy tinkering with Raspberry Pi 5!** 🤖🎯

---

*This workshop was designed to be beginner-friendly while providing depth for those who want to understand the underlying concepts. Feel free to modify, extend, and share these examples with others learning about Raspberry Pi!*

