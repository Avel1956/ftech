import sys
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.uic import loadUi
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
""""""
l = 0
h = 0
a = 0


class guiTest(QDialog):
    def __init__(self):
        super(guiTest, self).__init__()
        loadUi('Uitest.ui', self)
        self.setWindowTitle('First test')
        self.okBot.clicked.connect(self.on_pushButton_clicked)
        self.exBut.clicked.connect(self.on_pushButton_clicked2)

    @pyqtSlot()
    def on_pushButton_clicked(self):
        self.label.setText('welcome')

    def on_pushButton_clicked2(self):
        x = float(self.xEd.text())
        y = float(self.yEd.text())
        z = float(self.zEd.text())

        plotex(x, y, z)


app = QApplication(sys.argv)


def plotex(x, y, z):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter(x, y, z, c='r', marker='o')

    ax.set_xlabel('X Label')
    ax.set_ylabel('Y Label')
    ax.set_zlabel('Z Label')

    plt.show()


widget = guiTest()
widget.show()

sys.exit(app.exec_())
