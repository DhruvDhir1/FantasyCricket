# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import sqlite3
player=sqlite3.connect("Players.db")
curplayer=player.cursor()


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(498, 499)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(9, 39, 480, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.Calculate = QtWidgets.QPushButton(Form)
        self.Calculate.setGeometry(QtCore.QRect(210, 460, 78, 26))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Calculate.setFont(font)
        self.Calculate.setObjectName("Calculate")
        self.horizontalLayoutWidget = QtWidgets.QWidget(Form)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 76, 480, 382))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.PlayerList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.PlayerList.setObjectName("PlayerList")
        self.horizontalLayout_2.addWidget(self.PlayerList)
        self.ScoreList = QtWidgets.QListWidget(self.horizontalLayoutWidget)
        self.ScoreList.setObjectName("ScoreList")
        self.horizontalLayout_2.addWidget(self.ScoreList)
        self.layoutWidget = QtWidgets.QWidget(Form)
        self.layoutWidget.setGeometry(QtCore.QRect(9, 9, 481, 24))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.SelectTeam = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SelectTeam.setFont(font)
        self.SelectTeam.setObjectName("SelectTeam")
        self.SelectTeam.addItem("")
        self.horizontalLayout_3.addWidget(self.SelectTeam)
        self.SelectMatch = QtWidgets.QComboBox(self.layoutWidget)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.SelectMatch.setFont(font)
        self.SelectMatch.setObjectName("SelectMatch")
        self.SelectMatch.addItem("")
        self.SelectMatch.addItem("")
        self.SelectMatch.addItem("")
        self.SelectMatch.addItem("")
        self.SelectMatch.addItem("")
        self.horizontalLayout_3.addWidget(self.SelectMatch)
        self.layoutWidget1 = QtWidgets.QWidget(Form)
        self.layoutWidget1.setGeometry(QtCore.QRect(9, 48, 481, 22))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Players = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.Players.setFont(font)
        self.Players.setObjectName("Players")
        self.horizontalLayout.addWidget(self.Players)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Points = QtWidgets.QLabel(self.layoutWidget1)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.Points.setFont(font)
        self.Points.setObjectName("Points")
        self.horizontalLayout.addWidget(self.Points)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.Calculate.setText(_translate("Form", "Calculate"))
        self.SelectTeam.setItemText(0, _translate("Form", "SELECT TEAM"))
        self.SelectMatch.setItemText(0, _translate("Form", "SELECT MATCH"))
        self.SelectMatch.setItemText(1, _translate("Form", "MATCH 1"))
        self.SelectMatch.setItemText(2, _translate("Form", "MATCH 2"))
        self.SelectMatch.setItemText(3, _translate("Form", "MATCH 3"))
        self.SelectMatch.setItemText(4, _translate("Form", "MATCH 4"))
        self.Players.setText(_translate("Form", "Players"))
        self.Points.setText(_translate("Form", "Points"))

        curplayer.execute("SELECT * from teams;")
        record=curplayer.fetchall()
        teamlist=[]
        for records in record:
            teamlist.append(records[0])
        for item in set(teamlist):
            self.SelectTeam.addItem(item)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
