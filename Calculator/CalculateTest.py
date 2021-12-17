# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Calc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.setWindowModality(Qt.NonModal)
        Form.resize(356, 524)
        Form.setMouseTracking(True)
        self.gridLayout_2 = QGridLayout(Form)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalWidget = QWidget(Form)
        self.verticalWidget.setObjectName(u"verticalWidget")
        self.gridLayout = QGridLayout(self.verticalWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.butt_7 = QPushButton(self.verticalWidget)
        self.butt_7.setObjectName(u"butt_7")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.butt_7.sizePolicy().hasHeightForWidth())
        self.butt_7.setSizePolicy(sizePolicy)
        self.butt_7.setMinimumSize(QSize(75, 65))
        font = QFont()
        font.setFamily(u"Arial")
        font.setPointSize(11)
        font.setStyleStrategy(QFont.PreferAntialias)
        self.butt_7.setFont(font)

        self.horizontalLayout_3.addWidget(self.butt_7)

        self.butt_8 = QPushButton(self.verticalWidget)
        self.butt_8.setObjectName(u"butt_8")
        sizePolicy.setHeightForWidth(self.butt_8.sizePolicy().hasHeightForWidth())
        self.butt_8.setSizePolicy(sizePolicy)
        self.butt_8.setMinimumSize(QSize(75, 65))
        self.butt_8.setFont(font)

        self.horizontalLayout_3.addWidget(self.butt_8)

        self.Butt_9 = QPushButton(self.verticalWidget)
        self.Butt_9.setObjectName(u"Butt_9")
        sizePolicy.setHeightForWidth(self.Butt_9.sizePolicy().hasHeightForWidth())
        self.Butt_9.setSizePolicy(sizePolicy)
        self.Butt_9.setMinimumSize(QSize(75, 65))
        self.Butt_9.setFont(font)

        self.horizontalLayout_3.addWidget(self.Butt_9)

        self.Butt_multy = QPushButton(self.verticalWidget)
        self.Butt_multy.setObjectName(u"Butt_multy")
        sizePolicy.setHeightForWidth(self.Butt_multy.sizePolicy().hasHeightForWidth())
        self.Butt_multy.setSizePolicy(sizePolicy)
        self.Butt_multy.setMinimumSize(QSize(75, 65))
        self.Butt_multy.setFont(font)

        self.horizontalLayout_3.addWidget(self.Butt_multy)


        self.gridLayout.addLayout(self.horizontalLayout_3, 4, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetMaximumSize)
        self.Butt_1_X = QPushButton(self.verticalWidget)
        self.Butt_1_X.setObjectName(u"Butt_1_X")
        sizePolicy.setHeightForWidth(self.Butt_1_X.sizePolicy().hasHeightForWidth())
        self.Butt_1_X.setSizePolicy(sizePolicy)
        self.Butt_1_X.setMinimumSize(QSize(75, 65))
        self.Butt_1_X.setFont(font)

        self.horizontalLayout_2.addWidget(self.Butt_1_X)

        self.Butt_X2 = QPushButton(self.verticalWidget)
        self.Butt_X2.setObjectName(u"Butt_X2")
        sizePolicy.setHeightForWidth(self.Butt_X2.sizePolicy().hasHeightForWidth())
        self.Butt_X2.setSizePolicy(sizePolicy)
        self.Butt_X2.setMinimumSize(QSize(75, 65))
        self.Butt_X2.setFont(font)

        self.horizontalLayout_2.addWidget(self.Butt_X2)

        self.Butt_sqrtX = QPushButton(self.verticalWidget)
        self.Butt_sqrtX.setObjectName(u"Butt_sqrtX")
        sizePolicy.setHeightForWidth(self.Butt_sqrtX.sizePolicy().hasHeightForWidth())
        self.Butt_sqrtX.setSizePolicy(sizePolicy)
        self.Butt_sqrtX.setMinimumSize(QSize(75, 65))
        self.Butt_sqrtX.setFont(font)

        self.horizontalLayout_2.addWidget(self.Butt_sqrtX)

        self.Butt_div = QPushButton(self.verticalWidget)
        self.Butt_div.setObjectName(u"Butt_div")
        sizePolicy.setHeightForWidth(self.Butt_div.sizePolicy().hasHeightForWidth())
        self.Butt_div.setSizePolicy(sizePolicy)
        self.Butt_div.setMinimumSize(QSize(75, 65))
        self.Butt_div.setFont(font)

        self.horizontalLayout_2.addWidget(self.Butt_div)


        self.gridLayout.addLayout(self.horizontalLayout_2, 3, 0, 1, 1)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.Butt_1 = QPushButton(self.verticalWidget)
        self.Butt_1.setObjectName(u"Butt_1")
        sizePolicy.setHeightForWidth(self.Butt_1.sizePolicy().hasHeightForWidth())
        self.Butt_1.setSizePolicy(sizePolicy)
        self.Butt_1.setMinimumSize(QSize(75, 65))
        self.Butt_1.setFont(font)

        self.horizontalLayout_5.addWidget(self.Butt_1)

        self.Butt_2 = QPushButton(self.verticalWidget)
        self.Butt_2.setObjectName(u"Butt_2")
        sizePolicy.setHeightForWidth(self.Butt_2.sizePolicy().hasHeightForWidth())
        self.Butt_2.setSizePolicy(sizePolicy)
        self.Butt_2.setMinimumSize(QSize(75, 65))
        self.Butt_2.setFont(font)

        self.horizontalLayout_5.addWidget(self.Butt_2)

        self.Butt_3 = QPushButton(self.verticalWidget)
        self.Butt_3.setObjectName(u"Butt_3")
        sizePolicy.setHeightForWidth(self.Butt_3.sizePolicy().hasHeightForWidth())
        self.Butt_3.setSizePolicy(sizePolicy)
        self.Butt_3.setMinimumSize(QSize(75, 65))
        self.Butt_3.setFont(font)

        self.horizontalLayout_5.addWidget(self.Butt_3)

        self.Butt_add = QPushButton(self.verticalWidget)
        self.Butt_add.setObjectName(u"Butt_add")
        sizePolicy.setHeightForWidth(self.Butt_add.sizePolicy().hasHeightForWidth())
        self.Butt_add.setSizePolicy(sizePolicy)
        self.Butt_add.setMinimumSize(QSize(75, 65))
        self.Butt_add.setFont(font)

        self.horizontalLayout_5.addWidget(self.Butt_add)


        self.gridLayout.addLayout(self.horizontalLayout_5, 6, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetMinimumSize)
        self.Butt_percent = QPushButton(self.verticalWidget)
        self.Butt_percent.setObjectName(u"Butt_percent")
        sizePolicy.setHeightForWidth(self.Butt_percent.sizePolicy().hasHeightForWidth())
        self.Butt_percent.setSizePolicy(sizePolicy)
        self.Butt_percent.setMinimumSize(QSize(75, 65))
        self.Butt_percent.setFont(font)
        self.Butt_percent.setAutoDefault(False)
        self.Butt_percent.setFlat(False)

        self.horizontalLayout.addWidget(self.Butt_percent)

        self.Butt_CE = QPushButton(self.verticalWidget)
        self.Butt_CE.setObjectName(u"Butt_CE")
        sizePolicy.setHeightForWidth(self.Butt_CE.sizePolicy().hasHeightForWidth())
        self.Butt_CE.setSizePolicy(sizePolicy)
        self.Butt_CE.setMinimumSize(QSize(75, 65))
        self.Butt_CE.setFont(font)

        self.horizontalLayout.addWidget(self.Butt_CE)

        self.Butt_C = QPushButton(self.verticalWidget)
        self.Butt_C.setObjectName(u"Butt_C")
        sizePolicy.setHeightForWidth(self.Butt_C.sizePolicy().hasHeightForWidth())
        self.Butt_C.setSizePolicy(sizePolicy)
        self.Butt_C.setMinimumSize(QSize(75, 65))
        self.Butt_C.setFont(font)

        self.horizontalLayout.addWidget(self.Butt_C)

        self.Butt_del = QPushButton(self.verticalWidget)
        self.Butt_del.setObjectName(u"Butt_del")
        sizePolicy.setHeightForWidth(self.Butt_del.sizePolicy().hasHeightForWidth())
        self.Butt_del.setSizePolicy(sizePolicy)
        self.Butt_del.setMinimumSize(QSize(75, 65))
        self.Butt_del.setFont(font)

        self.horizontalLayout.addWidget(self.Butt_del)


        self.gridLayout.addLayout(self.horizontalLayout, 2, 0, 1, 1)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.Butt_pos_neg = QPushButton(self.verticalWidget)
        self.Butt_pos_neg.setObjectName(u"Butt_pos_neg")
        sizePolicy.setHeightForWidth(self.Butt_pos_neg.sizePolicy().hasHeightForWidth())
        self.Butt_pos_neg.setSizePolicy(sizePolicy)
        self.Butt_pos_neg.setMinimumSize(QSize(75, 65))
        self.Butt_pos_neg.setFont(font)

        self.horizontalLayout_6.addWidget(self.Butt_pos_neg)

        self.pushButton_0 = QPushButton(self.verticalWidget)
        self.pushButton_0.setObjectName(u"pushButton_0")
        sizePolicy.setHeightForWidth(self.pushButton_0.sizePolicy().hasHeightForWidth())
        self.pushButton_0.setSizePolicy(sizePolicy)
        self.pushButton_0.setMinimumSize(QSize(75, 65))
        self.pushButton_0.setFont(font)

        self.horizontalLayout_6.addWidget(self.pushButton_0)

        self.Butt_point = QPushButton(self.verticalWidget)
        self.Butt_point.setObjectName(u"Butt_point")
        sizePolicy.setHeightForWidth(self.Butt_point.sizePolicy().hasHeightForWidth())
        self.Butt_point.setSizePolicy(sizePolicy)
        self.Butt_point.setMinimumSize(QSize(75, 65))
        self.Butt_point.setFont(font)

        self.horizontalLayout_6.addWidget(self.Butt_point)

        self.Butt_eu = QPushButton(self.verticalWidget)
        self.Butt_eu.setObjectName(u"Butt_eu")
        sizePolicy.setHeightForWidth(self.Butt_eu.sizePolicy().hasHeightForWidth())
        self.Butt_eu.setSizePolicy(sizePolicy)
        self.Butt_eu.setMinimumSize(QSize(75, 65))
        self.Butt_eu.setFont(font)

        self.horizontalLayout_6.addWidget(self.Butt_eu)


        self.gridLayout.addLayout(self.horizontalLayout_6, 7, 0, 1, 1)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.Butt_4 = QPushButton(self.verticalWidget)
        self.Butt_4.setObjectName(u"Butt_4")
        sizePolicy.setHeightForWidth(self.Butt_4.sizePolicy().hasHeightForWidth())
        self.Butt_4.setSizePolicy(sizePolicy)
        self.Butt_4.setMinimumSize(QSize(75, 65))
        self.Butt_4.setFont(font)

        self.horizontalLayout_4.addWidget(self.Butt_4)

        self.Butt_5 = QPushButton(self.verticalWidget)
        self.Butt_5.setObjectName(u"Butt_5")
        sizePolicy.setHeightForWidth(self.Butt_5.sizePolicy().hasHeightForWidth())
        self.Butt_5.setSizePolicy(sizePolicy)
        self.Butt_5.setMinimumSize(QSize(75, 65))
        self.Butt_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.Butt_5)

        self.Butt_6 = QPushButton(self.verticalWidget)
        self.Butt_6.setObjectName(u"Butt_6")
        sizePolicy.setHeightForWidth(self.Butt_6.sizePolicy().hasHeightForWidth())
        self.Butt_6.setSizePolicy(sizePolicy)
        self.Butt_6.setMinimumSize(QSize(75, 65))
        self.Butt_6.setFont(font)

        self.horizontalLayout_4.addWidget(self.Butt_6)

        self.Butt_sub = QPushButton(self.verticalWidget)
        self.Butt_sub.setObjectName(u"Butt_sub")
        sizePolicy.setHeightForWidth(self.Butt_sub.sizePolicy().hasHeightForWidth())
        self.Butt_sub.setSizePolicy(sizePolicy)
        self.Butt_sub.setMinimumSize(QSize(75, 65))
        self.Butt_sub.setFont(font)

        self.horizontalLayout_4.addWidget(self.Butt_sub)


        self.gridLayout.addLayout(self.horizontalLayout_4, 5, 0, 1, 1)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.Result = QLineEdit(self.verticalWidget)
        self.Result.setObjectName(u"Result")
        self.Result.setEnabled(True)
        sizePolicy.setHeightForWidth(self.Result.sizePolicy().hasHeightForWidth())
        self.Result.setSizePolicy(sizePolicy)
        self.Result.setMinimumSize(QSize(0, 50))
        self.Result.setMaximumSize(QSize(16777215, 50))
        self.Result.setSizeIncrement(QSize(0, 50))
        font1 = QFont()
        font1.setFamily(u"Arial")
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        font1.setStyleStrategy(QFont.PreferDefault)
        self.Result.setFont(font1)
        self.Result.setMouseTracking(False)
        self.Result.setTabletTracking(False)
        self.Result.setFocusPolicy(Qt.NoFocus)
        self.Result.setToolTipDuration(-1)
        self.Result.setLayoutDirection(Qt.RightToLeft)
        self.Result.setAutoFillBackground(False)
        self.Result.setFrame(True)
        self.Result.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)
        self.Result.setDragEnabled(False)
        self.Result.setReadOnly(False)
        self.Result.setCursorMoveStyle(Qt.LogicalMoveStyle)
        self.Result.setClearButtonEnabled(False)

        self.horizontalLayout_8.addWidget(self.Result)


        self.gridLayout.addLayout(self.horizontalLayout_8, 1, 0, 1, 1)


        self.gridLayout_2.addWidget(self.verticalWidget, 1, 0, 1, 1)


        self.retranslateUi(Form)

        self.Butt_percent.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.butt_7.setText(QCoreApplication.translate("Form", u"7", None))
        self.butt_8.setText(QCoreApplication.translate("Form", u"8", None))
        self.Butt_9.setText(QCoreApplication.translate("Form", u"9", None))
        self.Butt_multy.setText(QCoreApplication.translate("Form", u"*", None))
        self.Butt_1_X.setText(QCoreApplication.translate("Form", u"1/X", None))
        self.Butt_X2.setText(QCoreApplication.translate("Form", u"X^2", None))
        self.Butt_sqrtX.setText(QCoreApplication.translate("Form", u"X^(1/2)", None))
        self.Butt_div.setText(QCoreApplication.translate("Form", u"/", None))
        self.Butt_1.setText(QCoreApplication.translate("Form", u"1", None))
        self.Butt_2.setText(QCoreApplication.translate("Form", u"2", None))
        self.Butt_3.setText(QCoreApplication.translate("Form", u"3", None))
        self.Butt_add.setText(QCoreApplication.translate("Form", u"+", None))
        self.Butt_percent.setText(QCoreApplication.translate("Form", u"%", None))
        self.Butt_CE.setText(QCoreApplication.translate("Form", u"CE", None))
        self.Butt_C.setText(QCoreApplication.translate("Form", u"C", None))
        self.Butt_del.setText(QCoreApplication.translate("Form", u"<=", None))
        self.Butt_pos_neg.setText(QCoreApplication.translate("Form", u"+/-", None))
        self.pushButton_0.setText(QCoreApplication.translate("Form", u"0", None))
        self.Butt_point.setText(QCoreApplication.translate("Form", u",", None))
        self.Butt_eu.setText(QCoreApplication.translate("Form", u"=", None))
        self.Butt_4.setText(QCoreApplication.translate("Form", u"4", None))
        self.Butt_5.setText(QCoreApplication.translate("Form", u"5", None))
        self.Butt_6.setText(QCoreApplication.translate("Form", u"6", None))
        self.Butt_sub.setText(QCoreApplication.translate("Form", u"-", None))
#if QT_CONFIG(tooltip)
        self.Result.setToolTip("")
#endif // QT_CONFIG(tooltip)
        self.Result.setText(QCoreApplication.translate("Form", u"0", None))
    # retranslateUi

