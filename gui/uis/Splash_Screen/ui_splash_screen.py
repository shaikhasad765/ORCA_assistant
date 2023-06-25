import os
import sys
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if SplashScreen.objectName():
                SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(680, 400)
        SplashScreen.setMaximumSize(QSize(680, 400))
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setContentsMargins(10, 10, 10, 10)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.dropShadowFrame = QFrame(self.centralwidget)
        
        self.dropShadowFrame.setStyleSheet(u"QFrame {\n"
"    color: rgb(220, 220, 220);\n"
"    background-color: rgb(255, 255, 255);\n"
"    border-radius: 70px;\n"
"}")
        self.dropShadowFrame.setFrameShape(QFrame.StyledPanel)
        self.dropShadowFrame.setFrameShadow(QFrame.Raised)
        self.dropShadowFrame.setObjectName(u"dropShadowFrame")
        self.label_title = QLabel(self.dropShadowFrame)
        self.label_title.setGeometry(QRect(10, 40, 641, 141))
        self.label_title.setText("")

        # Get the current directory of the script
        current_directory = os.path.dirname(os.path.abspath(__file__))

        # Construct the relative path to the image file
        image_path = os.path.join(current_directory, "splashscreen.png")

        self.label_title.setPixmap(QPixmap(image_path))
        self.label_title.setAlignment(Qt.AlignCenter)
        self.label_title.setObjectName(u"label_title")
        self.label_title.setStyleSheet(u"label_title {\n"
"    border-radius: 90px;\n""}")
        self.label_description = QLabel(self.dropShadowFrame)
        self.label_description.setGeometry(QRect(130, 180, 421, 81))
        self.label_description.setStyleSheet(u"font: 500 18pt \"My Font\";\n"
"color: rgb(73, 80, 204);")
        self.label_description.setAlignment(Qt.AlignCenter)
        self.label_description.setObjectName(u"label_description")
        self.progressBar = QProgressBar(self.dropShadowFrame)
        self.progressBar.setGeometry(QRect(30, 280, 601, 23))
        self.progressBar.setMaximumSize(QSize(16777215, 260))
        self.progressBar.setStyleSheet(u"QProgressBar {\n"
"    background-color: rgb(98, 114, 164);\n"
"    color: rgb(200, 200, 200);\n"
"    border-style: none;\n"
"    border-radius: 10px;\n"
"    text-align: center;\n"
"}\n"
"QProgressBar::chunk {\n"
"    border-radius: 10px;\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.517, x2:1, y2:0.517, stop:0 rgba(195, 195, 195, 255), stop:1 rgba(73, 80, 204, 255));\n"
"}")
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.label_loading = QLabel(self.dropShadowFrame)
        self.label_loading.setGeometry(QRect(170, 310, 341, 20))
        self.label_loading.setStyleSheet(u"font: 500 18pt \"My Font\";\n"
"color: rgb(73, 80, 204);")
        self.label_loading.setAlignment(Qt.AlignCenter)
        self.label_loading.setObjectName(u"label_loading")
        self.label_credits = QLabel(self.dropShadowFrame)
        self.label_credits.setGeometry(QRect(200, 360, 271, 20))
        self.label_credits.setStyleSheet(u"font: 500 18pt \"My Font\";\n"
"color: rgb(0, 0, 0);\n"
"")
        self.label_credits.setAlignment(Qt.AlignCenter)
        self.label_credits.setObjectName(u"label_credits")
        self.verticalLayout.addWidget(self.dropShadowFrame)
        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)
        QMetaObject.connectSlotsByName(SplashScreen)

    def retranslateUi(self, SplashScreen):
        _translate = QCoreApplication.translate
        SplashScreen.setWindowTitle(_translate(u"SplashScreen", "MainWindow"))
        self.label_description.setText(_translate(u"SplashScreen", "<html><head/><body><p><span style=\" font-size:24pt; font-weight:700; color:#4950cc;\">O </span><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">.</span><span style=\" font-size:24pt; font-weight:700; color:#4950cc;\"> R </span><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">.</span><span style=\" font-size:24pt; font-weight:700; color:#4950cc;\"> C </span><span style=\" font-size:24pt; font-weight:700; color:#ffffff;\">.</span><span style=\" font-size:24pt; font-weight:700; color:#4950cc;\"> A</span></p><p><span style=\" color:#000000;\">The Future Of AI</span></p></body></html>"))
        self.label_loading.setText(_translate(u"SplashScreen", "<html><head/><body><p><span style=\" font-size:14pt;\">Loading...</span></p></body></html>"))
        self.label_credits.setText(_translate(u"SplashScreen", "<html><head/><body><p align=\"center\"><span style=\" font-size:10pt; font-weight:700;\">Created By:</span><span style=\" font-size:9pt;\"> Asadullah Z. Shaikh</span></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    SplashScreen = QMainWindow()
    ui = Ui_SplashScreen()
    ui.setupUi(SplashScreen)
    SplashScreen.show()
    sys.exit(app.exec_())
