@ECHO OFF
CLS

ECHO Removing cache directory...
RMDIR /Q /S "__pycache__"
RMDIR /Q /S "__pycache__"

ECHO Removing build directory...
RMDIR /Q /S "build"
RMDIR /Q /S "build"

ECHO Removing installers directory...
RMDIR /Q /S "installers"
RMDIR /Q /S "installers"

ECHO Creating installers directory...
MD "installers"

ECHO Compiling executable...
setup.py build

ECHO.

ECHO Copying application files...
COPY /Y "*.png" "build"
COPY /Y "gpl.txt" "build"
COPY /Y "icons.txt" "build"
COPY /Y "license.txt" "build"
COPY /Y "whats_new.txt" "build"
COPY /Y "whitelist.csv" "build"
