# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'error.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_error(object):
    def setupUi(self, error):
        error.setObjectName("error")
        error.resize(452, 225)
        error.setStyleSheet("background-color: rgb(240, 240, 240);")
        self.error_text = QtWidgets.QLabel(error)
        self.error_text.setGeometry(QtCore.QRect(20, 60, 421, 71))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.error_text.setFont(font)
        self.error_text.setAlignment(QtCore.Qt.AlignCenter)
        self.error_text.setObjectName("error_text")
        self.ok_btn = QtWidgets.QPushButton(error)
        self.ok_btn.setGeometry(QtCore.QRect(190, 160, 93, 28))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ok_btn.setFont(font)
        self.ok_btn.setStyleSheet("background-color: rgb(182, 182, 182);")
        self.ok_btn.setDefault(True)
        self.ok_btn.setObjectName("ok_btn")
        self.label_2 = QtWidgets.QLabel(error)
        self.label_2.setGeometry(QtCore.QRect(20, 10, 41, 41))
        self.label_2.setStyleSheet("background-color: rgb(198, 198, 198);")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../../../../../../Desktop/err.jpg"))
        self.label_2.setScaledContents(True)
        self.label_2.setObjectName("label_2")

        self.retranslateUi(error)
        QtCore.QMetaObject.connectSlotsByName(error)

    def retranslateUi(self, error):
        _translate = QtCore.QCoreApplication.translate
        error.setWindowTitle(_translate("error", "Error"))
        self.error_text.setText(_translate("error", "Error this file cannot be saved"))
        self.ok_btn.setText(_translate("error", "OK"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Error = QtWidgets.QWidget()
    error_ui = Ui_error()
    error_ui.setupUi(Error)
    Error.show()
    sys.exit(app.exec_())
