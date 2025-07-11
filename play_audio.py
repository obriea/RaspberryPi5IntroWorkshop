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
