# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from . functions_main_window import *
import sys
import webbrowser
import os
import pyttsx3
from ORC import MainThread
from virtual_keyboard import KeyThread
from ORC import *
from subprocess import call

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

engine = pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('rate', 180)

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from . ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from . functions_main_window import *

# PY WINDOW
# ///////////////////////////////////////////////////////////////

startExecution = MainThread
startKeyboard = KeyThread

class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon" : "icon_home.svg",
            "btn_id" : "btn_home",
            "btn_text" : "Home",
            "btn_tooltip" : "Home page",
            "show_top" : True,
            "is_active" : True
        },
        {
            "btn_icon" : "icon_more_options.svg",
            "btn_id" : "btn_page_2",
            "btn_text" : "Advanced Options",
            "btn_tooltip" : "Advanced Options",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_info.svg",
            "btn_id" : "btn_page_3",
            "btn_text" : "Developer Information",
            "btn_tooltip" : "Developer Information",
            "show_top" : True,
            "is_active" : False
        },
        {
            "btn_icon" : "icon_arrow_right.svg",
            "btn_id" : "btn_settings",
            "btn_text" : "Basic Commands List",
            "btn_tooltip" : "Basic Commands List",
            "show_top" : False,
            "is_active" : False
        }
        
    ]

     # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon" : "icon_signal.svg",
            "btn_id" : "btn_top_settings",
            "btn_tooltip" : "Advance Commands",
            "is_active" : False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////

    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])
        
        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to O.R.C.A Assistant")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        #/////////////////////////////////
        


        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu = self.ui.left_column.menus.menu_1,
            title = "Basic Commands List",
            icon_path = Functions.set_svg_icon("icon_invisible.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ADD LOGO TO HOME

        self.logo = QSvgWidget(Functions.set_svg_image("ortitle.SVG"))

        # ADD TO LAYOUT
        self.ui.load_pages.logo_layout.addWidget(self.logo, Qt.AlignCenter, Qt.AlignHCenter)

        # ADD BUTTONS

        # PUSH BUTTON 1
        self.push_button_1 = PyPushButton(
            text = "START",
            radius  =8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.push_button_1.setMinimumHeight(40)
        self.push_button_1.clicked.connect(self.startTask)

        self.push_button_2 = PyPushButton(
            text = "VIRTUAL KEYBOARD",
            radius  =8,
            color = self.themes["app_color"]["text_foreground"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["dark_four"]
        )
        self.push_button_2.setMinimumHeight(50)
        self.push_button_2.clicked.connect(self.startKey)

        # ICON BUTTON 1
        self.icon_button_1 = PyIconButton(
            icon_path = Functions.set_image("instagram.png"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "INSTAGRAM",
            width = 40,
            height = 40,
            radius = 9,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )
        self.icon_button_1.setObjectName("icon_button_1") 
        self.icon_button_1.clicked.connect(self.openInsta)

        # ICON BUTTON 2
        self.icon_button_2 = PyIconButton(
            icon_path = Functions.set_image("facebook.png"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "FACEBOOK",
            width = 40,
            height = 40,
            radius = 9,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )
        self.icon_button_2.setObjectName("icon_button_2")
        self.icon_button_2.clicked.connect(self.openFB)

        # ICON BUTTON 3
        self.icon_button_3 = PyIconButton(
            icon_path = Functions.set_image("linkedin.png"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "LINKEDIN",
            width = 40,
            height = 40,
            radius = 10,
            dark_one = self.themes["app_color"]["dark_one"],
            icon_color = self.themes["app_color"]["icon_color"],
            icon_color_hover = self.themes["app_color"]["icon_hover"],
            icon_color_pressed = self.themes["app_color"]["icon_active"],
            icon_color_active = self.themes["app_color"]["icon_active"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )
        self.icon_button_3.setObjectName("icon_button_1")
        self.icon_button_3.clicked.connect(self.openLinkedin)

        # ICON BUTTON 4
        self.icon_button_4 = PyIconButton(
            icon_path = Functions.set_svg_icon("icon_info.svg"),
            parent = self,
            app_parent = self.ui.central_widget,
            tooltip_text = "STUDIES AT",
            width = 40,
            height = 40,
            radius = 10,
            dark_one = self.themes["app_color"]["dark_one"],
            bg_color = self.themes["app_color"]["dark_one"],
            bg_color_hover = self.themes["app_color"]["dark_three"],
            bg_color_pressed = self.themes["app_color"]["pink"]
        )
        self.icon_button_4.setObjectName("icon_button_1")
        self.icon_button_4.clicked.connect(self.openCollegesite)

        # ADD WIDGETS
        self.ui.load_pages.page_1_layout.addWidget(self.push_button_1)
        self.ui.load_pages.page_1_layout.setAlignment(Qt.AlignCenter)
        self.ui.load_pages.social_frame_layout.setAlignment(Qt.AlignVCenter|Qt.AlignCenter)
        self.ui.load_pages.social_frame_layout.addWidget(self.icon_button_1)
        self.ui.load_pages.social_frame_layout.addWidget(self.icon_button_2)
        self.ui.load_pages.social_frame_layout.addWidget(self.icon_button_3)
        self.ui.load_pages.social_frame_layout.addWidget(self.icon_button_4)
        self.ui.load_pages.key_frame_layout.setAlignment(Qt.AlignVCenter|Qt.AlignCenter)
        self.ui.load_pages.key_frame_layout.addWidget(self.push_button_2)
        
        # ///////////////////////////////////////////////////////////////
        # END - EXAMPLE CUSTOM WIDGETS
        # ///////////////////////////////////////////////////////////////
        
    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)