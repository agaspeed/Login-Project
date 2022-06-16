
from sys import get_coroutine_origin_tracking_depth
from PySide2 import QtCore, QtWidgets, QtGui

# The reason to import this is because it was auto generated
from forms.ce_login_main import Ui_Main_window

class User_login_controls(QtWidgets.QWidget):

    def __init__(self, broker):
        super(User_login_controls, self).__init__()
        print("Nice  Alma!")
        self.broker = broker
        self.ui = Ui_Main_window()
        self.ui.setupUi(self)

        #TODO: make the window show. 


        self.make_connections(self)

    def make_connections(self):
        # here is where you will make connections to the buttons and right click actions 
        # useful to look into how to connect actions to buttons (Hint: clicked.connect)
        # look into what lamda is in python
        pass

    def retranslateUi(self):
        self.ui.retranslateUi(self)

    def configure(self, source):
        pass

    def show_controls(self):
        pass


