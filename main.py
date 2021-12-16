from PySide2 import QtCore, QtWidgets
from practice2 import Ui_Form
from functools import partial


class Practice2(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Practice2, self).__init__(parent)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.pushbutton_move)
        self.ui.pushButton_2.clicked.connect(self.pushbutton_move)
        self.ui.pushButton_3.clicked.connect(self.pushbutton_move)
        self.ui.pushButton_4.clicked.connect(self.pushbutton_move)
        self.ui.pushButton_5.clicked.connect(self.pushbutton_move)
        self.ui.pushButton_6.clicked.connect(self.pushbutton_params)
        self.ui.dial.valueChanged.connect(self.lsdNumberValue)
        self.ui.horizontalSlider.valueChanged.connect(self.lsdNumberValue)
        self.ui.pushButton_6.setShortcut('F1')

    def pushbutton_move(self):
        screenWidth = QtWidgets.QApplication.screenAt(self.pos()).size().width()
        screenHeight = QtWidgets.QApplication.screenAt(self.pos()).size().height()
        if self.sender().objectName() == 'pushButton':
            self.move(0, 0)
        if self.sender().objectName() == 'pushButton_2':
            self.move(screenWidth - self.width(), 0)
        if self.sender().objectName() == 'pushButton_3':
            self.move(screenWidth / 2 - self.width() / 2, screenHeight / 2 - self.height() / 2)
        if self.sender().objectName() == 'pushButton_4':
            self.move(0, screenHeight - self.height())
        if self.sender().objectName() == 'pushButton_5':
            self.move(screenWidth - self.width(), screenHeight - self.height())

    def pushbutton_params(self):
        self.ui.plainTextEdit.appendPlainText(str(len(QtWidgets.QApplication.screens())))
        self.ui.plainTextEdit.appendPlainText(QtWidgets.QApplication.primaryScreen().name())
        self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.screenAt(self.pos()).size()))
        self.ui.plainTextEdit.appendPlainText(QtWidgets.QApplication.screenAt(self.pos()).name())
        self.ui.plainTextEdit.appendPlainText(str(self.size()))
        self.ui.plainTextEdit.appendPlainText(str(self.minimumSize()))
        self.ui.plainTextEdit.appendPlainText(str(self.pos()))
        self.ui.plainTextEdit.appendPlainText(
            f'{self.pos().x() + self.width() / 2}, {self.pos().y() + self.height() / 2}')

    def event(self, event: QtCore.QEvent):
        if event.type() == QtCore.QEvent.Type.Move:
            print(self.pos())
        if event.type() == QtCore.QEvent.Type.Resize:
            print(self.size())
        if event.type() == QtCore.QEvent.Type.WindowStateChange:
            self.ui.plainTextEdit.appendPlainText(str(QtWidgets.QApplication.applicationState()))
        return QtWidgets.QWidget.event(self, event)

    def eventFilter(self, watched: QtCore.QObject, event: QtCore.QEvent) -> bool:
        if watched == self.dial:
            self.ui.horizontalSlider.setValue(self.ui.lcdNumber.value())
        elif watched == self.slider:
            self.ui.lcdNumber.display(self.ui.horizontalSlider.value())
            self.ui.dial.setValue(self.ui.lcdNumber.value())
        return super(Practice2, self).eventFilter(watched, event)

    def dial(self):
        print("dial")
        self.ui.lcdNumber.display(self.ui.dial.value())
        self.ui.horizontalSlider.setValue(self.ui.lcdNumber.value())

    def slider(self):
        print("slider")
        self.ui.lcdNumber.display(self.ui.horizontalSlider.value())
        self.ui.dial.setValue(self.ui.lcdNumber.value())

    def lsdNumberValue(self):
        self.installEventFilter(self)



if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = Practice2()
    win.show()
    app.exec_()
