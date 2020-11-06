

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(824, 485)
        self.TeamScore = QtWidgets.QLabel(Form)
        self.TeamScore.setGeometry(QtCore.QRect(330, 120, 181, 51))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setItalic(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.TeamScore.setFont(font)
        self.TeamScore.setObjectName("TeamScore")
        self.Score = QtWidgets.QLineEdit(Form)
        self.Score.setGeometry(QtCore.QRect(290, 180, 221, 31))
        self.Score.setAlignment(QtCore.Qt.AlignCenter)
        self.Score.setObjectName("Score")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.TeamScore.setText(_translate("Form", "Your Team Score"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
