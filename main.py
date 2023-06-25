from email.mime import text
from pynput import keyboard
import shiboken6
from ORC import MainThread
from gui.core.functions import Functions
from gui.uis.windows.main_window.functions_main_window import *
import sys
import os
import webbrowser
import cv2

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# MAIN WINDOW
from gui.uis.windows.main_window import *

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *


# ADJUST QT FONT DPI FOR HIGHT SCALE AN 4K MONITOR
# ///////////////////////////////////////////////////////////////
os.environ["QT_FONT_DPI"] = "96"
# IF IS 4K MONITOR ENABLE 'os.environ["QT_SCALE_FACTOR"] = "2"'


import platform
import sys
from PySide6 import QtCore
from qt_core import *

from virtual_keyboard import KeyThread

#splash screen
from gui.uis.Splash_Screen.ui_splash_screen import Ui_SplashScreen

#main window
from gui.uis.windows.main_window.ui_main import UI_MainWindow

#Globals
counter = 0

recognizer = cv2.face.LBPHFaceRecognizer_create() # Local Binary Patterns Histograms
recognizer.read('trainer/trainer.yml') # load trained model
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath) # initializing haar cascade for object detection approach

font = cv2.FONT_HERSHEY_SIMPLEX # denotes the font type

id = 2 # number of persons you want to recognize

names = ['','Asad Shaikh'] # names, leave first empty because counter starts from 0

cam = cv2.VideoCapture(0, cv2.CAP_DSHOW) # cv2.CAP_DSHOW to remove warning
cam.set(3, 640) #set video FrameWidth
cam.set(4, 480) #set video FrameHeight

#define min window size to be recognized as a face
minW = 0.1*cam.get(3)
minH = 0.1*cam.get(4)

while True:

    ret, img =cam.read() # read the frames using the above created object

    converted_image = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) # the function converts an input image from one color space to another

    faces = faceCascade.detectMultiScale(
        converted_image,
        scaleFactor = 1.2,
        minNeighbors = 5,
        minSize = (int(minW), int(minH)),
    )

    for(x,y,w,h) in faces:

        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) #used to draw a rectangle on any image

        id, accuracy = recognizer.predict(converted_image[y:y+h,x:x+w]) # to predict on every single image

        # check if accuracy is less than 100 ==> "0" is perfect match
        if (accuracy < 100):
            id = names[id]
            accuracy = "   {0}%".format(round(100 - accuracy))

        else:
            id = "Face Not Recognized"
            accuracy = "   {0}%".format(round(100 - accuracy))

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(accuracy), (x+5,y+h-5), font, 1, (255,255,0), 1)

    cv2.imshow('Press Esc to Authenticate', img)

    k = cv2.waitKey(10) & 0xff # press 'Ese' to exit video
    if k==27:
        break

print("Thanks for using this program, have a good day.")
cam.release()
cv2.destroyAllWindows()

if id == "Face Not Recognized" or "":
    print("Unknown Person")
    sys.exit()

else:
    print("Face Verified")
    print("Welcome Back")
    class SplashScreen(QMainWindow):
        def __init__(self):
            QMainWindow.__init__(self)
            self.ui = Ui_SplashScreen()
            self.ui.setupUi(self)

            #remove title bar
            self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
            self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

            #drop shadow effect
            self.shadow = QGraphicsDropShadowEffect(self)
            self.shadow.setBlurRadius(20)
            self.shadow.setXOffset(0)
            self.shadow.setYOffset(0)
            self.shadow.setColor(QColor(0, 0, 0, 60))
            self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

            #timer

            self.timer = QtCore.QTimer()
            self.timer.timeout.connect(self.progress)

            #timer in miliseconds
            self.timer.start(35)

            #show mainwindow
            self.show()

        def progress(self):

            global counter
            #set value to progress bar
            self.ui.progressBar.setValue(counter)

            #close splash screen
            if counter > 100:

                #stop timer
                self.timer.stop()

                #show main window
                self.main = MainWindow()
                self.main.show()

                #close splash screen
                self.close()

            #increase 
            counter += 1

    # MAIN WINDOW
    # ///////////////////////////////////////////////////////////////

