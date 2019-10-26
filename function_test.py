import wentong as main
import os
import cv2
import numpy as np
import zipfile
from PySide2 import QtCore, QtWidgets , QtGui
from PySide2.QtWidgets import*
from PySide2.QtGui import*
import sys
app = QtWidgets.QApplication()

file_path='/home/chen/Downloads/[Rippadou] Cat\'s Woman Hard Core Edition (Cat\'s Eye, Batman) (English).zip'
f=zipfile.ZipFile(file_path,'r')
ls=f.namelist()
ls.sort()
for file_name in ls :
    with f.open(file_name) as this_pic:
        pic_data = this_pic.read()
        np_arr = np.fromstring(pic_data, np.uint8)
        img=cv2.imdecode(np_arr,1)

        wid = QtWidgets.QWidget()

        wid.setWindowTitle('NewWindow')
        wid.sourceView = QtWidgets.QGraphicsScene(wid)

        wid.sourceView.addPixmap(QPixmap(QImage.fromData(pic_data)))
        wid.show()

sys.exit(app.exec_())