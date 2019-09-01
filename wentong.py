from PySide2.QtCore import QPoint

from mainui import Ui_MainWindow
import sys
import os
from PySide2 import QtCore, QtWidgets
import time
from PySide2.QtWidgets import*
from PySide2.QtGui import*
import cv2 as cv
import numpy as np
import pytesseract
import copy
import youdao
import PIL
import textwrap
from PIL import Image, ImageDraw, ImageFont
from googletrans import Translator
import freetype
import json
def qt_image_to_array(img, share_memory=False):
    """ Creates a numpy array from a QImage.

        If share_memory is True, the numpy array and the QImage is shared.
        Be careful: make sure the numpy array is destroyed before the image,
        otherwise the array will point to unreserved memory!!
    """
    assert isinstance(img, QImage), "img must be a QtGui.QImage object"
    assert img.format() == QImage.Format.Format_RGB32, \
        "img format must be QImage.Format.Format_RGB32, got: {}".format(img.format())

    img_size = img.size()
    buffer = img.constBits()

    # Sanity check
    n_bits_buffer = len(buffer) * 8
    n_bits_image  = img_size.width() * img_size.height() * img.depth()
    assert n_bits_buffer == n_bits_image, \
        "size mismatch: {} != {}".format(n_bits_buffer, n_bits_image)

    assert img.depth() == 32, "unexpected image depth: {}".format(img.depth())

    # Note the different width height parameter order!
    arr = np.ndarray(shape  = (img_size.height(), img_size.width(), img.depth()//8),
                     buffer = buffer,
                     dtype  = np.uint8)

    if share_memory:
        return arr
    else:
        return copy.deepcopy(arr)

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.openFolder.clicked.connect(self.magic)
        self.transEdit.textChanged.connect(self.trans_text_change)
        self.preButton.clicked.connect(self.move_backward)
        self.NextButton.clicked.connect(self.move_forward)
        self.saveButton.clicked.connect(self.save_page)
        self.translater=Translator()
       # self.pushButton.clicked.connect(self.Pause)

    def trans_text_change(self):
        qImg = self.get_trans_image(self.crop_img,  self.transEdit.toPlainText())

        [self.pageView.scene().removeItem(i) for i in self.pageView.scene().items() if i.pos()==self.pageView.scene().originCropPoint.toPoint()]
        item = self.pageView.scene().addPixmap(QPixmap(qImg))
        item.setPos(self.pageView.scene().originCropPoint.toPoint())
        target_scene = QGraphicsScene()
        target_scene.addPixmap(QPixmap(qImg))
        self.targetView.setScene(target_scene)

    def save_page(self):
        if not (os.path.exists(self.file_path+"/translation/")) :
            os.mkdir(self.file_path+"/translation/")
        filename=self.file_path+"/translation/"+self.file_list[self.work_index]
        result_img= QImage(self.pageView.scene().sceneRect().size().toSize(),QImage.Format_ARGB32)
        painter = QPainter(result_img)
        self.pageView.scene().render(painter)
        painter.end()
        result_img.save(filename)


    def magic(self):
       filepath=self.FileDialog("F:\迅雷下载\[Jamming] It Ejaculates in the Teacher [English] [Brolen] [Decensored]",isFolder=True)
       if os.path.isdir(filepath):
           self.file_path = filepath
           self.file_list =[file for file in os.listdir(filepath) if file.endswith(".jpg") or file.endswith(".png")]
           if(len( self.file_list)>0):
               self.work_file_by_index(0)

    def move_forward(self):
        if self.work_index+1<len( self.file_list):
            self.work_file_by_index(self.work_index+1)

    def move_backward(self):
        if self.work_index - 1 >= 0:
            self.work_file_by_index(self.work_index - 1)

    def work_file_by_index(self,index):
        print("move to index "+str(index))
        filepath = self.file_path + "/" + self.file_list[index]
        self.picture = QPixmap(filepath)
        scene = QGraphicsScene()
        item = scene.addPixmap(self.picture)
        scene.mouseMoveEvent = self.mouseMove
        scene.mousePressEvent = self.mouseDownInScene
        scene.mouseReleaseEvent = self.mouseUpInScene
        self.cv_img = qt_image_to_array(self.picture.toImage())
        self.pageView.setScene(scene)
        self.pageView.fitInView(item)
        self.work_index=index

    def mouseMove(self,event):
        self.pageView.scene().currentQRubberBand.setGeometry(QtCore.QRect( self.pageView.scene().originQPoint, event.screenPos()))
        self.pageView.scene().currentQRubberBand.show()

    def mouseDownInScene(self,event):
        self.pageView.scene().originQPoint = event.screenPos()
        self.pageView.scene().currentQRubberBand = QtWidgets.QRubberBand(QtWidgets.QRubberBand.Rectangle)
        self.pageView.scene().originCropPoint = event.scenePos()


    def mouseUpInScene(self,event):
        self.pageView.scene().currentQRubberBand.hide()
        currentQRect =  self.pageView.scene().currentQRubberBand.geometry()

        self.currentQRect = QtCore.QRect( self.pageView.scene().originCropPoint.toPoint(), event.scenePos().toPoint())

        self.crop_img = self.cv_img[int(self.pageView.scene().originCropPoint.y()): int(event.scenePos().y()), int(self.pageView.scene().originCropPoint.toPoint().x()): int(event.scenePos().x())]
        q_crop_img = self.cv_img_to_Qimg(self.crop_img)
        crop_scene = QGraphicsScene()
        crop_scene.addPixmap(QPixmap(q_crop_img))
        self.sourceView.setScene(crop_scene)

        config = ("-l eng")
        text = pytesseract.image_to_string(self.crop_img, config=config)
        stmt=text.replace("-\n","").replace("\n"," ")
        print(stmt)
        trans_txt =self.translater.translate(stmt, dest="zh-CN").text
        #trs_txt=youdao.translate(stmt)
        # result_dict = json.loads(trs_txt)
        # trans_txt= "".join([i["tgt"] for i in result_dict["translateResult"][0]])
        self.transEdit.clear()
        self.transEdit.insertPlainText(trans_txt)

        qImg = self.get_trans_image(self.crop_img, trans_txt)
        target_scene= QGraphicsScene()
        target_scene.addPixmap(QPixmap(qImg))
        self.targetView.setScene(target_scene)
        item = self.pageView.scene().addPixmap(QPixmap(qImg))
        item.setPos(self.pageView.scene().originCropPoint.toPoint())

    def get_trans_image(self, crop_img, trans_txt):
        trans_img = np.empty_like(crop_img)
        trans_img.fill(255)
        img_PIL = Image.fromarray(cv.cvtColor(trans_img, cv.COLOR_BGR2RGB))
        font = ImageFont.truetype('C:\Windows\Fonts\YaHei Consolas Hybrid 1.12.ttf', 20)
        fillColor = (0, 0, 0)
        draw = ImageDraw.Draw(img_PIL)
        msg="\n".join(textwrap.wrap(trans_txt, int(crop_img.shape[1] / 20) - 1))
        w, h = draw.textsize(msg,font=font)
        img_h,img_w,img_d = crop_img.shape
        position = ((img_w-w)/2, (img_h-h)/2)
        draw.text(position,msg,font=font,align='center', fill=fillColor)
        qImg = self.cv_img_to_Qimg(img_PIL)
        return qImg

    def cv_img_to_Qimg(self, img_PIL):
        img_OpenCV = cv.cvtColor(np.asarray(img_PIL), cv.COLOR_RGB2BGR)
        height, width, channel = img_OpenCV.shape
        bytesPerLine = 3 * width
        qImg = QImage(img_OpenCV.data, width, height, bytesPerLine, QImage.Format_RGB888).rgbSwapped()
        return qImg

    def FileDialog(self,directory='', forOpen=True, fmt='', isFolder=False):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        options |= QFileDialog.DontUseCustomDirectoryIcons
        dialog = QFileDialog()
        dialog.setOptions(options)

        dialog.setFilter(dialog.filter() | QtCore.QDir.Hidden)

        # ARE WE TALKING ABOUT FILES OR FOLDERS
        if isFolder:
            dialog.setFileMode(QFileDialog.DirectoryOnly)
        else:
            dialog.setFileMode(QFileDialog.AnyFile)
        # OPENING OR SAVING
        dialog.setAcceptMode(QFileDialog.AcceptOpen) if forOpen else dialog.setAcceptMode(QFileDialog.AcceptSave)

        # SET FORMAT, IF SPECIFIED
        if fmt != '' and isFolder is False:
            dialog.setDefaultSuffix(fmt)
            dialog.setNameFilters([f'{fmt} (*.{fmt})'])

        # SET THE STARTING DIRECTORY
        if directory != '':
            dialog.setDirectory(str(directory))
        else:
            dialog.setDirectory(str(os.getcwd()))

        if dialog.exec_() == QDialog.Accepted:
            path = dialog.selectedFiles()[0]  # returns a list
            return path
        else:
            return ''


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec_())