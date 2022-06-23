
import sys

from PySide2.QtWidgets import QApplication, QMainWindow

# The reason to import this is because it was auto generated
from forms.ce_login_main import Ui_Main_window

class User_login_controls(QMainWindow):

    def __init__(self):
        super(User_login_controls, self).__init__()

        self.ui = Ui_Main_window()
        self.ui.setupUi(self)

        # self.setWindowTitle("C.E.inc Hi Alma")

        # Make Connections here
        self.make_connections()

        # Show UI 
        self.show()

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


if __name__ == "__main__":
    app = QApplication(sys.argv)

    window = User_login_controls()

    sys.exit(app.exec_())


