<font style="vertical-align: inherit;"><font style="vertical-align: inherit;">从aip导入AipOcr</font></font><font></font>
APP_ID = '16462688'<font></font>
API_KEY = 'uiSymXDuajlHu1zzDhzOxnrb'<font></font>
SECRET_KEY = '0SnZbzYzeKT7fwNBSIbdl0BGrDLzNLGW'<font></font>
client = AipOcr(APP_ID, API_KEY, SECRET_KEY)<font></font>
<font></font>
class get_text():<font></font>
    """ 读取图片 """<font></font>
    @staticmethod<font></font>
    def get_file_content(filePath):<font></font>
        with open(filePath, 'rb') as fp:<font></font>
            return fp.read()<font></font>
<font></font>
<font></font>
<font></font>
    """ 调用通用文字识别（高精度版） """<font></font>
<font></font>
    # client.basicAccurate(image)<font></font>
    @staticmethod<font></font>
    def gettext(filePath):<font></font>
        #print(filePath)<font></font>
        image = get_text.get_file_content(filePath)<font></font>
        """ 如果有可选参数 """<font></font>
        options = {}<font></font>
        options["detect_direction"] = "true"<font></font>
        options["probability"] = "true"<font></font>
<font></font>
        """ 带参数调用通用文字识别（高精度版） """<font></font>
        response = client.basicAccurate(image, options)<font></font>
        #print(response)<font></font>
        #data = response['words_result'][0]['words']<font></font>
        content = []<font></font>
        for info in response['words_result']:<font></font>
            #print(info['words'])<font></font>
            content.append(info['words'])<font></font>
        return content<font></font>
<font></font>
if __name__ == '__main__':<font></font>
    get_text.gettext('D:/PycharmProjects/baiduaipOcr/example.jpg')
# -*- coding: utf-8 -*-<font></font>
<font></font>
# Form implementation generated from reading ui file 'jiemian.ui'<font></font>
#<font></font>
# Created by: PyQt5 UI code generator 5.11.3<font></font>
#<font></font>
# WARNING! All changes made in this file will be lost!<font></font>
<font></font>
from PyQt5 import QtCore, QtGui, QtWidgets<font></font>
<font></font>
class Ui_Form(object):<font></font>
    def setupUi(self, Form):<font></font>
        Form.setObjectName("Form")<font></font>
        Form.resize(969, 597)<font></font>
        self.pushButton = QtWidgets.QPushButton(Form)<font></font>
        self.pushButton.setGeometry(QtCore.QRect(440, 500, 75, 23))<font></font>
        self.pushButton.setObjectName("pushButton")<font></font>
        self.pushButton_2 = QtWidgets.QPushButton(Form)<font></font>
        self.pushButton_2.setGeometry(QtCore.QRect(440, 540, 75, 23))<font></font>
        self.pushButton_2.setObjectName("pushButton_2")<font></font>
        self.lineEdit = QtWidgets.QLineEdit(Form)<font></font>
        self.lineEdit.setEnabled(False)<font></font>
        self.lineEdit.setGeometry(QtCore.QRect(110, 440, 741, 41))<font></font>
        self.lineEdit.setObjectName("lineEdit")<font></font>
        self.textEdit = QtWidgets.QTextEdit(Form)<font></font>
        self.textEdit.setGeometry(QtCore.QRect(10, 0, 951, 421))<font></font>
        font = QtGui.QFont()<font></font>
        font.setFamily("Agency FB")<font></font>
        self.textEdit.setFont(font)<font></font>
        self.textEdit.setObjectName("textEdit")<font></font>
        self.label = QtWidgets.QLabel(Form)<font></font>
        self.label.setEnabled(False)<font></font>
        self.label.setGeometry(QtCore.QRect(250, 500, 181, 61))<font></font>
        font = QtGui.QFont()<font></font>
        font.setPointSize(10)<font></font>
        font.setStyleStrategy(QtGui.QFont.PreferDefault)<font></font>
        self.label.setFont(font)<font></font>
        self.label.setWordWrap(True)<font></font>
        self.label.setObjectName("label")<font></font>
<font></font>
        self.retranslateUi(Form)<font></font>
        self.pushButton.clicked.connect(Form.open_img)<font></font>
        self.pushButton_2.clicked.connect(Form.shibie)<font></font>
        QtCore.QMetaObject.connectSlotsByName(Form)<font></font>
<font></font>
    def retranslateUi(self, Form):<font></font>
        _translate = QtCore.QCoreApplication.translate<font></font>
        Form.setWindowTitle(_translate("Form", "盘州市第一中学文字识别软件(beta1.0)"))<font></font>
        self.pushButton.setText(_translate("Form", "打开图片"))<font></font>
        self.pushButton_2.setText(_translate("Form", "开始识别"))<font></font>
        self.label.setText(_translate("Form", "软件利用百度AI高级识别助手，全世界上每天只能识别50次，非重要内容请别乱识别，谢谢！"))<font></font>
<font></font>
<font></font>
if __name__ == "__main__":<font></font>
    import sys<font></font>
    app = QtWidgets.QApplication(sys.argv)<font></font>
    Form = QtWidgets.QWidget()<font></font>
    ui = Ui_Form()<font></font>
    ui.setupUi(Form)<font></font>
    Form.show()<font></font>
    sys.exit(app.exec_())<font></font>
<font></font>
from PyQt5.Qt import QWidget,QApplication<font></font>
from PyQt5.QtWidgets import QFileDialog<font></font>
from jiemian import Ui_Form<font></font>
from baiduaip import get_text<font></font>
import sys<font></font>
<font></font>
class MF(QWidget,Ui_Form):<font></font>
    def __init__(self,parent = None,*args,**kwargs):<font></font>
        super().__init__(parent,*args,**kwargs)<font></font>
        self.setupUi(self)<font></font>
    def open_img(self):<font></font>
        print('打开图片')<font></font>
        openfile_name = QFileDialog.getOpenFileName(self, '选择文件', '', 'Image files(*.jpg , *.png, *.bmp)')<font></font>
        print(openfile_name[0])<font></font>
        self.lineEdit.setText('您打开的图片是：'+openfile_name[0])<font></font>
        self.imgagesurl = openfile_name[0]<font></font>
    def shibie(self):<font></font>
        print('识别')<font></font>
        content = get_text.gettext(self.imgagesurl)<font></font>
        data = '\n'.join(content)<font></font>
        self.textEdit.setText(data)<font></font>
        clipboard = QApplication.clipboard()<font></font>
        clipboard.setText(data)<font></font>
<font></font>
if __name__ == '__main__':<font></font>
    app = QApplication(sys.argv)<font></font>
    win = MF()<font></font>
    win.show()<font></font>
    sys.exit(app.exec_())<font></font>