# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Sun Sep  1 22:17:52 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1854, 1084)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.pageView = QtWidgets.QGraphicsView(self.centralWidget)
        self.pageView.setGeometry(QtCore.QRect(20, 30, 711, 981))
        self.pageView.setObjectName("pageView")
        self.preButton = QtWidgets.QPushButton(self.centralWidget)
        self.preButton.setGeometry(QtCore.QRect(40, 1020, 75, 23))
        self.preButton.setObjectName("preButton")
        self.NextButton = QtWidgets.QPushButton(self.centralWidget)
        self.NextButton.setGeometry(QtCore.QRect(480, 1020, 75, 23))
        self.NextButton.setObjectName("NextButton")
        self.openFolder = QtWidgets.QPushButton(self.centralWidget)
        self.openFolder.setGeometry(QtCore.QRect(20, 0, 75, 23))
        self.openFolder.setObjectName("openFolder")
        self.horizontalSlider = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(190, 1010, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName("horizontalSlider")
        self.horizontalSlider_2 = QtWidgets.QSlider(self.centralWidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(300, 1030, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName("horizontalSlider_2")
        self.label = QtWidgets.QLabel(self.centralWidget)
        self.label.setGeometry(QtCore.QRect(130, 1020, 54, 12))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.sourceView = QtWidgets.QGraphicsView(self.centralWidget)
        self.sourceView.setGeometry(QtCore.QRect(980, 460, 281, 261))
        self.sourceView.setObjectName("sourceView")
        self.transEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.transEdit.setGeometry(QtCore.QRect(1120, 730, 361, 151))
        self.transEdit.setObjectName("transEdit")
        self.targetView = QtWidgets.QGraphicsView(self.centralWidget)
        self.targetView.setGeometry(QtCore.QRect(1320, 460, 281, 261))
        self.targetView.setObjectName("targetView")
        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.saveButton.setGeometry(QtCore.QRect(1290, 920, 75, 23))
        self.saveButton.setObjectName("saveButton")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.preButton.setText(QtWidgets.QApplication.translate("MainWindow", "上一张", None, -1))
        self.NextButton.setText(QtWidgets.QApplication.translate("MainWindow", "下一张", None, -1))
        self.openFolder.setText(QtWidgets.QApplication.translate("MainWindow", "打开文件夹", None, -1))
        self.label.setText(QtWidgets.QApplication.translate("MainWindow", "缩放", None, -1))
        self.saveButton.setText(QtWidgets.QApplication.translate("MainWindow", "保存图片", None, -1))

