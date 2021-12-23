import datetime
import time
from PySide2 import QtCore, QtWidgets, QtGui
from PySide2.QtCore import QSettings

from PySide2.QtWidgets import QInputDialog, QLineEdit
from pythonping import ping

from PingMonitor_design import Ui_Form as PingMonitor_Ui_Form
from PingMonitorSettings_design import Ui_Form as PingMonitorSettings_Ui_Form
from Tracert_design import Ui_Form as Tracert_design_Ui_Form
from functools import partial


class PingMonitorSettings(QtWidgets.QWidget):
    signal_data = QtCore.Signal(str)
    signal_del = QtCore.Signal(int)

    def __init__(self, parent=None):
        super(PingMonitorSettings, self).__init__(parent)
        self.settings = QtCore.QSettings("IPList")
        # self.listIp = self.settings.value("IPList", [])
        self.ui = PingMonitorSettings_Ui_Form()
        self.ui.setupUi(self)
        self.loadData()
        self.ui.pushButton.clicked.connect(self.addip)
        self.ui.pushButton_2.clicked.connect(self.delip)

    def addip(self):
        self.settings = QtCore.QSettings("IPList")
        ip = QInputDialog.getText(self, "QInputDialog().getText()", "Ip adress:", QLineEdit.Normal)
        self.ui.listWidget.addItem(ip[0])
        self.signal_data.emit(str(ip[0]))

    def delip(self):
        listIp = self.ui.listWidget.selectedItems()
        if not listIp:
            return
        for ip in listIp:
            self.signal_del.emit(self.ui.listWidget.row(ip))
            self.ui.listWidget.takeItem(self.ui.listWidget.row(ip))

    def loadData(self):
        self.settings = QtCore.QSettings("IPList")
        # for i in self.listIp("IPList"):
        #     self.ui.listWidget.addItem(i)



    def closeEvent(self, event: QtGui.QCloseEvent) -> None:
        list_widget = self.ui.listWidget
        items = []
        for index in range(list_widget.count()):
            items.append(list_widget.item(index).text())
        self.settings.setValue("IPList", items)



class Tracert(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Tracert, self).__init__(parent)
        self.ui = Tracert_design_Ui_Form()
        self.ui.setupUi(self)


class PingMonitor(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(PingMonitor, self).__init__(parent)
        self.ui = PingMonitor_Ui_Form()
        self.ui.setupUi(self)
        self.row = 0
        self.PingThread = PingThread()
        self.ui.pushButton_4.clicked.connect(self.settings)
        self.ui.pushButton_3.clicked.connect(self.tracert)
        self.ui.pushButton.clicked.connect(self.start_ping)
        self.ui.pushButton_2.clicked.connect(self.stop_ping)



    def getdatafromsettings(self, text):
        self.ui.tableWidget.insertRow(self.row)
        self.ui.tableWidget.setItem(self.row, 0, QtWidgets.QTableWidgetItem(text))
        self.row += 1

    def deldatafromsettings(self, int):
        self.ui.tableWidget.removeRow(int)
        self.row -= 1

    def settings(self):
        self.win = PingMonitorSettings()
        self.win.show()
        self.win.signal_data.connect(self.getdatafromsettings)
        self.win.signal_del.connect(self.deldatafromsettings)

    def tracert(self):
        self.win = Tracert()
        self.win.show()


    def start_ping(self):
        for i in range(self.row):
            self.PingThread.setparametres(self.ui.tableWidget.item(i,0).text())
            self.PingThread.mysignal.connect(self.plainTextEdit, QtCore.Qt.QueuedConnection)
            self.PingThread.start()

    def stop_ping(self):
        self.PingThread.status = False

    def plainTextEdit(self, text):
        self.ui.plainTextEdit.appendPlainText(str(text))


class PingThread(QtCore.QThread):
    mysignal = QtCore.Signal(str)

    def run(self):
        self.status = True
        while self.status:
            r = ping(self.ip)
            self.mysignal.emit(str(r))

    def setparametres(self, ip):
        self.ip = ip




if __name__ == '__main__':
    app = QtWidgets.QApplication()
    win = PingMonitor()
    win.show()
    app.exec_()
