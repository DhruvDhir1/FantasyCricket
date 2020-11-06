


from PyQt5 import QtCore, QtGui, QtWidgets
from newfile import Ui_Form as createTeam
from OpenfileWindow import Ui_Form as openTeam
from evaluate import Ui_Form as evaluateTeam
from Score import Ui_Form as Score


import sqlite3
player=sqlite3.connect("Players.db")
curplayer=player.cursor()

class Ui_MainWindow(object):
    def __init__(self):
        self.create_dialog=QtWidgets.QMainWindow()
        self.create_screen=createTeam()
        self.create_screen.setupUi(self.create_dialog)

        self.open_dialog=QtWidgets.QMainWindow()
        self.open_screen=openTeam()
        self.open_screen.setupUi(self.open_dialog)

        self.eval_dialog=QtWidgets.QMainWindow()
        self.eval_screen=evaluateTeam()
        self.eval_screen.setupUi(self.eval_dialog)

        self.score_dialog=QtWidgets.QMainWindow()
        self.score_screen=Score()
        self.score_screen.setupUi(self.score_dialog)
        


    
    def setupUi(self, MainWindow):
        self.batcount=0
        self.wkcount=0
        self.arcount=0
        self.bowlcount=0
        self.totalcount=0
        
        

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(689, 649)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(9, 28, 608, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.Batsmen = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Batsmen.setFont(font)
        self.Batsmen.setObjectName("Batsmen")
        self.horizontalLayout.addWidget(self.Batsmen)
        self.Batcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Batcount.setObjectName("Batcount")
        self.horizontalLayout.addWidget(self.Batcount)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.Bowler = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Bowler.setFont(font)
        self.Bowler.setObjectName("Bowler")
        self.horizontalLayout.addWidget(self.Bowler)
        self.Bowlcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Bowlcount.setObjectName("Bowlcount")
        self.horizontalLayout.addWidget(self.Bowlcount)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.Allrounder = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Allrounder.setFont(font)
        self.Allrounder.setObjectName("Allrounder")
        self.horizontalLayout.addWidget(self.Allrounder)
        self.Arcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Arcount.setObjectName("Arcount")
        self.horizontalLayout.addWidget(self.Arcount)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem3)
        self.Wicketkeeper = QtWidgets.QLabel(self.horizontalLayoutWidget)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Wicketkeeper.setFont(font)
        self.Wicketkeeper.setObjectName("Wicketkeeper")
        self.horizontalLayout.addWidget(self.Wicketkeeper)
        self.Wkcount = QtWidgets.QLabel(self.horizontalLayoutWidget)
        self.Wkcount.setObjectName("Wkcount")
        self.horizontalLayout.addWidget(self.Wkcount)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 5, 101, 21))
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayoutWidget_4 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_4.setGeometry(QtCore.QRect(50, 170, 531, 22))
        self.horizontalLayoutWidget_4.setObjectName("horizontalLayoutWidget_4")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_4)
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.BATrb = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BATrb.setFont(font)
        self.BATrb.setObjectName("BATrb")
        self.horizontalLayout_4.addWidget(self.BATrb)
        self.BOWrb = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.BOWrb.setFont(font)
        self.BOWrb.setObjectName("BOWrb")
        self.horizontalLayout_4.addWidget(self.BOWrb)
        self.ARrb = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.ARrb.setFont(font)
        self.ARrb.setObjectName("ARrb")
        self.horizontalLayout_4.addWidget(self.ARrb)
        self.WKrb = QtWidgets.QRadioButton(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.WKrb.setFont(font)
        self.WKrb.setObjectName("WKrb")
        self.horizontalLayout_4.addWidget(self.WKrb)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem5)
        self.TeamName = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.TeamName.setFont(font)
        self.TeamName.setObjectName("TeamName")
        self.horizontalLayout_4.addWidget(self.TeamName)
        self.Name = QtWidgets.QLabel(self.horizontalLayoutWidget_4)
        self.Name.setObjectName("Name")
        self.horizontalLayout_4.addWidget(self.Name)
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem6)
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(50, 190, 531, 381))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listWidget_2 = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.horizontalLayout_3.addWidget(self.listWidget_2)
        spacerItem7 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem7)
        self.label_14 = QtWidgets.QLabel(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_14.setFont(font)
        self.label_14.setObjectName("label_14")
        self.horizontalLayout_3.addWidget(self.label_14)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem8)
        self.listWidget = QtWidgets.QListWidget(self.horizontalLayoutWidget_3)
        self.listWidget.setObjectName("listWidget")
        self.horizontalLayout_3.addWidget(self.listWidget)
        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(50, 80, 351, 41))
        self.horizontalLayoutWidget_2.setObjectName("horizontalLayoutWidget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.Totalplayers = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Totalplayers.setObjectName("Totalplayers")
        self.horizontalLayout_2.addWidget(self.Totalplayers)
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem9)
        self.Teamcount = QtWidgets.QLabel(self.horizontalLayoutWidget_2)
        self.Teamcount.setText("")
        self.Teamcount.setObjectName("Teamcount")
        self.horizontalLayout_2.addWidget(self.Teamcount)
        self.horizontalLayoutWidget_5 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_5.setGeometry(QtCore.QRect(50, 570, 531, 41))
        self.horizontalLayoutWidget_5.setObjectName("horizontalLayoutWidget_5")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_5)
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        spacerItem10 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem10)
        self.label_4 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_5.addWidget(self.label_4)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem11)
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem12)
        spacerItem13 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem13)
        spacerItem14 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem14)
        spacerItem15 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem15)
        self.label_2 = QtWidgets.QLabel(self.horizontalLayoutWidget_5)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_5.addWidget(self.label_2)
        spacerItem16 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem16)
        spacerItem17 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem17)
        self.horizontalLayoutWidget_6 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_6.setGeometry(QtCore.QRect(50, 130, 531, 41))
        self.horizontalLayoutWidget_6.setObjectName("horizontalLayoutWidget_6")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_6)
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.Points_Availaible = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.Points_Availaible.setFont(font)
        self.Points_Availaible.setObjectName("Points_Availaible")
        self.horizontalLayout_6.addWidget(self.Points_Availaible)
        self.TotalPoints = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.TotalPoints.setObjectName("TotalPoints")
        self.horizontalLayout_6.addWidget(self.TotalPoints)
        spacerItem18 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem18)
        self.Points_Used = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.Points_Used.setFont(font)
        self.Points_Used.setObjectName("Points_Used")
        self.horizontalLayout_6.addWidget(self.Points_Used)
        self.Used_Points = QtWidgets.QLabel(self.horizontalLayoutWidget_6)
        self.Used_Points.setObjectName("Used_Points")
        self.horizontalLayout_6.addWidget(self.Used_Points)
        spacerItem19 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem19)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 689, 21))

