import sys
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import QWebEngineView

class Browser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Programer Panel Shayan MeherSaz Pars | پنل برنامه نویسی شایان مهر‍‍ساز پارس')
        self.setGeometry(100, 100, 800, 800)
        
        self.browser = QWebEngineView()
        self.setCentralWidget(self.browser)
        
        # Load a fixed URL without input bar
        self.browser.setUrl(QUrl("https://MeherSazPars.ir"))

app = QApplication(sys.argv)
window = Browser()
window.show()
sys.exit(app.exec_())
