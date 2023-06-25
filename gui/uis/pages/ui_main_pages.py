from gui.widgets.py_icon_button.py_icon_button import PyIconButton
from qt_core import *


class Ui_MainPages(object):
    def setupUi(self, MainPages):
        if not MainPages.objectName():
            MainPages.setObjectName(u"MainPages")
        MainPages.resize(860, 600)
        self.main_pages_layout = QVBoxLayout(MainPages)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.pages = QStackedWidget(MainPages)
        self.pages.setObjectName(u"pages")
        self.page_1 = QWidget()
        self.page_1.setObjectName(u"page_1")
        self.page_1.setStyleSheet(u"font-size: 14pt")
        self.page_1_layout = QVBoxLayout(self.page_1)
        self.page_1_layout.setSpacing(5)
        self.page_1_layout.setObjectName(u"page_1_layout")
        self.page_1_layout.setContentsMargins(5, 5, 5, 5)
        self.welcome_base = QFrame(self.page_1)
        self.welcome_base.setObjectName(u"welcome_base")
        self.welcome_base.setMinimumSize(QSize(300, 150))
        self.welcome_base.setMaximumSize(QSize(300, 150))
        self.welcome_base.setFrameShape(QFrame.NoFrame)
        self.welcome_base.setFrameShadow(QFrame.Raised)
        self.center_page_layout = QVBoxLayout(self.welcome_base)
        self.center_page_layout.setSpacing(10)
        self.center_page_layout.setObjectName(u"center_page_layout")
        self.center_page_layout.setContentsMargins(0, 0, 0, 0)
        
        self.logo = QFrame(self.welcome_base)
        self.logo.setObjectName(u"logo")
        self.logo.setMinimumSize(QSize(300, 120))
        self.logo.setMaximumSize(QSize(300, 120))
        self.logo.setFrameShape(QFrame.NoFrame)
        self.logo.setFrameShadow(QFrame.Raised)
        self.logo_layout = QVBoxLayout(self.logo)
        self.logo_layout.setSpacing(0)
        self.logo_layout.setObjectName(u"logo_layout")
        self.logo_layout.setContentsMargins(0, 0, 0, 0)

        self.center_page_layout.addWidget(self.logo)

        self.label = QLabel(self.welcome_base)
        self.label.setObjectName(u"label")
        self.label.setAlignment(Qt.AlignCenter)

        self.center_page_layout.addWidget(self.label)

        self.page_1_layout.addWidget(self.welcome_base, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.page_1)

        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setSpacing(5)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setContentsMargins(5, 5, 5, 5)
        self.page_2_layout.setAlignment(Qt.AlignCenter)
        self.scroll_area = QScrollArea(self.page_2)
        self.scroll_area.setObjectName(u"scroll_area")
        self.scroll_area.setStyleSheet(u"background: transparent;")
        self.scroll_area.setFrameShape(QFrame.NoFrame)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.scroll_area.setWidgetResizable(True)
        self.contents = QWidget()
        self.contents.setObjectName(u"contents")
        self.contents.setGeometry(QRect(0, 0, 840, 580))
        self.contents.setStyleSheet(u"background: transparent;")
        self.verticalLayout = QVBoxLayout(self.contents)
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 5, 5, 5)
        self.title_label = QLabel(self.contents)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setMaximumSize(QSize(16777215, 40))
        font = QFont()
        font.setPointSize(16)
        self.title_label.setFont(font)
        self.title_label.setStyleSheet(u"font-size: 16pt")
        self.title_label.setAlignment(Qt.AlignCenter)

        

        self.description_label = QLabel(self.contents)
        self.description_label.setObjectName(u"description_label")
        self.description_label.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.description_label.setWordWrap(True)

        self.verticalLayout.addWidget(self.description_label)

        self.row_1_layout = QHBoxLayout()
        self.row_1_layout.setObjectName(u"row_1_layout")

        self.verticalLayout.addLayout(self.row_1_layout)

        self.row_2_layout = QHBoxLayout()
        self.row_2_layout.setObjectName(u"row_2_layout")

        self.verticalLayout.addLayout(self.row_2_layout)

        self.row_3_layout = QHBoxLayout()
        self.row_3_layout.setObjectName(u"row_3_layout")

        self.verticalLayout.addLayout(self.row_3_layout)

        self.row_4_layout = QVBoxLayout()
        self.row_4_layout.setObjectName(u"row_4_layout")

        self.verticalLayout.addLayout(self.row_4_layout)

        self.row_5_layout = QVBoxLayout()
        self.row_5_layout.setObjectName(u"row_5_layout")

        self.verticalLayout.addLayout(self.row_5_layout)

        self.scroll_area.setWidget(self.contents)

        self.page_2_layout.addWidget(self.scroll_area)

        self.pages.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.page_3.setStyleSheet(u"QFrame {\n"
"	font-size: 16pt;\n"
"}")
        self.page_3_layout = QVBoxLayout(self.page_3)
        self.page_3_layout.setObjectName(u"page_3_layout")
        self.page_3_layout.setAlignment(Qt.AlignCenter)
        self.social_frame = QFrame(self.page_3)
        self.social_frame.setObjectName(u"social_frame")
        self.social_frame.setMinimumWidth(500)
        self.social_frame.setMinimumHeight(60)
        self.social_frame.setFrameShape(QFrame.NoFrame)
        self.social_frame.setFrameShadow(QFrame.Raised)
        self.social_frame_layout = QHBoxLayout(self.social_frame)
        self.social_frame_layout.setObjectName(u"social_frame_layout")
        self.social_frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(44, 49, 60); \n"
