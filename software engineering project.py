import sys
import qtawesome as qta
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Main_window(QMainWindow):
    def __init__(self,role):
        QMainWindow.__init__(self)
        self.tempdata=['Training 1','Training 2','Training 3','Training 4','Training 5','Training 6','Training 7']
        if role == "hr":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             
            self.setWindowTitle("HR Assistant")
        elif role == "admin":
            self.setWindowTitle("Admin")
        else:
            self.setWindowTitle("Staff")
        self.widget = QWidget(self)
        self.title = QLabel(role)
        self.title.setStyleSheet("QLabel{font-size: 18pt;}")
        self.current = QLabel("DashBoard")
        self.current.setStyleSheet("QLabel{font-size: 18pt;}")

        if role == "admin":
            self.addbt = QPushButton('CREATE TRAINING')
            self.addbt.clicked.connect(self.createnewtraining)

        #scroll area
        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loaddashboard()

        self.windowscroll = QScrollArea()
        self.windowscroll.setMinimumSize(QSize(800,500))
        self.windowscroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.windowscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.windowscroll.setWidget(self.dashboardwid)
        self.windowscroll.setWidgetResizable(True)

        #content
        self.content = QVBoxLayout()
        self.content.addWidget(self.current)
        if role == "admin":
            self.content.addWidget(self.addbt)
        self.content.addWidget(self.windowscroll)

        #side menu
        icon = qta.icon("fa.angle-double-right")
        self.expandButton = QPushButton(icon,'')
        self.expandButton.setIconSize(QSize(35,35))
        self.expandButton.setFixedSize(50,50)
        self.expandButton.clicked.connect(self.expand)

        self.dashboardbt = QPushButton(qta.icon("ei.dashboard"),'')
        self.dashboardbt.setIconSize(QSize(35,35))
        self.dashboardbt.setFixedSize(50,50)
        self.dashboardbt.clicked.connect(self.dashboard)

        if role == "staff":
            self.trainingbt = QPushButton(qta.icon("fa5.list-alt"),'')
            self.trainingbt.setIconSize(QSize(35,35))
            self.trainingbt.setFixedSize(50,50)
            self.trainingbt.clicked.connect(self.training)

        if role == "hr":
            self.dropbt = QPushButton(qta.icon("mdi.account-remove"),'')
            self.dropbt.setIconSize(QSize(35,35))
            self.dropbt.setFixedSize(50,50)
            self.dropbt.clicked.connect(self.drop)

        self.historybt = QPushButton(qta.icon("msc.history"),'')
        self.historybt.setIconSize(QSize(35,35))
        self.historybt.setFixedSize(50,50)
        self.historybt.clicked.connect(self.history)

        self.accountButton = QPushButton(qta.icon("msc.account"),'')
        self.accountButton.setIconSize(QSize(35,35))
        self.accountButton.setFixedSize(50,50)
        self.accountButton.clicked.connect(self.account)

        self.logoutButton = QPushButton(qta.icon("ri.logout-box-r-line"),'')
        self.logoutButton.setIconSize(QSize(35,35))
        self.logoutButton.setFixedSize(50,50)
        self.logoutButton.clicked.connect(self.logout)

        self.sidemenuheader = QHBoxLayout()
        self.sidemenuheader.addWidget(self.title)
        self.title.setHidden(True)
        self.sidemenuheader.addWidget(self.expandButton)

        self.sidemenucontent = QVBoxLayout()
        self.sidemenucontent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidemenucontent.addWidget(self.dashboardbt)
        if role == "staff":
            self.sidemenucontent.addWidget(self.trainingbt)
        if role == "hr":
            self.sidemenucontent.addWidget(self.dropbt)
        self.sidemenucontent.addWidget(self.historybt)
        self.sidemenucontent.addStretch()

        self.sidemenufooter = QVBoxLayout()
        self.sidemenufooter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidemenufooter.addWidget(self.accountButton)
        self.sidemenufooter.addWidget(self.logoutButton)

        self.sidemenu = QVBoxLayout()
        self.sidemenu.addLayout(self.sidemenuheader,1)
        self.sidemenu.addLayout(self.sidemenucontent,100)
        self.sidemenu.addLayout(self.sidemenufooter,1)
        self.sidemenu.addStretch()

        #whole window
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.sidemenu,1)
        self.layout.addLayout(self.content,100)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def createnewtraining(self):
        self.addbt.hide()
        self.newtrainingname = QLabel('Training Name :')
        self.newtrainingnameinput = QLineEdit()

        self.newtrainingID = QLabel('Training ID :')
        self.newtrainingIDinput = QLineEdit()

        self.newtrainingDate = QLabel('Date :')
        self.newtrainingDateinput = QLineEdit()

        self.newtrainingTime = QLabel('Time :')
        self.newtrainingTimeinput = QLineEdit()

        self.newtrainingVenue = QLabel('Venue :')
        self.newtrainingVenueinput = QLineEdit()

        self.newtrainingCost = QLabel('Cost :')
        self.newtrainingCostinput = QLineEdit()

        self.newtrainingMaxPar = QLabel('Maximum Participants :')
        self.newtrainingMaxParinput = QLineEdit()

        self.newtrainingimage = QLabel('Add Image :')
        self.newtrainingimageinput = QFileDialog()

        self.newtrainingdepartment = QLabel('Add Department :')
        self.newtrainingdepartmentinput = QComboBox()
        self.newtrainingdepartmentinput.addItems(['test1','test2','test3'])

        self.newtraininginfo = QGridLayout()
        self.newtraininginfo.addWidget(self.newtrainingname,0,0)
        self.newtraininginfo.addWidget(self.newtrainingnameinput,0,1)
        self.newtraininginfo.addWidget(self.newtrainingID,1,0)
        self.newtraininginfo.addWidget(self.newtrainingIDinput,1,1)
        self.newtraininginfo.addWidget(self.newtrainingDate,2,0)
        self.newtraininginfo.addWidget(self.newtrainingDateinput,2,1)
        self.newtraininginfo.addWidget(self.newtrainingTime,3,0)
        self.newtraininginfo.addWidget(self.newtrainingTimeinput,3,1)
        self.newtraininginfo.addWidget(self.newtrainingVenue,4,0)
        self.newtraininginfo.addWidget(self.newtrainingVenueinput,4,1)
        self.newtraininginfo.addWidget(self.newtrainingCost,5,0)
        self.newtraininginfo.addWidget(self.newtrainingCostinput,5,1)
        self.newtraininginfo.addWidget(self.newtrainingMaxPar,6,0)
        self.newtraininginfo.addWidget(self.newtrainingMaxParinput,6,1)
        self.newtraininginfo.addWidget(self.newtrainingimage,7,0,Qt.AlignmentFlag.AlignTop)
        self.newtraininginfo.addWidget(self.newtrainingimageinput,7,1)
        self.newtraininginfo.addWidget(self.newtrainingdepartment,8,0)
        self.newtraininginfo.addWidget(self.newtrainingdepartmentinput,8,1)

        self.cancel = QPushButton('Cancel')
        self.cancel.setFixedWidth(150)
        self.cancel.clicked.connect(self.dashboard)
        self.addnew = QPushButton('ADD')
        self.addnew.setFixedWidth(150)

        self.addnewtrainingbutton = QHBoxLayout()
        self.addnewtrainingbutton.addWidget(self.cancel)
        self.addnewtrainingbutton.addWidget(self.addnew)
        self.addnewtrainingbutton.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.addnewtrainingwin = QWidget()
        self.addnewtrainingwindow = QVBoxLayout(self.addnewtrainingwin)
        self.addnewtrainingwindow.addLayout(self.newtraininginfo)
        self.addnewtrainingwindow.addLayout(self.addnewtrainingbutton)

        self.windowscroll.setWidget(self.addnewtrainingwin)
        print("bill")

    def loaddashboard(self): 
        for temp in self.tempdata:
            self.dashboardwindow.addLayout(self.createtrainingbt(temp))

    def createtrainingbt(self,training):
        temppic = QVBoxLayout()
        picbt = QPushButton(qta.icon('fa5s.images'),'')
        picbt.setFixedSize(250,250)
        picbt.setIconSize(QSize(50,50))
        temppic.addWidget(picbt)

        t_title = QLabel(training)
        tempcontent = QVBoxLayout()
        tempcontent.setAlignment(Qt.AlignmentFlag.AlignTop)
        tempcontent.addWidget(t_title)
        tempcontent.addStretch()

        tempbtsection = QHBoxLayout()
        tempbtsection.setAlignment(Qt.AlignmentFlag.AlignRight)
        if role == 'admin':
            editbt = QPushButton("edit")
            editbt.setFixedSize(100,25)
            removebt = QPushButton("remove")
            removebt.setFixedSize(100,25)
            tempbtsection.addWidget(editbt)
            tempbtsection.addWidget(removebt)
        if role == 'hr':
            requestbt = QPushButton("request")
            requestbt.setFixedSize(100,25)
            tempbtsection.addWidget(requestbt)
        if role == 'staff':
            registerbt = QPushButton("register")
            registerbt.setFixedSize(100,25)
            tempbtsection.addWidget(registerbt)

        tempcontentsection = QVBoxLayout()
        tempcontentsection.addLayout(tempcontent)
        tempcontentsection.addLayout(tempbtsection)
        
        temp = QHBoxLayout()
        temp.addLayout(temppic)
        temp.addLayout(tempcontentsection)

        return temp
    
    def dashboard(self):
        self.current.setText("DashBoard")
        if role == "admin":
            self.addbt.show()
        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loaddashboard()
        self.dashboardwindow.setAlignment(Qt.AlignmentFlag.AlignTop)

        #set scroll area widget
        self.windowscroll.setWidget(self.dashboardwid)
        print("Bill")
    
    def training(self):
        self.current.setText("Training")
        print("Bill")

    def drop(self):
        self.current.setText("Drop")
        print("Bill")

    def history(self):
        self.current.setText("History")
        if role == "admin":
            self.addbt.hide()
        self.bill = QWidget()
        self.billy = QVBoxLayout(self.bill)
        ding = QLabel("Billy")
        self.billy.addWidget(ding)
        self.billy.setAlignment(Qt.AlignmentFlag.AlignTop)

        #set scroll area widget
        self.windowscroll.setWidget(self.bill)
        print("Bill")

    def account(self):
        if role == "admin":
            self.addbt.hide()
        self.current.setText("Account")
        print("Bill")

    def logout(self):
        self.current.setText("Logout")
        print("Bill")

    def expand(self):
        self.expandButton.clicked.disconnect()
        self.expandButton.setIcon(qta.icon("fa.angle-double-left"))
        self.dashboardbt.setFixedSize(200, 50)
        self.dashboardbt.setStyleSheet("QPushButton { text-align: left;}")
        self.dashboardbt.setText("DashBoard")
        if role == "staff":
            self.trainingbt.setFixedSize(200, 50)
            self.trainingbt.setStyleSheet("QPushButton { text-align: left;}")
            self.trainingbt.setText("Training List")
        if role == "hr":
            self.dropbt.setFixedSize(200, 50)
            self.dropbt.setStyleSheet("QPushButton { text-align: left;}")
            self.dropbt.setText("Drop Participant")
        self.historybt.setFixedSize(200, 50)
        self.historybt.setStyleSheet("QPushButton { text-align: left;}")
        self.historybt.setText("History")
        self.accountButton.setFixedSize(200, 50)
        self.accountButton.setStyleSheet("QPushButton { text-align: left;}")
        self.accountButton.setText("Account")
        self.logoutButton.setFixedSize(200, 50)
        self.logoutButton.setStyleSheet("QPushButton { text-align: left;}")
        self.logoutButton.setText("Logout")
        self.title.show()
        self.expandButton.clicked.connect(self.contract)

    def contract(self):
        self.expandButton.clicked.disconnect()
        self.expandButton.setIcon(qta.icon("fa.angle-double-right"))
        self.dashboardbt.setFixedSize(50, 50)
        self.dashboardbt.setStyleSheet("QPushButton { text-align: center;}")
        self.dashboardbt.setText("")
        if role == "staff":
            self.trainingbt.setFixedSize(50, 50)
            self.trainingbt.setStyleSheet("QPushButton { text-align: center;}")
            self.trainingbt.setText("")
        if role == "hr":
            self.dropbt.setFixedSize(50, 50)
            self.dropbt.setStyleSheet("QPushButton { text-align: center;}")
            self.dropbt.setText("")
        self.historybt.setFixedSize(50, 50)
        self.historybt.setStyleSheet("QPushButton { text-align: center;}")
        self.historybt.setText("")
        self.accountButton.setFixedSize(50, 50)
        self.accountButton.setStyleSheet("QPushButton { text-align: center;}")
        self.accountButton.setText("")
        self.logoutButton.setFixedSize(50, 50)
        self.logoutButton.setStyleSheet("QPushButton { text-align: center;}")
        self.logoutButton.setText("")
        self.title.setHidden(True)
        self.expandButton.clicked.connect(self.expand)


if __name__ == '__main__':
    role = input("Enter Role")
    app = QApplication(sys.argv)
    window = Main_window(role)
    window.show()
    sys.exit(app.exec())