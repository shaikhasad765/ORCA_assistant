# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from category_encoders import one_hot
from requests.models import Response
from qt_core import *


class Ui_RightColumn(object):
    def setupUi(self, RightColumn):
        RightColumn.setObjectName(u"RightColumn")
        RightColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(RightColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(RightColumn)
        self.menus.setObjectName(u"menus")
        self.menu_1 = QWidget()
        self.menu_1.setObjectName(u"menu_1")
        self.verticalLayout = QVBoxLayout(self.menu_1)
        self.verticalLayout.setSpacing(5)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)

        self.label_1 = QLabel(self.menu_1)
        self.label_1.setObjectName(u"label_1")
        font = QFont()
        font.setPointSize(16)
        self.label_1.setFont(font)
        self.label_1.setStyleSheet(u"font-size: 16pt")
        self.label_1.setAlignment(Qt.AlignCenter|Qt.AlignTop)
        self.label_1.setStyleSheet(u"QLabel {\n"
"   font: 57 16pt \"My Font\"; \n"
"}")
        self.verticalLayout.addWidget(self.label_1)

        self.menus.addWidget(self.menu_1)

        self.response_box = QTextBrowser(self.menu_1)
        self.response_box.setMinimumSize(QSize(210, 550))
        self.response_box.setStyleSheet("background-color: rgb(27, 30, 35);\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.response_box.setFrameShape(QFrame.NoFrame)
        self.response_box.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.response_box.setObjectName("response_box")
        self.response_box.setAlignment(Qt.AlignCenter)
        self.verticalLayout.addWidget(self.response_box)

        self.main_pages_layout.addWidget(self.menus)
        self.retranslateUi(RightColumn)
        self.menus.setCurrentIndex(1)
        QMetaObject.connectSlotsByName(RightColumn)
    # setupUi
    
    def retranslateUi(self, RightColumn):
        RightColumn.setWindowTitle(QCoreApplication.translate("RightColumn", u"Form", None))
        self.label_1.setText(QCoreApplication.translate("RightColumn", u"Response Box", None))
    # retranslateUi
