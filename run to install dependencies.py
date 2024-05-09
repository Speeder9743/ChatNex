import subprocess

subprocess.call(['cd', 'Downloads'])
subprocess.call(['unzip', 'ChatNex.zip', '-d', 'Downloads'])
subprocess.call(['cd', 'ChatNex'])
subprocess.call(['pip', 'install', '-r', 'requirements.txt'])
subprocess.call(['sudo', 'apt-get', 'update'])
subprocess.call(['sudo', 'apt-get', 'install', 'espeak'])
subprocess.call(['sudo', 'apt-get', 'install', 'stockfish'])
