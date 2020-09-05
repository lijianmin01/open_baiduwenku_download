import sys

from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import QApplication, QWidget, QMessageBox
from UI import Ui_Form
import BraisedPork2

class Demo(QWidget, Ui_Form):
    def __init__(self):
        super(Demo, self).__init__()
        self.setupUi(self)   # 1

        # 选择是doc文档还是pdf格式
        self.type = 0

        # 文件地址
        self.url = ''

        self.doc_pdf_init()

        self.pushButton.clicked.connect(self.begin_download_func)

        # # 进度
        # self.step = 0
        # self.is_finished = False
        # self.progressBar.setValue(0)
        # self.timer = QTimer(self)  # 4
        # self.timer.timeout.connect(self.update_func)

    # doc pdf 按钮初始化
    def doc_pdf_init(self):
        self.radioButton.setChecked(True)
        self.radioButton.toggled.connect(self.doc_pdf_bulb_func)
        # self.radioButton_2.toggled.connect(self.doc_pdf_bulb_func)

    def doc_pdf_bulb_func(self):  # 8
        if self.radioButton.isChecked():
            self.type = 0
            print('doc')
        else:
            self.type = 1
            print('pdf')

    # 下载按钮初始化  self.pushButton
    def begin_download_func(self):
        self.progressBar.setValue(0)
        self.url = str(self.textEdit.toPlainText())

        if self.url=='':
            QMessageBox.information(self, 'Title', 'URL为空~')
        else:
            print(self.url)
            try:
                if self.type == 0:
                    filename = BraisedPork2.DOC(self.url)
                    if BraisedPork2.is_file_null(filename):
                        print("Doc读取失败，正尝试下种方法")
                        BraisedPork2.TXT(self.url)
                else:
                    choice = QMessageBox.question(self, 'Change Text?', '原文件为pdf格式（yes）,原文件为ppt格式（no）,最终文件以pdf格式保存',
                                                  QMessageBox.Yes | QMessageBox.No)

                    if choice == QMessageBox.Yes:  # 2
                        BraisedPork2.PPT(self.url)
                    elif choice == QMessageBox.No:  # 4
                        BraisedPork2.PPT(self.url)

                self.textEdit.setText("")
                self.url=''
                self.progressBar.setValue(100)

                QMessageBox.information(self, 'Title', '执行成功')
            except:
                QMessageBox.information(self, 'Title', '程序运行错误，请检查')







if __name__ == '__main__':
    app = QApplication(sys.argv)
    demo = Demo()
    demo.show()
    sys.exit(app.exec_())