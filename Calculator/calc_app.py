from PySide2 import QtCore, QtWidgets
from CalculateTest import Ui_Form


class CalcApp(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(CalcApp, self).__init__(parent)
        self.method = None
        self.a = None
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.ui.pushButton_0.clicked.connect(self.push_number)
        self.ui.Butt_1.clicked.connect(self.push_number)
        self.ui.Butt_2.clicked.connect(self.push_number)
        self.ui.Butt_3.clicked.connect(self.push_number)
        self.ui.Butt_4.clicked.connect(self.push_number)
        self.ui.Butt_5.clicked.connect(self.push_number)
        self.ui.Butt_6.clicked.connect(self.push_number)
        self.ui.butt_7.clicked.connect(self.push_number)
        self.ui.butt_8.clicked.connect(self.push_number)
        self.ui.Butt_9.clicked.connect(self.push_number)
        self.ui.Butt_point.clicked.connect(self.push_point)
        self.ui.Butt_pos_neg.clicked.connect(self.push_pos_neg)
        self.ui.Butt_add.clicked.connect(self.push_add)
        self.ui.Butt_sub.clicked.connect(self.push_sub)
        self.ui.Butt_multy.clicked.connect(self.push_multy)
        self.ui.Butt_div.clicked.connect(self.push_div)
        self.ui.Butt_del.clicked.connect(self.push_del)
        self.ui.Butt_C.clicked.connect(self.push_C)
        self.ui.Butt_CE.clicked.connect(self.push_CE)
        self.ui.Butt_eu.clicked.connect(self.push_eu)
        self.ui.Butt_sqrtX.clicked.connect(self.push_sqrtX)
        self.ui.Butt_X2.clicked.connect(self.push_X2)
        self.ui.Butt_1_X.clicked.connect(self.push_1_X)
        self.ui.Butt_percent.clicked.connect(self.push_percent)

    def push_number(self):
        if self.method != 'eu':
            if self.ui.Result.text() == '0':
                if self.sender().text() == ',':
                    self.ui.Result.setText('0' + self.sender().text())
                else:
                    self.ui.Result.setText(self.sender().text())
            else:
                self.ui.Result.setText(self.ui.Result.text() + self.sender().text())

    def push_pos_neg(self):
        if self.ui.Result.text()[0] == '-':
            self.ui.Result.setText(self.ui.Result.text()[1:])
        else:
            self.ui.Result.setText('-' + self.ui.Result.text())

    def push_point(self):
        self.ui.Result.setText(self.ui.Result.text() + '.')

    def push_add(self):
        if self.method != "add":
            if self.method == 'eu' or self.method is None:
                self.a = float(self.ui.Result.text())
            self.ui.Result.setText('0')
            self.method = "add"
        else:
            if self.a != 0:
                self.a += float(self.ui.Result.text())
                self.ui.Result.setText('0')
                self.method = "add"
                # self.push_eu()

    def push_sub(self):
        if self.method != "sub":
            if self.method == 'eu' or self.method is None:
                self.a = float(self.ui.Result.text())
            self.ui.Result.setText('0')
            self.method = "sub"
        else:
            if self.a != 0:
                self.a -= float(self.ui.Result.text())
                self.ui.Result.setText('0')
                self.method = "sub"

    def push_multy(self):
        if self.method != "multy":
            if self.method == 'eu' or self.method is None:
                self.a = float(self.ui.Result.text())
            self.ui.Result.setText('0')
            self.method = "multy"
        else:
            if self.a != 0:
                self.a *= float(self.ui.Result.text())
                self.ui.Result.setText('0')
                self.method = "multy"

    def push_div(self):
        if self.method != "div":
            if self.method == 'eu' or self.method is None:
                self.a = float(self.ui.Result.text())
            self.ui.Result.setText('0')
            self.method = "div"
        else:
            if self.a != 0:

                self.a /= float(self.ui.Result.text())
                self.ui.Result.setText('0')
                self.method = "div"

    def push_del(self):
        if len(self.ui.Result.text()) > 1:
            self.ui.Result.setText(self.ui.Result.text()[:-1])
        else:
            self.ui.Result.setText('0')

    def push_C(self):
        self.ui.Result.setText('0')
        self.a = None
        self.method = None

    def push_CE(self):
        self.ui.Result.setText('0')
        if self.method == 'eu':
            self.a = None
            self.method = None

    def push_eu(self):
        b = float(self.ui.Result.text())
        if self.method == "add":
            result = self.a + b
            if result % 1 == 0:
                result = int(result)
                self.ui.Result.setText(str(result))
                self.method = 'eu'
            else:
                self.ui.Result.setText(str(result))
                self.method = 'eu'
        if self.method == "sub":
            result = self.a - b
            if result % 1 == 0:
                result = int(result)
                self.ui.Result.setText(str(result))
                self.method = 'eu'
            else:
                self.ui.Result.setText(str(result))
                self.method = 'eu'
        if self.method == "multy":
            result = self.a * b
            if result % 1 == 0:
                result = int(result)
                self.ui.Result.setText(str(result))
                self.method = 'eu'
            else:
                self.ui.Result.setText(str(result))
                self.method = 'eu'
        if self.method == "div":
            result = self.a / b
            if result % 1 == 0:
                result = int(result)
                self.ui.Result.setText(str(result))
                self.method = 'eu'
            else:
                self.ui.Result.setText(str(result))
                self.method = 'eu'

    def push_sqrtX(self):
        b = float(self.ui.Result.text())
        if float(self.ui.Result.text()) >= 0:
            result = b**0.5

            if result % 1 == 0:
                result = int(result)
                self.ui.Result.setText(str(result))

            else:
                self.ui.Result.setText(str(result))
        else:
            result = 'Неверный ввод'
            self.ui.Result.setText(result)
        self.method = 'eu'

    def push_X2(self):
        result = float(self.ui.Result.text())**2
        if result % 1 == 0:
            result = int(result)
            self.ui.Result.setText(str(result))
        else:
            self.ui.Result.setText(str(result))
        self.method = 'eu'

    def push_1_X(self):
        result = 1/float(self.ui.Result.text())
        if result % 1 == 0:
            result = int(result)
            self.ui.Result.setText(str(result))
        else:
            self.ui.Result.setText(str(result))
        self.method = 'eu'

    def push_percent(self):
        b = float(self.ui.Result.text())
        if self.method == "add":
            result = self.a + b * self.a / 100
        elif self.method == "sub":
            result = self.a - b * self.a / 100
        elif self.method == "multy":
            result = self.a * b / 100
        elif self.method == "div":
            result = self.a / (b / 100)
        else:
            result = 0
        if result % 1 == 0:
            result = int(result)
            self.ui.Result.setText(str(result))
            self.method = 'eu'
        else:
            self.ui.Result.setText(str(result))
            self.method = 'eu'

if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = CalcApp()
    win.show()
    app.exec_()
