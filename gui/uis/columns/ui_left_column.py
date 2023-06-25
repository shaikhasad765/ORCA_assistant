# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *


class Ui_LeftColumn(object):
    def setupUi(self, LeftColumn):    
        LeftColumn.setObjectName(u"LeftColumn")
        LeftColumn.resize(240, 600)
        self.main_pages_layout = QVBoxLayout(LeftColumn)
        self.main_pages_layout.setSpacing(0)
        self.main_pages_layout.setObjectName(u"main_pages_layout")
        self.main_pages_layout.setContentsMargins(5, 5, 5, 5)
        self.menus = QStackedWidget(LeftColumn)
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
        self.label_1.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_1)

        self.label_4 = QLabel(self.menu_1)
        self.label_4.setObjectName(u"label_4")
        font = QFont()
        font.setPointSize(16)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet(u"font-size: 12pt")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_4)

        self.label_5 = QLabel(self.menu_1)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setPointSize(16)
        self.label_5.setFont(font)
        self.label_5.setStyleSheet(u"font-size: 12pt")
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)

        self.label_6 = QLabel(self.menu_1)
        self.label_6.setObjectName(u"label_6")
        font = QFont()
        font.setPointSize(16)
        self.label_6.setFont(font)
        self.label_6.setStyleSheet(u"font-size: 12pt")
        self.label_6.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_6)

        self.label = QLabel(self.menu_1)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setStyleSheet(u"font-size: 12pt")
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.label_8 = QLabel(self.menu_1)
        self.label_8.setObjectName(u"label_8")
        font = QFont()
        font.setPointSize(16)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet(u"font-size: 12pt")
        self.label_8.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_8)

        self.label_10 = QLabel(self.menu_1)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(16)
        self.label_10.setFont(font)
        self.label_10.setStyleSheet(u"font-size: 12pt")
        self.label_10.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_10)

        self.label_12 = QLabel(self.menu_1)
        self.label_12.setObjectName(u"label_12")
        font = QFont()
        font.setPointSize(16)
        self.label_12.setFont(font)
        self.label_12.setStyleSheet(u"font-size: 12pt")
        self.label_12.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_12)

        self.label_9 = QLabel(self.menu_1)
        self.label_9.setObjectName(u"label_9")
        font = QFont()
        font.setPointSize(16)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet(u"font-size: 12pt")
        self.label_9.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_9)

        self.label_13 = QLabel(self.menu_1)
        self.label_13.setObjectName(u"label_13")
        font = QFont()
        font.setPointSize(16)
        self.label_13.setFont(font)
        self.label_13.setStyleSheet(u"font-size: 12pt")
        self.label_13.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_13)

        self.label_11 = QLabel(self.menu_1)
        self.label_11.setObjectName(u"label_11")
        font = QFont()
        font.setPointSize(16)
        self.label_11.setFont(font)
        self.label_11.setStyleSheet(u"font-size: 12pt")
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_11)

        self.label_15 = QLabel(self.menu_1)
        self.label_15.setObjectName(u"label_15")
        font = QFont()
        font.setPointSize(16)
        self.label_15.setFont(font)
        self.label_15.setStyleSheet(u"font-size: 12pt")
        self.label_15.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_15)

        self.label_16 = QLabel(self.menu_1)
        self.label_16.setObjectName(u"label_16")
        font = QFont()
        font.setPointSize(16)
        self.label_16.setFont(font)
        self.label_16.setStyleSheet(u"font-size: 12pt")
        self.label_16.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_16)

        self.label_17 = QLabel(self.menu_1)
        self.label_17.setObjectName(u"label_17")
        font = QFont()
        font.setPointSize(16)
        self.label_17.setFont(font)
        self.label_17.setStyleSheet(u"font-size: 12pt")
        self.label_17.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_17)

        self.label_18 = QLabel(self.menu_1)
        self.label_18.setObjectName(u"label_18")
        font = QFont()
        font.setPointSize(16)
        self.label_18.setFont(font)
        self.label_18.setStyleSheet(u"font-size: 12pt")
        self.label_18.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_18)

        self.label_19 = QLabel(self.menu_1)
        self.label_19.setObjectName(u"label_19")
        font = QFont()
        font.setPointSize(16)
        self.label_19.setFont(font)
        self.label_19.setStyleSheet(u"font-size: 12pt")
        self.label_19.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_19)

        self.label_14 = QLabel(self.menu_1)
        self.label_14.setObjectName(u"label_14")
        font = QFont()
        font.setPointSize(16)
        self.label_14.setFont(font)
        self.label_14.setStyleSheet(u"font-size: 12pt")
        self.label_14.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_14)

        self.label_20 = QLabel(self.menu_1)
        self.label_20.setObjectName(u"label_20")
        font = QFont()
        font.setPointSize(16)
        self.label_20.setFont(font)
        self.label_20.setStyleSheet(u"font-size: 12pt")
        self.label_20.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_20)

        self.label_7 = QLabel(self.menu_1)
        self.label_7.setObjectName(u"label_7")
        font = QFont()
        font.setPointSize(16)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet(u"font-size: 12pt")
        self.label_7.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_7)

        self.menus.addWidget(self.menu_1)
        self.menu_2 = QWidget()
        self.menu_2.setObjectName(u"menu_2")
        self.verticalLayout_2 = QVBoxLayout(self.menu_2)
        self.verticalLayout_2.setSpacing(5)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(5, 5, 5, 5)


        self.label_2 = QLabel(self.menu_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setStyleSheet(u"font-size: 16pt")
        self.label_2.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.label_2)

        self.label_3 = QLabel(self.menu_2)
        self.label_3.setObjectName(u"label_3")
        font1 = QFont()
        font1.setPointSize(9)
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"font-size: 9pt")
        self.label_3.setAlignment(Qt.AlignCenter)
        self.label_3.setWordWrap(True)

        self.verticalLayout_2.addWidget(self.label_3)

        self.menus.addWidget(self.menu_2)

        self.main_pages_layout.addWidget(self.menus)


        self.retranslateUi(LeftColumn)

        self.menus.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(LeftColumn)
    # setupUi

    def retranslateUi(self, LeftColumn):
        LeftColumn.setWindowTitle(QCoreApplication.translate("LeftColumn", u"Form", None))
        self.label_4.setText(QCoreApplication.translate("LeftColumn", u"1. Play Music"))
        self.label_5.setText(QCoreApplication.translate("LeftColumn", u"2. Open Youtube"))
        self.label_6.setText(QCoreApplication.translate("LeftColumn", u"3. Wikipedia"))
        self.label.setText(QCoreApplication.translate("LeftColumn", u"4. Sleep Now(stops Listening)"))
        self.label_8.setText(QCoreApplication.translate("LeftColumn", u"5. Open Stackoverflow"))
        self.label_10.setText(QCoreApplication.translate("LeftColumn", u"6. The Time"))
        self.label_12.setText(QCoreApplication.translate("LeftColumn", u"7. Open/Close Code"))
        self.label_9.setText(QCoreApplication.translate("LeftColumn", u"8. Open/Close Notepad"))
        self.label_13.setText(QCoreApplication.translate("LeftColumn", u"9. Open Adobe Reader"))
        self.label_11.setText(QCoreApplication.translate("LeftColumn", u"10. Open Command Prompt"))
        self.label_15.setText(QCoreApplication.translate("LeftColumn", u"11. Open Google"))
        self.label_16.setText(QCoreApplication.translate("LeftColumn", u"12. Tell Me A Joke"))
        self.label_17.setText(QCoreApplication.translate("LeftColumn", u"13. IP Address"))
        self.label_18.setText(QCoreApplication.translate("LeftColumn", u"14. Open/Close Facebook"))
        self.label_19.setText(QCoreApplication.translate("LeftColumn", u"15. Take A Screenshot"))
        self.label_14.setText(QCoreApplication.translate("LeftColumn", u"16. Open/Close Instagram"))
        self.label_20.setText(QCoreApplication.translate("LeftColumn", u"16. Open/Close Chrome"))
        self.label_7.setText(QCoreApplication.translate("LeftColumn", u"17. Open/Close Edge"))
        self.label_1.setText(QCoreApplication.translate("LeftColumn", u"Voice Commands", None))

    # retranslateUi

