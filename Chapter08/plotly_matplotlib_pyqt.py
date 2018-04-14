# -*- coding: utf-8 -*-

"""
注意，本案例需要PyQt5.6以及以下版本才能运行。
否则会提示 cannot import name 'QtWebKitWidgets'
"""


"""
请注意是PyQt5.6以及以下！！！
请注意是PyQt5.6以及以下！！！
请注意是PyQt5.6以及以下！！！
"""
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QMainWindow

from Ui_plotly_matplotlib_pyqt import Ui_MainWindow

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
from Plotly_PyQt5 import Plotly_PyQt5


class MainWindow(QMainWindow, Ui_MainWindow):
    """
    Class documentation goes here.
    """

    def __init__(self, parent=None):
        """
        Constructor

        @param parent reference to the parent widget
        @type QWidget
        """
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.plotly_pyqt5 = Plotly_PyQt5()
        self.webView.setGeometry(QRect(50, 20, 1200, 600))
        self.webView.load(QUrl.fromLocalFile(self.plotly_pyqt5.get_plot_path_matplotlib_plotly()))


app = QApplication(sys.argv)
win = MainWindow()
win.showMaximized()
app.exec_()
