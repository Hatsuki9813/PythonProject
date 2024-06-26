# Form implementation generated from reading ui file 'LoginPage.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(450, 550)
        self.widget_2 = QtWidgets.QWidget(parent=Form)
        self.widget_2.setGeometry(QtCore.QRect(30, 30, 370, 480))
        self.widget_2.setStyleSheet("QPushButton #pushButton{\n"
"border-radius: 10px;\n"
"background-color:rgb(16, 24, 37);\n"
"}\n"
"\n"
"QPushButton #pushButton:hover{\n"
"background-color:#85C1E9;\n"
"}")
        self.widget_2.setObjectName("widget_2")
        self.label = QtWidgets.QLabel(parent=self.widget_2)
        self.label.setGeometry(QtCore.QRect(30, 30, 320, 420))
        self.label.setStyleSheet("border-radius: 20px;\n"
"background-color: rgb(19, 19, 29);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.LoginLabel = QtWidgets.QLabel(parent=self.widget_2)
        self.LoginLabel.setGeometry(QtCore.QRect(145, 95, 81, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.LoginLabel.setFont(font)
        self.LoginLabel.setStyleSheet("color:white;")
        self.LoginLabel.setMidLineWidth(4)
        self.LoginLabel.setObjectName("LoginLabel")
        self.lineEdit = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(100, 180, 181, 31))
        self.lineEdit.setStyleSheet("border-radius: 10px;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(parent=self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(130, 320, 120, 40))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit_2 = QtWidgets.QLineEdit(parent=self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(100, 250, 181, 31))
        self.lineEdit_2.setStyleSheet("border-radius: 10px;")
        self.lineEdit_2.setText("")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(parent=self.widget_2)
        self.label_2.setGeometry(QtCore.QRect(85, 380, 211, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color:white")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.LoginLabel.setText(_translate("Form", "Log in"))
        self.pushButton.setText(_translate("Form", "Login"))
        self.label_2.setText(_translate("Form", "Don\'t have an account? Register now"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec())