"    border-radius: 10px;\n"
"}")

        self.page_2_layout = QVBoxLayout(self.page_2)
        self.page_2_layout.setObjectName(u"page_2_layout")
        self.page_2_layout.setAlignment(Qt.AlignCenter)
        self.key_frame = QFrame(self.page_2)
        self.key_frame.setObjectName(u"social_frame")
        self.key_frame.setMinimumWidth(500)
        self.key_frame.setMinimumHeight(100)
        self.key_frame.setFrameShape(QFrame.NoFrame)
        self.key_frame.setFrameShadow(QFrame.Raised)
        self.key_frame_layout = QVBoxLayout(self.key_frame)
        self.key_frame_layout.setObjectName(u"key_frame_layout")
        self.key_frame.setStyleSheet("QFrame{\n"
"    background-color: rgb(44, 49, 60); \n"
"    border-radius: 10px;\n"
"}")
        self.key_frame_layout.addWidget(self.title_label)

        self.label_profile = QLabel(self.page_3)
        self.label_profile.setObjectName(u"label_profile")
        self.label_profile.setFont(font)
        self.label_profile.setPixmap(QPixmap(u"C:/Users/Asad/ORCA_Main/gui/images/svg_images/asad_profile.png"))
        self.label_profile.setMaximumHeight(500)
        self.label_profile.setMaximumWidth(500)
        self.label_profile.setAlignment(Qt.AlignCenter)
        self.label_profile.setStyleSheet("QLabel{\n"
"    background: transparent; \n"
"    border-radius: 250px;\n"
"}")

        self.label2 = QLabel(self.page_3)
        self.label2.setObjectName(u"label2")
        self.label2.setFont(font)
        self.label2.setMaximumHeight(40)
        self.label2.setMinimumWidth(500)
        self.label2.setAlignment(Qt.AlignCenter)
        self.label2.setStyleSheet("QLabel{\n"
"    font: 57 16pt \"My Font\"; \n"
"    background-color: rgb(27, 30, 35); \n"
"    border-radius: 10px;\n"
"}")

        self.label3 = QLabel(self.page_3)
        self.label3.setObjectName(u"label3")
        self.label3.setFont(font)
        self.label3.setMaximumHeight(40)
        self.label3.setMaximumWidth(500)
        self.label3.setAlignment(Qt.AlignCenter)
        self.label3.setStyleSheet("QLabel{\n"
"    font: 57 16pt \"My Font\"; \n"
"    background-color: rgb(27, 30, 35); \n"
"    border-radius: 10px;\n"
"}")

        self.page_3_layout.addWidget(self.label_profile)
        self.page_3_layout.addWidget(self.label2)
        self.page_3_layout.addWidget(self.label3)
        self.page_3_layout.addWidget(self.social_frame)

        self.pages.addWidget(self.page_3)

        self.main_pages_layout.addWidget(self.pages)


        self.retranslateUi(MainPages)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainPages)
    # setupUi

    def retranslateUi(self, MainPages):
        MainPages.setWindowTitle(QCoreApplication.translate("MainPages", u"Form", None))
        self.label.setText(QCoreApplication.translate("MainPages", u"Welcome To O.R.C.A Assistant", None))
        self.title_label.setText(QCoreApplication.translate("MainPages", u"O.R.C.A Widgets", None))
        self.label2.setText(QCoreApplication.translate("MainPages", u"NAME: ASADULLAH ZAINNULAH SHAIKH", None))
        self.label3.setText(QCoreApplication.translate("MainPages", u"CLASS: MCA III", None))

