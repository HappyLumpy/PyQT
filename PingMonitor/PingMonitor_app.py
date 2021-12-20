import requests
from PySide2 import QtCore, QtWidgets
from PySide2.QtWidgets import QInputDialog, QLineEdit

from PingMonitor_design import Ui_Form as PingMonitor_Ui_Form
from PingMonitorSettings_design import Ui_Form as PingMonitorSettings_Ui_Form
from Tracert_design import Ui_Form as Tracert_design_Ui_Form
from AddIP import Ui_Form as AddIP_Ui_Form
from functools import partial


class PingMonitorSettings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PingMonitorSettings, self).__init__(parent)
        self.ui = PingMonitorSettings_Ui_Form()
        self.ipThread = IpThread()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.addip)
        self.ui.pushButton_2.clicked.connect(self.delip)

    def addip(self):
        ip = QInputDialog.getText(self, "QInputDialog().getText()", "Ip adress:", QLineEdit.Normal)
        self.ui.listWidget.addItem(ip[0])
        self.ipThread.getip(ip)

    def delip(self):
        listIp = self.ui.listWidget.selectedItems()
        if not listIp:
            return
        for ip in listIp:
            self.ui.listWidget.takeItem(self.ui.listWidget.row(ip))


class Tracert(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Tracert, self).__init__(parent)
        self.ui = Tracert_design_Ui_Form()
        self.ui.setupUi(self)


class PingMonitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PingMonitor, self).__init__(parent)
        self.ui = PingMonitor_Ui_Form()
        self.ipThread = IpThread()
        self.ui.setupUi(self)
        self.ui.pushButton_4.clicked.connect(self.settings)
        self.ui.pushButton_3.clicked.connect(self.tracert)
        # self.ui.pushButton.clicked.connect(self.start_ping)
        # self.ipThread.mysignal.connect(self.ui.plainTextEdit, QtCore.Qt.QueuedConnection)

    def settings(self):
        self.win = PingMonitorSettings()
        self.win.show()

    def tracert(self):
        self.win = Tracert()
        self.win.show()


#     @QtCore.Slot()
#     def start_ping(self):
#         self.ipThread.setparametres(self.ui.tableWidget.text())
#         self.ipThread.start()
#
class IpThread(QtCore.QThread):
    mysignal = QtCore.Signal(str)

    def run(self):
        while True:
            r = requests.get(self.ip)
            self.mysignal.emit(str(f'Статус {r.status_code}'))

    def getip(self, ip):
        self.ip = ip


if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = PingMonitor()
    win.show()
    app.exec_()
