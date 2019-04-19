# bwenc

An application to convert file encodings.


## How to use

### Caution!

If you are not 100% certain of what you are about to do or if you don't even
know what file encodings are then please do yourself a favor and don't even
download this application. You can ruin all your files with a single click of a
button. This application doesn't create backup files before conversion. You have
been warned.

## Getting started

Add files to the filelist using the menu commands. Select the input and output
encodings and push convert.


## Menu commands

### File > Add files...
Adds one or more files to filelist. Only supported files are added.

### File > Add directory...
Adds all the files from the selected directory to the filelist. Only supported
files are added.

### File > Clear filelist
Clears the filelist.

### File > Quit
Quits the application.

### Settings > Maximum file size...
Determines the maximum allowed file size. Files that are larger than this will
not be processed.

### Help > About...
Application information.


## Customising whitelist
There is a special file in the application directory named "whitelist.csv". This
file contains the allowed file types for the application. You may add or remove
these but keep in mind that not all files are supposed to be converted.


## Running on Linux

### Installing dependencies (Debian-based systems)
Open your terminal application and type:
`sudo apt-get install python3 python3-pyqt4`

Hit enter. Enter your password when prompted. Answer yes to the question about
using additional disk space.

### Downloading the source
git clone https://github.com/bulkware/bwenc.git

### Running the application
You can run the application from the source code using this command:
`python3 main.py`
