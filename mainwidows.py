from PySide2 import  QtWidgets
from PySide2.QtWidgets import *

from uid import Ui_MainWindow
import sys
from PIL import Image
import re
import easyocr
import os
import xlrd
import torch.jit

import easyocr.model.vgg_model
class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.butten)
        self.pushButton_2.clicked.connect(self.butten2)
        self.pushButton_3.clicked.connect(self.butten3)
        self.pushButton_4.clicked.connect(self.butten4)
        self.pushButton_5.clicked.connect(self.xuandi)
        self.pushButton_6.clicked.connect(self.xuandi2)
        self.pushButton_7.clicked.connect(self.xuandi3)
        self.pushButton_8.clicked.connect(self.xuandi4)
        self.pushButton_9.clicked.connect(self.xuandi5)
        self.pushButton_10.clicked.connect(self.xuandi6)
        self.pushButton_11.clicked.connect(self.xuandi7)
        self.pushButton_12.clicked.connect(self.xuandi8)
        self.pushButton_13.clicked.connect(self.xuandi9)
        self.pushButton_14.clicked.connect(self.zhitupian)
        self.pushButton_15.clicked.connect(self.xuandi10)
        self.pushButton_16.clicked.connect(self.xuandi11)

    def script_method(fn, _rcb=None):
            return fn

    def script(obj, optimize=True, _frames_up=0, _rcb=None):
            return obj



    def butten(self):
        csdata=self.lineEdit.text();
        cfdata=self.lineEdit_2.text();
        csdata=csdata.replace('\\','/')
        cfdata=cfdata.replace('\\','/')

        name=csdata.split("/");

        filepath=os.listdir(csdata)
        kk=0;
        for k in filepath:
            kk+=1;

        # num=kk/3
        # if kk%3!=0:
        #     num=num+1;
        w=500;
        h=1000;
        newImage=Image.new('RGB',(int(kk*w),int(h)),'WHITE');
        x=0
        y=0

        for imf in filepath:
            print(imf)
            im=Image.open(csdata+'/'+imf)

            im=im.resize((w,h))
            newImage.paste(im,(x,y))
            x+=w

        newImage.save(cfdata+'/'+name[-1]+'.jpg')
        self.textBrowser.setText(name[-1]+'的图片已经拼接完成啦！')

    def butten3(self):
        stu=self.lineEdit_5.text();
        cfdata=self.lineEdit_6.text();
        stu=stu.replace('\\','/')
        cfdata = cfdata.replace('\\', '/')
        data = xlrd.open_workbook(stu)
        shet = data.sheet_by_index(0)
        for i in range(shet.nrows):
            isExists = os.path.exists(cfdata + '\\' + shet.cell_value(i, 0))
            if not isExists:
                os.makedirs(cfdata + '\\' + shet.cell_value(i, 0))
        self.textBrowser.setText('每个学生的文件夹已经创建完成！')

    def butten4(self):
        stu = self.lineEdit_7.text();
        csdata = self.lineEdit_8.text();
        stu = stu.replace('\\', '/')
        csdata = csdata.replace('\\', '/')
        data = xlrd.open_workbook(stu)
        shet = data.sheet_by_index(0)
        student=[];
        for i in range(shet.nrows):
            student.append(shet.cell_value(i, 0))
        pths = os.listdir(csdata)
        true = 0;
        for dir in pths:
            pth2 = os.listdir(csdata + '/' + dir)
            for name in pth2:
                zname = name.split('.')[0]
                if zname == dir:
                    true = 1;
            if true == 1:
                student.remove(dir)
                true = 0;


        number=shet.nrows
        lenth=len(student)
        queshi=number-lenth;

        if lenth==0:
            self.textBrowser.setText('检查完毕！已经全部交齐')
        else:
            self.textBrowser.append("检查情况如下：\n"+"应交："+str(number)+"\n实交："+str(queshi)+"\n未交："+str(lenth)+"\n缺失学生名单如下:\n")
            for i in range(len(student)):
                self.textBrowser.append(str(i+1)+' '+student[i]+'\n')


    def butten2(self):
        stu = self.lineEdit_3.text();
        csdata = self.lineEdit_4.text();
        cfdata = self.lineEdit_9.text();
        stu = stu.replace('\\', '/')
        csdata = csdata.replace('\\', '/')
        cfdata = cfdata.replace('\\', '/')
        data = xlrd.open_workbook(stu)
        shet = data.sheet_by_index(0)
        student = []
        stuk = []
        for i in range(shet.nrows):
            student.append(shet.cell_value(i, 0))
            stuk.append(shet.cell_value(i, 0))
        pathlist = os.listdir(csdata);
        lenstu = len(student)

        for i in range(lenstu):
            pinjie = []
            for fn in pathlist:
                m = re.search(student[i], fn)
                if m != None:
                    pinjie.append(fn)
            pjlen = len(pinjie);
            if pjlen != 0:
                w = 500;
                h = 1000;
                newImage = Image.new('RGB', (int(pjlen * w), int(h)), 'WHITE');
                x = 0
                y = 0
                for imf in range(pjlen):
                    im = Image.open(csdata + '/' + pinjie[imf])
                    im = im.resize((w, h))
                    newImage.paste(im, (x, y))
                    x += w
                isExists = os.path.exists(cfdata + '/' + student[i])
                if not isExists:
                    os.makedirs(cfdata + '/' + student[i])
                newImage.save(cfdata + '/' + student[i] + '/' + student[i] + '.jpg')
                stuk.remove(student[i])
        number = shet.nrows
        lenth = len(stuk)
        queshi = number - lenth;

        if lenth == 0:
            self.textBrowser.setText('查找并存储分类完毕！已经全部交齐')
        else:
            self.textBrowser.append(
                "查找并存储分类完成情况如下：\n" + "应存储分类：" + str(number) + "\n实存储分类：" + str(queshi) + "\n未交：" + str(lenth) + "\n缺失学生名单如下:\n")
            for i in range(len(stuk)):
                self.textBrowser.append(str(i + 1) + ' ' + stuk[i] + '\n')

    def xuandi(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit.setText(m)
    def xuandi2(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_2.setText(m)
    def xuandi3(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件夹", "C:/")  # 起始路径

        self.lineEdit_3.setText(m[0])
    def xuandi4(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径

        self.lineEdit_4.setText(m)
    def xuandi5(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_9.setText(m)

    def xuandi6(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_5.setText(m[0])

    def xuandi7(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_6.setText(m)

    def xuandi8(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_7.setText(m[0])

    def xuandi9(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_8.setText(m)

    def xuandi10(self):
        m = QtWidgets.QFileDialog.getOpenFileName(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_10.setText(m[0])
    def xuandi11(self):
        m = QtWidgets.QFileDialog.getExistingDirectory(None, "选取文件夹", "C:/")  # 起始路径
        self.lineEdit_11.setText(m)
    def zhitupian(self):

        script_method1 = torch.jit.script_method
        script1 = torch.jit.script
        torch.jit.script_method = script_method1
        torch.jit.script = script1
        stu = self.lineEdit_10.text();
        csdata = self.lineEdit_11.text();
        stu = stu.replace('\\', '/')
        csdata = csdata.replace('\\', '/')
        path = csdata
        file = os.listdir(path)
        data = xlrd.open_workbook(stu)
        shet = data.sheet_by_index(0)
        reader = easyocr.Reader(['ch_sim'])
        student = []
        stuk = []
        for i in range(shet.nrows):
            student.append(shet.cell_value(i, 0))
            stuk.append(shet.cell_value(i, 0))

        sjm = 100
        for name in file:
            print(name)
            OCRresult = reader.readtext(path + '/' + name);
            k = 1;
            for res in OCRresult:
                strn = res[1];
                for stuname in range(len(student)):
                    m = strn.find(student[stuname])
                    print(m)
                    if m != -1 and k == 1:
                        print(student[stuname])
                        self.textBrowser.append(
                            "图片识别情况如下：\n"+student[stuname]+'识别成功！\n')
                        os.rename(path + '/' + name, path + '/' + student[stuname] + str(sjm) + '.jpg')
                        sjm += 1;
                        k = 0

        self.textBrowser.append('--------识别完成 -------')
if __name__ == '__main__':

    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())