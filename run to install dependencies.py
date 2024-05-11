import subprocess
import os

os.chdir('/home/ethan/Downloads/ChatNex-main')
subprocess.call(['pip', 'install', '--break-system-packages', '-r', 'requirements.txt'])
subprocess.call(['sudo', 'apt-get', 'update'])
subprocess.call(['sudo', 'apt-get', 'install', 'espeak'])
subprocess.call(['sudo', 'apt-get', 'install', 'stockfish'])
subprocess.call(['sudo', 'apt-get', 'install', 'python3-pyaudio'])
