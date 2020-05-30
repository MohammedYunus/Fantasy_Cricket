# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'fantasy_score.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_fscore(object):
    def setupUi(self, fscore):
        fscore.setObjectName("fscore")
        fscore.resize(400, 300)
        fscore.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(fscore)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(fscore)
        self.frame.setStyleSheet("color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setLineWidth(2)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.score_val = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.score_val.setFont(font)
        self.score_val.setStyleSheet("color: rgb(255, 255, 255);")
        self.score_val.setAlignment(QtCore.Qt.AlignCenter)
        self.score_val.setObjectName("score_val")
        self.verticalLayout_3.addWidget(self.score_val)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(fscore)
        QtCore.QMetaObject.connectSlotsByName(fscore)

    def retranslateUi(self, fscore):
        _translate = QtCore.QCoreApplication.translate
        fscore.setWindowTitle(_translate("fscore", "Score"))
        self.label.setText(_translate("fscore", "Your score is:"))
        self.score_val.setText(_translate("fscore", "0"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    fscore = QtWidgets.QWidget()
    ui = Ui_fscore()
    ui.setupUi(fscore)
    fscore.show()
    sys.exit(app.exec_())
