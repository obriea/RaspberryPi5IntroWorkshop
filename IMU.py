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
