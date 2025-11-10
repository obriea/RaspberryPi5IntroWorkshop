# RaspberryPi5IntroWorkshop

Welcome to this **RaspberryPi5 Introduction Workshop**! This workshop is designed to provide step-by-step guidance on getting started with Raspberry Pi 5, focusing on GPIO, audio playback, and analog-to-digital conversion (ADC) using the Raspberry Pi. 

---

## 🚀 Getting Started

### Step 1-1: Setting Up Your Raspberry Pi 5 if you have a Monitor
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

### Step 1-2: Setting Up Your Raspberry Pi 5 Without a Monitor

[📄 Getting Started Without a Monitor](Raspberry_Pi_Getting_Started_Guide_v2.pdf)

This PDF is from Thode Makerspace and includes all the instructions needed to connect to the Raspberry Pi on campus and access it from your laptop.

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
   ```
3. Run the script:
   ```bash
   python3 button_input.py
   ```

---
## 🌿 Module 3: Working with an IMU Chip (MPU-6050)

### Example 1: Controlling LEDs with Tilt (IMU)


1. Create the Python file `IMU.py` and paste this code:

   ```python
   #!/usr/bin/env python3
   import time
   import math
   from smbus2 import SMBus
   from gpiozero import LED

   # ---------- Config ----------
   I2C_BUS = 1
   ADDR = 0x68          # use 0x69 if AD0 is pulled high
   WHO_AM_I   = 0x75
   PWR_MGMT_1 = 0x6B
   ACCEL_CFG  = 0x1C
   ACCEL_XOUT_H = 0x3B

   ACCEL_SF = 16384.0      # LSB per g for +/-2g
   SAMPLE_PERIOD = 0.05    # seconds between loops (~20 Hz)
   CAL_SECONDS = 1.0       # baseline calibration duration
   TILT_DEG = 10.0         # degrees to trigger
   HOLD_TIME = 1.0         # seconds LED stays on after triggering
   PRINT_RAW = False       # True to print pitch/roll continuously

   # LEDs (using BCM numbering)
   led_right   = LED(6)
   led_left    = LED(19)
   led_forward = LED(26)
   led_backward= LED(13)

   # ---------- Helpers ----------
   def i16(hi, lo):
       v = (hi << 8) | lo
       return v - 65536 if (v & 0x8000) else v

   def init_mpu(bus):
       who = bus.read_byte_data(ADDR, WHO_AM_I)
       if who not in (0x68, 0x69):
           raise RuntimeError("Unexpected WHO_AM_I 0x{:02X}".format(who))
       # Reset and basic init
       bus.write_byte_data(ADDR, PWR_MGMT_1, 0x80)  # reset
       time.sleep(0.1)
       bus.write_byte_data(ADDR, PWR_MGMT_1, 0x01)  # clock = X gyro
       time.sleep(0.05)
       bus.write_byte_data(ADDR, ACCEL_CFG, 0x00)   # +/-2g
       time.sleep(0.05)

   def read_accel(bus):
       data = bus.read_i2c_block_data(ADDR, ACCEL_XOUT_H, 14)
       ax = i16(data[0],  data[1])  / ACCEL_SF
       ay = i16(data[2],  data[3])  / ACCEL_SF
       az = i16(data[4],  data[5])  / ACCEL_SF
       return ax, ay, az

   def accel_to_angles(ax, ay, az):
       roll = math.degrees(math.atan2(ay, az))
       pitch = math.degrees(math.atan2(-ax, math.sqrt(ay*ay + az*az)))
       return pitch, roll

   def calibrate_baseline(bus, seconds):
       t0 = time.time()
       ps, rs = [], []
       while time.time() - t0 < seconds:
           ax, ay, az = read_accel(bus)
           p, r = accel_to_angles(ax, ay, az)
           ps.append(p); rs.append(r)
           time.sleep(0.01)
       ps.sort(); rs.sort()
       return ps[len(ps)//2], rs[len(rs)//2]  # median baseline offsets

   # ---------- Main ----------
   if __name__ == "__main__":
       led_right.off(); led_left.off(); led_forward.off(); led_backward.off()

       with SMBus(I2C_BUS) as bus:
           init_mpu(bus)
           print("Hold still for calibration...")
           p0, r0 = calibrate_baseline(bus, CAL_SECONDS)
           print("Baseline pitch={:+.2f} roll={:+.2f}".format(p0, r0))

           expiry = { "F": 0.0, "B": 0.0, "L": 0.0, "R": 0.0 }
           last_print = ""

           try:
               while True:
                   now = time.time()

                   ax, ay, az = read_accel(bus)
                   pitch_deg, roll_deg = accel_to_angles(ax, ay, az)

                   p = pitch_deg - p0
                   r = roll_deg - r0

                   triggered = []

                   if p < -TILT_DEG:
                       expiry["F"] = now + HOLD_TIME
                       triggered.append("FORWARD")
                   elif p > TILT_DEG:
                       expiry["B"] = now + HOLD_TIME
                       triggered.append("BACKWARD")

                   if r > TILT_DEG:
                       expiry["R"] = now + HOLD_TIME
                       triggered.append("RIGHT")
                   elif r < -TILT_DEG:
                       expiry["L"] = now + HOLD_TIME
                       triggered.append("LEFT")

                   led_forward.on() if now < expiry["F"] else led_forward.off()
                   led_backward.on() if now < expiry["B"] else led_backward.off()
                   led_left.on() if now < expiry["L"] else led_left.off()
                   led_right.on() if now < expiry["R"] else led_right.off()

                   label = " ".join(triggered) if triggered else "No movement"

                   if PRINT_RAW:
                       print("{} | pitch={:+.1f} roll={:+.1f}".format(label, pitch_deg, roll_deg))
                   elif label != last_print:
                       print(label); last_print = label

                   time.sleep(SAMPLE_PERIOD)

           except KeyboardInterrupt:
               print("Stopped.")
           finally:
               led_right.off(); led_left.off(); led_forward.off(); led_backward.off()


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

