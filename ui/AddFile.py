# Form implementation generated from reading ui file 'AddFile.ui'
#
# Created by: PyQt6 UI code generator 6.6.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Dialog)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.widget = QtWidgets.QWidget(parent=Dialog)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.PlayFileButton = QtWidgets.QPushButton(parent=self.widget)
        self.PlayFileButton.setObjectName("PlayFileButton")
        self.verticalLayout.addWidget(self.PlayFileButton)
        self.DecryptFileButton = QtWidgets.QPushButton(parent=self.widget)
        self.DecryptFileButton.setObjectName("DecryptFileButton")
        self.verticalLayout.addWidget(self.DecryptFileButton)
        self.EncryptFileButton = QtWidgets.QPushButton(parent=self.widget)
        self.EncryptFileButton.setObjectName("EncryptFileButton")
        self.verticalLayout.addWidget(self.EncryptFileButton)
        self.horizontalLayout.addWidget(self.widget)
        self.pushButton_2 = QtWidgets.QPushButton(parent=Dialog)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.lineEdit = QtWidgets.QLineEdit(parent=Dialog)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.PlayFileButton.setText(_translate("Dialog", "Play"))
        self.DecryptFileButton.setText(_translate("Dialog", "Encrypt"))
        self.EncryptFileButton.setText(_translate("Dialog", "Decrypt"))
        self.pushButton_2.setText(_translate("Dialog", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec())
