#!/usr/bin/python3

from PyQt5 import QtCore, QtGui, QtWidgets
from string import punctuation
import sqlite3

con = sqlite3.connect('match_info.db') #Connecting to database

#Display info dialog
def displayMsg(title,msg,ico_type=None):
    MsgBox = QtWidgets.QMessageBox()
    MsgBox.setText(msg)
    MsgBox.setWindowTitle(title)
    if ico_type == 'err':
        ico = QtWidgets.QMessageBox.Critical
    else:
        ico = QtWidgets.QMessageBox.Information
    MsgBox.setIcon(ico)
    MsgBox.exec()


#Class for new team dialog
class Ui_NewTeamDialog(object):
    def setupUi(self, NewTeamDialog):
        NewTeamDialog.setObjectName("NewTeamDialog")
        NewTeamDialog.resize(356, 105)
        self.buttonBox = QtWidgets.QDialogButtonBox(NewTeamDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 60, 181, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(NewTeamDialog)
        self.label.setGeometry(QtCore.QRect(20, 30, 91, 16))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(NewTeamDialog)
        self.lineEdit.setGeometry(QtCore.QRect(120, 30, 181, 20))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(NewTeamDialog)
        self.buttonBox.accepted.connect(NewTeamDialog.accept)
        self.buttonBox.rejected.connect(NewTeamDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(NewTeamDialog)

    def retranslateUi(self, NewTeamDialog):
        _translate = QtCore.QCoreApplication.translate
        NewTeamDialog.setWindowTitle(_translate("NewTeamDialog", "Create New Team"))
        self.label.setText(_translate("NewTeamDialog", "Enter Team Name"))

#Class for open team dialog
class Ui_OpenTeamDialog(object):
    def setupUi(self, OpenTeamDialog):
        OpenTeamDialog.setObjectName("OpenTeamDialog")
        OpenTeamDialog.resize(303, 117)
        self.buttonBox = QtWidgets.QDialogButtonBox(OpenTeamDialog)
        self.buttonBox.setGeometry(QtCore.QRect(80, 70, 161, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(OpenTeamDialog)
        self.label.setGeometry(QtCore.QRect(10, 30, 71, 16))
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(OpenTeamDialog)
        self.comboBox.setGeometry(QtCore.QRect(80, 30, 171, 22))
        self.comboBox.setObjectName("comboBox")

        self.retranslateUi(OpenTeamDialog)
        self.buttonBox.accepted.connect(OpenTeamDialog.accept)
        self.buttonBox.rejected.connect(OpenTeamDialog.reject)
        QtCore.QMetaObject.connectSlotsByName(OpenTeamDialog)

    def retranslateUi(self, OpenTeamDialog):
        _translate = QtCore.QCoreApplication.translate
        OpenTeamDialog.setWindowTitle(_translate("OpenTeamDialog", "Open Team"))
        self.label.setText(_translate("OpenTeamDialog", "Select Team:"))

#Class for evaluate window
class Ui_evaluateWindow(object):
    def setupUi(self, evaluateWindow):
        evaluateWindow.setObjectName("evaluateWindow")
        evaluateWindow.resize(432, 395)
        evaluateWindow.setStyleSheet("font-family:\"Comic Sans MS\";")
        self.label = QtWidgets.QLabel(evaluateWindow)
        self.label.setGeometry(QtCore.QRect(80, 10, 281, 20))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setPointSize(9)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.comboBox = QtWidgets.QComboBox(evaluateWindow)
        self.comboBox.setGeometry(QtCore.QRect(60, 40, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox_2 = QtWidgets.QComboBox(evaluateWindow)
        self.comboBox_2.setGeometry(QtCore.QRect(260, 40, 111, 22))
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.line = QtWidgets.QFrame(evaluateWindow)
        self.line.setGeometry(QtCore.QRect(20, 70, 391, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.label_2 = QtWidgets.QLabel(evaluateWindow)
        self.label_2.setGeometry(QtCore.QRect(40, 100, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.listWidget = QtWidgets.QListWidget(evaluateWindow)
        self.listWidget.setGeometry(QtCore.QRect(40, 120, 161, 221))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(evaluateWindow)
        self.listWidget_2.setGeometry(QtCore.QRect(230, 120, 161, 221))
        self.listWidget_2.setStyleSheet("color: rgb(0, 85, 255);")
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_3 = QtWidgets.QLabel(evaluateWindow)
        self.label_3.setGeometry(QtCore.QRect(230, 100, 47, 13))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(evaluateWindow)
        self.label_4.setGeometry(QtCore.QRect(270, 100, 47, 13))
        self.label_4.setStyleSheet("color: rgb(0, 85, 255);")
        self.label_4.setText("")
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(evaluateWindow)
        self.pushButton.setGeometry(QtCore.QRect(160, 360, 91, 23))
        self.pushButton.setObjectName("pushButton")

        self.retranslateUi(evaluateWindow)
        QtCore.QMetaObject.connectSlotsByName(evaluateWindow)

    def retranslateUi(self, evaluateWindow):
        _translate = QtCore.QCoreApplication.translate
        evaluateWindow.setWindowTitle(_translate("evaluateWindow", "Evaluate Team"))
        self.label.setText(_translate("evaluateWindow", "Evaluate the performance of your Fantasy Team"))
        self.comboBox.setItemText(0, _translate("evaluateWindow", "Select Team"))
        self.comboBox_2.setItemText(0, _translate("evaluateWindow", "Select Match"))
        self.label_2.setText(_translate("evaluateWindow", "Players"))
        self.label_3.setText(_translate("evaluateWindow", "Points"))
        self.pushButton.setText(_translate("evaluateWindow", "Calculate Score"))



class Ui_MainWindow(object):
    
    #Fetch Players
    def fetchPlayers(self):
        if self.radioButton.isChecked():
            ctg = 'BAT'
        elif self.radioButton_2.isChecked():
            ctg = 'BWL'
        elif self.radioButton_3.isChecked():
            ctg = 'AR'
        elif self.radioButton_4.isChecked():
            ctg = 'WK'
        else:
            return
        try:
            cursor = con.execute("SELECT PLAYER from PLAYER_INFO WHERE CTG='"+ctg+"'")
        except:
            displayMsg('Database Error','Could not execute database command!','err')
            return
        self.listWidget.clear()
        list2_items = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
        for i in cursor:
            if i[0] not in list2_items:
                self.listWidget.addItem(i[0])

    #Updates Values
    def updateValues(self):
        points_available,bat,bow,ar,wk = 1000,0,0,0,0
        list2_items = [self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())]
        for i in range(self.listWidget_2.count()):
            val,ctg = list(con.execute("SELECT VALUE,CTG from PLAYER_INFO WHERE PLAYER='"+self.listWidget_2.item(i).text()+"'"))[0]
            if ctg == 'BAT':
                bat += 1
            elif ctg == 'BWL':
                bow += 1
            elif ctg == 'AR':
                ar += 1
            else:
                wk += 1
            points_available -= val
        self.label_10.setText(str(bat))
        self.label_11.setText(str(bow))
        self.label_12.setText(str(ar))
        self.label_13.setText(str(wk))
        self.label_14.setText(str(points_available))
        self.label_15.setText(str(1000-points_available))
        return (points_available,bat,bow,ar,wk)

    #Resets the environment of main window
    def resetEnv(self):
        self.radioButton.setCheckable(True)
        self.radioButton_2.setCheckable(True)
        self.radioButton_3.setCheckable(True)
        self.radioButton_4.setCheckable(True)
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.updateValues()
        self.fetchPlayers()
    
    #Get Team Name when creating new team    
    def getname(self):
        teamName = self.ui.lineEdit.text()
        if teamName == '':
            displayMsg('Error',"Team name can't be empty",'err')
        elif any(char in punctuation for char in teamName):
            displayMsg('Error',"Team name can't contain special charcters",'err')
        else:
            self.resetEnv()
            self.label_16.setText(teamName)

    #Create New Team 
    def createNewTeam(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_NewTeamDialog()
        self.ui.setupUi(self.window)
        self.window.show()
        self.ui.buttonBox.accepted.connect(self.getname)

    #Get players of selected team
    def getTeam(self):
        team_name = self.ui.comboBox.currentText()
        try:
            players = list(con.execute("SELECT PLAYERS from TEAMS WHERE NAME='"+team_name+"'"))[0][0].split(",")
        except:
            displayMsg('Database Error','Could not execute database command!','err')
            return
        self.resetEnv()
        self.label_16.setText(team_name)
        for i in players:
            self.listWidget_2.addItem(i)
        self.fetchPlayers()
        self.updateValues()

    #Open team    
    def openTeam(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_OpenTeamDialog()
        self.ui.setupUi(self.window)
        self.window.show()
        try:
            for i in con.execute("SELECT NAME from TEAMS"):
                self.ui.comboBox.addItem(i[0])
        except:
            self.window.close()
            displayMsg('Database Error','Could not execute database command!','err')
            return
        self.ui.buttonBox.accepted.connect(self.getTeam)

    #Save team
    def saveTeam(self):
        res = self.updateValues()
        if sum(res[1:])<11:
            displayMsg('Error','Team has less than 11 players.\nChoose more players','err')
        elif res[4]<1:
            displayMsg('Error','You must select 1 wicket-keeper','err')
        else:
            teamName = self.label_16.text()
            team_players = ",".join([self.listWidget_2.item(i).text() for i in range(self.listWidget_2.count())])
            try:
                if teamName in [i[0] for i in con.execute("SELECT NAME from TEAMS")]:
                    displayMsg('Information','Team already exists!\nTeam players will be updated')
                    con.execute("UPDATE TEAMS set PLAYERS=? WHERE NAME=?",(team_players,teamName))
                else:
                    con.execute("INSERT INTO TEAMS(NAME,PLAYERS) \
                        VALUES(?,?)",(teamName,team_players));
                    displayMsg('Information','Team successfully saved!')
                con.commit()
            except:
                con.rollback()
                displayMsg('Database Error',"Can't execute database command!\nAll changes are rolled back",'err')

    #Calculate score of selected team
    def calculateScore(self):
        score = sum([int(self.ui.listWidget_2.item(i).text()) for i in range(self.ui.listWidget_2.count())])
        self.ui.label_4.setText(str(score))
        displayMsg('Score','Your score is '+str(score))

    #Get match data
    def getMatchData(self):
        team = self.ui.comboBox.currentText()
        match = self.ui.comboBox_2.currentText()
        if team != 'Select Team' and match != 'Select Match':
            try:
                players = list(con.execute("SELECT PLAYERS from TEAMS WHERE NAME='"+team+"'"))[0][0].split(",")
            except:
                displayMsg('Database Error','Could not execute database command!','err')
                return
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            for player in players:
                try:
                    scored,faced,fours,sixes,wkts,bowled,given,catches,stumping,ro = list(con.execute("SELECT SCORED,FACED,FOURS,SIXES,WKTS,BOWLED,GIVEN,CATCHES,STUMPING,RO from '"+match+"' WHERE PLAYER = '"+player+"'"))[0]
                except:
                    displayMsg('Database Error','Could not execute database command!','err')
                    return
                strike_rate = scored*100/faced if faced != 0 else 0
                economy_rate = given/(bowled/6) if bowled != 0 else 0
                bat_points = scored//2+(5 if scored>=50 else 0)+(10 if scored>=100 else 0)+(2 if strike_rate>=80 and strike_rate<=100 else (4 if strike_rate>100 else 0))+fours+2*sixes
                bwl_points = 10*wkts+(5 if wkts>=3 else 0)+(10 if wkts>=5 else 0)+(4 if economy_rate>=3.5 and economy_rate<=4.5 else (7 if economy_rate>=2 and economy_rate<3.5 else (10 if economy_rate<2 else 0)))
                fld_points = 10*(catches+stumping+ro)
                points = bat_points+bwl_points+fld_points
                self.ui.listWidget.addItem(player)
                self.ui.listWidget_2.addItem(str(points))
        else:
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
        self.ui.label_4.setText("")
        
    #Evaluate Team
    def evalTeam(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_evaluateWindow()
        self.ui.setupUi(self.window)
        self.window.show()
        try:
            for i in con.execute("SELECT NAME from TEAMS"):
                self.ui.comboBox.addItem(i[0])
            for i in con.execute("SELECT name from sqlite_master where type='table' and (name != 'TEAMS' and name != 'PLAYER_INFO')"):
                self.ui.comboBox_2.addItem(i[0])
        except:
            self.window.close()
            displayMsg('Database Error','Could not execute database command!','err')
            return
        self.ui.comboBox.currentIndexChanged.connect(self.getMatchData)
        self.ui.comboBox_2.currentIndexChanged.connect(self.getMatchData)
        self.ui.pushButton.clicked.connect(self.calculateScore)
        
    #Moves items from players list to selected players list
    def moveItem(self):
        curritem = self.listWidget.currentItem()
        try:
            val,ctg = list(con.execute("SELECT VALUE,CTG from PLAYER_INFO WHERE PLAYER='"+curritem.text()+"'"))[0]
        except:
            displayMsg('Database Error','Could not execute database command!','err')
            return
        res = self.updateValues()
        if sum(res[1:])<11:
            if val<=res[0]:
                if ctg == 'WK' and res[4]==1:
                    displayMsg('Error',"You can't select more than one wicket-keeper",'err')
                    return
                self.listWidget_2.addItem(curritem.text())
                self.listWidget.takeItem(ui.listWidget.row(curritem))
                self.updateValues()
            else:
                displayMsg('Error',"You need more points to select the player",'err')
        else:
            displayMsg('Error',"Can't add more than 11 players!",'err')

    #Unselects items from selected players list
    def removeItem(self):
        curritem = self.listWidget_2.currentItem()
        self.listWidget_2.takeItem(self.listWidget_2.row(curritem))
        self.fetchPlayers()
        self.updateValues()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(714, 491)
        MainWindow.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 30, 671, 71))
        self.frame.setStyleSheet("border: 1px solid black;\n"
"background-color: rgb(220, 220, 220);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.label.setFont(font)
        self.label.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(10, 40, 91, 16))
        self.label_2.setStyleSheet("font-weight: bold;\n"
"border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.label_2.setObjectName("label_2")
        self.label_7 = QtWidgets.QLabel(self.frame)
        self.label_7.setGeometry(QtCore.QRect(150, 40, 81, 16))
        self.label_7.setStyleSheet("font-weight: bold;\n"
"border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.frame)
        self.label_8.setGeometry(QtCore.QRect(300, 40, 91, 16))
        self.label_8.setStyleSheet("font-weight: bold;\n"
"border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.frame)
        self.label_9.setGeometry(QtCore.QRect(460, 40, 111, 16))
        self.label_9.setStyleSheet("font-weight: bold;\n"
"border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.frame)
        self.label_10.setGeometry(QtCore.QRect(100, 40, 31, 16))
        self.label_10.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";\n"
"color: rgb(0, 0, 255);")
        self.label_10.setText("")
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.frame)
        self.label_11.setGeometry(QtCore.QRect(240, 40, 31, 16))
        self.label_11.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";\n"
"color: rgb(0, 0, 255);")
        self.label_11.setText("")
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.frame)
        self.label_12.setGeometry(QtCore.QRect(400, 40, 31, 16))
        self.label_12.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";\n"
"color: rgb(0, 0, 255);")
        self.label_12.setText("")
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.frame)
        self.label_13.setGeometry(QtCore.QRect(580, 40, 31, 16))
        self.label_13.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";\n"
"color: rgb(0, 0, 255);")
        self.label_13.setText("")
        self.label_13.setObjectName("label_13")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(30, 120, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.frame_2 = QtWidgets.QFrame(self.centralwidget)
        self.frame_2.setGeometry(QtCore.QRect(30, 150, 261, 291))
        self.frame_2.setStyleSheet("border: 1px solid black;")
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(10, 10, 82, 17))
        self.radioButton.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.radioButton.setCheckable(False)
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(70, 10, 82, 17))
        self.radioButton_2.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.radioButton_2.setCheckable(False)
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(130, 10, 82, 17))
        self.radioButton_3.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.radioButton_3.setCheckable(False)
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_4.setGeometry(QtCore.QRect(190, 10, 82, 17))
        self.radioButton_4.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";")
        self.radioButton_4.setCheckable(False)
        self.radioButton_4.setObjectName("radioButton_4")
        self.listWidget = QtWidgets.QListWidget(self.frame_2)
        self.listWidget.setGeometry(QtCore.QRect(20, 40, 221, 231))
        self.listWidget.setObjectName("listWidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(380, 120, 91, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setGeometry(QtCore.QRect(380, 150, 271, 291))
        self.frame_3.setStyleSheet("border: 1px solid black;")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.label_6 = QtWidgets.QLabel(self.frame_3)
        self.label_6.setGeometry(QtCore.QRect(20, 10, 71, 16))
        self.label_6.setStyleSheet("border: none;\n"
"font-family: \"Comic Sans MS\";\n"
"font-weight: bold;")
        self.label_6.setObjectName("label_6")
        self.label_16 = QtWidgets.QLabel(self.frame_3)
        self.label_16.setGeometry(QtCore.QRect(100, 10, 131, 16))
        self.label_16.setStyleSheet("border:none;\n"
"font-family: \"Comic Sans MS\";\n"
"color: rgb(0, 0, 255);")
        self.label_16.setText("")
        self.label_16.setObjectName("label_16")
        self.listWidget_2 = QtWidgets.QListWidget(self.frame_3)
        self.listWidget_2.setGeometry(QtCore.QRect(20, 40, 231, 231))
        self.listWidget_2.setObjectName("listWidget_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 270, 47, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(130, 120, 51, 16))
        self.label_14.setStyleSheet("font-family: \"Comic Sans MS\";\n"
"color: rgb(0, 0, 255);")
        self.label_14.setText("")
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(460, 120, 47, 16))
        self.label_15.setStyleSheet("font-family: \"Comic Sans MS\";\n"
"color: rgb(0, 0, 255);")
        self.label_15.setText("")
        self.label_15.setObjectName("label_15")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 714, 23))
        self.menubar.setObjectName("menubar")
        self.menuManage_Teams = QtWidgets.QMenu(self.menubar)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.menuManage_Teams.setFont(font)
        self.menuManage_Teams.setObjectName("menuManage_Teams")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNEW_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.actionNEW_Team.setFont(font)
        self.actionNEW_Team.setObjectName("actionNEW_Team")
        self.actionOPEN_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.actionOPEN_Team.setFont(font)
        self.actionOPEN_Team.setObjectName("actionOPEN_Team")
        self.actionSAVE_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.actionSAVE_Team.setFont(font)
        self.actionSAVE_Team.setObjectName("actionSAVE_Team")
        self.actionEVALUATE_Team = QtWidgets.QAction(MainWindow)
        font = QtGui.QFont()
        font.setFamily("Comic Sans MS")
        self.actionEVALUATE_Team.setFont(font)
        self.actionEVALUATE_Team.setObjectName("actionEVALUATE_Team")
        self.menuManage_Teams.addAction(self.actionNEW_Team)
        self.menuManage_Teams.addAction(self.actionOPEN_Team)
        self.menuManage_Teams.addAction(self.actionSAVE_Team)
        self.menuManage_Teams.addAction(self.actionEVALUATE_Team)
        self.menubar.addAction(self.menuManage_Teams.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        #Menu Item Actions
        self.actionNEW_Team.triggered.connect(self.createNewTeam)
        self.actionOPEN_Team.triggered.connect(self.openTeam)
        self.actionSAVE_Team.triggered.connect(self.saveTeam)
        self.actionEVALUATE_Team.triggered.connect(self.evalTeam)

        #Radio Button Click Events
        self.radioButton.clicked.connect(self.fetchPlayers)
        self.radioButton_2.clicked.connect(self.fetchPlayers)
        self.radioButton_3.clicked.connect(self.fetchPlayers)
        self.radioButton_4.clicked.connect(self.fetchPlayers)

        #Player Click Events
        self.listWidget.itemDoubleClicked.connect(self.moveItem)
        self.listWidget_2.itemDoubleClicked.connect(self.removeItem)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Fantasy Cricket"))
        self.label.setText(_translate("MainWindow", "Your Selections"))
        self.label_2.setText(_translate("MainWindow", "Batsman (BAT)"))
        self.label_7.setText(_translate("MainWindow", "Bowlers (BOW)"))
        self.label_8.setText(_translate("MainWindow", "Allrounders (AR)"))
        self.label_9.setText(_translate("MainWindow", "Wicket-keeper (WK)"))
        self.label_3.setText(_translate("MainWindow", "Points Available"))
        self.radioButton.setText(_translate("MainWindow", "BAT"))
        self.radioButton_2.setText(_translate("MainWindow", "BOW"))
        self.radioButton_3.setText(_translate("MainWindow", "AR"))
        self.radioButton_4.setText(_translate("MainWindow", "WK"))
        self.label_4.setText(_translate("MainWindow", "Points Used"))
        self.label_6.setText(_translate("MainWindow", "Team Name"))
        self.label_5.setText(_translate("MainWindow", ">"))
        self.menuManage_Teams.setTitle(_translate("MainWindow", "Manage Teams"))
        self.actionNEW_Team.setText(_translate("MainWindow", "NEW Team"))
        self.actionOPEN_Team.setText(_translate("MainWindow", "OPEN Team"))
        self.actionSAVE_Team.setText(_translate("MainWindow", "SAVE Team"))
        self.actionEVALUATE_Team.setText(_translate("MainWindow", "EVALUATE Team"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

