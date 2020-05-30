# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'openteam.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

import sqlite3
ovs=sqlite3.connect('FantasyGame.db') #importing sqlite database
cursov=ovs.cursor()

class Ui_open(object):
    def setupUi(self, open):
        open.setObjectName("open")
        open.resize(750, 539)
        open.setStyleSheet("background-color: rgb(255, 134, 134);")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(open)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame = QtWidgets.QFrame(open)
        self.frame.setFrameShape(QtWidgets.QFrame.Box)
        self.frame.setFrameShadow(QtWidgets.QFrame.Plain)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem1)
        self.open_team_label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.open_team_label.setFont(font)
        self.open_team_label.setAlignment(QtCore.Qt.AlignCenter)
        self.open_team_label.setObjectName("open_team_label")
        self.verticalLayout.addWidget(self.open_team_label)
        self.open_team_comboBox = QtWidgets.QComboBox(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.open_team_comboBox.setFont(font)
        self.open_team_comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.open_team_comboBox.setObjectName("open_team_comboBox")
        self.verticalLayout.addWidget(self.open_team_comboBox)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem4)
        self.open_btn = QtWidgets.QPushButton(self.frame)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.open_btn.setFont(font)
        self.open_btn.setStyleSheet("")
        self.open_btn.setIconSize(QtCore.QSize(20, 20))
        self.open_btn.setDefault(True)
        self.open_btn.setFlat(True)
        self.open_btn.setObjectName("open_btn")
        self.verticalLayout.addWidget(self.open_btn)
        spacerItem5 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem6)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem7)
        self.verticalLayout_3.addLayout(self.verticalLayout)
        self.verticalLayout_2.addWidget(self.frame)
        tms=cursov.execute("SELECT DISTINCT Name FROM teams;")
        x=tms.fetchall()
        for i in x:                                 #access the data from database and add the same to combo box
            self.open_team_comboBox.addItem(i[0])

        self.retranslateUi(open)
        QtCore.QMetaObject.connectSlotsByName(open)

        

    def retranslateUi(self, open):
        _translate = QtCore.QCoreApplication.translate
        open.setWindowTitle(_translate("open", "Open team"))
        self.open_team_label.setText(_translate("open", "Open team"))
        self.open_btn.setText(_translate("open", "Open"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    open = QtWidgets.QWidget()
    ui = Ui_open()
    ui.setupUi(open)
    open.show()
    sys.exit(app.exec_())
