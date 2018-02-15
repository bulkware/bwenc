# !/usr/bin/env python3
# -*- coding: utf-8 -*-

""" A class to convert file encoding. """

# Python imports
import os # Miscellaneous operating system interfaces
import sys # System-specific parameters and functions

# A class to convert file encoding
class EncConv(object):

    # Initialization
    def __init__(self):

        # Declare class variables
        self.message = "" # Error/success message


    # A method to convert file encoding
    def convert_encoding(self, file, inputenc, outputenc):

        # Clear message
        self.message = ""

        # Check if file path is not empty
        if file == "":
            self.message = "Filename is empty."
            return False

        # Check if file exists
        if not os.path.exists(file):
            self.message = "File does not exist:\n"
            self.message += "File: " + file
            return False

        # Check if path is an existing regular file
        if not os.path.isfile(file):
            self.message = "Not a file:\n"
            self.message += "File: " + file
            return False

        # Empty list for file contents
        filedata = []

        # Try to change file encoding
        try:

            filehandle = open(file, "r", encoding=inputenc)
            for line in filehandle:
                filedata.append(line)
            filehandle.close()

            filehandle = open(file, "w", encoding=outputenc)
            for line in filedata:
                filehandle.write(line)
            filehandle.close()

        except IOError as e:
            self.message = "I/O error({0}): {1}".format(e.errno, e.strerror)
            return False

        except UnicodeDecodeError:
            self.message = "Unicode Decode Error:\n"
            self.message += "File: " + file
            return False

        except UnicodeEncodeError:
            self.message = "Unicode Encode Error:\n"
            self.message += "File: " + file
            return False

        except:
            self.message = "Unexpected error:", sys.exc_info()[1]
            return False

        # OK
        return True
