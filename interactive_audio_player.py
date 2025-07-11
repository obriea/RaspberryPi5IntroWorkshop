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