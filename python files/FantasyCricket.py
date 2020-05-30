# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Fc.ui'
#
# Created by: PyQt5 UI code generator 5.13.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from newteam import Ui_New_team       ##importing new team files##
from openteam import Ui_open                ##importing open team files##
from evaluateteam import Ui_Evaluate_team   ##importing evaluate team files##
from error import Ui_error      ##importing error window files
from points import Player_points  ##importing players points from database

import sqlite3
fanta=sqlite3.connect('FantasyGame.db')     #importing sqlite database
cursfanta=fanta.cursor()

class Ui_Fantasy_Cricket(object):
    def __init__(self):                         #constructor method
        self.New_team=QtWidgets.QWidget()
        self.new_ui=Ui_New_team()
        self.new_ui.setupUi(self.New_team)

        self.open=QtWidgets.QWidget()
        self.open_ui=Ui_open()
        self.open_ui.setupUi(self.open)

        self.Evaluate_team = QtWidgets.QWidget()
        self.eva_ui = Ui_Evaluate_team()
        self.eva_ui.setupUi(self.Evaluate_team)

        self.Error = QtWidgets.QWidget()
        self.error_ui = Ui_error()
        self.error_ui.setupUi(self.Error)

    
  ## function for opening new team window##
    def new_team(self):
        self.New_team.show()
    
 ## function for opening created teams##
    def open_team(self):
        self.open.show()
        self.open_ui.open_btn.clicked.connect(self.opentm)
        
 ## function for evaluating team##
    def evaluate_team(self):
        self.Evaluate_team.show()
        
 ## function for closing##
    def quit(self):
        print("You have exited the fantasy cricket game")
        print("Thank You for playing!")
        sys.exit(app.exec_())
        
 ##function to display error##
    def err(self):
        self.Error.show()
    
    def setupUi(self, Fantasy_Cricket):
    #initialisation
        self.avp =1000 #points available
        self.usdpnts = 0#points used
        self.Bats = 0 #batsmen count
        self.bol = 0 #bowlers count
        self.alRn = 0 #allrounder count
        self.wkt = 0 #wicket keepers count
        self.total=0 #total players count
        

        self.p=[]#batsmen list
        self.q=[]#bowlers list
        self.r=[]#all rounders list
        self.s=[]#wicket keepers list
        self.list = []#selected players list 
        
        
        Fantasy_Cricket.setObjectName("Fantasy_Cricket")
        Fantasy_Cricket.resize(1027, 783)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        Fantasy_Cricket.setFont(font)
        Fantasy_Cricket.setStyleSheet("background-color: rgb(255, 252, 144);")
        self.centralwidget = QtWidgets.QWidget(Fantasy_Cricket)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem)
        self.line_2 = QtWidgets.QFrame(self.centralwidget)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(2)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.verticalLayout_2.addWidget(self.line_2)
        self.your_selections = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.your_selections.setFont(font)
        self.your_selections.setIndent(25)
        self.your_selections.setObjectName("your_selections")
        self.verticalLayout_2.addWidget(self.your_selections)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem5)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem6)
        self.batlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batlabel.setFont(font)
        self.batlabel.setObjectName("batlabel")
        self.horizontalLayout.addWidget(self.batlabel)
        self.batmain = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.batmain.setFont(font)
        self.batmain.setStyleSheet("color: rgb(10, 2, 255);")
        self.batmain.setText("")
        self.batmain.setFrame(False)
        self.batmain.setReadOnly(True)
        self.batmain.setObjectName("batmain")
        self.horizontalLayout.addWidget(self.batmain)
        self.bowlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bowlabel.setFont(font)
        self.bowlabel.setObjectName("bowlabel")
        self.horizontalLayout.addWidget(self.bowlabel)
        self.bowlmain = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.bowlmain.setFont(font)
        self.bowlmain.setStyleSheet("color: rgb(10, 2, 255);")
        self.bowlmain.setText("")
        self.bowlmain.setFrame(False)
        self.bowlmain.setReadOnly(True)
        self.bowlmain.setObjectName("bowlmain")
        self.horizontalLayout.addWidget(self.bowlmain)
        self.arlabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.arlabel.setFont(font)
        self.arlabel.setObjectName("arlabel")
        self.horizontalLayout.addWidget(self.arlabel)
        self.armain = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.armain.setFont(font)
        self.armain.setStyleSheet("color: rgb(10, 2, 255);")
        self.armain.setText("")
        self.armain.setFrame(False)
        self.armain.setReadOnly(True)
        self.armain.setObjectName("armain")
        self.horizontalLayout.addWidget(self.armain)
        self.wklabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wklabel.setFont(font)
        self.wklabel.setObjectName("wklabel")
        self.horizontalLayout.addWidget(self.wklabel)
        self.wkmain = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.wkmain.setFont(font)
        self.wkmain.setStyleSheet("color: rgb(10, 2, 255);")
        self.wkmain.setText("")
        self.wkmain.setFrame(False)
        self.wkmain.setReadOnly(True)
        self.wkmain.setObjectName("wkmain")
        self.horizontalLayout.addWidget(self.wkmain)
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.horizontalLayout.addWidget(self.label_10)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem7)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(13, 2)
        self.verticalLayout_2.addLayout(self.horizontalLayout)
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(2)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.verticalLayout_2.addWidget(self.line)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem8)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(0, -1, -1, -1)
        self.horizontalLayout_2.setSpacing(7)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pointsAvailable = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pointsAvailable.setFont(font)
        self.pointsAvailable.setIndent(157)
        self.pointsAvailable.setObjectName("pointsAvailable")
        self.horizontalLayout_2.addWidget(self.pointsAvailable)
        self.pointsAvlinp = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pointsAvlinp.setFont(font)
        self.pointsAvlinp.setStyleSheet("color: rgb(10, 2, 255);")
        self.pointsAvlinp.setText("")
        self.pointsAvlinp.setFrame(False)
        self.pointsAvlinp.setReadOnly(True)                 #points available label
        self.pointsAvlinp.setObjectName("pointsAvlinp")
        self.horizontalLayout_2.addWidget(self.pointsAvlinp)
        self.pointsUsed = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.pointsUsed.setFont(font)
        self.pointsUsed.setIndent(136)
        self.pointsUsed.setObjectName("pointsUsed")
        self.horizontalLayout_2.addWidget(self.pointsUsed)
        self.pointsUsedinp = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pointsUsedinp.setFont(font)
        self.pointsUsedinp.setStyleSheet("color: rgb(10, 2, 255);")
        self.pointsUsedinp.setText("")
        self.pointsUsedinp.setFrame(False)
        self.pointsUsedinp.setReadOnly(True)                        #points used label
        self.pointsUsedinp.setObjectName("pointsUsedinp")
        self.horizontalLayout_2.addWidget(self.pointsUsedinp)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem9)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem10)
        self.batradio = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.batradio.setFont(font)
        self.batradio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.batradio.setObjectName("batradio")
        self.batradio.setDisabled(True)
        self.batradio.clicked.connect(self.checkstate)#Bat radio button signal
        self.horizontalLayout_4.addWidget(self.batradio)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem11)
        self.bowradio = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.bowradio.setFont(font)
        self.bowradio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.bowradio.setObjectName("bowradio")
        self.bowradio.setDisabled(True)
        self.bowradio.clicked.connect(self.checkstate)#Bow radio button signal
        self.horizontalLayout_4.addWidget(self.bowradio)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem12)
        self.ar_radio = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.ar_radio.setFont(font)
        self.ar_radio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.ar_radio.setObjectName("ar_radio")
        self.ar_radio.setDisabled(True)
        self.ar_radio.clicked.connect(self.checkstate)#AR radio button signal
        self.horizontalLayout_4.addWidget(self.ar_radio)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem13)
        self.wkradio = QtWidgets.QRadioButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.wkradio.setFont(font)
        self.wkradio.setFocusPolicy(QtCore.Qt.StrongFocus)
        self.wkradio.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.wkradio.setObjectName("wkradio")
        self.wkradio.setDisabled(True)
        self.wkradio.clicked.connect(self.checkstate)#WK radio button signal
        self.horizontalLayout_4.addWidget(self.wkradio)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem14)
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.horizontalLayout_4.addWidget(self.label_12)
        spacerItem15 = QtWidgets.QSpacerItem(0, 0, QtWidgets.QSizePolicy.MinimumExpanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem15)
        self.TeamNamelabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(85)
        self.TeamNamelabel.setFont(font)
        self.TeamNamelabel.setIndent(31)
        self.TeamNamelabel.setObjectName("TeamNamelabel")
        self.horizontalLayout_4.addWidget(self.TeamNamelabel)
        self.teamNameInput = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.teamNameInput.setFont(font)
        self.teamNameInput.setStyleSheet("color: rgb(26, 6, 255);")
        self.teamNameInput.setFrame(False)
        self.teamNameInput.setReadOnly(True)
        self.teamNameInput.setObjectName("teamNameInput")       #sets the team name upon creating team
        self.horizontalLayout_4.addWidget(self.teamNameInput)
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.horizontalLayout_4.addWidget(self.label_8)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem16)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem17)
        self.radList = QtWidgets.QListWidget(self.centralwidget)
        self.radList.setStyleSheet("background-color: rgb(183, 255, 166);")
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.radList.setFont(font)
        self.radList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.radList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.radList.setObjectName("radList")
        self.radList.itemDoubleClicked.connect(self.removelist1)##Double click to remove player from available player list##
        self.horizontalLayout_3.addWidget(self.radList)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem18)
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setIndent(0)
        self.label_11.setObjectName("label_11")
        self.horizontalLayout_3.addWidget(self.label_11)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem19)
        self.teamList = QtWidgets.QListWidget(self.centralwidget)
        self.teamList.setStyleSheet("background-color: rgb(183, 255, 166);")
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.teamList.setFont(font)
        self.teamList.setFrameShape(QtWidgets.QFrame.WinPanel)
        self.teamList.setFrameShadow(QtWidgets.QFrame.Plain)
        self.teamList.setObjectName("teamList")
        self.teamList.itemDoubleClicked.connect(self.removelist2)##Double click to remove player from team list##
        self.horizontalLayout_3.addWidget(self.teamList)
        spacerItem20 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem20)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem21 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout_2.addItem(spacerItem21)
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        spacerItem22 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem22)
        self.SaveBtn = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SaveBtn.setFont(font)
        self.SaveBtn.setStyleSheet("background-color: rgb(151, 198, 255);")
        self.SaveBtn.setObjectName("SaveBtn")
        self.SaveBtn.clicked.connect(self.savetm) #Save Team signal
        self.SaveBtn.setDisabled(True)
        self.horizontalLayout_6.addWidget(self.SaveBtn)
        spacerItem23 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem23)
        self.verticalLayout_2.addLayout(self.horizontalLayout_6)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2.addWidget(self.frame)
        Fantasy_Cricket.setCentralWidget(self.centralwidget)
        self.manageTeams = QtWidgets.QMenuBar(Fantasy_Cricket)
        self.manageTeams.setGeometry(QtCore.QRect(0, 0, 1027, 30))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.manageTeams.setFont(font)
        self.manageTeams.setStyleSheet("background-color: rgb(164, 255, 248);\n"
"")
        self.manageTeams.setObjectName("manageTeams")
        self.menuManage_teams = QtWidgets.QMenu(self.manageTeams)
        self.menuManage_teams.setStyleSheet("background-color: rgb(255, 135, 135);")
        self.menuManage_teams.setObjectName("menuManage_teams")
        Fantasy_Cricket.setMenuBar(self.manageTeams)
        self.statusbar = QtWidgets.QStatusBar(Fantasy_Cricket)
        self.statusbar.setObjectName("statusbar")
        Fantasy_Cricket.setStatusBar(self.statusbar)
        self.New_Team = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.New_Team.setFont(font)
        self.New_Team.setObjectName("New_Team")
        self.New_Team.triggered.connect(self.new_team) #New Team signal
        self.Open_Team = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.Open_Team.setFont(font)
        self.Open_Team.setObjectName("Open_Team")
        self.Open_Team.triggered.connect(self.open_team) #open Team signal
        self.Save_team = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.Save_team.setFont(font)
        self.Save_team.setObjectName("Save_team")
        self.Save_team.triggered.connect(self.savetm)
        self.Evaluate_Team = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.Evaluate_Team.setFont(font)
        self.Evaluate_Team.setObjectName("Evaluate_Team")
        self.Evaluate_Team.triggered.connect(self.evaluate_team)#Evaluate Team signal
        self.actionQuit = QtWidgets.QAction(Fantasy_Cricket)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.actionQuit.setFont(font)
        self.actionQuit.setObjectName("actionQuit")
        self.actionQuit.triggered.connect(self.quit)
        self.menuManage_teams.addAction(self.New_Team)
        self.menuManage_teams.addSeparator()
        self.menuManage_teams.addAction(self.Open_Team)
        self.menuManage_teams.addSeparator()
        self.menuManage_teams.addAction(self.Save_team)
        self.menuManage_teams.addSeparator()
        self.menuManage_teams.addAction(self.Evaluate_Team)
        self.menuManage_teams.addSeparator()
        self.menuManage_teams.addAction(self.actionQuit)
        self.manageTeams.addAction(self.menuManage_teams.menuAction())
        self.new_ui.createteam.clicked.connect(self.create) #new team signal
        self.error_ui.ok_btn.clicked.connect(self.close)    #error button signal
        self.stats={}       #stats list
        self.retranslateUi(Fantasy_Cricket)
        QtCore.QMetaObject.connectSlotsByName(Fantasy_Cricket)

    def retranslateUi(self, Fantasy_Cricket):
        _translate = QtCore.QCoreApplication.translate
        Fantasy_Cricket.setWindowTitle(_translate("Fantasy_Cricket", "Fantasy Cricket"))
        self.your_selections.setText(_translate("Fantasy_Cricket", "Your Selections"))
        self.batlabel.setText(_translate("Fantasy_Cricket", "    Batsmen(BAT)"))
        self.batmain.setPlaceholderText(_translate("Fantasy_Cricket", "##"))
        self.bowlabel.setText(_translate("Fantasy_Cricket", "Bowlers(BOW)"))
        self.bowlmain.setPlaceholderText(_translate("Fantasy_Cricket", "##"))
        self.arlabel.setText(_translate("Fantasy_Cricket", "All-Rounders(AR)"))
        self.armain.setPlaceholderText(_translate("Fantasy_Cricket", "##"))
        self.wklabel.setText(_translate("Fantasy_Cricket", "Wicket-Keeper(WK)"))
        self.wkmain.setPlaceholderText(_translate("Fantasy_Cricket", "##"))
        self.pointsAvailable.setText(_translate("Fantasy_Cricket", "Points Available:"))
        self.pointsAvlinp.setPlaceholderText(_translate("Fantasy_Cricket", "####"))
        self.pointsUsed.setText(_translate("Fantasy_Cricket", "Points Used:"))
        self.pointsUsedinp.setPlaceholderText(_translate("Fantasy_Cricket", "####"))
        self.batradio.setText(_translate("Fantasy_Cricket", "BAT"))
        self.bowradio.setText(_translate("Fantasy_Cricket", "BOW"))
        self.ar_radio.setText(_translate("Fantasy_Cricket", "AR"))
        self.wkradio.setText(_translate("Fantasy_Cricket", "WK"))
        self.TeamNamelabel.setText(_translate("Fantasy_Cricket", "Team Name:"))
        self.teamNameInput.setPlaceholderText(_translate("Fantasy_Cricket","your team name"))
        self.label_11.setText(_translate("Fantasy_Cricket", ">"))
        self.SaveBtn.setText(_translate("Fantasy_Cricket", "Save"))
        self.SaveBtn.setShortcut(_translate("Fantasy_Cricket", "Ctrl+S"))
        self.menuManage_teams.setTitle(_translate("Fantasy_Cricket", "Manage teams"))
        self.New_Team.setText(_translate("Fantasy_Cricket", "New Team"))
        self.New_Team.setShortcut(_translate("Fantasy_Cricket", "Ctrl+N"))
        self.Open_Team.setText(_translate("Fantasy_Cricket", "Open Team"))
        self.Open_Team.setShortcut(_translate("Fantasy_Cricket", "Ctrl+O"))
        self.Save_team.setText(_translate("Fantasy_Cricket", "Save team"))
        self.Save_team.setShortcut(_translate("Fantasy_Cricket", "Ctrl+S"))
        self.Evaluate_Team.setText(_translate("Fantasy_Cricket", "Evaluate Team"))
        self.Evaluate_Team.setShortcut(_translate("Fantasy_Cricket", "Ctrl+E"))
        self.actionQuit.setText(_translate("Fantasy_Cricket", "Quit"))
        self.actionQuit.setShortcut(_translate("Fantasy_Cricket", "Ctrl+X"))

    ##function for Creating Team##
    def create(self):
        self.tname=self.new_ui.inpteamname.text()       #throws an error if name is left empty
        if len(self.tname) == 0:
            self.err()
            self.error_ui.error_text.setText("This field cannot be empty!")

        elif self.tname.isnumeric():            #throws an error if name is numbers only#
            self.err()
            self.error_ui.error_text.setText("Please enter a valid teamname\n(Name must contain atleast one character)!!")
            
        else:
            self.tname=self.new_ui.inpteamname.text()
            self.teamNameInput.setText(" "+self.tname)      #creates the team with the given name#
            self.reset()
            self.New_team.close()

    def close(self):            #closes error window
        self.Error.close()

    def savetm(self):       #save team function#
        self.tname=self.teamNameInput.text()         
        cursfanta.execute("SELECT DISTINCT Name FROM teams")
        y=cursfanta.fetchall()
        for i in y:
            if i[0]==self.tname:                        #checks if team already exists#
                self.err()
                self.error_ui.error_text.setText("Team with same name already exists!!\nPlease choose another name")
                return 0
            
        if self.mist():     #Error handler
            self.err()
            self.error_ui.error_text.setText("Insufficient Players or Points!!!")
            return 0
            
        elif self.teamList.count() <=10: #counts the number of players if players are less throws an error
            self.err()
            self.error_ui.error_text.setText("Insufficient Players!!!")
            return 0
            
        else:
            try:
                cursfanta.execute("SELECT DISTINCT Name FROM teams;")
                h=cursfanta.fetchall()
                for k in h:                             
                    if self.teamNameInput.text() == k[0]:
                        cursfanta.execute("DELETE FROM teams WHERE Name='"+ self.teamNameInput.text() + "';")
            except:
                print("error1")
            for k in range(self.teamList.count()):      #saves the players list into database 
                try:
                    cursfanta.execute("INSERT INTO teams (Name, Players, Value) VALUES (?,?,?);",(self.teamNameInput.text(), self.list[k], Player_points[self.list[k]]))
                    fanta.commit()
                except:
                    print("error2")
            fanta.commit()         
        
    def reset(self):                                    #resets all the functions when new team or existing team is opened#
        self.enablebuttons()
        self.checkstate()
        self.avp =1000
        self.pointsAvlinp.setText(str(self.avp))
        self.usdpnts = 0
        self.pointsUsedinp.setText(str(self.usdpnts))
        self.Bats = 0
        self.batmain.setText(str(self.Bats))
        self.bol = 0
        self.bowlmain.setText(str(self.bol))
        self.alRn = 0
        self.armain.setText(str(self.alRn))
        self.wkt = 0
        self.wkmain.setText(str(self.wkt))
        self.list.clear()
        self.checkstate()
        self.teamList.clear()
        
    def enablebuttons(self):
        self.batradio.setEnabled(True)
        self.bowradio.setEnabled(True)
        self.ar_radio.setEnabled(True)          #enables all the features once toolbar menu is clicked#
        self.wkradio.setEnabled(True)
        self.SaveBtn.setEnabled(True)
        
    def checkstate(self):

        sql1="SELECT * from stats WHERE Ctg='BAT';"
        sql2="SELECT * from stats WHERE Ctg='BWL';"     #fetches the data from stats table in database#
        sql3="SELECT * from stats WHERE Ctg='AR';"
        sql4="SELECT * from stats WHERE Ctg='WK';"
          
        cursfanta.execute(sql1)
        a=cursfanta.fetchall()
        bats=[] #batsmen list
        for w in a:
            bats.append(w[0]) #appends batsmen name into lists# 
            self.p.append(w[0])#copy of batsmen lists# 
            self.stats[w[0]]=w[5]#selects value of respective players into list#
    
        cursfanta.execute(sql2)
        b=cursfanta.fetchall()
        bwl=[] #bowlers lists#
        for x in b:
            bwl.append(x[0])#appends bowlers name into lists#
            self.q.append(x[0])#copy of bowlers lists# 
            self.stats[x[0]]=x[5]#selects value of respective players into list#

        cursfanta.execute(sql3)
        c=cursfanta.fetchall()
        alR=[] #all-rounders lists#
        for y in c:
            alR.append(y[0])#appends all-rounders name into lists#
            self.stats[y[0]]=y[5]#copy of all-rounders lists# 
            self.r.append(y[0])#selects value of respective players into list#

        cursfanta.execute(sql4)
        d=cursfanta.fetchall()
        wK=[] #wicket-keepers lists#
        for z in d:
            wK.append(z[0])#appends wicket-keepers name into lists#
            self.stats[z[0]]=z[5]#copy of wicket-keepers lists#
            self.s.append(z[0])#selects value of respective players into list#

        for j in self.list:
            if j in bats:      
                bats.remove(j)
            elif j in bwl:
                bwl.remove(j)            #avoids occurence of players once removed from list#
            elif j in alR:
                alR.remove(j)
            elif j in wK:
                wK.remove(j)
                
        if self.batradio.isChecked() == True:           #adds Batsmen list upon clicking bat radio button#
            self.radList.clear()
            for i in range(len(bats)):
                item = QtWidgets.QListWidgetItem(bats[i])
                self.radList.addItem(item)

        elif self.bowradio.isChecked() == True:         #adds bowlers list upon clicking bwl radio button#
            self.radList.clear()
            for i in range(len(bwl)):
                item = QtWidgets.QListWidgetItem(bwl[i])
                self.radList.addItem(item)

        elif self.ar_radio.isChecked() == True:         #adds allrounders list upon clicking ar radio button#
            self.radList.clear()
            for i in range(len(alR)):
                item = QtWidgets.QListWidgetItem(alR[i])
                self.radList.addItem(item)
                
        elif self.wkradio.isChecked() == True:          #adds wicketkeeper list upon clicking wk radio button#
            self.radList.clear()
            for i in range(len(wK)):
                item = QtWidgets.QListWidgetItem(wK[i])
                self.radList.addItem(item)

        
    def removelist1(self, item):    #removes item from available player's list#
        self.total=self.teamList.count()
        if self.total > 10:
            self.err()
            self.error_ui.error_text.setText("Not more or less than 11 players allowed!")
        
        else:
            self.test_1(item.text())
            self.radList.takeItem(self.radList.row(item))
            self.teamList.addItem(item.text())
            self.list.append(item.text())
            self.mist()
    
    def test_1(self, pt): #adding points to used points and deducting from available points#
        self.avp -= self.stats[pt]
        self.usdpnts += self.stats[pt]
        if pt in self.p:
            self.Bats+= 1
        elif pt in self.q:
            self.bol+= 1
        elif pt in self.r:
            self.alRn+= 1
        elif pt in self.s:
            self.wkt+=1
        self.pointsAvlinp.setText(str(self.avp))
        self.pointsUsedinp.setText(str(self.usdpnts))
        self.batmain.setText(str(self.Bats))
        self.bowlmain.setText(str(self.bol))
        self.armain.setText(str(self.alRn))   
        self.wkmain.setText(str(self.wkt)) 
            
    def removelist2(self, item):#removes item from selected player's list#
        self.total=self.teamList.count()
        self.teamList.takeItem(self.teamList.row(item))
        self.radList.addItem(item.text())
        self.list.remove(item.text())
        self.test_2(item.text())


    def test_2(self, pt):   #adding points to available points and deducting from used points#
        self.avp += self.stats[pt]
        self.usdpnts -= self.stats[pt]
        if pt in self.p:
            self.Bats-=1
        elif pt in self.q:
            self.bol-=1
        elif pt in self.r:
            self.alRn-=1
        elif pt in self.s:
            self.wkt-=1

        self.pointsAvlinp.setText(str(self.avp))
        self.pointsUsedinp.setText(str(self.usdpnts))
        self.batmain.setText(str(self.Bats))
        self.bowlmain.setText(str(self.bol))
        self.armain.setText(str(self.alRn))
        self.wkmain.setText(str(self.wkt))
        
        
    def opentm(self): #function to open team when clicked open button#
        self.reset()
        tmname=self.open_ui.open_team_comboBox.currentText()
        self.teamNameInput.setText(tmname)
        cursfanta.execute("SELECT Players from teams WHERE Name= '" + tmname + "';")
        y=cursfanta.fetchall()
        score=[]
        for i in y:
            cursfanta.execute("SELECT Value from stats WHERE Player='"+i[0]+"';")
            z=cursfanta.fetchone()
            score.append(z[0])
        sum=0
        for i in score:
            sum+=i
        self.teamList.clear()
        self.checkstate()
        for i in y:
            self.teamList.addItem(i[0])
            self.list.append(i[0])
            self.test_1(i[0])
        self.usdpnts = sum
        self.avp = 1000-sum
        self.pointsAvlinp.setText(str(self.avp))
        self.pointsUsedinp.setText(str(self.usdpnts))
        self.open.close()

    def mist(self): #error handling function
         if self.wkt>1:
            self.err()
            self.error_ui.error_text.setText("Only one wicketkeeper allowed!")
            self.reset()
            return 0
         elif self.avp <= -1:
            self.err()
            self.error_ui.error_text.setText("Insufficient Points!")
            self.reset()
            return 0
        

        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Fantasy_Cricket = QtWidgets.QMainWindow()
    ui = Ui_Fantasy_Cricket()
    ui.setupUi(Fantasy_Cricket)
    Fantasy_Cricket.show()
    sys.exit(app.exec_())
