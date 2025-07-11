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
