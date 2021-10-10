from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWebEngineWidgets import *

WebbrowserName = "S.A.I. Web Browser"
Version = "0.1"
Author = "Jack Franklin - SAI Tech"

DisplayName = (WebbrowserName + " | " + "Version " + Version)

class MyWebBrowser(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MyWebBrowser, self).__init__(*args, **kwargs)

        self.window = QWidget()
        self.window.setWindowTitle(DisplayName)

        self.layout = QVBoxLayout()
        self.horizontal = QHBoxLayout()

        self.url_bar = QTextEdit()
        self.url_bar.setMaximumHeight(30)

        self.go_btn = QPushButton("Go")
        self.go_btn.setMinimumHeight(30)

        self.back_btn = QPushButton("<")
        self.back_btn.setMinimumHeight(30)

        self.forward_btn = QPushButton(">")
        self.forward_btn.setMinimumHeight(30)

        self.horizontal.addWidget(self.url_bar)
        self.horizontal.addWidget(self.go_btn)
        self.horizontal.addWidget(self.back_btn)
        self.horizontal.addWidget(self.forward_btn)

        self.browser = QWebEngineView()

        self.go_btn.clicked.connect(lambda: self.navigate(self.url_bar.toPlainText()))
        self.back_btn.clicked.connect(self.browser.back)
        self.forward_btn.clicked.connect(self.browser.forward)



        self.layout.addLayout(self.horizontal)
        self.layout.addWidget(self.browser)

        self.browser.setUrl(QUrl("http://google.com/"))

        self.window.setLayout(self.layout)
        self.window.show()

    def navigate(self, url):
        if "www." in url:
            url = url.replace("www.", "http://")
            self.url_bar.setText(url)
            self.browser.setUrl(QUrl(url))
        else:
            url = "https://google.com/search?q=%s" % url
            self.url_bar.setText(url)
            self.browser.setUrl(QUrl(url))
        f = open("SAI_Search_History.txt", "a")
        f.write(" | " + url + " | ")
        f.close()

app = QApplication([])
window = MyWebBrowser()
app.exec_()
