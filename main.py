from zipfile import ZipFile
import os
from PyQt5.QtWidgets import QWidget, QApplication
from PyQt5.QtGui import QPixmap
import sys
from PIL.ImageQt import ImageQt
from PIL import Image
from design import Ui_Form as Design
from PyQt5 import QtCore
from PyQt5.QtWidgets import QFileDialog
from copy import copy
from PyQt5 import QtCore


class Widget(QWidget, Design):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.output_select)
        self.pushButton_2.clicked.connect(self.input_select)
        self.pushButton_3.clicked.connect(self.archive)
        self.plainTextEdit.setReadOnly(True)

    def output_select(self):
        try:
            path = QFileDialog.getExistingDirectory()
            self.lineEdit.setText(path)
        except:
            pass

    def input_select(self):
        try:
            path = QFileDialog.getExistingDirectory()
            self.lineEdit_2.setText(path)
        except:
            pass

    def archive(self):
        try:
            source = self.lineEdit_2.text()
            dest = self.lineEdit.text()
            counter = 0
            for i in os.walk(source):
                counter += 1
                counter += len(i[-1])
            with ZipFile(f'{dest}\\archive.zip', 'w') as myzip:
                counters = 0
                for i in os.walk(source):
                    counters += 1
                    self.updater(counters, counter)
                    myzip.write(i[0])
                    self.plainTextEdit.appendPlainText(f'Archived: {i[0]}')
                    for j in i[-1]:
                        counters += 1
                        self.updater(counters, counter)
                        myzip.write(f'{i[0]}\\{j}')
                        self.plainTextEdit.appendPlainText(f'Archived: {i[0]}\\{j}')
            self.plainTextEdit.appendPlainText(f'Done!')
        except:
            pass

    def updater(self, num1, num2):
        self.progressBar.setValue(round(num1 / num2 * 100))

# make_reserve_arc('.\\..\\', '.\\..\\..\\')


app = QApplication(sys.argv)
ex = Widget()
ex.show()
sys.exit(app.exec_())