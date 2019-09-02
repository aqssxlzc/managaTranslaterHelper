# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Mon Sep  2 23:53:59 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1030, 685)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.centralWidget)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.openFolder = QtWidgets.QPushButton(self.centralWidget)
        self.openFolder.setObjectName("openFolder")
        self.verticalLayout_4.addWidget(self.openFolder)
        self.pageView = QtWidgets.QGraphicsView(self.centralWidget)
        self.pageView.setObjectName("pageView")
        self.verticalLayout_4.addWidget(self.pageView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.preButton = QtWidgets.QPushButton(self.centralWidget)
        self.preButton.setObjectName("preButton")
        self.horizontalLayout_2.addWidget(self.preButton)
        self.NextButton = QtWidgets.QPushButton(self.centralWidget)
        self.NextButton.setObjectName("NextButton")
        self.horizontalLayout_2.addWidget(self.NextButton)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3.addLayout(self.verticalLayout_4)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.targetView = QtWidgets.QGraphicsView(self.centralWidget)
        self.targetView.setObjectName("targetView")
        self.horizontalLayout.addWidget(self.targetView)
        self.sourceView = QtWidgets.QGraphicsView(self.centralWidget)
        self.sourceView.setObjectName("sourceView")
        self.horizontalLayout.addWidget(self.sourceView)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.transEdit = QtWidgets.QTextEdit(self.centralWidget)
        self.transEdit.setObjectName("transEdit")
        self.verticalLayout.addWidget(self.transEdit)
        self.saveButton = QtWidgets.QPushButton(self.centralWidget)
        self.saveButton.setObjectName("saveButton")
        self.verticalLayout.addWidget(self.saveButton)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        self.horizontalLayout_3.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.openFolder.setText(QtWidgets.QApplication.translate("MainWindow", "打开文件夹", None, -1))
        self.preButton.setText(QtWidgets.QApplication.translate("MainWindow", "上一张", None, -1))
        self.NextButton.setText(QtWidgets.QApplication.translate("MainWindow", "下一张", None, -1))
        self.saveButton.setText(QtWidgets.QApplication.translate("MainWindow", "保存图片", None, -1))

