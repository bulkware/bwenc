# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt4 UI code generator 4.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(800, 600)
        MainWindow.setMinimumSize(QtCore.QSize(800, 600))
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.verticalLayout = QtGui.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.tblFileList = QtGui.QTableWidget(self.centralwidget)
        self.tblFileList.setAcceptDrops(True)
        self.tblFileList.setObjectName(_fromUtf8("tblFileList"))
        self.tblFileList.setColumnCount(0)
        self.tblFileList.setRowCount(0)
        self.tblFileList.horizontalHeader().setStretchLastSection(True)
        self.tblFileList.verticalHeader().setVisible(True)
        self.verticalLayout.addWidget(self.tblFileList)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.lblInputEncoding = QtGui.QLabel(self.centralwidget)
        self.lblInputEncoding.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.lblInputEncoding.setObjectName(_fromUtf8("lblInputEncoding"))
        self.horizontalLayout.addWidget(self.lblInputEncoding)
        self.cboInputEnc = QtGui.QComboBox(self.centralwidget)
        self.cboInputEnc.setObjectName(_fromUtf8("cboInputEnc"))
        self.horizontalLayout.addWidget(self.cboInputEnc)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.lblOutputEncoding = QtGui.QLabel(self.centralwidget)
        self.lblOutputEncoding.setObjectName(_fromUtf8("lblOutputEncoding"))
        self.horizontalLayout.addWidget(self.lblOutputEncoding)
        self.cboOutputEnc = QtGui.QComboBox(self.centralwidget)
        self.cboOutputEnc.setObjectName(_fromUtf8("cboOutputEnc"))
        self.horizontalLayout.addWidget(self.cboOutputEnc)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.btnConvert = QtGui.QPushButton(self.centralwidget)
        self.btnConvert.setEnabled(False)
        self.btnConvert.setObjectName(_fromUtf8("btnConvert"))
        self.horizontalLayout.addWidget(self.btnConvert)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        self.menuHelp = QtGui.QMenu(self.menubar)
        self.menuHelp.setObjectName(_fromUtf8("menuHelp"))
        self.menuSettings = QtGui.QMenu(self.menubar)
        self.menuSettings.setObjectName(_fromUtf8("menuSettings"))
        MainWindow.setMenuBar(self.menubar)
        self.statusBar = QtGui.QStatusBar(MainWindow)
        self.statusBar.setObjectName(_fromUtf8("statusBar"))
        MainWindow.setStatusBar(self.statusBar)
        self.toolBar = QtGui.QToolBar(MainWindow)
        self.toolBar.setToolButtonStyle(QtCore.Qt.ToolButtonTextUnderIcon)
        self.toolBar.setObjectName(_fromUtf8("toolBar"))
        MainWindow.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar)
        self.actionQuit = QtGui.QAction(MainWindow)
        self.actionQuit.setObjectName(_fromUtf8("actionQuit"))
        self.actionAddFiles = QtGui.QAction(MainWindow)
        self.actionAddFiles.setObjectName(_fromUtf8("actionAddFiles"))
        self.actionAddFolder = QtGui.QAction(MainWindow)
        self.actionAddFolder.setObjectName(_fromUtf8("actionAddFolder"))
        self.actionClearList = QtGui.QAction(MainWindow)
        self.actionClearList.setEnabled(False)
        self.actionClearList.setObjectName(_fromUtf8("actionClearList"))
        self.actionAbout = QtGui.QAction(MainWindow)
        self.actionAbout.setObjectName(_fromUtf8("actionAbout"))
        self.actionMaximumFileSize = QtGui.QAction(MainWindow)
        self.actionMaximumFileSize.setObjectName(_fromUtf8("actionMaximumFileSize"))
        self.actionRemoveFiles = QtGui.QAction(MainWindow)
        self.actionRemoveFiles.setEnabled(False)
        self.actionRemoveFiles.setObjectName(_fromUtf8("actionRemoveFiles"))
        self.menuFile.addAction(self.actionAddFiles)
        self.menuFile.addAction(self.actionAddFolder)
        self.menuFile.addAction(self.actionRemoveFiles)
        self.menuFile.addAction(self.actionClearList)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuHelp.addAction(self.actionAbout)
        self.menuSettings.addAction(self.actionMaximumFileSize)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())
        self.menubar.addAction(self.menuHelp.menuAction())
        self.toolBar.addAction(self.actionAddFiles)
        self.toolBar.addAction(self.actionAddFolder)
        self.toolBar.addAction(self.actionRemoveFiles)
        self.toolBar.addAction(self.actionClearList)
        self.toolBar.addAction(self.actionQuit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "bwEnc", None))
        self.lblInputEncoding.setText(_translate("MainWindow", "Input encoding:", None))
        self.lblOutputEncoding.setText(_translate("MainWindow", "Output encoding:", None))
        self.btnConvert.setText(_translate("MainWindow", "Convert", None))
        self.menuFile.setTitle(_translate("MainWindow", "File", None))
        self.menuHelp.setTitle(_translate("MainWindow", "Help", None))
        self.menuSettings.setTitle(_translate("MainWindow", "Settings", None))
        self.toolBar.setWindowTitle(_translate("MainWindow", "toolBar", None))
        self.actionQuit.setText(_translate("MainWindow", "Quit", None))
        self.actionAddFiles.setText(_translate("MainWindow", "Add files...", None))
        self.actionAddFolder.setText(_translate("MainWindow", "Add folder...", None))
        self.actionAddFolder.setToolTip(_translate("MainWindow", "Add folder", None))
        self.actionClearList.setText(_translate("MainWindow", "Clear list", None))
        self.actionClearList.setToolTip(_translate("MainWindow", "Clear list", None))
        self.actionAbout.setText(_translate("MainWindow", "About...", None))
        self.actionMaximumFileSize.setText(_translate("MainWindow", "Maximum file size...", None))
        self.actionRemoveFiles.setText(_translate("MainWindow", "Remove files", None))
        self.actionRemoveFiles.setToolTip(_translate("MainWindow", "Remove files", None))

