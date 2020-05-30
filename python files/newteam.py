# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'nt.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_New_team(object):
    def setupUi(self, New_team):
        New_team.setObjectName("New_team")
        New_team.resize(710, 499)
        New_team.setStyleSheet("background-color: rgb(71, 255, 225);")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(New_team)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(New_team)
        self.frame.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem1)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.inpteamname = QtWidgets.QLineEdit(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.inpteamname.setFont(font)
        self.inpteamname.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inpteamname.setCursorPosition(0)
        self.inpteamname.setAlignment(QtCore.Qt.AlignCenter)
        self.inpteamname.setClearButtonEnabled(True)
        self.inpteamname.setObjectName("inpteamname")
        self.verticalLayout_2.addWidget(self.inpteamname)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem4)
        self.createteam = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.createteam.setFont(font)
        self.createteam.setDefault(True)
        self.createteam.setFlat(True)
        self.createteam.setObjectName("createteam")
        self.verticalLayout_2.addWidget(self.createteam)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem6)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.retranslateUi(New_team)
        QtCore.QMetaObject.connectSlotsByName(New_team)

    def retranslateUi(self, New_team):
        _translate = QtCore.QCoreApplication.translate
        New_team.setWindowTitle(_translate("New_team", "New team"))
        self.label.setText(_translate("New_team", "Create a new team"))
        self.label_2.setText(_translate("New_team", "Enter your team name below"))
        self.inpteamname.setPlaceholderText(_translate("New_team", "your team name"))
        self.createteam.setText(_translate("New_team", "Create"))
        self.createteam.setShortcut(_translate("Fantasy_Cricket", "Return"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    New_team = QtWidgets.QWidget()
    new_ui = Ui_New_team()
    new_ui.setupUi(New_team)
    New_team.show()
    sys.exit(app.exec_())
