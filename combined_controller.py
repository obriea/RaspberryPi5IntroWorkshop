from gpiozero import Button, LED
import subprocess
from time import sleep
from pathlib import Path

class RaspberryPiController:
    """
    Combined example using LEDs, buttons, and audio
    Demonstrates integration of all workshop concepts
    """
    
    def __init__(self):
        # Hardware setup
        self.led = LED(17)  # GPIO17 - Physical pin 11
        self.button1 = Button(18, pull_up=True)  # GPIO18 - Physical pin 12
        self.button2 = Button(23, pull_up=True)  # GPIO23 - Physical pin 16
        
        # Audio setup
        self.audio_files = self.find_audio_files()
        self.current_audio_process = None
        
        # State variables
        self.led_blinking = False
        self.blink_process = None
        
    def find_audio_files(self):
        """Find available audio files"""
        audio_extensions = ['.mp3', '.wav', '.ogg']
        files = []
        for ext in audio_extensions:
            files.extend(list(Path(".").glob(f"*{ext}")))
        return [f.name for f in files]
    
    def start_blinking(self):
        """Start LED blinking pattern"""
        if not self.led_blinking:
            self.led_blinking = True
            print("🔆 Starting LED blink pattern")
            
            try:
                while self.led_blinking:
                    self.led.on()
                    sleep(0.5)
                    if self.led_blinking:  # Check again in case stopped
                        self.led.off()
                        sleep(0.5)
            except Exception as e:
                print(f"Blink error: {e}")
                self.led.off()
    
    def stop_blinking(self):
        """Stop LED blinking"""
        if self.led_blinking:
            self.led_blinking = False
            self.led.off()
            print("🔅 LED blinking stopped")
    
    def play_audio(self):
        """Play first available audio file"""
        if self.audio_files:
            filename = self.audio_files[0]
            try:
                if self.current_audio_process:
                    self.current_audio_process.terminate()
                
                self.current_audio_process = subprocess.Popen(['mpg123', '-q', filename])
                print(f"🎵 Playing: {filename}")
                return True
            except FileNotFoundError:
                print("❌ mpg123 not installed!")
                return False
            except Exception as e:
                print(f"❌ Audio error: {e}")
                return False
        else:
            print("❌ No audio files found!")
            return False
    
    def stop_audio(self):
        """Stop audio playback"""
        if self.current_audio_process:
            self.current_audio_process.terminate()
            self.current_audio_process = None
            print("🔇 Audio stopped")
    
    def show_status(self):
        """Display current system status"""
        print("\n" + "="*40)
        print("📊 SYSTEM STATUS")
        print("="*40)
        print(f"LED Blinking: {'Yes' if self.led_blinking else 'No'}")
        print(f"Audio Playing: {'Yes' if self.current_audio_process else 'No'}")
        print(f"Audio Files Found: {len(self.audio_files)}")
        if self.audio_files:
            print("Available files:")
            for file in self.audio_files:
                print(f"  - {file}")
        print("="*40)
    
    def run(self):
        """Main control loop"""
        print("🚀 Raspberry Pi Multi-Function Controller")
        print("=" * 50)
        print("CONTROLS:")
        print("Button 1 (GPIO18): Toggle LED blinking")
        print("Button 2 (GPIO23): Toggle audio playback")
        print("Both buttons: Show status")
        print("Ctrl+C: Exit program")
        print("=" * 50)
        
        try:
            while True:
                # Check button states
                if self.button1.is_pressed and self.button2.is_pressed:
                    self.show_status()
                    sleep(1)  # Prevent rapid repeated status displays
                    
                elif self.button1.is_pressed:
                    if self.led_blinking:
                        self.stop_blinking()
                    else:
                        # Start blinking in a way that doesn't block button checking
                        import threading
                        if not self.led_blinking:
                            self.led_blinking = True
                            threading.Thread(target=self.blink_led_thread).start()
                    sleep(0.5)  # Debounce
                    
                elif self.button2.is_pressed:
                    if self.current_audio_process:
                        self.stop_audio()
                    else:
                        self.play_audio()
                    sleep(0.5)  # Debounce
                
                sleep(0.1)  # Small delay to prevent excessive CPU usage
                
        except KeyboardInterrupt:
            print("\n🛑 Shutting down...")
            self.cleanup()
    
    def blink_led_thread(self):
        """LED blinking function for threading"""
        try:
            while self.led_blinking:
                self.led.on()
                sleep(0.5)
                if self.led_blinking:  # Check again
                    self.led.off()
                    sleep(0.5)
        except Exception as e:
            print(f"Blink thread error: {e}")
        finally:
            self.led.off()
    
    def cleanup(self):
        """Clean shutdown of all systems"""
        print("🧹 Cleaning up...")
        self.stop_blinking()
        self.stop_audio()
        print("✅ All systems stopped. Goodbye!")

# Main program
if __name__ == "__main__":
    controller = RaspberryPiController()
    controller.run()