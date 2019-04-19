@ECHO OFF
CLS

ECHO Removing cache directory...
RMDIR /Q /S "__pycache__"
RMDIR /Q /S "__pycache__"

ECHO Removing build directory...
RMDIR /Q /S "build"
RMDIR /Q /S "build"

ECHO Removing windows-version directory...
RMDIR /Q /S "windows-version"
RMDIR /Q /S "windows-version"

ECHO Creating windows-version directory...
MD "windows-version"

ECHO Compiling executable...
setup.py build

ECHO.

ECHO Copying application files...
COPY /Y "whitelist.csv" "build"

COPY /Y "about.png" "build"
COPY /Y "add_files.png" "build"
COPY /Y "add_folder.png" "build"
COPY /Y "clear.png" "build"
COPY /Y "convert.png" "build"
COPY /Y "icon.png" "build"
COPY /Y "max_file_size.png" "build"
COPY /Y "quit.png" "build"
COPY /Y "remove.png" "build"

COPY /Y "gpl.txt" "build"
COPY /Y "icons.txt" "build"
COPY /Y "license.txt" "build"
COPY /Y "README.md" "build"
COPY /Y "whats_new.txt" "build"