#---------------------------menu bar------------------
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

#------------------------NEW TEAM---------------------
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.actionNEW_Team.triggered.connect(self.create_teams)

      #----------------OPEN TEAM-------------------
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.actionOPEN_Team.triggered.connect(self.open_file)
    #----------------------SAVE TEAM----------------
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.actionSAVE_Team.triggered.connect(self.save_team)
      #-------------------EVALUATE TEAM---------------------  
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.actionQUIT = QtWidgets.QAction(MainWindow)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.actionEVALUATE_Team.triggered.connect(self.eval_file)
     #------------------------QUIT ACTION-----------------
        self.actionQUIT.setObjectName("actionQUIT")
        self.menuManage_Teams.addAction(self.actionQUIT)
        self.menubar.addAction(self.menuManage_Teams.menuAction())
        self.actionQUIT.triggered.connect(self.quit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    #----------------------------RADIO BUTTON----------------
        self.BATrb.clicked.connect(self.add_names)
        self.BOWrb.clicked.connect(self.add_names)
        self.ARrb.clicked.connect(self.add_names)
        self.WKrb.clicked.connect(self.add_names)
    #---------------------------LIST WIDGET-----------------
        self.listWidget_2.itemDoubleClicked.connect(self.removelist1)
        self.listWidget.itemDoubleClicked.connect(self.removelist2)
        self.eval_screen.SelectTeam.currentTextChanged.connect(self.combo)
        
#----------------------------
        self.create_screen.pushButton.clicked.connect(self.showTeam_name)
        self.open_screen.pushButton.clicked.connect(self.open_file)
        self.eval_screen.Calculate.clicked.connect(self.score)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Batsmen.setText(_translate("MainWindow", "Batsmen (BAT)"))
        self.Batcount.setText(_translate("MainWindow", "##"))
        self.Bowler.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.Bowlcount.setText(_translate("MainWindow", "##"))
        self.Allrounder.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.Arcount.setText(_translate("MainWindow", "##"))
        self.Wicketkeeper.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.Wkcount.setText(_translate("MainWindow", "##"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.BATrb.setText(_translate("MainWindow", "BAT"))
        self.BOWrb.setText(_translate("MainWindow", "BOW"))
        self.ARrb.setText(_translate("MainWindow", "AR"))
        self.WKrb.setText(_translate("MainWindow", "WK"))
        self.TeamName.setText(_translate("MainWindow", "Team Name"))
        self.Name.setText(_translate("MainWindow", "Displayed Here"))
        self.label_14.setText(_translate("MainWindow", ">"))
        self.label_3.setText(_translate("MainWindow", "Total Players"))
        self.Totalplayers.setText(_translate("MainWindow", "##"))
        self.label_4.setText(_translate("MainWindow", "PLAYERS AVAILAIBLE"))
        self.label_2.setText(_translate("MainWindow", "PLAYERS USED"))
        self.Points_Availaible.setText(_translate("MainWindow", "Points Availaible"))
        self.TotalPoints.setText(_translate("MainWindow", "1000"))
        self.Points_Used.setText(_translate("MainWindow", "Points Used"))
        self.Used_Points.setText(_translate("MainWindow", "##"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionNEW_Team.setShortcut(_translate("MainWindow", "Alt+N"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionOPEN_Team.setShortcut(_translate("MainWindow", "Alt+O"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionSAVE_Team.setShortcut(_translate("MainWindow", "Alt+S"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))
        self.actionEVALUATE_Team.setShortcut(_translate("MainWindow", "Alt+E"))
        self.actionQUIT.setText(_translate("MainWindow", "QUIT"))
        self.actionQUIT.setShortcut(_translate("MainWindow", "Alt+Q"))

    
            

    
    def add_names(self):
        batlist=[]
        bowllist=[]
        arlist=[]
        wklist=[]
        teamlist_2=[]
        for i in range(self.listWidget.count()):
            teamlist_2.append(self.listWidget.item(i).text())
        

        sql="SELECT * FROM stats"
        curplayer.execute(sql)
        
        if self.BATrb.isChecked()==True:
            self.listWidget_2.clear()
            result=curplayer.fetchall()
            for results in result:
                if results[6]=='BAT':
                    batlist.append(results[0])
            for item in batlist:
                if item not in teamlist_2:
                    self.listWidget_2.addItem(item)
                        
                            
        if self.BOWrb.isChecked()==True:
            self.listWidget_2.clear()
            result=curplayer.fetchall()
            for results in result:
                if results[6]=='BWL':
                    bowllist.append(results[0])
            for item in bowllist:
                if item not in teamlist_2:
                    self.listWidget_2.addItem(item)
 
        if self.ARrb.isChecked()==True:
            self.listWidget_2.clear()
            result=curplayer.fetchall()
            for results in result:
                if results[6]=='AR':
                    arlist.append(results[0])
            for item in arlist:
                if item not in teamlist_2:
                    self.listWidget_2.addItem(item)

        if self.WKrb.isChecked()==True:
            self.listWidget_2.clear()
            result=curplayer.fetchall()
            for results in result:
                if results[6]=='WK':
                    wklist.append(results[0])
            for item in wklist:
                if item not in teamlist_2:
                    self.listWidget_2.addItem(item)
        
        
        



    def points(self):
        self.usedpoints=0
        self.total=self.TotalPoints.text()
        teamlist=[]
        for item in range(self.listWidget.count()):
            teamlist.append(self.listWidget.item(item).text())
        for item in teamlist:
            curplayer.execute("SELECT * from stats;")
            results=curplayer.fetchall()
            for result in results:
                if result[0]== item:
                    self.totalpoints=int(self.total)-result[5]
                    self.usedpoints=self.usedpoints+int(self.total)-int(self.totalpoints)
                    self.TotalPoints.setText(str(self.totalpoints))
                    self.Used_Points.setText(str(self.usedpoints))
            
        
    def points_1(self):
        curplayer.execute("SELECT value from stats WHERE player='"+self.remove+"';")
        self.avail=self.TotalPoints.text()
        self.used=self.Used_Points.text()
        value=curplayer.fetchone()
        for values in value:
            self.avail=int(self.avail)+values
            self.used=int(self.used)-values
            self.TotalPoints.setText(str(self.avail))
            self.Used_Points.setText(str(self.used))
             

    def removelist1(self,item):
        
        if self.BATrb.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget.addItem(item.text())
            self.points()
            self.batcount +=1
            self.totalplayers=self.listWidget.count() 
            self.error()
            self.Batcount.setText(str(self.batcount))
            self.Totalplayers.setText(str(self.totalplayers))
            
        elif self.BOWrb.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget.addItem(item.text())
            self.points()
            self.bowlcount +=1
            self.totalplayers=self.listWidget.count()
            self.error()
            self.Bowlcount.setText(str(self.bowlcount))
            self.Totalplayers.setText(str(self.totalplayers))

        elif self.ARrb.isChecked()==True:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget.addItem(item.text())
            self.points()
            self.arcount +=1
            self.totalplayers=self.listWidget.count()
            self.error()
            self.Arcount.setText(str(self.arcount))
            self.Totalplayers.setText(str(self.totalplayers))
        else:
            self.listWidget_2.takeItem(self.listWidget_2.row(item))
            self.listWidget.addItem(item.text())
            self.points()
            self.wkcount +=1
            self.totalplayers=self.listWidget.count()
            self.error()
            self.Wkcount.setText(str(self.wkcount))
            self.Totalplayers.setText(str(self.totalplayers))
        


    def removelist2(self,item):
        curplayer.execute("SELECT * from stats;")
        results=curplayer.fetchall()
        if self.BATrb.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.remove=item.text()
            self.points_1()
            self.batcount -=1
            self.totalplayers=self.listWidget.count()
            self.error() 
            self.Batcount.setText(str(self.batcount))
            self.Totalplayers.setText(str(self.totalplayers))

        elif self.BOWrb.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.remove=item.text()
            self.points_1()
            self.bowlcount -=1
            self.totalplayers=self.listWidget.count()
            self.error()
            self.Bowlcount.setText(str(self.bowlcount))
            self.Totalplayers.setText(str(self.totalplayers))

        elif self.ARrb.isChecked()==True:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.remove=item.text()
            self.points_1()
            self.arcount -=1
            self.totalplayers=self.listWidget.count()
            self.error() 
            self.Arcount.setText(str(self.arcount))
            self.Totalplayers.setText(str(self.totalplayers))

        else:
            self.listWidget.takeItem(self.listWidget.row(item))
            self.listWidget_2.addItem(item.text())
            self.remove=item.text()
            self.points_1()
            self.wkcount -=1
            self.totalplayers=self.listWidget.count()
            self.error()
            self.Wkcount.setText(str(self.wkcount))
            self.Totalplayers.setText(str(self.totalplayers))
        

    def error(self):
        error_dialog=QtWidgets.QErrorMessage()
        if self.batcount>=0 and self.batcount<=4:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 4 Batsmen are allowed.')
            error_dialog.exec_()

        if self.bowlcount>=0 and self.bowlcount<=3:
            pass
        else:
            error_dialog.showMessage('Oh no! Only 3 Bowlers are allowed.')
            error_dialog.exec_()

        if self.arcount>=0 and self.arcount<=3:
            pass
        else:
            error_dialog.showMessage("Oh no! Only 3 All-Rounders are allowed.")
            error_dialog.exec_()
            
        if self.wkcount>=0 and self.wkcount<=1:
            pass
        else:
            error_dialog.showMessage("Oh no! Only 1 Wicket-Keeper is allowed.")
            error_dialog.exec_()

        if self.totalcount>=0 and self.totalcount<=11:
            pass
        else:
            error_dialog.showMessage("Insufficient Players")
            error_dialog.exec_()

        if self.totalpoints<0 and self.usedpoints>1000:
            error_dialog.showMessage("Please select the players within the provided points")
            error_dialog.exec_()
        else:
            pass
                

    def create_teams(self):
        
        self.create_dialog.show()
        self.clear()
        
    def showTeam_name(self):
        teamname=self.create_screen.lineEdit.text()
        
        listname=[]
        error_dialog=QtWidgets.QErrorMessage()
        curplayer.execute("SELECT * from teams")
        results=curplayer.fetchall()
        for result in results:
            listname.append(result[0])
        for item in set(listname):
            if item == teamname:
                error_dialog.showMessage("Team with this name already exists.")
                error_dialog.exec_()
                break
            elif teamname not in listname:
                self.Name.setText(str(teamname))
            else:
                pass
        self.create_screen.lineEdit.clear()
            
                
                

    def save_team(self):
        error_dialog=QtWidgets.QErrorMessage()
        if (self.batcount+self.bowlcount+self.arcount+self.wkcount)!= 11:
            error_dialog.showMessage("You have to select 11 players!")
            error_dialog.exec_()
        else:
            pass
        

        team_list = []
        team_name=self.Name.text()
        

        for item in range(self.listWidget.count()):
            team_list.append(self.listWidget.item(item).text())
        if team_name=="Displayed Here":
            error_dialog.showMessage("You need to first create a new team before saving!...Please select New Team from menubar.")
            error_dialog.exec_()
        else:
    
            for item in set(team_list):
                curplayer.execute("SELECT * from match;")
                results=curplayer.fetchall()
                for result in results:
                    if result[0]==item:
                        runs=result[1]
                        balls=result[2]
                        fours=result[3]
                        six=result[4]
                        self.batscore=int(runs/2)
                        if runs>=50:
                            self.batscore += 5
                        if runs>=100:
                            self.batscore += 10
                        if runs>0:
                            sr=runs*100/balls
                            if sr>=80 and sr<=100:
                                self.batscore +=2
                            if sr>100:
                                self.batscore += 4
                        self.batscore = self.batscore+int(fours)
                        self.batscore = self.batscore+ 2*int(six)

                        
                        wicket=result[8]
                        bowled=result[5]
                        given=result[7]
                        self.bowlscore=int(wicket)*10
                        if wicket >=3:
                            self.bowlscore +=5
                        if wicket >=5:
                            self.bowlscore +=10
                        if bowled>0:
                            overs=int(bowled)/6
                            er=int(given)/overs
                            if er>=3.5 and er<4.5:
                                self.bowlscore += 4
                            if er>=2 and er<3.5:
                                self.bowlscore += 7
                            if er<2:
                                self.bowlscore =+ 10

                        catch=result[9]
                        stumping=result[10]
                        runout=result[11]
                        self.fieldscore=0
                        if catch>0:
                            self.fieldscore += 10
                        if stumping>0:
                            self.fieldscore += 10
                        if runout>0:
                            self.fieldscore += 10
                        total=int(int(self.batscore)+int(self.bowlscore)+int(self.fieldscore))

                        curplayer.execute("SELECT * from stats")
                        records=curplayer.fetchall()
                        for record in records:
                            if item==record[0] and team_name != "Displayed Here":
                                curplayer.execute("INSERT INTO teams(name, players, value, scores) VALUES(?,?,?,?);",(team_name, item, record[5], total))
                                player.commit()


    def clear(self):
        self.batcount=0
        self.bowlcount=0
        self.arcount=0
        self.wkcount=0
        self.totalpoints=1000
        self.usedpoints=0
        self.Batcount.clear()
        self.Bowlcount.clear()
        self.Wkcount.clear()
        self.Arcount.clear()
        self.Totalplayers.clear()
        self.listWidget_2.clear()
        self.listWidget.clear()
        self.TotalPoints.setText(str(1000))
        self.Used_Points.clear()

    def open_file(self):
        self.clear()
        self.open_dialog.show()
        self.Name.setText(str(self.open_screen.lineEdit.text()))
        curplayer.execute("SELECT * from teams;")
        record=curplayer.fetchall()
        for records in record:
            if self.open_screen.lineEdit.text()==records[0]:
                self.listWidget.addItem(records[1])
        
        itemlist=[]
        for i in range(self.listWidget.count()):
            itemlist.append(self.listWidget.item(i).text())
        for item in itemlist:
            curplayer.execute("SELECT * from stats;")
            results=curplayer.fetchall()
            for result in results:
                if item==result[0]:
                    if result[6]=='BAT':
                        self.batcount +=1
                        self.Batcount.setText(str(self.batcount))
                        
                    elif result[6]=='BWL':
                        self.bowlcount +=1
                        self.Bowlcount.setText(str(self.bowlcount))

                    elif result[6]=='AR':
                        self.arcount +=1
                        self.Arcount.setText(str(self.arcount))
                    else:
                        self.wkcount +=1
                        self.Wkcount.setText(str(self.wkcount))
                    self.total=self.TotalPoints.text()
                    self.totalpoints=int(self.total)-result[5]
                    self.usedpoints=self.usedpoints+int(self.total)-int(self.totalpoints)
                    self.TotalPoints.setText(str(self.totalpoints))
                    self.Used_Points.setText(str(self.usedpoints))
        
        self.open_screen.lineEdit.clear()
            

    def eval_file(self):
        self.eval_dialog.show()
    def combo(self):
        self.eval_screen.SelectMatch.currentTextChanged.connect(self.combo2)
    def combo2(self):
        
        curplayer.execute("SELECT * from teams;")
        record=curplayer.fetchall()
        self.eval_screen.PlayerList.clear()
        self.eval_screen.ScoreList.clear()
        for records in record:
            if self.eval_screen.SelectTeam.currentText()==records[0]:
                self.eval_screen.PlayerList.addItem(records[1])
                self.eval_screen.ScoreList.addItem(str(records[3]))

    def score(self):
        self.score_screen.Score.clear()
        self.score_dialog.show()
        curplayer.execute("SELECT * from teams;")
        results=curplayer.fetchall()
        record=0
        for result in results:
            if self.eval_screen.SelectTeam.currentText()==result[0]:
                record=record+result[3]
        self.score_screen.Score.setText(str(record))
              

    def quit(self):
        sys.exit()

        
                    
        
      


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
