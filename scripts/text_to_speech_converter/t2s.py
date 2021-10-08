# Import the required module for text
# to speech conversion

import sys
from gtts import gTTS
from playsound import playsound
from PyQt5.QtWidgets import (
    QMainWindow,
    QApplication,
    QWidget,
    QPushButton,
    QAction,
    QLineEdit,
    QMessageBox,
)
from PyQt5.QtCore import pyqtSlot


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "Text to Speech Converter"
        self.left = 400
        self.top = 400
        self.width = 400
        self.height = 200
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton("Convert to Audio", self)
        self.button.move(20, 80)
        self.button.resize(200, 30)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        txt = self.textbox.text()
        language = "en"
        filteredtext = ""
        for i in txt:
            if i == " ":
                continue
            filteredtext += i

        if filteredtext.isalpha():
            myobj = gTTS(text=txt, lang=language, slow=False)
        else:
            myobj = gTTS("Please Enter correct value", lang=language, slow=False)

        myobj.save("welcome.mp3")
        playsound("welcome.mp3")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
