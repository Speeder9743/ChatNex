# ChatNex 

# IN PROGRESS, DO NOT DOWNLOAD

## Description
This is a AI language model to make your HIWONDER AiNex robot more realistic. It adds conversational abilities and chess and checkers playing, and integrates AiNex's (I will explain later) climbing stairs, hurdling, auto shooting, etc. scripts burnt into the Raspberry Pi by the factory. It also adds walking and obstical avoidance, and other things that humans do. I specifically made this JUST FOR HIWONDER's AiNex robot. If you want to check it out, visit https://www.hiwonder.com/products/ainex?variant=40257678147671.

## Installation
- PLEASE READ BEFORE INSTALLING: This is meant to be downloaded on Windows, then moved to AiNex's Raspberry Pi board using a USB stick or other external storage device.
1. Click "<> Code"
2. Click "Download ZIP"
3. Extract the ZIP
4. Move/Copy the folder to a USB stick or other external storage device
5. Eject it and plug it into your AiNex's Raspberry Pi
6. Start LX Terminal by clicking the icon on the desktop
7. Type in the following commands:
    sudo apt-get update (You don't need to run this if your apt-get is up-to-date)
    sudo apt-get install eSpeak
    sudo apt-get install stockfish
    cd /media/<Your username(default is pi)>/<Your drive label(NOT LETTER, ONLY WINDOWS USES LETTERS)>
    sudo pip install -r requirements.txt
3. Install the required dependencies by clicking the "run to install dependencies.py" file

## Usage
1. Run `python main.py` to start the program
2. Follow the on-screen instructions to interact with the AI

## Contributing
If you want to contribute to this project, please follow these steps:
1. Fork the repository
2. Create a new branch
3. Make your changes
4. Submit a pull request

## Tips
- Don't speak into the microphone like you're a mouse! Google will not be able to process the words correctly. I'm not saying that you can't describe emotions or punctuation by changing the tone of voice like you normally would in a conversation - I'm just saying not to speak too high-pitched, or to quietly, or vice versa of both. All I'm trying to say is you need to speak clearly for best results.

- If you find that you're not getting accurate results even by typing, it might be because of the cutoff value for difflib. Go into the main python script, and change the cutoff value. Smaller values will make the algorithm more "lenient," while larger values will make it more precise. 

- I used Python 3.11.9 to code this. Please don't use other versions that have changes that modify library functions or function attributes, or else it might not work.

## License
This project is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives (CC BY-NC-ND) License. - see the LICENSE.md file for details.

## Contact
If you have any questions or feedback, please contact Ethan at speederbosman@gmail.com.

## Date
7:14 PM, 5/8/2024
