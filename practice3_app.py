from PySide2 import QtCore, QtWidgets
from practice3 import Ui_Form
import time


class ThereadTimer(QtCore.QThread):
    mysignal = QtCore.Signal(str)

    def setTimerParameters(self, startTimer):
        self.startTimer = startTimer

    def run(self) -> None:
        self.status = True
        while self.status:
            time.sleep(1)
            self.mysignal.emit(str(self.startTimer))
            self.startTimer -= 1


class Practice3(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Practice3, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.start_timer)
        self.ui.spinBox.setMinimum(0)
        self.timer1 = ThereadTimer()
        self.ui.pushButton_3.clicked.connect(self.stopTimer)
        self.timer1.mysignal.connect(self.setLineTimer, QtCore.Qt.QueuedConnection)

    def setLineTimer(self, text):
        self.ui.lineEdit.setText(text)

    def start_timer(self):
        self.timer1.setTimerParameters(self.ui.spinBox.value())
        self.ui.lineEdit.setText(str(self.ui.spinBox.value()))
        self.timer1.start()

    @QtCore.Slot()
    def stopTimer(self):
        self.timer1.status = False

#psutil
if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = Practice3()
    win.show()
    app.exec_()