startExecution = MainThread() 
startKeyboard = KeyThread()
class MainWindow(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # SETUP MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.hide_grips = True # Show/Hide resize grips
        SetupMainWindow.setup_gui(self)

        # SHOW MAIN WINDOW
        # ///////////////////////////////////////////////////////////////
        self.show()

    # LEFT MENU BTN IS CLICKED
    # Run function when btn is clicked
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////

    def startTask(self):
        startExecution.start()

    def startKey(self):
        startKeyboard.start()
    
    def openInsta(self):
        webbrowser.open("https://www.instagram.com/asadshaikh5908/")

    def openFB(self):
        webbrowser.open("https://www.facebook.com/profile.php?id=100016331925690")

    def openLinkedin(self):
        webbrowser.open("https://www.linkedin.com/in/asad-shaikh-a1ab9a223/")

    def openCollegesite(self):
        webbrowser.open("http://cms.sinhgad.edu/sinhgad_management_institutes/sibar_mba/about-sibar.aspx")

    def btn_clicked(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        #Left Menu
        # ///////////////////

        # Home Page 1
        if btn.objectName() == "btn_home":
            #select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            #load page
            MainFunctions.set_page(self, self.ui.load_pages.page_1)

        # More Options page 2
        if btn.objectName() == "btn_page_2":
            #select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            #load page
            MainFunctions.set_page(self, self.ui.load_pages.page_2)

        # Developer Info page 3
        if btn.objectName() == "btn_page_3":
            #select menu
            self.ui.left_menu.select_only_one(btn.objectName())

            #load page
            MainFunctions.set_page(self, self.ui.load_pages.page_3)

        #get advanced command
        top_settings = MainFunctions.get_title_bar_btn(self, "btn_top_settings")

        # open basic commands
        if btn.objectName() == "btn_settings" or btn.objectName() == "btn_close_left_column":
            #disable selection on title bar
            top_settings.set_active(False)

            #check if left column is visible
            if not MainFunctions.left_column_is_visible(self):
                #show / Hide
                MainFunctions.toggle_left_column(self)
                self.ui.left_menu.select_only_one_tab(btn.objectName())
            else:
                if btn.objectName() == "btn_close_left_column": 
                    #deselect all tabs selected
                    self.ui.left_menu.deselect_all_tab()

                    #show / hide 
                    MainFunctions.toggle_left_column(self)

                #select tab
                self.ui.left_menu.select_only_one_tab(btn.objectName())

            if btn.objectName() != "btn_close_left_column":
                MainFunctions.set_left_column_menu(
                    self,
                    menu = self.ui.left_column.menus.menu_1,
                    title = "Basic Commands List",
                    icon_path= Functions.set_svg_icon("icon_invisible.svg")
                )

        # TITLE BAR MENU
        # ///////////////////////////////////////////////////////////////
        
        # SETTINGS TITLE BAR
        if btn.objectName() == "btn_top_settings":
            # Toogle Active
            if not MainFunctions.right_column_is_visible(self):
                btn.set_active(True)
                
                # Show / Hide
                MainFunctions.toggle_right_column(self)
            else:
                btn.set_active(False)

                # Show / Hide
                MainFunctions.toggle_right_column(self)

            # Get Left Menu Btn            
            top_settings = MainFunctions.get_left_menu_btn(self, "btn_settings")
            top_settings.set_active_tab(False)            

        # DEBUG
        print(f"Button {btn.objectName()}, clicked!")

    # LEFT MENU BTN IS RELEASED
    # Run function when btn is released
    # Check funtion by object name / btn_id
    # ///////////////////////////////////////////////////////////////
    def btn_released(self):
        # GET BT CLICKED
        btn = SetupMainWindow.setup_btns(self)

        # DEBUG
        print(f"Button {btn.objectName()}, released!")

    # RESIZE EVENT
    # ///////////////////////////////////////////////////////////////
    def resizeEvent(self, event):
        SetupMainWindow.resize_grips(self)

    # MOUSE CLICK EVENTS
    # ///////////////////////////////////////////////////////////////
    def mousePressEvent(self, event):
        # SET DRAG POS WINDOW
        self.dragPos = event.globalPos()




# SETTINGS WHEN TO START
# Set the initial class and also additional parameters of the "QApplication" class
# ///////////////////////////////////////////////////////////////
if __name__ == "__main__":
    # APPLICATION
    # ///////////////////////////////////////////////////////////////
    app = QApplication(sys.argv)
    app.setWindowIcon(QIcon("icon.ico"))
    window = SplashScreen()

    # EXEC APP
    # ///////////////////////////////////////////////////////////////
    sys.exit(app.exec_())