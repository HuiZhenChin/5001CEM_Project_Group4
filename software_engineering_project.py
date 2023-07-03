import sys
import re
import qtawesome as qta
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import bcrypt
import base64
import mysql.connector

class LoginPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Login Page")
        self.setFixedWidth(350)
        self.setFixedHeight(400)
        self.initUI()
    
    def initUI(self):
        # Create username label and input field
        self.username_label = QLabel("Username:")
        self.username_input = QLineEdit()

        # Create password label and input field
        self.password_label = QLabel("Password:")
        self.password_input = QLineEdit()
        self.password_input.setEchoMode(QLineEdit.Password)

        # Create login button
        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.login)

        # Create layout and add widgets
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.username_label)
        self.layout.addWidget(self.username_input)
        self.layout.addWidget(self.password_label)
        self.layout.addWidget(self.password_input)
        self.layout.addWidget(self.login_button)

        # Set the layout for the window
        self.setLayout(self.layout)

    def login(self):#work on it(UI)
        username = self.username_input.text()
        password = self.password_input.text()

        if username[0].upper() == 'A':
            role = 'admin'
            self.loginvalidation(role,username,password)
        elif username[0].upper() == 'H':
            role = 'hr'
            self.loginvalidation(role,username,password)
        elif username[0].upper() == 'S':
            role = 'staff'
            self.loginvalidation(role,username,password)
        else:
            QMessageBox.warning(self, "Login", "Invalid ID.")

    def loginvalidation(self,role,username,password):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test"
            )
            cursor = connection.cursor()
            if role == 'admin':
                cursor.execute("SELECT ID FROM admin")
            elif role == 'hr':
                cursor.execute("SELECT ID FROM hrassistant")
            elif role == 'staff':
                cursor.execute("SELECT ID FROM staff")
            else:
                QMessageBox.warning(self, "Login", "Invalid ID.")
            ids = cursor.fetchall()

        except mysql.connector.Error as error:
            print("Failed to connect: {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

        valid = False
        for id in ids:
            print(id[0],username.upper())
            if id[0] == username.upper():
                try:
                    connection = mysql.connector.connect(
                        host="localhost",
                        user="root",
                        password="",
                        database="test"
                    )
                    cursor = connection.cursor()
                    print("bill")
                    if role == 'admin':
                        cursor.execute("SELECT * FROM admin WHERE ID = %s",(id[0],))
                    elif role == 'hr':
                        cursor.execute("SELECT * FROM hrassistant WHERE ID = %s",(id[0],))
                    elif role == 'staff':
                        cursor.execute("SELECT * FROM staff WHERE ID = %s",(id[0],))
                    else:
                        QMessageBox.warning(self, "Login", "Invalid ID.")
                    credential = cursor.fetchall()

                except mysql.connector.Error as error:
                    print("Failed to connect: {}".format(error))

                finally:
                    if connection.is_connected():
                        cursor.close()
                        connection.close()

                print(credential[0][7])
                print(credential[0][6])
                hashpass = bcrypt.hashpw(password.encode('utf-8'),credential[0][7].encode('utf-8'))
                print(hashpass)
                if credential[0][6].encode('utf-8') == hashpass:
                    self.close()
                    self.openwindow(role,credential[0])
                    valid = True
                    break
            else:
                valid = False
        
        if valid == False:
            QMessageBox.warning(self, "Login", "Invalid username or password.")
            
    def openwindow(self,role,credential):
        self.mainwindow = Main_window(role,credential)
        self.mainwindow.show()

class Main_window(QMainWindow):
    def __init__(self, role,credential):
        QMainWindow.__init__(self)
        # update database data and load data
        self.role = role
        self.credential = credential
        self.update()
        self.loaddata()
        
        self.widget = QWidget(self)
        picd = QByteArray.fromBase64(b'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')
        t_img = QPixmap(QImage.fromData(picd))
        self.setWindowIcon(QIcon(t_img))
        self.title = QLabel(self.role)
        self.title.setStyleSheet("QLabel{font-size: 18pt;color:white;}")
        self.current = QLabel("DashBoard")
        self.current.setStyleSheet("QLabel{font-size: 18pt;}")
        
        # specific role button
        if self.role == "admin":
            # dashboard
            self.addbt = QPushButton('CREATE TRAINING')
            self.addbt.setFixedWidth(150)
            self.addbt.clicked.connect(self.createnewtraining)

            # history
            self.addedbt = QPushButton('Added Training')
            self.addedbt.setFixedSize(150, 35)
            self.addedbt.clicked.connect(self.adminAdded)
            self.addedbt.hide()
            self.modifiedbt = QPushButton('Modified Training')
            self.modifiedbt.setFixedSize(150, 35)
            self.modifiedbt.clicked.connect(self.adminModify)
            self.modifiedbt.hide()
            self.removebt = QPushButton('Remove Training')
            self.removebt.setFixedSize(150, 35)
            self.removebt.clicked.connect(self.adminRemove)
            self.removebt.hide()

        if self.role == 'hr':
            self.approvebt = QPushButton('Approved Participant')
            self.approvebt.setFixedSize(150, 35)
            self.approvebt.clicked.connect(self.hrApprove)
            self.approvebt.hide()
            self.rejectbt = QPushButton('Rejected Participant')
            self.rejectbt.setFixedSize(150, 35)
            self.rejectbt.clicked.connect(self.hrReject)
            self.rejectbt.hide()

        if self.role == 'staff':
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

        # additional validation lists
        self.filterlist = []

        # scroll area
        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loaddashboard()
        self.dashboardwindow.addStretch()

        self.windowscroll = QScrollArea()
        self.windowscroll.setMinimumSize(QSize(800, 500))
        self.windowscroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.windowscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.windowscroll.setWidget(self.dashboardwid)
        self.windowscroll.setWidgetResizable(True)

        # content
        self.content = QVBoxLayout()
        self.content.addWidget(self.current)
        if self.role == "admin":
            temp = QHBoxLayout()
            temp.addWidget(self.addbt)
            temp.addWidget(self.addedbt)
            temp.addWidget(self.modifiedbt)
            temp.addWidget(self.removebt)
            temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.content.addLayout(temp)
        if self.role == "hr":
            temp = QHBoxLayout()
            temp.addWidget(self.approvebt)
            temp.addWidget(self.rejectbt)
            temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.content.addLayout(temp)
        if self.role == "staff":
            temp = QHBoxLayout()
            temp.addWidget(self.completedbt)
            temp.addWidget(self.rejectedbt)
            temp.addWidget(self.pendingbt)
            temp.addWidget(self.approvebt)
            temp.addWidget(self.ongoingbt)
            temp.setAlignment(Qt.AlignmentFlag.AlignRight)
            self.content.addLayout(temp)
        self.content.addWidget(self.windowscroll)

        # side menu
        #expand contract button
        icon = qta.icon("fa.angle-double-right",color='white')
        self.expandButton = QPushButton(icon, '')
        self.expandButton.setIconSize(QSize(35, 35))
        self.expandButton.setFixedSize(50, 50)
        self.expandButton.setStyleSheet("QPushButton{border-style: outset;color: #ffffff;}")
        self.expandButton.clicked.connect(self.expand)

        # dashboard button
        self.dashboardbt = QPushButton(qta.icon("ei.dashboard",color='white'), '')
        self.dashboardbt.setIconSize(QSize(35, 35))
        self.dashboardbt.setFixedSize(50, 50)
        self.dashboardbt.setStyleSheet("QPushButton{border-style: outset;color: #ffffff;}")
        self.dashboardbt.clicked.connect(self.dashboard)

        # training list button
        if self.role == "staff":
            self.trainingbt = QPushButton(qta.icon("fa5.list-alt",color='white'), '')
            self.trainingbt.setIconSize(QSize(35, 35))
            self.trainingbt.setFixedSize(50, 50)
            self.trainingbt.setStyleSheet("QPushButton{border-style: outset;color: #ffffff;}")
            self.trainingbt.clicked.connect(self.training)

        #add department button
        if self.role == "hr":
            self.adddepartmentbt = QPushButton(qta.icon("ei.group-alt",color='white'),'')
            self.adddepartmentbt.setIconSize(QSize(35, 35))
            self.adddepartmentbt.setFixedSize(50, 50)
            self.adddepartmentbt.setStyleSheet("QPushButton{border-style: outset;color: #ffffff;}")
            self.adddepartmentbt.clicked.connect(self.adddepartment)

        # historybutton
        self.historybt = QPushButton(qta.icon("msc.history",color='white'), '')
        self.historybt.setIconSize(QSize(35, 35))
        self.historybt.setFixedSize(50, 50)
        self.historybt.setStyleSheet("QPushButton{border-style: outset;color: #ffffff;}")
        self.historybt.clicked.connect(self.history)

        # profile button
        if self.credential[5] != '':
            profilepicd = QByteArray.fromBase64(self.credential[5])
            t_img = QPixmap(QImage.fromData(profilepicd))
            if t_img.width() > t_img.height():
                trans = t_img.copy((t_img.width() / 4), 0, t_img.width(), t_img.width())
            if t_img.height() > t_img.width():
                trans = t_img.copy(0, (t_img.height() / 4), t_img.width(), t_img.width())
            if t_img.height == t_img.width():
                trans = t_img

            try:
                t_image = QIcon(trans)
            except:
                t_image = None
                print("Error in loading image")

        if t_image != None:
            self.accountButton = QPushButton(t_image, '')
            self.accountButton.setIconSize(QSize(35, 35))
        else:
            self.accountButton = QPushButton(qta.icon("msc.account",color='white'), '')
            self.accountButton.setIconSize(QSize(35, 35))
        self.accountButton.setFixedSize(50, 50)
        self.accountButton.setStyleSheet("QPushButton{border-style: outset;color: #ffffff;}")
        self.accountButton.clicked.connect(self.account)

        # logout button
        self.logoutButton = QPushButton(qta.icon("ri.logout-box-r-line",color='white'), '')
        self.logoutButton.setIconSize(QSize(35, 35))
        self.logoutButton.setFixedSize(50, 50)
        self.logoutButton.setStyleSheet("QPushButton{border-style: outset;color: #ffffff;}")
        self.logoutButton.clicked.connect(self.logout)

        self.sidemenuheader = QHBoxLayout()
        self.sidemenuheader.addWidget(self.title)
        self.title.setHidden(True)
        self.sidemenuheader.addWidget(self.expandButton)

        self.sidemenucontent = QVBoxLayout()
        self.sidemenucontent.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidemenucontent.addWidget(self.dashboardbt)
        if self.role == "staff":
            self.sidemenucontent.addWidget(self.trainingbt)
        if self.role == "hr":
            self.sidemenucontent.addWidget(self.adddepartmentbt)
        self.sidemenucontent.addWidget(self.historybt)
        self.sidemenucontent.addStretch()

        self.sidemenufooter = QVBoxLayout()
        self.sidemenufooter.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.sidemenufooter.addWidget(self.accountButton)
        self.sidemenufooter.addWidget(self.logoutButton)

        self.sidemenuc = QVBoxLayout()
        self.sidemenuc.addLayout(self.sidemenuheader, 1)
        self.sidemenuc.addLayout(self.sidemenucontent, 100)
        self.sidemenuc.addLayout(self.sidemenufooter, 1)
        self.sidemenuc.addStretch()

        self.sidemenu = QWidget()
        self.sidemenu.setLayout(self.sidemenuc)
        self.sidemenu.setStyleSheet("background-color: #031C44;")
        
        # whole window
        self.layout = QHBoxLayout()
        self.layout.addWidget(self.sidemenu, 1)
        self.layout.addLayout(self.content, 100)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    # dashboard
    # admin
    def selectimage(self):
        fname = QFileDialog.getOpenFileNames(self, 'Select Images', '',
                                             'Image files (*.png *.jpg *.jpeg *.xpm *.bmp *.pdf)')
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
        self.newtrainingDateinput = QDateEdit(QDate.currentDate())

        self.newtrainingTime = QLabel('Time :')
        self.newtrainingTimeinput = QTimeEdit(QTime.currentTime())

        self.newtrainingVenue = QLabel('Venue :')
        self.newtrainingVenueinput = QLineEdit()

        self.newtrainingCost = QLabel('Cost :')
        self.newtrainingCostinput = QLineEdit()

        self.newtrainingimage = QLabel('Add Image :')
        self.newtrainingimageinput = QPushButton('Select Image')
        self.newtrainingimageinput.clicked.connect(self.selectimage)
        self.newtrainingimagepath = QLineEdit()
        self.newtrainingimagepath.setDisabled(True)

        self.newtrainingdescription = QLabel('Description :')
        self.newtrainingdescriptioninput = QLineEdit()

        self.newtraininginfo = QGridLayout()
        self.newtraininginfo.addWidget(self.newtrainingname, 0, 0)
        self.newtraininginfo.addWidget(self.newtrainingnameinput, 0, 1)
        self.newtraininginfo.addWidget(self.newtrainingID, 1, 0)
        self.newtraininginfo.addWidget(self.newtrainingIDinput, 1, 1)
        self.newtraininginfo.addWidget(self.newtrainingDate, 2, 0)
        self.newtraininginfo.addWidget(self.newtrainingDateinput, 2, 1)
        self.newtraininginfo.addWidget(self.newtrainingTime, 3, 0)
        self.newtraininginfo.addWidget(self.newtrainingTimeinput, 3, 1)
        self.newtraininginfo.addWidget(self.newtrainingVenue, 4, 0)
        self.newtraininginfo.addWidget(self.newtrainingVenueinput, 4, 1)
        self.newtraininginfo.addWidget(self.newtrainingCost, 5, 0)
        self.newtraininginfo.addWidget(self.newtrainingCostinput, 5, 1)
        self.newtraininginfo.addWidget(self.newtrainingimage, 6, 0)
        img = QVBoxLayout()
        img.addWidget(self.newtrainingimageinput)
        img.addWidget(self.newtrainingimagepath)
        self.newtraininginfo.addLayout(img, 6, 1)
        self.newtraininginfo.addWidget(self.newtrainingdescription, 7, 0)
        self.newtraininginfo.addWidget(self.newtrainingdescriptioninput, 7, 1)

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

    def created(self):#date data change
        t_title = self.newtrainingnameinput.text()
        t_ID = self.newtrainingIDinput.text()
        t_Date = self.newtrainingDateinput.text()
        t_Time = self.newtrainingTimeinput.text()
        t_Venue = self.newtrainingVenueinput.text()
        t_Cost = self.newtrainingCostinput.text()
        t_img = self.newtrainingimagepath.text()
        t_dep = None
        t_description = self.newtrainingdescriptioninput.text()
        self.tempdata.append([t_title, t_ID, t_Date, t_Time, t_Venue, t_Cost, t_img, t_dep, t_description])
        self.addedtrainingdata.append([self.credential[0], t_ID, QDateTime.currentDateTime()])
        self.dashboard()

    def edittraining(self, id):
        count = 0
        for button in self.editbtgroup.buttons():
            print(button)
            print(id)
            if button != id:
                count += 1
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
        self.newtrainingIDinput.setDisabled(True)

        self.newtrainingDate = QLabel('Date :')
        self.newtrainingDateinput = QDateEdit()
        self.newtrainingDateinput.setDate(QDate.fromString(self.data[2],'M/d/yyyy'))

        self.newtrainingTime = QLabel('Time :')
        self.newtrainingTimeinput = QTimeEdit()
        self.newtrainingTimeinput.setTime(QTime.fromString(self.data[3],'h:mm AP'))

        self.newtrainingVenue = QLabel('Venue :')
        self.newtrainingVenueinput = QLineEdit()
        self.newtrainingVenueinput.setText(self.data[4])

        self.newtrainingCost = QLabel('Cost :')
        self.newtrainingCostinput = QLineEdit()
        self.newtrainingCostinput.setText(self.data[5])

        self.newtrainingimage = QLabel('Add Image :')
        self.newtrainingimageinput = QPushButton('Select Image')
        self.newtrainingimageinput.clicked.connect(self.selectimage)
        self.newtrainingimagepath = QLineEdit()
        self.newtrainingimagepath.setDisabled(True)
        self.newtrainingimagepath.setText(self.data[6])

        self.newtrainingdescription = QLabel('Description :')
        self.newtrainingdescriptioninput = QLineEdit()
        self.newtrainingdescriptioninput.setText(self.data[8])

        self.newtraininginfo = QGridLayout()
        self.newtraininginfo.addWidget(self.newtrainingname, 0, 0)
        self.newtraininginfo.addWidget(self.newtrainingnameinput, 0, 1)
        self.newtraininginfo.addWidget(self.newtrainingID, 1, 0)
        self.newtraininginfo.addWidget(self.newtrainingIDinput, 1, 1)
        self.newtraininginfo.addWidget(self.newtrainingDate, 2, 0)
        self.newtraininginfo.addWidget(self.newtrainingDateinput, 2, 1)
        self.newtraininginfo.addWidget(self.newtrainingTime, 3, 0)
        self.newtraininginfo.addWidget(self.newtrainingTimeinput, 3, 1)
        self.newtraininginfo.addWidget(self.newtrainingVenue, 4, 0)
        self.newtraininginfo.addWidget(self.newtrainingVenueinput, 4, 1)
        self.newtraininginfo.addWidget(self.newtrainingCost, 5, 0)
        self.newtraininginfo.addWidget(self.newtrainingCostinput, 5, 1)
        self.newtraininginfo.addWidget(self.newtrainingimage, 6, 0)
        img = QVBoxLayout()
        img.addWidget(self.newtrainingimageinput)
        img.addWidget(self.newtrainingimagepath)
        self.newtraininginfo.addLayout(img, 6, 1)
        self.newtraininginfo.addWidget(self.newtrainingdescription, 7, 0)
        self.newtraininginfo.addWidget(self.newtrainingdescriptioninput, 7, 1)

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

    def saveedit(self):#date data change
        t_title = self.newtrainingnameinput.text()
        t_ID = self.newtrainingIDinput.text()
        t_Date = self.newtrainingDateinput.text()
        t_Time = self.newtrainingTimeinput.text()
        t_Venue = self.newtrainingVenueinput.text()
        t_Cost = self.newtrainingCostinput.text()
        t_img = self.newtrainingimagepath.text()
        t_dep = None
        t_description = self.newtrainingdescriptioninput.text()
        for temp in self.tempdata:
            if self.data == temp:
                self.tempdata.remove(temp)
        self.tempdata.append([t_title, t_ID, t_Date, t_Time, t_Venue, t_Cost, t_img, t_dep, t_description])
        self.edittrainingdata.append([self.credential[0], t_ID, QDateTime.currentDateTime()])
        print(self.edittrainingdata)
        self.dashboard()

    def removetraining(self, id):#date data change
        count = 0
        for button in self.removebtgroup.buttons():
            print(button)
            print(id)
            if button != id:
                count += 1
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
                self.removetrainingdata.append([self.credential[0], QDateTime.currentDateTime(), temp[0], temp[1], temp[2], temp[3], temp[4], temp[5], temp[6], temp[7], temp[8]])

        for temp in self.registereddata:
            if self.data[1] == temp[0]:
                self.registereddata.remove(temp)
        
        for temp in self.approveddata:
            if self.data[1] == temp[0]:
                self.approveddata.remove(temp)

        for temp in self.rejecteddata:
            if self.data[1] == temp[0]:
                self.rejecteddata.remove(temp)

        # load window
        self.dashboard()

    # staff
    def register(self, id):
        count = 0
        for button in self.registerbtgroup.buttons():
            if button != id:
                count += 1
            else:
                break

        if self.filterlist == []:
            self.data = self.dashboarddata[count]
        else:
            for i in self.tempdata:
                if self.filterlist[count] == i[1]:
                    self.data = i
                    break
        self.registereddata.append([self.data[1], self.credential[0]])

        self.dashboard()

    # hr
    def request(self, id):
        count = 0
        for button in self.requestbtgroup.buttons():
            if button != id:
                count += 1
            else:
                break

        self.data = self.dashboarddata[count]

        self.current.setText(self.data[1] + " : " + self.data[0])

        y = 0
        label = QLabel("List or requester")
        temp = []
        for request in self.registereddata:
            if request[0] == self.data[1]:
                for staff in self.stafflist:
                    if staff[0] == request[1]:
                        temp.append(staff)
                        break
        self.checkbuttongroup = []

        no = QLabel("No")
        sid = QLabel("Staff ID")
        sname = QLabel("Name")
        phone = QLabel("Phone")
        dep = QLabel("Department")

        self.checkall = QPushButton('Check All')
        self.checkall.setFixedWidth(150)
        self.checkall.clicked.connect(self.check_all_bt)
        self.requestlist = QGridLayout()
        self.requestlist.addWidget(no, y, 0)
        self.requestlist.addWidget(sid, y, 1)
        self.requestlist.addWidget(sname, y, 2)
        self.requestlist.addWidget(phone, y, 3)
        self.requestlist.addWidget(dep, y, 4)
        self.requestlist.addWidget(self.checkall, y, 5)
        y += 1

        for reqlist in temp:
            checkbutton = QCheckBox()
            checkbutton.setAutoExclusive(True)
            no = QLabel(str(y))
            sid = QLabel(reqlist[0])
            sname = QLabel(reqlist[1])
            phone = QLabel(reqlist[2])
            dep = QLabel(reqlist[3])

            self.requestlist.addWidget(no, y, 0)
            self.requestlist.addWidget(sid, y, 1)
            self.requestlist.addWidget(sname, y, 2)
            self.requestlist.addWidget(phone, y, 3)
            self.requestlist.addWidget(dep, y, 4)
            y += 1

        for i in range(0, y - 1):
            self.checkbuttongroup.append('')

        for i, v in enumerate(self.checkbuttongroup):
            self.checkbuttongroup[i] = QCheckBox(v)
            if self.checkbuttongroup[i].isChecked():
                print("True")
            self.requestlist.addWidget(self.checkbuttongroup[i], (i + 1), 5, Qt.AlignmentFlag.AlignHCenter)

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

        # set scroll area widget
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
        for i, v in enumerate(self.checkbuttongroup):
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
                    request.append(self.credential[0])
                    self.approveddata.append(request)

        self.dashboard()

    def reject(self):
        checkedarray = []
        for i, v in enumerate(self.checkbuttongroup):
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
                    request.append(self.credential[0])
                    self.rejecteddata.append(request)

        self.dashboard()

    # general
    def loaddashboard(self):
        self.dashboarddata = []
        count = 0
        if self.role == 'admin':
            self.editbtgroup = QButtonGroup()
            self.removebtgroup = QButtonGroup()
            for temp in self.tempdata:
                self.dashboarddata.append(temp)
        if self.role == 'hr':
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
        if self.role == 'staff':
            self.registerbtgroup = QButtonGroup()
            for temp in self.tempdata:
                self.dashboarddata.append(temp)
            for tempa in self.registereddata:
                for temp in self.dashboarddata:
                    if temp[1] == tempa[0]:
                        self.dashboarddata.remove(temp)
            for tempa in self.approveddata:
                for temp in self.dashboarddata:
                    if temp[1] == tempa[0]:
                        self.dashboarddata.remove(temp)
            for tempa in self.rejecteddata:
                for temp in self.dashboarddata:
                    if temp[1] == tempa[0]:
                        self.dashboarddata.remove(temp)

        if self.role == 'admin' or self.role == 'staff':
            self.filterinput = QLineEdit()
            filterbt = QPushButton(qta.icon('mdi.filter-outline'), 'Filter')
            filterbt.clicked.connect(self.filter)
            filtersection = QHBoxLayout()
            filtersection.addWidget(self.filterinput)
            filtersection.addWidget(filterbt)

            self.dashboardwindow.addLayout(filtersection)

        for temp in self.dashboarddata:
            self.dashboardwindow.addLayout(self.createtrainingbt(temp, count))
            self.dashboardwindow.addStretch()
            count += 1

        if self.role == 'admin':
            self.editbtgroup.buttonClicked.connect(self.edittraining)
            self.removebtgroup.buttonClicked.connect(self.removetraining)
        if self.role == 'hr':
            self.requestbtgroup.buttonClicked.connect(self.request)
        if self.role == 'staff':
            self.registerbtgroup.buttonClicked.connect(self.register)

    def createtrainingbt(self, training, count):
        t_title = QLabel(training[0])
        t_ID = QLabel(training[1])
        t_Date = QLabel(training[2])
        t_Time = QLabel(training[3])
        t_Venue = QLabel(training[4])
        t_Cost = QLabel(training[5])
        t_description = QLabel(training[8])

        t_description.setWordWrap(True)

        if training[6] != '':
            t_img = QPixmap(training[6])
            if t_img.width() > t_img.height():
                trans = t_img.copy((t_img.width() / 4), 0, t_img.width(), t_img.width())
            if t_img.height() > t_img.width():
                trans = t_img.copy(0, (t_img.height() / 4), t_img.width(), t_img.width())
            if t_img.height == t_img.width():
                trans = t_img
            t_image = QIcon(trans)

        temppic = QVBoxLayout()
        if training[6] != '':
            picbt = QPushButton(t_image, '')
            picbt.setIconSize(QSize(240, 240))
        else:
            picbt = QPushButton(qta.icon('ph.image'), '')
            picbt.setIconSize(QSize(50, 50))
        picbt.setFixedSize(250, 250)
        temppic.addWidget(picbt)

        tempcontent = QVBoxLayout()
        tempcontent.setAlignment(Qt.AlignmentFlag.AlignTop)
        tempcontent.addWidget(t_title)
        tempcontent.addWidget(t_ID)
        tempcontent.addWidget(t_Date)
        tempcontent.addWidget(t_Time)
        tempcontent.addWidget(t_Venue)
        tempcontent.addWidget(t_Cost)
        tempcontent.addWidget(t_description)
        tempcontent.addStretch()

        tempbtsection = QHBoxLayout()
        tempbtsection.setAlignment(Qt.AlignmentFlag.AlignRight)
        if self.role == 'admin':
            editbt = QPushButton("edit")
            editbt.setFixedSize(100, 25)

            removebt = QPushButton("remove")
            removebt.setFixedSize(100, 25)

            tempbtsection.addWidget(editbt)
            tempbtsection.addWidget(removebt)
            self.editbtgroup.addButton(editbt, count)
            self.removebtgroup.addButton(removebt, count)
        if self.role == 'hr':
            requestbt = QPushButton("request")
            requestbt.setFixedSize(100, 25)
            self.requestbtgroup.addButton(requestbt, count)
            tempbtsection.addWidget(requestbt)
        if self.role == 'staff':
            registerbt = QPushButton("register")
            registerbt.setFixedSize(100, 25)
            self.registerbtgroup.addButton(registerbt, count)
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
        pattern = ".*" + self.filterinput.text() + ".*"
        self.filterlist = [x[1] for x in self.dashboarddata if re.match(pattern, x[1])]

        print(self.filterlist)

        filterbt = QPushButton(qta.icon('mdi.filter-outline'), 'Filter')
        filterbt.clicked.connect(self.filter)
        filtersection = QHBoxLayout()
        filtersection.addWidget(self.filterinput)
        filtersection.addWidget(filterbt)

        if self.role == 'admin':
            self.editbtgroup = QButtonGroup()
            self.removebtgroup = QButtonGroup()
        if self.role == 'staff':
            self.registerbtgroup = QButtonGroup()

        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.dashboardwindow.addLayout(filtersection)

        count = 0
        for temp in self.filterlist:
            for tempa in self.tempdata:
                if temp == tempa[1]:
                    self.dashboardwindow.addLayout(self.createtrainingbt(tempa, count))
                    self.dashboardwindow.addStretch()
                    count += 1

        if self.role == 'admin':
            self.editbtgroup.buttonClicked.connect(self.edittraining)
            self.removebtgroup.buttonClicked.connect(self.removetraining)
        if self.role == 'staff':
            self.registerbtgroup.buttonClicked.connect(self.register)

        self.dashboardwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.dashboardwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(self.dashboardwid)

    # training
    # only staff
    def loadpending(self):
        TrainingNoTitle = QLabel("No.")
        TrainingID = QLabel("Training ID")
        TrainingTitle = QLabel("Training Title")
        TrainingDate = QLabel("Date")
        TrainingTime = QLabel("Time")
        TrainingVenue = QLabel("Venue")

        pendingdetials = QGridLayout()
        pendingdetials.addWidget(TrainingNoTitle, 0, 0)
        pendingdetials.addWidget(TrainingID, 0, 1)
        pendingdetials.addWidget(TrainingTitle, 0, 2)
        pendingdetials.addWidget(TrainingDate, 0, 3)
        pendingdetials.addWidget(TrainingTime, 0, 4)
        pendingdetials.addWidget(TrainingVenue, 0, 5)

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
            pendingdetials.addWidget(number, count, 0)
            pendingdetials.addWidget(TID, count, 1)
            pendingdetials.addWidget(Ttitle, count, 2)
            pendingdetials.addWidget(Date, count, 3)
            pendingdetials.addWidget(Time, count, 4)
            pendingdetials.addWidget(Venue, count, 5)
            count += 1

        pendingwid = QWidget()
        pendingwindow = QVBoxLayout(pendingwid)
        pendingwindow.addLayout(pendingdetials)
        pendingwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        pendingwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(pendingwid)

    def loadapprove(self):
        TrainingNoTitle = QLabel("No.")
        TrainingID = QLabel("Training ID")
        TrainingTitle = QLabel("Training Title")
        TrainingDate = QLabel("Date")
        TrainingTime = QLabel("Time")
        TrainingVenue = QLabel("Venue")
        ApproverID = QLabel("Approver ID")

        approvedetials = QGridLayout()
        approvedetials.addWidget(TrainingNoTitle, 0, 0)
        approvedetials.addWidget(TrainingID, 0, 1)
        approvedetials.addWidget(TrainingTitle, 0, 2)
        approvedetials.addWidget(TrainingDate, 0, 3)
        approvedetials.addWidget(TrainingTime, 0, 4)
        approvedetials.addWidget(TrainingVenue, 0, 5)
        approvedetials.addWidget(ApproverID, 0, 6)

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

            approvedetials.addWidget(number, count, 0)
            approvedetials.addWidget(TID, count, 1)
            approvedetials.addWidget(Ttitle, count, 2)
            approvedetials.addWidget(Date, count, 3)
            approvedetials.addWidget(Time, count, 4)
            approvedetials.addWidget(Venue, count, 5)
            approvedetials.addWidget(ApproverID, count, 6)

            count += 1

        approvewid = QWidget()
        approvewindow = QVBoxLayout(approvewid)
        approvewindow.addLayout(approvedetials)
        approvewindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        approvewindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(approvewid)

    def loadongoing(self):
        TrainingNoTitle = QLabel("No.")
        TrainingID = QLabel("Training ID")
        TrainingTitle = QLabel("Training Title")
        TrainingDate = QLabel("Date")
        TrainingTime = QLabel("Time")
        TrainingVenue = QLabel("Venue")

        ongoingdetials = QGridLayout()
        ongoingdetials.addWidget(TrainingNoTitle, 0, 0)
        ongoingdetials.addWidget(TrainingID, 0, 1)
        ongoingdetials.addWidget(TrainingTitle, 0, 2)
        ongoingdetials.addWidget(TrainingDate, 0, 3)
        ongoingdetials.addWidget(TrainingTime, 0, 4)
        ongoingdetials.addWidget(TrainingVenue, 0, 5)

        ongoingdata = []

        for temp in self.done:
            for tempa in self.ongoing:
                if temp[0] == tempa[1]:
                    ongoingdata.append(tempa)

        count = 1

        for i in ongoingdata:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Ttitle = QLabel(i[0])
            Date = QLabel(i[2])
            Time = QLabel(i[3])
            Venue = QLabel(i[4])

            ongoingdetials.addWidget(number, count, 0)
            ongoingdetials.addWidget(TID, count, 1)
            ongoingdetials.addWidget(Ttitle, count, 2)
            ongoingdetials.addWidget(Date, count, 3)
            ongoingdetials.addWidget(Time, count, 4)
            ongoingdetials.addWidget(Venue, count, 5)

            count += 1

        ongoingwid = QWidget()
        ongoingwindow = QVBoxLayout(ongoingwid)
        ongoingwindow.addLayout(ongoingdetials)
        ongoingwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        ongoingwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(ongoingwid)

    #add department
    #hr only
    def addselecteddepartment(self):
        checkedarray = []
        for i, v in enumerate(self.departmentlist):
            if v.isChecked():
                checkedarray.append(i)

        departmentstring = ''

        for i in checkedarray:
            if departmentstring == '':
                departmentstring = self.depdata[i]
            else:
                departmentstring = departmentstring+','+self.depdata[i]

        if self.data[7] != None:
            departmentstring = departmentstring + ',' + self.data[7]

        staff = []
        for i in self.stafflist:
            for x in checkedarray:
                if i[4] == self.depdata[x]:
                    staff.append(i[0])

        for x in staff:
            for i in self.registereddata:    
                if i[0] == self.data[1]:
                    if i[1] == x:
                        self.registereddata.remove(i)

        for x in staff:
            for i in self.rejecteddata:
                if i[0] == self.data[1]:
                    if i[1] == x:
                        self.rejecteddata.remove(i)

        for x in staff:
            for i in self.approveddata:
                if i[0] == self.data[1]:
                    if i[1] == x:
                        self.approveddata.remove(i)

        for i in staff:
            self.approveddata.append([self.data[1],i,self.credential[0]])
        
        self.tempdata.remove(self.data)
        self.data[7] = departmentstring
        self.tempdata.append(self.data)

        self.adddepartment()

    def insertdepartment(self,id):
        count = 0
        for button in self.adddepartmentbtgroup.buttons():
            print(button)
            print(id)
            if button != id:
                count += 1
            else:
                break

        if self.filterlist == []:
            self.data = self.adddepartmentdata[count]
        else:
            for i in self.tempdata:
                if self.filterlist[count] == i[1]:
                    self.data = i
                    break
        
        t_title = QLabel(self.data[0])
        t_ID = QLabel(self.data[1])
        t_Date = QLabel(self.data[2])
        t_Time = QLabel(self.data[3])
        t_Venue = QLabel(self.data[4])
        t_Cost = QLabel(self.data[5])
        t_description = QLabel(self.data[8])

        t_description.setWordWrap(True)

        if self.data[6] != '':
            t_img = QPixmap(self.data[6])
            if t_img.width() > t_img.height():
                trans = t_img.copy((t_img.width() / 4), 0, t_img.width(), t_img.width())
            if t_img.height() > t_img.width():
                trans = t_img.copy(0, (t_img.height() / 4), t_img.width(), t_img.width())
            if t_img.height == t_img.width():
                trans = t_img
            t_image = QIcon(trans)

        temppic = QVBoxLayout()
        if self.data[6] != '':
            picbt = QPushButton(t_image, '')
            picbt.setIconSize(QSize(240, 240))
        else:
            picbt = QPushButton(qta.icon('ph.image'), '')
            picbt.setIconSize(QSize(50, 50))
        picbt.setFixedSize(250, 250)
        temppic.addWidget(picbt)

        self.departmentlist = []
        y = 0
        for i in self.stafflist:
            if i[4] not in self.departmentlist:
                self.departmentlist.append(i[4])
                y+=1

        if self.data[7] != None:
            dep = self.data[7].rsplit(",")
            for i in dep:
                for x in self.departmentlist:
                    print(x,i)
                    if x==i:
                        print("1")
                        self.departmentlist.remove(x)
                        y-=1
        else:
            dep = None

        self.depdata = []
        for x in self.departmentlist:
            self.depdata.append(x)
        print(self.depdata)

        departmentdisplaytitle = QLabel("List Of Department")
        departmentdisplay = QVBoxLayout()

        for i, v in enumerate(self.departmentlist):
            self.departmentlist[i] = QCheckBox(v)
            departmentdisplay.addWidget(self.departmentlist[i])

        adddepartmentbt = QPushButton('Add Department')
        adddepartmentbt.setFixedWidth(150)
        adddepartmentbt.clicked.connect(self.addselecteddepartment)

        adddepartmentbtsection = QHBoxLayout()
        adddepartmentbtsection.addWidget(adddepartmentbt)
        adddepartmentbtsection.setAlignment(Qt.AlignmentFlag.AlignRight)

        tempcontent = QVBoxLayout()
        tempcontent.setAlignment(Qt.AlignmentFlag.AlignTop)
        tempcontent.addWidget(t_title)
        tempcontent.addWidget(t_ID)
        tempcontent.addWidget(t_Date)
        tempcontent.addWidget(t_Time)
        tempcontent.addWidget(t_Venue)
        tempcontent.addWidget(t_Cost)
        tempcontent.addWidget(t_description)
        tempcontent.addWidget(departmentdisplaytitle)
        tempcontent.addLayout(departmentdisplay)
        tempcontent.addLayout(adddepartmentbtsection)
        tempcontent.addStretch()

        tempcontentsection = QVBoxLayout()
        tempcontentsection.addLayout(tempcontent)

        tempwid = QWidget()
        temp = QHBoxLayout(tempwid)
        temp.addLayout(temppic)
        temp.addLayout(tempcontentsection)

        self.windowscroll.setWidget(tempwid)

    def loaddepartment(self):
        self.adddepartmentdata = []
        count = 0

        self.adddepartmentbtgroup = QButtonGroup()

        departmentlist = []
        for i in self.stafflist:
            if i[4] not in departmentlist:
                departmentlist.append(i[4])

        for temp in self.tempdata:
            if temp[7] == None:
                self.adddepartmentdata.append(temp)
            else:
                dep = temp[7].split(',')
                if len(dep) != len(departmentlist):
                    self.adddepartmentdata.append(temp)

        self.filterinput = QLineEdit()
        filterbt = QPushButton(qta.icon('mdi.filter-outline'), 'Filter')
        filterbt.clicked.connect(self.adddepartmentfilter)
        filtersection = QHBoxLayout()
        filtersection.addWidget(self.filterinput)
        filtersection.addWidget(filterbt)

        self.adddepartmentwindow.addLayout(filtersection)

        for temp in self.adddepartmentdata:
            self.adddepartmentwindow.addLayout(self.createadddepartmentbt(temp, count))
            self.adddepartmentwindow.addStretch()
            count += 1

        self.adddepartmentbtgroup.buttonClicked.connect(self.insertdepartment)

    def createadddepartmentbt(self, training, count):
        t_title = QLabel(training[0])
        t_ID = QLabel(training[1])
        t_Date = QLabel(training[2])
        t_Time = QLabel(training[3])
        t_Venue = QLabel(training[4])
        t_Cost = QLabel(training[5])
        t_description = QLabel(training[8])

        t_description.setWordWrap(True)

        if training[6] != '':
            t_img = QPixmap(training[6])
            if t_img.width() > t_img.height():
                trans = t_img.copy((t_img.width() / 4), 0, t_img.width(), t_img.width())
            if t_img.height() > t_img.width():
                trans = t_img.copy(0, (t_img.height() / 4), t_img.width(), t_img.width())
            if t_img.height == t_img.width():
                trans = t_img
            t_image = QIcon(trans)

        temppic = QVBoxLayout()
        if training[6] != '':
            picbt = QPushButton(t_image, '')
            picbt.setIconSize(QSize(240, 240))
        else:
            picbt = QPushButton(qta.icon('ph.image'), '')
            picbt.setIconSize(QSize(50, 50))
        picbt.setFixedSize(250, 250)
        temppic.addWidget(picbt)

        tempcontent = QVBoxLayout()
        tempcontent.setAlignment(Qt.AlignmentFlag.AlignTop)
        tempcontent.addWidget(t_title)
        tempcontent.addWidget(t_ID)
        tempcontent.addWidget(t_Date)
        tempcontent.addWidget(t_Time)
        tempcontent.addWidget(t_Venue)
        tempcontent.addWidget(t_Cost)
        tempcontent.addWidget(t_description)
        tempcontent.addStretch()

        tempbtsection = QHBoxLayout()
        tempbtsection.setAlignment(Qt.AlignmentFlag.AlignRight)

        adddepbt = QPushButton("add department")
        adddepbt.setFixedSize(100, 25)
        self.adddepartmentbtgroup.addButton(adddepbt, count)
        tempbtsection.addWidget(adddepbt)

        tempcontentsection = QVBoxLayout()
        tempcontentsection.addLayout(tempcontent)
        tempcontentsection.addLayout(tempbtsection)

        temp = QHBoxLayout()
        temp.addLayout(temppic)
        temp.addLayout(tempcontentsection)

        return temp

    def adddepartmentfilter(self):
        self.filterlist = []
        pattern = ".*" + self.filterinput.text() + ".*"
        self.filterlist = [x[1] for x in self.adddepartmentdata if re.match(pattern, x[1])]

        print(self.filterlist)

        filterbt = QPushButton(qta.icon('mdi.filter-outline'), 'Filter')
        filterbt.clicked.connect(self.adddepartmentfilter)
        filtersection = QHBoxLayout()
        filtersection.addWidget(self.filterinput)
        filtersection.addWidget(filterbt)

        self.adddepartmentbtgroup = QButtonGroup()

        self.adddepartmentwid = QWidget()
        self.adddepartmentwindow = QVBoxLayout(self.adddepartmentwid)
        self.adddepartmentwindow.addLayout(filtersection)

        count = 0
        for temp in self.filterlist:
            for tempa in self.tempdata:
                if temp == tempa[1]:
                    self.adddepartmentwindow.addLayout(self.createadddepartmentbt(tempa, count))
                    self.adddepartmentwindow.addStretch()
                    count += 1

        self.adddepartmentbtgroup.buttonClicked.connect(self.insertdepartment)

        self.adddepartmentwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.adddepartmentwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(self.adddepartmentwid)

    # history
    # admin
    def adminAdded(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")

        addDetails = QGridLayout()
        addDetails.addWidget(HistoryNoTitle, 0, 0)
        addDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        addDetails.addWidget(HistoryTrainingTitle, 0, 2)
        addDetails.addWidget(HistoryDateList, 0, 3)

        addeddata = []

        for temp in self.addedtrainingdata:
            for tempa in self.tempdata:
                if temp[1] == tempa[1]:
                    addeddata.append([tempa[0], temp[1], temp[2]])

        for temp in self.addedtrainingdata:
            for tempa in self.ongoing:
                if temp[1] == tempa[1]:
                    addeddata.append([tempa[0], temp[1], temp[2]])

        for temp in self.addedtrainingdata:
            for tempa in self.completed:
                if temp[1] == tempa[1]:
                    addeddata.append([tempa[0], temp[1], temp[2]])

        for temp in self.addedtrainingdata:
            for tempa in self.removetrainingdata:
                if temp[1] == tempa[3]:
                    addeddata.append([tempa[2], temp[1], temp[2]])

        count = 1

        for i in addeddata:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Title = QLabel(i[0])
            Date = QLabel(i[2])
            addDetails.addWidget(number, count, 0)
            addDetails.addWidget(TID, count, 1)
            addDetails.addWidget(Title, count, 2)
            addDetails.addWidget(Date, count, 3)
            count += 1

        addwid = QWidget()
        addwindow = QVBoxLayout(addwid)
        addwindow.addLayout(addDetails)
        addwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        addwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(addwid)

    def adminModify(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")

        editDetails = QGridLayout()
        editDetails.addWidget(HistoryNoTitle, 0, 0)
        editDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        editDetails.addWidget(HistoryTrainingTitle, 0, 2)
        editDetails.addWidget(HistoryDateList, 0, 3)

        editdata = []

        for temp in self.edittrainingdata:
            for tempa in self.tempdata:
                if temp[1] == tempa[1]:
                    editdata.append([tempa[0], temp[1], temp[2]])

        for temp in self.edittrainingdata:
            for tempa in self.ongoing:
                if temp[1] == tempa[1]:
                    editdata.append([tempa[0], temp[1], temp[2]])

        for temp in self.edittrainingdata:
            for tempa in self.completed:
                if temp[1] == tempa[1]:
                    editdata.append([tempa[0], temp[1], temp[2]])

        for temp in self.edittrainingdata:
            for tempa in self.removetrainingdata:
                if temp[1] == tempa[3]:
                    editdata.append([tempa[2], temp[1], temp[2]])

        count = 1

        for i in editdata:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Title = QLabel(i[0])
            Date = QLabel(i[2])
            editDetails.addWidget(number, count, 0)
            editDetails.addWidget(TID, count, 1)
            editDetails.addWidget(Title, count, 2)
            editDetails.addWidget(Date, count, 3)
            count += 1

        editwid = QWidget()
        editwindow = QVBoxLayout(editwid)
        editwindow.addLayout(editDetails)
        editwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        editwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(editwid)

    def adminRemove(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")

        removeDetails = QGridLayout()
        removeDetails.addWidget(HistoryNoTitle, 0, 0)
        removeDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        removeDetails.addWidget(HistoryTrainingTitle, 0, 2)
        removeDetails.addWidget(HistoryDateList, 0, 3)

        count = 1

        for i in self.removetrainingdata:
            number = QLabel(str(count))
            TID = QLabel(i[3])
            Title = QLabel(i[2])
            Date = QLabel(i[1])
            removeDetails.addWidget(number, count, 0)
            removeDetails.addWidget(TID, count, 1)
            removeDetails.addWidget(Title, count, 2)
            removeDetails.addWidget(Date, count, 3)
            count += 1

        removewid = QWidget()
        removewindow = QVBoxLayout(removewid)
        removewindow.addLayout(removeDetails)
        removewindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        removewindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(removewid)

    # staff
    def staffcomplete(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingID = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")

        completedetials = QGridLayout()
        completedetials.addWidget(HistoryNoTitle, 0, 0)
        completedetials.addWidget(HistoryTrainingID, 0, 1)
        completedetials.addWidget(HistoryTrainingTitle, 0, 2)
        completedetials.addWidget(HistoryDateList, 0, 3)

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
            completedetials.addWidget(number, count, 0)
            completedetials.addWidget(TID, count, 1)
            completedetials.addWidget(Ttitle, count, 2)
            completedetials.addWidget(Date, count, 3)
            count += 1

        completewid = QWidget()
        completewindow = QVBoxLayout(completewid)
        completewindow.addLayout(completedetials)
        completewindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        completewindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(completewid)

    def staffreject(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingID = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")

        rejectdetials = QGridLayout()
        rejectdetials.addWidget(HistoryNoTitle, 0, 0)
        rejectdetials.addWidget(HistoryTrainingID, 0, 1)
        rejectdetials.addWidget(HistoryTrainingTitle, 0, 2)
        rejectdetials.addWidget(HistoryDateList, 0, 3)

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
            rejectdetials.addWidget(number, count, 0)
            rejectdetials.addWidget(TID, count, 1)
            rejectdetials.addWidget(Ttitle, count, 2)
            rejectdetials.addWidget(Date, count, 3)
            count += 1

        rejectwid = QWidget()
        rejectwindow = QVBoxLayout(rejectwid)
        rejectwindow.addLayout(rejectdetials)
        rejectwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        rejectwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(rejectwid)

    # hr
    def hrApprove(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")
        HistoryStaffID = QLabel("Staff ID")

        approveParticipantDetails = QGridLayout()
        approveParticipantDetails.addWidget(HistoryNoTitle, 0, 0)
        approveParticipantDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        approveParticipantDetails.addWidget(HistoryTrainingTitle, 0, 2)
        approveParticipantDetails.addWidget(HistoryDateList, 0, 3)
        approveParticipantDetails.addWidget(HistoryStaffID, 0, 4)

        approveParticipantData = []

        for temp in self.approveddata:
            for tempa in self.tempdata:
                if temp[0] == tempa[1]:
                    approveParticipantData.append([tempa[1], tempa[0], tempa[2], temp[1]])

        for temp in self.approveddata:
            for tempa in self.ongoing:
                if temp[0] == tempa[1]:
                    approveParticipantData.append([tempa[1], tempa[0], tempa[2], temp[1]])

        for temp in self.approveddata:
            for tempa in self.completed:
                if temp[0] == tempa[1]:
                    approveParticipantData.append([tempa[1], tempa[0], tempa[2], temp[1]])

        count = 1

        for i in approveParticipantData:
            number = QLabel(str(count))
            TID = QLabel(i[0])
            Ttitle = QLabel(i[1])
            Date = QLabel(i[2])
            ParticipantName = QLabel(i[3])
            approveParticipantDetails.addWidget(number, count, 0)
            approveParticipantDetails.addWidget(TID, count, 1)
            approveParticipantDetails.addWidget(Ttitle, count, 2)
            approveParticipantDetails.addWidget(Date, count, 3)
            approveParticipantDetails.addWidget(ParticipantName, count, 4)
            count += 1

        approveParticipantwid = QWidget()
        approveParticipantwindow = QVBoxLayout(approveParticipantwid)
        approveParticipantwindow.addLayout(approveParticipantDetails)
        approveParticipantwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        approveParticipantwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(approveParticipantwid)

    def hrReject(self):
        HistoryNoTitle = QLabel("No.")
        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryDateList = QLabel("Date")
        HistoryStaffID = QLabel("Staff ID")

        rejectParticipantDetails = QGridLayout()
        rejectParticipantDetails.addWidget(HistoryNoTitle, 0, 0)
        rejectParticipantDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        rejectParticipantDetails.addWidget(HistoryTrainingTitle, 0, 2)
        rejectParticipantDetails.addWidget(HistoryDateList, 0, 3)
        rejectParticipantDetails.addWidget(HistoryStaffID, 0, 4)

        rejectParticipantData = []

        for temp in self.rejecteddata:
            for tempa in self.tempdata:
                if temp[0] == tempa[1]:
                    rejectParticipantData.append([tempa[1], tempa[0], tempa[2], temp[1]])

        for temp in self.rejecteddata:
            for tempa in self.ongoing:
                if temp[0] == tempa[1]:
                    rejectParticipantData.append([tempa[1], tempa[0], tempa[2], temp[1]])

        for temp in self.rejecteddata:
            for tempa in self.completed:
                if temp[0] == tempa[1]:
                    rejectParticipantData.append([tempa[1], tempa[0], tempa[2], temp[1]])

        count = 1

        for i in rejectParticipantData:
            number = QLabel(str(count))
            TID = QLabel(i[0])
            Ttitle = QLabel(i[1])
            Date = QLabel(i[2])
            ParticipantName = QLabel(i[3])
            rejectParticipantDetails.addWidget(number, count, 0)
            rejectParticipantDetails.addWidget(TID, count, 1)
            rejectParticipantDetails.addWidget(Ttitle, count, 2)
            rejectParticipantDetails.addWidget(Date, count, 3)
            rejectParticipantDetails.addWidget(ParticipantName, count, 4)
            count += 1

        rejectParticipantwid = QWidget()
        rejectParticipantwindow = QVBoxLayout(rejectParticipantwid)
        rejectParticipantwindow.addLayout(rejectParticipantDetails)
        rejectParticipantwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        rejectParticipantwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(rejectParticipantwid)

    # account
    # admin,staff,hr
    def loadaccount(self):
        if self.credential[5] != '':
            profilepicd = QByteArray.fromBase64(self.credential[5])
            t_img = QPixmap(QImage.fromData(profilepicd))
            if t_img.width() > t_img.height():
                trans = t_img.copy((t_img.width() / 4), 0, t_img.width(), t_img.width())
            if t_img.height() > t_img.width():
                trans = t_img.copy(0, (t_img.height() / 4), t_img.width(), t_img.width())
            if t_img.height == t_img.width():
                trans = t_img

            try:
                t_image = QIcon(trans)
            except:
                t_image = None
                print("Error in loading image")

        if t_image != None:
            profilepic = QPushButton(t_image, '')
            profilepic.setIconSize(QSize(290, 290))
        else:
            profilepic = QPushButton(qta.icon('ph.image'), '')
            profilepic.setIconSize(QSize(50, 50))
        profilepic.setFixedSize(300, 300)

        Id = QLabel("Employee ID")
        Idinput = QLabel(self.credential[0])
        Name = QLabel("Name")
        Nameinput = QLabel(self.credential[1])
        Phone = QLabel("Phone")
        Phoneinput = QLabel(self.credential[2])
        Email = QLabel("Email")
        Emailinput = QLabel(self.credential[3])
        Department = QLabel("Department")
        Departmentinput = QLabel(self.credential[4])

        Id.setStyleSheet("QLabel{font-size: 12pt;}")
        Idinput.setStyleSheet("QLabel{font-size: 12pt;}")
        Name.setStyleSheet("QLabel{font-size: 12pt;}")
        Nameinput.setStyleSheet("QLabel{font-size: 12pt;}")
        Phone.setStyleSheet("QLabel{font-size: 12pt;}")
        Phoneinput.setStyleSheet("QLabel{font-size: 12pt;}")
        Email.setStyleSheet("QLabel{font-size: 12pt;}")
        Emailinput.setStyleSheet("QLabel{font-size: 12pt;}")
        Department.setStyleSheet("QLabel{font-size: 12pt;}")
        Departmentinput.setStyleSheet("QLabel{font-size: 12pt;}")

        profilecontent = QGridLayout()
        profilecontent.addWidget(Id, 0, 0)
        profilecontent.addWidget(Idinput, 0, 1)
        profilecontent.addWidget(Name, 1, 0)
        profilecontent.addWidget(Nameinput, 1, 1)
        profilecontent.addWidget(Phone, 2, 0)
        profilecontent.addWidget(Phoneinput, 2, 1)
        profilecontent.addWidget(Email, 3, 0)
        profilecontent.addWidget(Emailinput, 3, 1)
        profilecontent.addWidget(Department, 4, 0)
        profilecontent.addWidget(Departmentinput, 4, 1)

        profilewindow = QHBoxLayout()
        profilewindow.addWidget(profilepic)
        profilewindow.addLayout(profilecontent)

        self.accountwindow.addLayout(profilewindow)

    # functions
    def dashboard(self): 
        self.current.setText("DashBoard")
        if self.role == "admin":
            self.addbt.show()
            self.addedbt.hide()
            self.modifiedbt.hide()
            self.removebt.hide()
        if self.role == "hr":
            self.approvebt.hide()
            self.rejectbt.hide()
        if self.role == "staff":
            self.completedbt.hide()
            self.rejectedbt.hide()
            self.pendingbt.hide()
            self.approvebt.hide()
            self.ongoingbt.hide()
        if self.role == 'admin' or self.role == 'staff':
            if self.filterlist != []:
                self.filterlist = []
        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loaddashboard()
        self.dashboardwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.dashboardwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(self.dashboardwid)

    def training(self):
        self.current.setText("Training")
        self.pendingbt.show()
        self.approvebt.show()
        self.ongoingbt.show()
        self.completedbt.hide()
        self.rejectedbt.hide()
        self.loadpending()

    def adddepartment(self):
        self.current.setText("Add Department")
        self.adddepartmentwid = QWidget()
        self.adddepartmentwindow = QVBoxLayout(self.adddepartmentwid)
        self.loaddepartment()
        self.adddepartmentwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.adddepartmentwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(self.adddepartmentwid)

    def history(self):
        self.current.setText("History")
        if self.role == "admin":
            self.addbt.hide()
            self.addedbt.show()
            self.modifiedbt.show()
            self.removebt.show()
            self.adminAdded()
        if self.role == "hr":
            self.approvebt.show()
            self.rejectbt.show()
            self.hrApprove()
        if self.role == "staff":
            self.pendingbt.hide()
            self.approvebt.hide()
            self.ongoingbt.hide()
            self.completedbt.show()
            self.rejectedbt.show()
            self.staffcomplete()

    def account(self):
        self.current.setText("Account")
        if self.role == "admin":
            self.addbt.hide()
            self.addedbt.hide()
            self.modifiedbt.hide()
            self.removebt.hide()
        if self.role == "hr":
            self.approvebt.hide()
            self.rejectbt.hide()
        if self.role == "staff":
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

        # set scroll area widget
        self.windowscroll.setWidget(self.accountwid)

    def logout(self):
        loginwindow.show()
        loginwindow.username_input.setText("")
        loginwindow.password_input.setText("")
        self.credential = ""
        loginwindow.mainwindow.close()

    # sidemenu expand contract features
    def expand(self):
        self.expandButton.clicked.disconnect()
        self.expandButton.setIcon(qta.icon("fa.angle-double-left",color='white'))
        self.dashboardbt.setFixedSize(200, 50)
        self.dashboardbt.setStyleSheet("QPushButton { text-align: left;border-style: outset;color: #ffffff;}")
        self.dashboardbt.setText("DashBoard")
        if self.role == "staff":
            self.trainingbt.setFixedSize(200, 50)
            self.trainingbt.setStyleSheet("QPushButton { text-align: left;border-style: outset;color: #ffffff;}")
            self.trainingbt.setText("Training List")
        if self.role == "hr":
            self.adddepartmentbt.setFixedSize(200, 50)
            self.adddepartmentbt.setStyleSheet("QPushButton { text-align: left;border-style: outset;color: #ffffff;}")
            self.adddepartmentbt.setText("Add Department")
        self.historybt.setFixedSize(200, 50)
        self.historybt.setStyleSheet("QPushButton { text-align: left;border-style: outset;color: #ffffff;}")
        self.historybt.setText("History")
        self.accountButton.setFixedSize(200, 50)
        self.accountButton.setStyleSheet("QPushButton { text-align: left;border-style: outset;color: #ffffff;}")
        self.accountButton.setText(self.credential[1])
        self.logoutButton.setFixedSize(200, 50)
        self.logoutButton.setStyleSheet("QPushButton { text-align: left;border-style: outset;color: #ffffff;}")
        self.logoutButton.setText("Logout")
        self.title.show()
        self.expandButton.clicked.connect(self.contract)

    def contract(self):
        self.expandButton.clicked.disconnect()
        self.expandButton.setIcon(qta.icon("fa.angle-double-right",color='white'))
        self.dashboardbt.setFixedSize(50, 50)
        self.dashboardbt.setStyleSheet("QPushButton { text-align: center;border-style: outset;color: #ffffff;}")
        self.dashboardbt.setText("")
        if self.role == "staff":
            self.trainingbt.setFixedSize(50, 50)
            self.trainingbt.setStyleSheet("QPushButton { text-align: center;border-style: outset;color: #ffffff;}")
            self.trainingbt.setText("")
        if self.role == "hr":
            self.adddepartmentbt.setFixedSize(50, 50)
            self.adddepartmentbt.setStyleSheet("QPushButton { text-align: center;border-style: outset;color: #ffffff;}")
            self.adddepartmentbt.setText("")
        self.historybt.setFixedSize(50, 50)
        self.historybt.setStyleSheet("QPushButton { text-align: center;border-style: outset;color: #ffffff;}")
        self.historybt.setText("")
        self.accountButton.setFixedSize(50, 50)
        self.accountButton.setStyleSheet("QPushButton { text-align: center;border-style: outset;color: #ffffff;}")
        self.accountButton.setText("")
        self.logoutButton.setFixedSize(50, 50)
        self.logoutButton.setStyleSheet("QPushButton { text-align: center;border-style: outset;color: #ffffff;}")
        self.logoutButton.setText("")
        self.title.setHidden(True)
        self.expandButton.clicked.connect(self.expand)

    #load data
    def loaddata(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test"
            )
            cursor = connection.cursor()

            query1 = "SELECT * FROM training"
            cursor.execute(query1)
            self.tempdata = cursor.fetchall()

            query2 = "SELECT * FROM ongoing"
            cursor.execute(query2)
            self.ongoing = cursor.fetchall()

            query3 = "SELECT * FROM completed"
            cursor.execute(query3)
            self.completed = cursor.fetchall()

            query4 = "SELECT * FROM registered"
            cursor.execute(query4)
            self.registereddata = cursor.fetchall()

            query5 = "SELECT * FROM approved"
            cursor.execute(query5)
            self.approveddata = cursor.fetchall()

            query6 = "SELECT * FROM rejected"
            cursor.execute(query6)
            self.rejecteddata = cursor.fetchall()

            if self.role == 'admin':
                self.setWindowTitle("Admin")
                query7 = "SELECT * FROM addedtraining"
                cursor.execute(query7)
                self.addedtrainingdata = cursor.fetchall()

                query8 = "SELECT * FROM edittraining"
                cursor.execute(query8)
                self.edittrainingdata = cursor.fetchall()

                query9 = "SELECT * FROM removetraining"
                cursor.execute(query9)
                self.removetrainingdata = cursor.fetchall()

            elif self.role == 'hr':
                self.setWindowTitle("HR Assistant")
                query7 = "SELECT * FROM staff"
                cursor.execute(query7)
                self.stafflist = cursor.fetchall()

                query8 = "SELECT * FROM done"
                cursor.execute(query8)
                self.done = cursor.fetchall()

            elif self.role == 'staff':
                self.setWindowTitle("Staff")
                query7 = "SELECT * FROM done"
                cursor.execute(query7)
                self.done = cursor.fetchall()

        except mysql.connector.Error as error:
            print("Failed to connect: {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
    #load data
    def update(self):
        try:
            connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="test"
            )
            cursor = connection.cursor()

            query1 = "SELECT * FROM training"
            cursor.execute(query1)
            tempdata1 = cursor.fetchall()

            for temp1 in tempdata1:
                if QDate.fromString(temp1[2],'M/d/yyyy') == QDate.currentDate():
                    query2 = "DELETE FROM training WHERE ID = %s"
                    values2 = (temp1[1],)
                    cursor.execute(query2,values2)
                    connection.commit()

                    query3 = "INSERT INTO ongoing (TITLE, ID, DATE, TIME, VENUE, COST, IMAGE, DEPARTMENT, DESCRIPTION) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values3 = (temp1[0],temp1[1],temp1[2],temp1[3],temp1[4],temp1[5],temp1[6],temp1[7],temp1[8])
                    cursor.execute(query3,values3)
                    connection.commit()

                    query4 = "SELECT * FROM approved WHERE TID = %s"
                    values4 = (temp1[1],)
                    cursor.execute(query4,values4)
                    tempdata2 = cursor.fetchall()

                    query5 = "DELETE FROM approved WHERE TID = %s"
                    values5 = (temp1[1],)
                    cursor.execute(query5,values5)
                    connection.commit()

                    cost = temp1[5] * len(tempdata2)
                    print(temp1[1]+" ["+temp1[0]+"] cost per person is RM"+str(temp1[5])+" which results in total of RM"+str(cost)+" with total participant of "+str(len(tempdata2)))

                    for temp2 in tempdata2:
                        query6 = "INSERT INTO done (TID, SID, HID) VALUES (%s, %s, %s)"
                        values6 = (temp2[0],temp2[1],temp2[2])
                        cursor.execute(query6,values6)
                        connection.commit()

                    query7 = "SELECT * FROM registered WHERE TID = %s"
                    values7 = (temp1[1],)
                    cursor.execute(query7,values7)
                    tempdata3 = cursor.fetchall()

                    query8 = "DELETE FROM registered WHERE TID = %s"
                    values8 = (temp1[1],)
                    cursor.execute(query8,values8)
                    connection.commit()

                    for temp3 in tempdata3:
                        query9 = "INSERT INTO rejected (TID, SID, HID) VALUES (%s, %s, %s)"
                        values9 = (temp3[0],temp3[1],"SYST")
                        cursor.execute(query9,values9)
                        connection.commit()

            query10 = "SELECT * FROM ongoing"
            cursor.execute(query10)
            tempdata4 = cursor.fetchall()
            for temp4 in tempdata4:
                if QDate.fromString(temp4[2],'M/d/yyyy') < QDate.currentDate():
                    query11 = "DELETE FROM ongoing WHERE ID = %s"
                    values11 = (temp4[1],)
                    cursor.execute(query11,values11)
                    connection.commit()

                    query12 = "INSERT INTO completed (TITLE, ID, DATE, TIME, VENUE, COST, IMAGE, DEPARTMENT, DESCRIPTION) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    values12 = (temp4[0],temp4[1],temp4[2],temp4[3],temp4[4],temp4[5],temp4[6],temp4[7],temp4[8])
                    cursor.execute(query12,values12)
                    connection.commit()                
        
        except mysql.connector.Error as error:
            print("Failed to connect: {}".format(error))

        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()                
if __name__ == '__main__':
    app = QApplication(sys.argv)
    loginwindow = LoginPage()
    loginwindow.show()
    sys.exit(app.exec())
