import sys
import re
import qtawesome as qta
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *

class Main_window(QMainWindow):
    def __init__(self,role):
        QMainWindow.__init__(self)#role is department
        #update database data and load data
        self.credential = ['ID','101WIZARD','011-10533650','jqgammers@gmail.com',role,'']
        self.tempdata=[['Admin', 'T104', '23Dec2025', '03.04', 'Hall A', '3000', '', '30', None,'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .'],
                       ['Bill', 'T105', '23Dec2024', '04.05', 'Hall B', '30000', '', '30', None,'Cybersecurity is the practice of protecting critical systems and sensitive information from digital attacks. In this training, participants will learn about different types of cyber attacks, acquire knowledge and skills to protect digital systems, networks, and data from unauthorized access and involve in hands-on practical activities.'],
                       ['MARKETING', 'T103', '6/24/2023', '10.00 AM', 'Alpha Enterprise Conference Hall', '2000', '', '45', None, 'Marketing is the activity of promoting, market researching and advertising of products or services. In this training, participants will learn about market research, consumer behaviour, branding, advertising and digital marketing strategies, involve in interactive sessions to study the real-world case studies,  gain insight into promoting and building the digital platforms and apply data analytics skills to implement the marketing plans.'],
                       ['Hill', 'T110', '23Dec2025', '03.04', 'Hall A', '3000', '', '30', None,'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .'],
                       ['Gill', 'T109', '23Dec2025', '03.04', 'Hall A', '3000', '', '30', None,'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .'],
                       ['Mill', 'T145', '23Dec2025', '03.04', 'Hall A', '3000', '', '30', None,'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .'],
                       ['Fuck You', 'T123', '23Dec2025', '03.04', 'Hall A', '3000', '', '30', None,'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .']]
        if role == "hr":                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            self.setWindowTitle("HR Assistant")
            self.registereddata=[['T104','S101'],['T104','S102'],['T105','S101']]
            self.approveddata=[['T105','S104','HRID']]
            self.rejecteddata=[['T103','S104','HRID']]
            self.stafflist = [['S101','NAME1','011-134500234','IT STAFF'],
                              ['S102','NAME2','012-136880234','DP STAFF'],
                              ['S103','NAME3','012-134500091','AP STAFF'],
                              ['S104','NAME4','016-134500235','IT STAFF']]
        elif role == "admin":
            self.setWindowTitle("Admin")
            self.addedtrainingdata = [['AID','T104','01Dec2025']]
            self.edittrainingdata = [['AID','TID','20Dec2025']]
            self.removetrainingdata = [['AID','21Dec2025','Dill', 'T111', '23Dec2025', '03.04', 'Hall A', '3000', '', '30', None,'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .']]
        else:
            self.setWindowTitle("Staff")
            self.registereddata=[['T104','SID']]
            self.approveddata=[['T105','SID','HRID']]
            self.rejecteddata=[['T103','SID','HRID'],['T167','SID','HRID']]
            self.done=[['T111','SID','HRID']]
            self.ongoing = [['Akau', 'T167', '23Dec2025', '03.04', 'Hall A', '3000', '', '30', None,'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .']]
            self.completed = [['Dill', 'T111', '23Dec2025', '03.04', 'Hall A', '3000', '', '30', None,'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .']]
        
        self.widget = QWidget(self)
        self.title = QLabel(role)
        self.title.setStyleSheet("QLabel{font-size: 18pt;}")
        self.current = QLabel("DashBoard")
        self.current.setStyleSheet("QLabel{font-size: 18pt;}")

        #specific role button
        if role == "admin":
            #dashboard
            self.addbt = QPushButton('CREATE TRAINING')
            self.addbt.setFixedWidth(150)
            self.addbt.clicked.connect(self.createnewtraining)

            #history
            self.addedbt = QPushButton('Added Training')
            self.addedbt.setFixedSize(150, 35)
            self.addedbt.clicked.connect(self.adminAdded)
            self.addedbt.hide()
            self.modifiedbt =QPushButton('Modified Training')
            self.modifiedbt.setFixedSize(150, 35)
            self.modifiedbt.clicked.connect(self.adminModify)
            self.modifiedbt.hide()
            self.removebt = QPushButton('Remove Training')
            self.removebt.setFixedSize(150, 35)
            self.removebt.clicked.connect(self.adminRemove)
            self.removebt.hide()

        if role == 'hr':
            self.approvebt = QPushButton('Approved Participant')
            self.approvebt.setFixedSize(150, 35)
            self.approvebt.clicked.connect(self.hrApprove)
            self.approvebt.hide()
            self.rejectbt = QPushButton('Rejected Participant')
            self.rejectbt.setFixedSize(150, 35)
            self.rejectbt.clicked.connect(self.hrReject)
            self.rejectbt.hide()

        if role == 'staff':
            self.completedbt = QPushButton('Completed Training')
            self.completedbt.setFixedSize(150, 35)
            self.completedbt.clicked.connect(self.staffcomplete)
            self.completedbt.hide()
            self.rejectedbt = QPushButton('Rejected Request')
            self.rejectedbt.setFixedSize(150, 35)
            self.rejectedbt.clicked.connect(self.staffreject)
            self.rejectedbt.hide()
            self.pendingbt = QPushButton('Pending')
            self.pendingbt.setFixedSize(150, 35)
            self.pendingbt.clicked.connect(self.loadpending)
            self.pendingbt.hide()
            self.approvebt = QPushButton('Approved')
            self.approvebt.setFixedSize(150, 35)
            self.approvebt.clicked.connect(self.loadapprove)
            self.approvebt.hide()
            self.ongoingbt = QPushButton('Ongoing')
            self.ongoingbt.setFixedSize(150, 35)
            self.ongoingbt.clicked.connect(self.loadongoing)
            self.ongoingbt.hide()

        #additional validation lists
        if role == "admin" or role == 'staff':
            self.filterlist = []
        
        #scroll area
        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loaddashboard()
        self.dashboardwindow.addStretch()

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
            temp = QHBoxLayout()
            temp.addWidget(self.addbt)
            temp.addWidget(self.addedbt)
            temp.addWidget(self.modifiedbt)
            temp.addWidget(self.removebt)
            temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.content.addLayout(temp)
        if role == "hr":
            temp = QHBoxLayout()
            temp.addWidget(self.approvebt)
            temp.addWidget(self.rejectbt)
            temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.content.addLayout(temp)
        if role == "staff":
            temp = QHBoxLayout()
            temp.addWidget(self.completedbt)
            temp.addWidget(self.rejectedbt)
            temp.addWidget(self.pendingbt)
            temp.addWidget(self.approvebt)
            temp.addWidget(self.ongoingbt)
            temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.content.addLayout(temp)
        self.content.addWidget(self.windowscroll)

        #side menu
        icon = qta.icon("fa.angle-double-right")
        self.expandButton = QPushButton(icon,'')
        self.expandButton.setIconSize(QSize(35,35))
        self.expandButton.setFixedSize(50,50)
        self.expandButton.clicked.connect(self.expand)

        #dashboard button
        self.dashboardbt = QPushButton(qta.icon("ei.dashboard"),'')
        self.dashboardbt.setIconSize(QSize(35,35))
        self.dashboardbt.setFixedSize(50,50)
        self.dashboardbt.clicked.connect(self.dashboard)

        #training list button
        if role == "staff":
            self.trainingbt = QPushButton(qta.icon("fa5.list-alt"),'')
            self.trainingbt.setIconSize(QSize(35,35))
            self.trainingbt.setFixedSize(50,50)
            self.trainingbt.clicked.connect(self.training)

        #historybutton
        self.historybt = QPushButton(qta.icon("msc.history"),'')
        self.historybt.setIconSize(QSize(35,35))
        self.historybt.setFixedSize(50,50)
        self.historybt.clicked.connect(self.history)

        #profile button
        if self.credential[5] != '':
            t_img = QPixmap(self.credential[5])
            if t_img.width() > t_img.height():
                trans = t_img.copy((t_img.width()/4),0,t_img.width(),t_img.width())
            if t_img.height() > t_img.width():
                trans = t_img.copy(0,(t_img.height()/4),t_img.width(),t_img.width())
            if t_img.height == t_img.width():
                trans = t_img
            t_image = QIcon(trans)

        if self.credential[5] != '':
            self.accountButton = QPushButton(t_image,'')
            self.accountButton.setIconSize(QSize(35,35)) 
        else:
            self.accountButton = QPushButton(qta.icon("msc.account"),'')
            self.accountButton.setIconSize(QSize(35,35)) 
        self.accountButton.setFixedSize(50,50)
        self.accountButton.clicked.connect(self.account)

        #logout button
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

    #dashboard
    #admin
    def selectimage(self):
        fname = QFileDialog.getOpenFileNames(self, 'Select Images','','Image files (*.png *.jpg *.jpeg *.xpm *.bmp *.pdf)')
        flist = str(fname).rsplit(',')
        fpath = flist[0]
        fpath = fpath.lstrip("(['")
        fpath = fpath.rstrip("']")
        self.newtrainingimagepath.setText(fpath)

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
        self.newtrainingimageinput = QPushButton('Select Image')
        self.newtrainingimageinput.clicked.connect(self.selectimage)
        self.newtrainingimagepath = QLineEdit()
        self.newtrainingimagepath.setDisabled(True)

        self.newtrainingdepartment = QLabel('Add Department :')
        self.newtrainingdepartmentinput = QComboBox()
        self.newtrainingdepartmentinput.addItems(['test1','test2','test3'])

        self.newtrainingdescription = QLabel('Description :')
        self.newtrainingdescriptioninput = QLineEdit()

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
        self.newtraininginfo.addWidget(self.newtrainingimage,7,0)
        img = QVBoxLayout()
        img.addWidget(self.newtrainingimageinput)
        img.addWidget(self.newtrainingimagepath)
        self.newtraininginfo.addLayout(img,7,1)
        self.newtraininginfo.addWidget(self.newtrainingdepartment,8,0)
        self.newtraininginfo.addWidget(self.newtrainingdepartmentinput,8,1)
        self.newtraininginfo.addWidget(self.newtrainingdescription,9,0)
        self.newtraininginfo.addWidget(self.newtrainingdescriptioninput,9,1)

        self.cancel = QPushButton('Cancel')
        self.cancel.setFixedWidth(150)
        self.cancel.clicked.connect(self.dashboard)
        self.addnew = QPushButton('ADD')
        self.addnew.setFixedWidth(150)
        self.addnew.clicked.connect(self.created)

        self.addnewtrainingbutton = QHBoxLayout()
        self.addnewtrainingbutton.addWidget(self.cancel)
        self.addnewtrainingbutton.addWidget(self.addnew)
        self.addnewtrainingbutton.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.addnewtrainingwin = QWidget()
        self.addnewtrainingwindow = QVBoxLayout(self.addnewtrainingwin)
        self.addnewtrainingwindow.addLayout(self.newtraininginfo)
        self.addnewtrainingwindow.addLayout(self.addnewtrainingbutton)
        self.addnewtrainingwindow.addStretch()

        self.windowscroll.setWidget(self.addnewtrainingwin)

    def created(self):
        t_title = self.newtrainingnameinput.text()
        t_ID = self.newtrainingIDinput.text()
        t_Date = self.newtrainingDateinput.text()
        t_Time = self.newtrainingTimeinput.text()
        t_Venue = self.newtrainingVenueinput.text()
        t_Cost = self.newtrainingCostinput.text()
        t_img = self.newtrainingimagepath.text()
        t_MaxPar = self.newtrainingMaxParinput.text()
        t_dep = self.newtrainingdepartmentinput.currentData()
        t_description = self.newtrainingdescriptioninput.text()
        self.tempdata.append([t_title,t_ID,t_Date,t_Time,t_Venue,t_Cost,t_img,t_MaxPar,t_dep,t_description])
        self.dashboard()

    def edittraining(self,id):
        count = 0
        for button in self.editbtgroup.buttons():
            print(button)
            print(id)
            if button != id:
                count+=1
            else:
                break

        if self.filterlist == []:
            self.data = self.dashboarddata[count]
        else:
            for i in self.tempdata:
                if self.filterlist[count] == i[1]:
                    self.data = i
                    break

        self.addbt.hide()
        self.newtrainingname = QLabel('Training Name :')
        self.newtrainingnameinput = QLineEdit()
        self.newtrainingnameinput.setText(self.data[0])

        self.newtrainingID = QLabel('Training ID :')
        self.newtrainingIDinput = QLineEdit()
        self.newtrainingIDinput.setText(self.data[1])

        self.newtrainingDate = QLabel('Date :')
        self.newtrainingDateinput = QLineEdit()
        self.newtrainingDateinput.setText(self.data[2])

        self.newtrainingTime = QLabel('Time :')
        self.newtrainingTimeinput = QLineEdit()
        self.newtrainingTimeinput.setText(self.data[3])

        self.newtrainingVenue = QLabel('Venue :')
        self.newtrainingVenueinput = QLineEdit()
        self.newtrainingVenueinput.setText(self.data[4])

        self.newtrainingCost = QLabel('Cost :')
        self.newtrainingCostinput = QLineEdit()
        self.newtrainingCostinput.setText(self.data[5])

        self.newtrainingMaxPar = QLabel('Maximum Participants :')
        self.newtrainingMaxParinput = QLineEdit()
        self.newtrainingMaxParinput.setText(self.data[7])

        self.newtrainingimage = QLabel('Add Image :')
        self.newtrainingimageinput = QPushButton('Select Image')
        self.newtrainingimageinput.clicked.connect(self.selectimage)
        self.newtrainingimagepath = QLineEdit()
        self.newtrainingimagepath.setDisabled(True)
        self.newtrainingimagepath.setText(self.data[6])

        self.newtrainingdepartment = QLabel('Add Department :')
        self.newtrainingdepartmentinput = QComboBox()
        self.newtrainingdepartmentinput.addItems(['test1','test2','test3'])

        self.newtrainingdescription = QLabel('Description :')
        self.newtrainingdescriptioninput = QLineEdit()
        self.newtrainingdescriptioninput.setText(self.data[9])

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
        self.newtraininginfo.addWidget(self.newtrainingimage,7,0)
        img = QVBoxLayout()
        img.addWidget(self.newtrainingimageinput)
        img.addWidget(self.newtrainingimagepath)
        self.newtraininginfo.addLayout(img,7,1)
        self.newtraininginfo.addWidget(self.newtrainingdepartment,8,0)
        self.newtraininginfo.addWidget(self.newtrainingdepartmentinput,8,1)
        self.newtraininginfo.addWidget(self.newtrainingdescription,9,0)
        self.newtraininginfo.addWidget(self.newtrainingdescriptioninput,9,1)

        cancel = QPushButton('Cancel')
        cancel.setFixedWidth(150)
        cancel.clicked.connect(self.dashboard)

        save = QPushButton('Save')
        save.setFixedWidth(150)
        save.clicked.connect(self.saveedit)

        self.addnewtrainingbutton = QHBoxLayout()
        self.addnewtrainingbutton.addWidget(cancel)
        self.addnewtrainingbutton.addWidget(save)
        self.addnewtrainingbutton.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.addnewtrainingwin = QWidget()
        self.addnewtrainingwindow = QVBoxLayout(self.addnewtrainingwin)
        self.addnewtrainingwindow.addLayout(self.newtraininginfo)
        self.addnewtrainingwindow.addLayout(self.addnewtrainingbutton)
        self.addnewtrainingwindow.addStretch()

        self.windowscroll.setWidget(self.addnewtrainingwin)

    def saveedit(self):
        t_title = self.newtrainingnameinput.text()
        t_ID = self.newtrainingIDinput.text()
        t_Date = self.newtrainingDateinput.text()
        t_Time = self.newtrainingTimeinput.text()
        t_Venue = self.newtrainingVenueinput.text()
        t_Cost = self.newtrainingCostinput.text()
        t_img = self.newtrainingimagepath.text()
        t_MaxPar = self.newtrainingMaxParinput.text()
        t_dep = self.newtrainingdepartmentinput.currentData()
        t_description = self.newtrainingdescriptioninput.text()
        for temp in self.tempdata:
            if self.data == temp:
                self.tempdata.remove(temp)
                self.tempdata.append([t_title,t_ID,t_Date,t_Time,t_Venue,t_Cost,t_img,t_MaxPar,t_dep,t_description])
                print(temp)
        self.dashboard()

    def removetraining(self,id):
        count = 0
        for button in self.removebtgroup.buttons():
            print(button)
            print(id)
            if button != id:
                count+=1
            else:
                break

        if self.filterlist == []:
            self.data = self.dashboarddata[count]
        else:
            for i in self.tempdata:
                if self.filterlist[count] == i[1]:
                    self.data = i
                    break

        for temp in self.tempdata:
            if self.data == temp:
                self.tempdata.remove(temp)
                print(temp)  

        #load window
        self.dashboard()    
 
    #staff
    def register(self,id):#incomplete
        count = 0
        for button in self.registerbtgroup.buttons():
            if button != id:
                count+=1
            else:
                break

        if self.filterlist == []:
            self.data = self.dashboarddata[count]
        else:
            for i in self.tempdata:
                if self.filterlist[count] == i[1]:
                    self.data = i
                    break
        self.registereddata.append([self.data[1],'ID'])

        self.dashboard()   

    #hr
    def request(self,id):
        count = 0
        for button in self.requestbtgroup.buttons():
            if button != id:
                count+=1
            else:
                break

        self.data = self.dashboarddata[count]

        self.current.setText(self.data[1]+" : "+self.data[0])

        y = 0
        label = QLabel()
        label.setText("List or requester")
        temp = []
        for request in self.registereddata:
            if request[0] == self.data[1]:
                for staff in self.stafflist:
                    if staff[0] == request[1]:
                        temp.append(staff)
                        break
        self.checkbuttongroup = []

        no = QLabel()
        no.setText("No")
        sid = QLabel()
        sid.setText("Staff ID")
        sname = QLabel()
        sname.setText("Name")
        phone = QLabel()
        phone.setText("Phone")
        dep = QLabel()
        dep.setText("Department")
        self.checkall = QPushButton('Check All')
        self.checkall.setFixedWidth(150)
        self.checkall.clicked.connect(self.check_all_bt)
        self.requestlist = QGridLayout()
        self.requestlist.addWidget(no,y,0)
        self.requestlist.addWidget(sid,y,1)
        self.requestlist.addWidget(sname,y,2)
        self.requestlist.addWidget(phone,y,3)
        self.requestlist.addWidget(dep,y,4)
        self.requestlist.addWidget(self.checkall,y,5)
        y+=1
        
        for reqlist in temp:
            checkbutton = QCheckBox()
            checkbutton.setAutoExclusive(True)
            no = QLabel()
            no.setText(str(y))
            sid = QLabel()
            sid.setText(reqlist[0])
            sname = QLabel()
            sname.setText(reqlist[1])
            phone = QLabel()
            phone.setText(reqlist[2])
            dep = QLabel()
            dep.setText(reqlist[3])
            self.requestlist.addWidget(no,y,0)
            self.requestlist.addWidget(sid,y,1)
            self.requestlist.addWidget(sname,y,2)
            self.requestlist.addWidget(phone,y,3)
            self.requestlist.addWidget(dep,y,4)
            y+=1
        
        for i in range(0, y-1):
            self.checkbuttongroup.append('')

        for i,v in enumerate(self.checkbuttongroup):
            self.checkbuttongroup[i] = QCheckBox(v)
            if self.checkbuttongroup[i].isChecked():
                print("True")
            self.requestlist.addWidget(self.checkbuttongroup[i],(i+1),5,Qt.AlignmentFlag.AlignHCenter)

        approve = QPushButton('Approve')
        approve.setFixedWidth(150)
        approve.clicked.connect(self.approve)

        reject = QPushButton('Reject')
        reject.setFixedWidth(150)
        reject.clicked.connect(self.reject)

        self.requestwindowbtsection = QHBoxLayout()
        self.requestwindowbtsection.addWidget(approve)
        self.requestwindowbtsection.addWidget(reject)
        self.requestwindowbtsection.setAlignment(Qt.AlignmentFlag.AlignRight)

        self.reqlistwid = QWidget()
        self.requestwindow = QVBoxLayout(self.reqlistwid)
        self.requestwindow.addWidget(label)
        self.requestwindow.addLayout(self.requestlist)
        self.requestwindow.addLayout(self.requestwindowbtsection)
        self.requestwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.requestwindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(self.reqlistwid)

    def check_all_bt(self):
        for i in self.checkbuttongroup:
            if i.isChecked():
                print('True')
            else:
                print('False')
                i.setChecked(True)

    def approve(self):
        checkedarray = []
        for i,v in enumerate(self.checkbuttongroup):
            if v.isChecked():
                checkedarray.append(i)
        temp = []
        for request in self.registereddata:
            if request[0] == self.data[1]:
                for staff in self.stafflist:
                    if staff[0] == request[1]:
                        temp.append(request)
                        break
        for i in checkedarray:
            for request in self.registereddata:
                if temp[i] == request:
                    self.registereddata.remove(request)
                    request.append('HRID')
                    self.approveddata.append(request)
        print(self.registereddata)
        print(self.approveddata)

        self.dashboard()

    def reject(self):
        checkedarray = []
        for i,v in enumerate(self.checkbuttongroup):
            if v.isChecked():
                checkedarray.append(i)
        temp = []
        for request in self.registereddata:
            if request[0] == self.data[1]:
                for staff in self.stafflist:
                    if staff[0] == request[1]:
                        temp.append(request)
                        break
        for i in checkedarray:
            for request in self.registereddata:
                if temp[i] == request:
                    self.registereddata.remove(request)
                    request.append('HRID')
                    self.rejecteddata.append(request)
        print(self.registereddata)
        print(self.rejecteddata)

        self.dashboard()

    #general
    def loaddashboard(self): 
        self.dashboarddata = []
        count = 0
        if role == 'admin':
            self.editbtgroup = QButtonGroup()
            self.removebtgroup = QButtonGroup()
            for temp in self.tempdata:
                self.dashboarddata.append(temp)
        if role == 'hr':
            self.requestbtgroup = QButtonGroup()
            for tempa in self.registereddata:
                for temp in self.tempdata:
                    if temp[1] == tempa[0]:
                        if self.dashboarddata == []:
                            self.dashboarddata.append(temp)
                        else:
                            for tempb in self.dashboarddata:
                                if tempb == temp:
                                    break
                                else:
                                    self.dashboarddata.append(temp)
        if role == 'staff':
            self.registerbtgroup = QButtonGroup()
            for temp in self.tempdata:
                self.dashboarddata.append(temp)
            for tempa in self.registereddata:
                for temp in self.dashboarddata:
                    if temp[1] == tempa [0]:
                        self.dashboarddata.remove(temp)
            for tempa in self.approveddata:
                for temp in self.dashboarddata:
                    if temp[1] == tempa [0]:
                        self.dashboarddata.remove(temp)
            for tempa in self.rejecteddata:
                for temp in self.dashboarddata:
                    if temp[1] == tempa [0]:
                        self.dashboarddata.remove(temp)

        if role == 'admin' or role == 'staff':
            self.filterinput = QLineEdit()
            filterbt = QPushButton(qta.icon('mdi.filter-outline'),'Filter')
            filterbt.clicked.connect(self.filter)
            filtersection = QHBoxLayout()
            filtersection.addWidget(self.filterinput)
            filtersection.addWidget(filterbt)

            self.dashboardwindow.addLayout(filtersection)

        for temp in self.dashboarddata:
            self.dashboardwindow.addLayout(self.createtrainingbt(temp,count))
            self.dashboardwindow.addStretch()
            count+=1
            
        if role == 'admin':
            self.editbtgroup.buttonClicked.connect(self.edittraining)
            self.removebtgroup.buttonClicked.connect(self.removetraining)
        if role == 'hr':
            self.requestbtgroup.buttonClicked.connect(self.request)
        if role == 'staff':
            self.registerbtgroup.buttonClicked.connect(self.register)
            
    def createtrainingbt(self,training,count):
        t_title = QLabel(training[0])
        t_ID = QLabel(training[1])
        t_Date = QLabel(training[2])
        t_Time = QLabel(training[3])
        t_Venue = QLabel(training[4])
        t_Cost = QLabel(training[5])
        t_MaxPar = QLabel(training[7])
        t_description = QLabel(training[9])

        t_description.setWordWrap(True)

        if training[6] != '':
            t_img = QPixmap(training[6])
            if t_img.width() > t_img.height():
                trans = t_img.copy((t_img.width()/4),0,t_img.width(),t_img.width())
            if t_img.height() > t_img.width():
                trans = t_img.copy(0,(t_img.height()/4),t_img.width(),t_img.width())
            if t_img.height == t_img.width():
                trans = t_img
            t_image = QIcon(trans)

        temppic = QVBoxLayout()
        if training[6] != '':
            picbt = QPushButton(t_image,'')
            picbt.setIconSize(QSize(240,240))
        else:
            picbt = QPushButton(qta.icon('ph.image'),'')
            picbt.setIconSize(QSize(50,50))
        picbt.setFixedSize(250,250)
        temppic.addWidget(picbt)
        
        tempcontent = QVBoxLayout()
        tempcontent.setAlignment(Qt.AlignmentFlag.AlignTop)
        tempcontent.addWidget(t_title)
        tempcontent.addWidget(t_ID)
        tempcontent.addWidget(t_Date)
        tempcontent.addWidget(t_Time)
        tempcontent.addWidget(t_Venue)
        tempcontent.addWidget(t_Cost)
        tempcontent.addWidget(t_MaxPar)
        tempcontent.addWidget(t_description)
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
            self.editbtgroup.addButton(editbt,count)
            self.removebtgroup.addButton(removebt,count)
        if role == 'hr':
            requestbt = QPushButton("request")
            requestbt.setFixedSize(100,25)
            self.requestbtgroup.addButton(requestbt,count)
            tempbtsection.addWidget(requestbt)
        if role == 'staff':
            registerbt = QPushButton("register")
            registerbt.setFixedSize(100,25)
            self.registerbtgroup.addButton(registerbt,count)
            tempbtsection.addWidget(registerbt)
            
        tempcontentsection = QVBoxLayout()
        tempcontentsection.addLayout(tempcontent)
        tempcontentsection.addLayout(tempbtsection)
        
        temp = QHBoxLayout()
        temp.addLayout(temppic)
        temp.addLayout(tempcontentsection)

        return temp
    
    def filter(self):
        self.filterlist = []
        pattern = ".*"+self.filterinput.text()+".*"
        self.filterlist = [x[1] for x in self.dashboarddata if re.match(pattern,x[1])]

        print(self.filterlist)

        filterbt = QPushButton(qta.icon('mdi.filter-outline'),'Filter')
        filterbt.clicked.connect(self.filter)
        filtersection = QHBoxLayout()
        filtersection.addWidget(self.filterinput)
        filtersection.addWidget(filterbt)

        if role == 'admin':
            self.editbtgroup = QButtonGroup()
            self.removebtgroup = QButtonGroup()
        if role == 'staff':
            self.registerbtgroup = QButtonGroup()

        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.dashboardwindow.addLayout(filtersection)

        count = 0
        for temp in self.filterlist:
            for tempa in self.tempdata:
                if temp == tempa[1]:
                    self.dashboardwindow.addLayout(self.createtrainingbt(tempa,count))
                    self.dashboardwindow.addStretch()
                    count+=1
            
        if role == 'admin':
            self.editbtgroup.buttonClicked.connect(self.edittraining)
            self.removebtgroup.buttonClicked.connect(self.removetraining)
        if role == 'staff':
            self.registerbtgroup.buttonClicked.connect(self.register)

        self.dashboardwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.dashboardwindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(self.dashboardwid)

    #training
    #only staff
    def loadpending(self):
        TrainingNoTitle = QLabel("No.")
        TrainingID = QLabel("Training ID")
        TrainingTitle = QLabel("Training Title")
        TrainingDate = QLabel("Date")
        TrainingTime = QLabel("Time")
        TrainingVenue = QLabel("Venue")

        pendingdetials = QGridLayout()
        pendingdetials.addWidget(TrainingNoTitle,0,0)
        pendingdetials.addWidget(TrainingID,0,1)
        pendingdetials.addWidget(TrainingTitle,0,2)
        pendingdetials.addWidget(TrainingDate,0,3)
        pendingdetials.addWidget(TrainingTime,0,4)
        pendingdetials.addWidget(TrainingVenue,0,5)

        registerdata = []

        for temp in self.registereddata:
            for tempa in self.tempdata:
                if temp[0] == tempa[1]:
                    registerdata.append(tempa)
        
        count = 1

        for i in registerdata:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Ttitle = QLabel(i[0])
            Date = QLabel(i[2])
            Time = QLabel(i[3])
            Venue = QLabel(i[4])
            
            pendingdetials.addWidget(number,count,0)
            pendingdetials.addWidget(TID,count,1)
            pendingdetials.addWidget(Ttitle,count,2)
            pendingdetials.addWidget(Date,count,3)
            pendingdetials.addWidget(Time,count,4)
            pendingdetials.addWidget(Venue,count,5)

            count+=1

        pendingwid = QWidget()
        pendingwindow = QVBoxLayout(pendingwid)
        pendingwindow.addLayout(pendingdetials)
        pendingwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        pendingwindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(pendingwid)

    def loadapprove(self):#tbd
        TrainingNoTitle = QLabel("No.")
        TrainingID = QLabel("Training ID")
        TrainingTitle = QLabel("Training Title")
        TrainingDate = QLabel("Date")
        TrainingTime = QLabel("Time")
        TrainingVenue = QLabel("Venue")
        ApproverID = QLabel("Approver ID")

        approvedetials = QGridLayout()
        approvedetials.addWidget(TrainingNoTitle,0,0)
        approvedetials.addWidget(TrainingID,0,1)
        approvedetials.addWidget(TrainingTitle,0,2)
        approvedetials.addWidget(TrainingDate,0,3)
        approvedetials.addWidget(TrainingTime,0,4)
        approvedetials.addWidget(TrainingVenue,0,5)
        approvedetials.addWidget(ApproverID,0,6)

        approvedata = []

        for temp in self.approveddata:
            for tempa in self.tempdata:
                if temp[0] == tempa[1]:
                    approvedata.append([tempa[0], tempa[1], tempa[2], tempa[3], tempa[4], temp[2]])
        
        count = 1

        for i in approvedata:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Ttitle = QLabel(i[0])
            Date = QLabel(i[2])
            Time = QLabel(i[3])
            Venue = QLabel(i[4])
            ApproverID = QLabel(i[5])

            approvedetials.addWidget(number,count,0)
            approvedetials.addWidget(TID,count,1)
            approvedetials.addWidget(Ttitle,count,2)
            approvedetials.addWidget(Date,count,3)
            approvedetials.addWidget(Time,count,4)
            approvedetials.addWidget(Venue,count,5)
            approvedetials.addWidget(ApproverID,count,6)

            count+=1

        approvewid = QWidget()
        approvewindow = QVBoxLayout(approvewid)
        approvewindow.addLayout(approvedetials)
        approvewindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        approvewindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(approvewid)

    def loadongoing(self):#tbd
        TrainingNoTitle = QLabel("No.")
        TrainingID = QLabel("Training ID")
        TrainingTitle = QLabel("Training Title")
        TrainingDate = QLabel("Date")
        TrainingTime = QLabel("Time")
        TrainingVenue = QLabel("Venue")

        ongoingdetials = QGridLayout()
        ongoingdetials.addWidget(TrainingNoTitle,0,0)
        ongoingdetials.addWidget(TrainingID,0,1)
        ongoingdetials.addWidget(TrainingTitle,0,2)
        ongoingdetials.addWidget(TrainingDate,0,3)
        ongoingdetials.addWidget(TrainingTime,0,4)
        ongoingdetials.addWidget(TrainingVenue,0,5)

        ongoingdata = []

        for temp in self.ongoing:
            ongoingdata.append(temp)
        
        count = 1

        for i in ongoingdata:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Ttitle = QLabel(i[0])
            Date = QLabel(i[2])
            Time = QLabel(i[3])
            Venue = QLabel(i[4])
            
            ongoingdetials.addWidget(number,count,0)
            ongoingdetials.addWidget(TID,count,1)
            ongoingdetials.addWidget(Ttitle,count,2)
            ongoingdetials.addWidget(Date,count,3)
            ongoingdetials.addWidget(Time,count,4)
            ongoingdetials.addWidget(Venue,count,5)

            count+=1

        ongoingwid = QWidget()
        ongoingwindow = QVBoxLayout(ongoingwid)
        ongoingwindow.addLayout(ongoingdetials)
        ongoingwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        ongoingwindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(ongoingwid)


    #history
    #admin * big problem
    def adminAdded(self):
        print('bill')

    def adminModify(self):
        print('bill')

    def adminRemove(self):
        print('bill')

    #staff
    def staffcomplete(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingID = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")

        completedetials = QGridLayout()
        completedetials.addWidget(HistoryNoTitle,0,0)
        completedetials.addWidget(HistoryTrainingID,0,1)
        completedetials.addWidget(HistoryTrainingTitle,0,2)
        completedetials.addWidget(HistoryDateList,0,3)

        completedata = []

        for temp in self.done:
            for tempa in self.completed:
                if temp[0] == tempa[1]:
                    completedata.append(tempa)
        
        count = 1

        for i in completedata:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Ttitle = QLabel(i[0])
            Date = QLabel(i[2])
            completedetials.addWidget(number,count,0)
            completedetials.addWidget(TID,count,1)
            completedetials.addWidget(Ttitle,count,2)
            completedetials.addWidget(Date,count,3)
            count+=1

        completewid = QWidget()
        completewindow = QVBoxLayout(completewid)
        completewindow.addLayout(completedetials)
        completewindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        completewindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(completewid)

    def staffreject(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingID = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")

        rejectdetials = QGridLayout()
        rejectdetials.addWidget(HistoryNoTitle,0,0)
        rejectdetials.addWidget(HistoryTrainingID,0,1)
        rejectdetials.addWidget(HistoryTrainingTitle,0,2)
        rejectdetials.addWidget(HistoryDateList,0,3)

        rejectdata = []
        for temp in self.rejecteddata:
            for tempa in self.tempdata:
                if temp[0] == tempa[1]:
                    rejectdata.append(tempa)

        for temp in self.rejecteddata:
            for tempa in self.ongoing:
                if temp[0] == tempa[1]:
                    rejectdata.append(tempa)

        for temp in self.rejecteddata:
            for tempa in self.completed:
                if temp[0] == tempa[1]:
                    rejectdata.append(tempa)
        
        count = 1

        for i in rejectdata:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Ttitle = QLabel(i[0])
            Date = QLabel(i[2])
            rejectdetials.addWidget(number,count,0)
            rejectdetials.addWidget(TID,count,1)
            rejectdetials.addWidget(Ttitle,count,2)
            rejectdetials.addWidget(Date,count,3)
            count+=1

        rejectwid = QWidget()
        rejectwindow = QVBoxLayout(rejectwid)
        rejectwindow.addLayout(rejectdetials)
        rejectwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        rejectwindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(rejectwid)

    #hr
    def hrApprove(self):#tbd
        print('bill')

    def hrReject(self):#tbd
        print('bill')

    #account
    #admin,staff,hr
    def loadaccount(self):
        if self.credential[5] != '':
            t_img = QPixmap(self.credential[5])
            if t_img.width() > t_img.height():
                trans = t_img.copy((t_img.width()/4),0,t_img.width(),t_img.width())
            if t_img.height() > t_img.width():
                trans = t_img.copy(0,(t_img.height()/4),t_img.width(),t_img.width())
            if t_img.height == t_img.width():
                trans = t_img
            t_image = QIcon(trans)

        if self.credential[5] != '':
            profilepic = QPushButton(t_image,'')
            profilepic.setIconSize(QSize(290,290))
        else:
            profilepic = QPushButton(qta.icon('ph.image'),'')
            profilepic.setIconSize(QSize(50,50))
        profilepic.setFixedSize(300,300)
        
        Id = QLabel()
        Idinput = QLabel()
        Name = QLabel()
        Nameinput = QLabel()
        Phone = QLabel()
        Phoneinput = QLabel()
        Email = QLabel()
        Emailinput = QLabel()
        Department = QLabel()
        Departmentinput = QLabel()

        Id.setText("Employee ID")
        Id.setStyleSheet("QLabel{font-size: 12pt;}")
        Idinput.setText(self.credential[0])
        Idinput.setStyleSheet("QLabel{font-size: 12pt;}")
        Name.setText("Name")
        Name.setStyleSheet("QLabel{font-size: 12pt;}")
        Nameinput.setText(self.credential[1])
        Nameinput.setStyleSheet("QLabel{font-size: 12pt;}")
        Phone.setText("Phone")
        Phone.setStyleSheet("QLabel{font-size: 12pt;}")
        Phoneinput.setText(self.credential[2])
        Phoneinput.setStyleSheet("QLabel{font-size: 12pt;}")
        Email.setText("Email")
        Email.setStyleSheet("QLabel{font-size: 12pt;}")
        Emailinput.setText(self.credential[3])
        Emailinput.setStyleSheet("QLabel{font-size: 12pt;}")
        Department.setText("Department")
        Department.setStyleSheet("QLabel{font-size: 12pt;}")
        Departmentinput.setText(self.credential[4])
        Departmentinput.setStyleSheet("QLabel{font-size: 12pt;}")

        profilecontent = QGridLayout()
        profilecontent.addWidget(Id,0,0)
        profilecontent.addWidget(Idinput,0,1)
        profilecontent.addWidget(Name,1,0)
        profilecontent.addWidget(Nameinput,1,1)
        profilecontent.addWidget(Phone,2,0)
        profilecontent.addWidget(Phoneinput,2,1)
        profilecontent.addWidget(Email,3,0)
        profilecontent.addWidget(Emailinput,3,1)
        profilecontent.addWidget(Department,4,0)
        profilecontent.addWidget(Departmentinput,4,1)

        profilewindow = QHBoxLayout()
        profilewindow.addWidget(profilepic)
        profilewindow.addLayout(profilecontent)

        self.accountwindow.addLayout(profilewindow)

    #functions
    def dashboard(self):#minor adjustment
        self.current.setText("DashBoard")
        if role == "admin":
            self.addbt.show()
            self.addedbt.hide()
            self.modifiedbt.hide()
            self.removebt.hide()
        if role == "hr":
            self.approvebt.hide()
            self.rejectbt.hide()
        if role =="staff":
            self.completedbt.hide()
            self.rejectedbt.hide()
            self.pendingbt.hide()
            self.approvebt.hide()
            self.ongoingbt.hide()    
        if role == 'admin' or role == 'staff':
            if self.filterlist != []:
                self.filterlist = []
        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loaddashboard()
        self.dashboardwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.dashboardwindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(self.dashboardwid)
    
    def training(self):#tbd
        self.current.setText("Training")
        if role =="staff":
            self.pendingbt.show()
            self.approvebt.show()
            self.ongoingbt.show()
            self.completedbt.hide()
            self.rejectedbt.hide() 
            self.loadpending()
            self.loadapprove()
            self.loadongoing()

    def history(self):
        self.current.setText("History")
        if role == "admin":
            self.addbt.hide()
            self.addedbt.show()
            self.modifiedbt.show()
            self.removebt.show()
            self.adminAdded()
        if role == "hr":
            self.approvebt.show()
            self.rejectbt.show()
            self.hrApprove()
        if role =="staff":
            self.pendingbt.hide()
            self.approvebt.hide()
            self.ongoingbt.hide() 
            self.completedbt.show()
            self.rejectedbt.show()
            self.staffcomplete()

    def account(self):
        self.current.setText("Account")
        if role == "admin":
            self.addbt.hide()
            self.addedbt.hide()
            self.modifiedbt.hide()
            self.removebt.hide()
        if role == "hr":
            self.approvebt.hide()
            self.rejectbt.hide()
        if role =="staff":
            self.completedbt.hide()
            self.rejectedbt.hide()
            self.pendingbt.hide()
            self.approvebt.hide()
            self.ongoingbt.hide()  
        self.accountwid = QWidget()
        self.accountwindow = QVBoxLayout(self.accountwid)
        self.loadaccount()
        self.accountwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.accountwindow.addStretch()

        #set scroll area widget
        self.windowscroll.setWidget(self.accountwid)
        
    def logout(self):
        self.current.setText("Logout")
        print("Bill")

    #sidemenu expand contract features
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
