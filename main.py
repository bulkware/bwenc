# !/usr/bin/env python3
# -*- coding: utf-8 -*-

""" An application to convert file encodings. """

# Python imports
import csv # CSV File Reading and Writing
import os # Miscellaneous operating system interfaces
import sys # System-specific parameters and functions

# PyQt imports
from PyQt4 import QtCore, QtGui

# Application classes
from encconv import EncConv # A class to convert file encoding

# Application functions
import functions # Useful functions

# Import mainwindow
from mainwindow import *

# Create a class for our mainwindow
class Main(QtGui.QMainWindow):

    # Initialize mainwindow
    def __init__(self):

        # Declare class variables
        self.filelist = [] # File list for files to process
        self.maxsize = 524288 # Maximum file size
        self.path = "" # String for path
        self.encodings = [
            ["ASCII", "ascii"],
            ["ISO-8859-1", "latin_1"],
            ["ISO-8859-2", "iso8859_2"],
            ["ISO-8859-3", "iso8859_3"],
            ["ISO-8859-4", "iso8859_4"],
            ["ISO-8859-5", "iso8859_5"],
            ["ISO-8859-6", "iso8859_6"],
            ["ISO-8859-7", "iso8859_7"],
            ["ISO-8859-8", "iso8859_8"],
            ["ISO-8859-9", "iso8859_9"],
            ["ISO-8859-10", "iso8859_10"],
            ["ISO-8859-13", "iso8859_13"],
            ["ISO-8859-14", "iso8859_14"],
            ["ISO-8859-15", "iso8859_15"],
            ["KOI8-R", "koi8_r"],
            ["KOI8-U", "koi8_u"],
            ["UTF-8 with BOM", "utf_8_sig"],
            ["UTF-8 without BOM", "utf_8"],
            ["UTF-16BE", "utf_16_be"],
            ["UTF-16LE", "utf_16_le"],
            ["UTF-32BE", "utf_32_be"],
            ["UTF-32LE", "utf_32_le"],
            ["Windows-1250", "cp1250"],
            ["Windows-1251", "cp1251"],
            ["Windows-1252", "cp1252"],
            ["Windows-1253", "cp1253"],
            ["Windows-1254", "cp1254"],
            ["Windows-1255", "cp1255"],
            ["Windows-1256", "cp1256"],
            ["Windows-1257", "cp1257"],
            ["Windows-1258", "cp1258"]
        ]
        self.typefilter = "" # Type filter for add files dialog
        self.whitelist = {"txt": "Text files"} # Whitelist for file extensions
        self.whitelistfile = "whitelist.csv" # Whitelist file

        # Create an instance of encoding converter
        self.encconv = EncConv()

        # Initialize top level window widget
        QtGui.QMainWindow.__init__(self)

        # This is always the same
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Connect signals, menu and toolbar
        self.ui.actionAddFiles.triggered.connect(self.addFiles)
        self.ui.actionAddFolder.triggered.connect(self.addFolder)
        self.ui.actionRemoveFiles.triggered.connect(self.removeFiles)
        self.ui.actionClearList.triggered.connect(self.clearList)
        self.ui.actionMaximumFileSize.triggered.connect(self.maximumFileSize)
        self.ui.actionQuit.triggered.connect(self.quitApplication)
        self.ui.actionAbout.triggered.connect(self.aboutMessage)

        # Connect signals, buttons
        self.ui.btnConvert.clicked.connect(self.convertFiles)

        # Drag-and-drop events for file list
        self.ui.tblFileList.dragEnterEvent = self.dragEnterEvent
        self.ui.tblFileList.dragMoveEvent = self.dragEnterEvent
        self.ui.tblFileList.dropEvent = self.dropEvent

        # Icons
        self.setWindowIcon(QtGui.QIcon("icon.png"))
        self.ui.actionAddFiles.setIcon(QtGui.QIcon("add_files.png"))
        self.ui.actionAddFolder.setIcon(QtGui.QIcon("add_folder.png"))
        self.ui.actionRemoveFiles.setIcon(QtGui.QIcon("remove.png"))
        self.ui.actionClearList.setIcon(QtGui.QIcon("clear.png"))
        self.ui.actionMaximumFileSize.setIcon(QtGui.QIcon("max_file_size.png"))
        self.ui.actionQuit.setIcon(QtGui.QIcon("quit.png"))
        self.ui.actionAbout.setIcon(QtGui.QIcon("about.png"))
        self.ui.btnConvert.setIcon(QtGui.QIcon("convert.png"))

        # Loop and set encodings to comboboxes
        for item in self.encodings:
            self.ui.cboInputEnc.addItem(item[0])
            self.ui.cboOutputEnc.addItem(item[0])

        # Set default encodings
        self.ui.cboInputEnc.setCurrentIndex(24)
        self.ui.cboOutputEnc.setCurrentIndex(17)

        # Load settings
        self.loadSettings()

        # Load whitelist file
        if not self.loadWhitelist():
            self.whitelist = {"txt": "Text files"}

        # Make new type filters
        alltypes = ""
        for key, value in sorted(self.whitelist.items()):
            if self.typefilter == "":
                alltypes = "All supported files (*." + key
                self.typefilter += value + " (*." + key + ")"
            else:
                alltypes += " *." + key
                self.typefilter += ";;" + value + " (*." + key + ")"

        self.typefilter = alltypes + ");;" + self.typefilter

        # Check if command line arguments has files in it
        if sys.argv[1:]:
            self.loopItems(sys.argv[1:])

        # Refresh table
        self.refreshTable()


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #+ Actions
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    # Add files
    def addFiles(self):

        # Get file list using a dialog
        items = QtGui.QFileDialog.getOpenFileNames(self, "Add files",
            self.path, self.typefilter)

        # Check list for items
        if len(items) < 1:
            return

        # Loop items to main file list
        self.loopItems(items)


    # Add folder
    def addFolder(self):

        # Get folder using a dialog
        path = QtGui.QFileDialog.getExistingDirectory(self, "Add folder",
            self.path)

        # Check path
        if path == "":
            return

        # Check dir
        if not os.path.isdir(path):
            return

        # Create a list with full paths
        items = []
        for item in os.listdir(path):
            items.append(os.path.join(path, item))

        # Loop items to main file list
        self.loopItems(items)


    # Loop items to main file list
    def loopItems(self, items):

        nonexist = 0
        duplicates = 0
        folders = 0
        oversized = 0
        unallowed = 0
        for item in items:

            # Check if item does not exist
            if not os.path.exists(item):
                nonexist += 1
                continue

            # Check for duplicates
            if item in self.filelist:
                duplicates += 1
                continue

            # Check for folders
            if os.path.isdir(item):
                folders += 1
                continue

            # Check file size
            if os.path.getsize(item) > self.maxsize:
                oversized += 1
                continue

            # Check for extension
            ext = os.path.splitext(item)[1][1:].lower()
            if ext not in self.whitelist:
                unallowed += 1
                continue

            # Check if file path is an existing regular file
            if not os.path.isfile(item):
                continue

            # Set the path from first file
            if item == items[0]:
                self.path = os.path.split(item)[0]

            # Add file
            self.filelist.append(item)

        # Check for files, sort them, enable widgets and refresh table
        if len(self.filelist) > 0:
            self.filelist.sort()
            self.enableWidgets()
            self.refreshTable()

        # Count total adds and message user, if necessary
        total = nonexist
        total += duplicates
        total += folders
        total += oversized
        total += unallowed
        if total > 0:
            msg = "%s items were skipped:\n" % (total)
            msg += "\n"
            msg += "%s doesn't exist\n" % (nonexist)
            msg += "%s duplicates\n" % (duplicates)
            msg += "%s folders\n" % (folders)
            msg += "%s over maximum size\n" % (oversized)
            msg += "%s unallowed extensions\n" % (unallowed)
            QtGui.QMessageBox.information(self, "Info", msg)


    # Clear list
    def clearList(self):
        self.filelist[:] = []
        self.disableWidgets()
        self.refreshTable()


    # Remove files
    def removeFiles(self):

        # Check if file list is empty
        if len(self.filelist) < 1:
            msg = "No files in list."
            QtGui.QMessageBox.critical(self, "Error", msg)
            return

        # Check table's selected items
        if not self.ui.tblFileList.selectedIndexes():
            msg = "Please select file."
            QtGui.QMessageBox.critical(self, "Error", msg)
            return

        # Get indexes from table
        rows = []
        for item in self.ui.tblFileList.selectedIndexes():
            index = int(item.row())
            if index not in rows:
                rows.append(index)

        # Remove items in reverse order (so the indexes won't change)
        for index in sorted(rows, reverse=True):
            del self.filelist[index]

        # Check file list for files
        if len(self.filelist) < 1:
            self.disableWidgets()

        # Refresh table
        self.refreshTable()


    # Settings > Set maximum file size
    def maximumFileSize(self):

        # Get user input
        maxsize, ok = QtGui.QInputDialog.getInt(self, "Maximum file size",
            "Enter maximum file size in bytes:", self.maxsize, 1, 1073741824)

        # User cancelled
        if not ok:
            return

        # Check if maximum size is less than 1
        if maxsize < 1:
            message = "Maximum file size cannot be less than 1."
            QtGui.QMessageBox.critical(self, "Error", message)
            return

        # Set new maximum file size
        self.maxsize = maxsize


    # File > Quit
    def quitApplication(self):
        QtGui.QApplication.quit()


    # Help > About...
    def aboutMessage(self):
        message = """<strong>bwEnc</strong><br />
        Version 1.3.0<br />
        <br />
        This is free software.<br />
        Released under the General Public License.<br />
        <br />
        <a href="http://sourceforge.net/projects/bwenc/">SourceForge</a>"""
        QtGui.QMessageBox.about(self, "About", message)


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #+ Events
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    # Drag
    def dragEnterEvent(self, event):
        if (event.type() == QtCore.QEvent.DragEnter):
            if event.mimeData().hasUrls():
                event.accept()
            else:
                event.ignore()

    # Drop
    def dropEvent(self, event):
        if (event.type() == QtCore.QEvent.Drop):
            if event.mimeData().hasUrls():

                # Make a list of items from drag-and-drop
                items = []
                for i in event.mimeData().urls():
                    items.append(i.toLocalFile())

                # Loop items to main file list
                self.loopItems(items)


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #+ Settings
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    def loadSettings(self):
        try:
            settings = QtCore.QSettings("bulkware", "bwEnc")
            if settings.contains("geometry"): # Window geometry
                self.restoreGeometry(settings.value("geometry"))
            if settings.contains("state"): # Window state
                self.restoreState(settings.value("state"))
            if settings.contains("inputenc"):
                inputenc = settings.value("inputenc", type=int)
                self.ui.cboInputEnc.setCurrentIndex(inputenc)
            if settings.contains("outputenc"):
                outputenc = settings.value("outputenc", type=int)
                self.ui.cboOutputEnc.setCurrentIndex(outputenc)
            if settings.contains("maxsize"):
                self.maxsize = settings.value("maxsize", type=int)
            if settings.contains("path"):
                self.path = settings.value("path", type=str)
        except:
            self.path = ""
            self.maxsize = 524288
            return False
        else:
            return True


    # Save settings when closing the application
    def closeEvent(self, event):
        settings = QtCore.QSettings("bulkware", "bwEnc")
        settings.setValue("geometry", self.saveGeometry())
        settings.setValue("state", self.saveState())
        settings.setValue("inputenc", self.ui.cboInputEnc.currentIndex())
        settings.setValue("outputenc", self.ui.cboOutputEnc.currentIndex())
        settings.setValue("maxsize", self.maxsize)
        settings.setValue("path", self.path)


    # Load whitelist file
    def loadWhitelist(self):

        # Try to load whitelist file
        try:
            with open(self.whitelistfile, "r") as csvfile:
                csvhandle = csv.reader(csvfile, delimiter=",", quotechar='"')
                for line in csvhandle:
                    self.whitelist[line[1].lower()] = line[0]
        # Except
        except:
            return False

        # Finally
        finally:
            return True


    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    #+ Widgets
    #+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

    # Refresh table
    def refreshTable(self):

        # Clear widgets
        self.ui.tblFileList.setColumnCount(0)
        self.ui.tblFileList.setRowCount(0)
        self.ui.tblFileList.clear()

        # Check if file list is empty
        if len(self.filelist) == 0:
            return False

        # Set columns and rows
        self.ui.tblFileList.setColumnCount(3)
        self.ui.tblFileList.setRowCount(len(self.filelist))

        # Set header labels
        self.ui.tblFileList.setHorizontalHeaderLabels(["File", "Size", ""])

        # Populate table
        for i, file in enumerate(self.filelist):

            item = QtGui.QTableWidgetItem(os.path.basename(file))
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignLeft)
            self.ui.tblFileList.setItem(i, 0, item)

            size = functions.convert_bytes(os.path.getsize(file))
            item = QtGui.QTableWidgetItem(size)
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            item.setTextAlignment(QtCore.Qt.AlignVCenter | QtCore.Qt.AlignRight)
            self.ui.tblFileList.setItem(i, 1, item)

            item = QtGui.QTableWidgetItem()
            item.setFlags(QtCore.Qt.ItemIsEnabled | QtCore.Qt.ItemIsSelectable)
            self.ui.tblFileList.setItem(i, 2, item)

        # Resize columns to contents
        # setVisible lines are because of QTBUG-9352!
        self.ui.tblFileList.setVisible(False)
        self.ui.tblFileList.resizeColumnsToContents()
        self.ui.tblFileList.setVisible(True)


    # Convert file encodings
    def convertFiles(self):

        # Check if file list is empty
        if len(self.filelist) == 0:
            message = "No files to process."
            QtGui.QMessageBox.critical(self, "Error", message)
            return False

        # Get encodings from comboboxes
        inputenc = str(self.encodings[self.ui.cboInputEnc.currentIndex()][1])
        outputenc = str(self.encodings[self.ui.cboOutputEnc.currentIndex()][1])

        # Check that input and output encodings differ
        if inputenc == outputenc:
            message = "Input encoding cannot be the same as output encoding."
            QtGui.QMessageBox.critical(self, "Error", message)
            return False

        # Loop files and convert encoding(s)
        for file in self.filelist:

            # Try to change file encoding
            ok = self.encconv.convert_encoding(file, inputenc, outputenc)
            if not ok:
                message = self.encconv.message
                QtGui.QMessageBox.critical(self, "Error", message)
                return False

        # Conversion(s) successful, message user
        message = "File encodings converted."
        QtGui.QMessageBox.information(self, "Information", message)


    # Disable widgets
    def disableWidgets(self):
        self.ui.actionRemoveFiles.setEnabled(False)
        self.ui.actionClearList.setEnabled(False)
        self.ui.btnConvert.setEnabled(False)


    # Enable widgets
    def enableWidgets(self):
        self.ui.actionRemoveFiles.setEnabled(True)
        self.ui.actionClearList.setEnabled(True)
        self.ui.btnConvert.setEnabled(True)


# Creates an application object and begins the event handling loop
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    window = Main()
    window.show()
    ret = app.exec_()
    sys.exit(ret)
