# STEGANOGRAPHY TOOL
## Introduction
A simple python based tool to hide secret messages inside images using LSB steganograpghy with a user-friendly GUI
### Features
- Hide text inside PNG/BMP images
- Extract hidden text from stego images
- Separated windows for hiding and extracting
- Simple file browsing dialogs
- GUI built with Tkinter
### Tools used
- Python 3.13
- Tkinter -GUI interface
- Pillow - Image handling
- Stepic - LSB based steganography
### Usage
- Click "Hide Data in image" -> select image -> Enter message -> save new image
- Click "Extract Data from image" -> Load the stego image -> Message will apear
- Press esc to exit full screen
- Click "Close and Return" buttons to switch windows
