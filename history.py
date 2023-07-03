import sys
import qtawesome as qta
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


# main window
class Main_window(QMainWindow):
    def __init__(self, role):
        QMainWindow.__init__(self)
        self.credential = ['ID', '101WIZARD', '011-10533650', 'jqgammers@gmail.com', role,
                           '']
        self.tempdata = [['ARTIFICIAL INTELLIGENCE', 'T104', '23Dec2025', '03.04', 'Hall A', '3000',
                          '', '30', None,
                          'AI is the development of computer systems that is able to perform tasks that require human intelligence. AI can learn and perform complex problem-solving. In this training, participants will understand what is an AI model, determine the impact of AI, develop and design a simple AI model .'],
                         ['CYBERSECURITY', 'T105', '23Dec2024', '04.05', 'Hall B', '30000',
                          '', '30', None,
                          'Cybersecurity is the practice of protecting critical systems and sensitive information from digital attacks. In this training, participants will learn about different types of cyber attacks, acquire knowledge and skills to protect digital systems, networks, and data from unauthorized access and involve in hands-on practical activities.'],
                         ['MARKETING', 'T103', '6/24/2023', '10.00 AM', 'Alpha Enterprise Conference Hall', '2000',
                          '', '45', None,
                          'Marketing is the activity of promoting, market researching and advertising of products or services. In this training, participants will learn about market research, consumer behaviour, branding, advertising and digital marketing strategies, involve in interactive sessions to study the real-world case studies,  gain insight into promoting and building the digital platforms and apply data analytics skills to implement the marketing plans.'],
                         ['Leadership', 'T110', '23Dec2025', '03.04', 'Hall A', '3000',
                          '', '30', None,
                          'Leadership is the behaviour of directing and leading a group of people to achieve a goal. In this training, participants will involve in various activities such as team building, learn about various communication techniques and decision-making strategies and acquire knowledge of using practical tools to enhance the leadership capabilities.'],
                         ['Networking', 'T109', '23Dec2025', '03.04', 'Hall A', '3000',
                          '', '30', None,
                          'Networking is a practice of transporting data between nodes over a shared medium in an information system. In this training, participants will learn about network protocols, IP addressing, routing, network security, and troubleshooting techniques, gain practical knowledge by setting up and configuring network devices, monitoring network performance, and implementing security measures.']]


        if role == "hr":
            self.setWindowTitle("HR Assistant")
            self.approveddata = [['T105', 'S104', 'H102']]
            self.rejecteddata = [['T103', 'S104', 'H102']]
            self.ongoing = [['Agile Development', 'T167', '23Dec2025', '03.04', 'Hall A', '3000',
                             '', '30', None,
                             'Agile methodology allows the project to run in a dynamic and face-paced environment. In this training, participants will understand the principles of agile project management, learn how to break down a complex project into smaller tasks, create prioritized backlogs and learn how to use tools such as Kanban Board or Gantt Chart to keep track of the work progress. ']]
            self.completed = [['Management', 'T111', '23Dec2025', '03.04', 'Hall A', '3000',
                               '', '30', None,
                                'Management is the coordination and administration of tasks to achieve a goal. Such administration activities include setting the organization’s strategy and coordinating the efforts of staff to accomplish these objectives through the application of available resources. Management can also refer to the seniority structure of staff members within an organization.']]
        elif role == "admin":
            self.setWindowTitle("Admin")
            self.addedtrainingdata = [['A102', 'T104', '01Dec2025']]
            self.edittrainingdata = [['A102', 'T105', '20Dec2025']]
            self.removetrainingdata = [['A102', '21Dec2025', 'Management', 'T111', '23Dec2025', '03.04', 'Hall A', '3000',
                                        '', '30', None,
                                        'Management is the coordination and administration of tasks to achieve a goal. Such administration activities include setting the organization’s strategy and coordinating the efforts of staff to accomplish these objectives through the application of available resources. Management can also refer to the seniority structure of staff members within an organization.']]
        else:
            self.setWindowTitle("Staff")
            self.registereddata = [['T104', 'ID']]
            self.approveddata = [['T105', 'S103', 'H102']]
            self.rejecteddata = [['T103', 'S104', 'H102']]
            self.done = [['T167', 'S105', 'H102'], ['T111', 'S103', 'H102']]
            self.ongoing = [['Agile Development', 'T167', '23Dec2025', '03.04', 'Hall A', '3000',
                             '', '30', None,
                             'Agile methodology allows the project to run in a dynamic and face-paced environment. In this training, participants will understand the principles of agile project management, learn how to break down a complex project into smaller tasks, create prioritized backlogs and learn how to use tools such as Kanban Board or Gantt Chart to keep track of the work progress. ']]
            self.completed = [['Management', 'T111', '23Dec2025', '03.04', 'Hall A', '3000',
                               '', '30', None,
                               'Management is the coordination and administration of tasks to achieve a goal. Such administration activities include setting the organization’s strategy and coordinating the efforts of staff to accomplish these objectives through the application of available resources. Management can also refer to the seniority structure of staff members within an organization.']]
        self.widget = QWidget(self)
        self.title = QLabel(role)
        self.title.setStyleSheet("QLabel{font-size: 18pt;}")
        self.current = QLabel("Dashboard")
        self.current.setStyleSheet("QLabel{font-size: 18pt;}")

        # history menu
        self.Historymenu = QHBoxLayout()
        self.Historymenu.setAlignment(Qt.AlignmentFlag.AlignRight)

        # create those buttons according to specific role
        # once create, connect the function and hide button first
        if role == 'admin':
            self.addedbt = QPushButton('Added Training')
            self.addedbt.setFixedSize(150, 35)
            self.addedbt.setStyleSheet(
                "QPushButton{background-color: #2B5336; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.addedbt.clicked.connect(self.adminAdded)
            self.addedbt.hide()
            self.modifiedbt = QPushButton('Modified Training')
            self.modifiedbt.setFixedSize(150, 35)
            self.modifiedbt.setStyleSheet(
                "QPushButton{background-color: #063887; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.modifiedbt.clicked.connect(self.adminModify)
            self.modifiedbt.hide()
            self.removebt = QPushButton('Remove Training')
            self.removebt.setFixedSize(150, 35)
            self.removebt.setStyleSheet(
                "QPushButton{background-color:  #8B0000; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.removebt.clicked.connect(self.adminRemove)
            self.removebt.hide()
            # add those buttons to history menu
            self.Historymenu.addWidget(self.addedbt)
            self.Historymenu.addWidget(self.modifiedbt)
            self.Historymenu.addWidget(self.removebt)
        if role == 'hr':
            self.approvebt = QPushButton('Approved Participant')
            self.approvebt.setFixedSize(150, 35)
            self.approvebt.setStyleSheet(
                "QPushButton{background-color: #2B5336; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.approvebt.clicked.connect(self.hrApprove)
            self.approvebt.hide()
            self.rejectbt = QPushButton('Rejected Participant')
            self.rejectbt.setFixedSize(150, 35)
            self.rejectbt.setStyleSheet(
                "QPushButton{background-color: black; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.rejectbt.clicked.connect(self.hrReject)
            self.rejectbt.hide()
            self.Historymenu.addWidget(self.approvebt)
            self.Historymenu.addWidget(self.rejectbt)
        if role == 'staff':
            self.completedbt = QPushButton('Completed Training')
            self.completedbt.setFixedSize(150, 35)
            self.completedbt.setStyleSheet(
                "QPushButton{background-color: #2B5336; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.completedbt.clicked.connect(self.staffcomplete)
            self.completedbt.hide()
            self.rejectedbt = QPushButton('Rejected Request')
            self.rejectedbt.setFixedSize(150, 35)
            self.rejectedbt.setStyleSheet(
                "QPushButton{background-color: black; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.rejectedbt.clicked.connect(self.staffreject)
            self.rejectedbt.hide()
            self.Historymenu.addWidget(self.completedbt)
            self.Historymenu.addWidget(self.rejectedbt)

        # scroll area
        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loadDashboard()

        ##staff
        self.trainingwid = QWidget()
        self.trainingwindow = QVBoxLayout(self.trainingwid)
        self.loadTraining()

        # set the size of scroll area
        self.windowscroll = QScrollArea()
        self.windowscroll.setMinimumSize(QSize(800, 500))
        self.windowscroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.windowscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.windowscroll.setWidget(self.dashboardwid)
        self.windowscroll.setWidgetResizable(True)
        self.windowscroll.setWidget(self.trainingwid)
        self.windowscroll.setWidgetResizable(True)

        # content
        self.content = QVBoxLayout()
        self.content.addWidget(self.current)
        self.content.addLayout(self.Historymenu)
        self.content.addWidget(self.windowscroll)
        self.content.addStretch()

        # side menu
        # create icon at the side menu
        icon = qta.icon("fa.angle-double-right")
        self.expandButton = QPushButton(icon, '')
        self.expandButton.setIconSize(QSize(35, 35))
        self.expandButton.setFixedSize(50, 50)
        self.expandButton.clicked.connect(self.expand)

        self.dashboardbt = QPushButton(qta.icon("ei.dashboard"), '')
        self.dashboardbt.setIconSize(QSize(35, 35))
        self.dashboardbt.setFixedSize(50, 50)
        self.dashboardbt.clicked.connect(self.dashboard)

        if role == "staff":
            self.trainingbt = QPushButton(qta.icon("fa5.list-alt"), '')
            self.trainingbt.setIconSize(QSize(35, 35))
            self.trainingbt.setFixedSize(50, 50)
            self.trainingbt.clicked.connect(self.trainingListStatus)

        self.historybt = QPushButton(qta.icon("msc.history"), '')
        self.historybt.setIconSize(QSize(35, 35))
        self.historybt.setFixedSize(50, 50)

        # page to show when click on particular button
        if role == 'staff':
            self.historybt.clicked.connect(self.staffcomplete)

        if role == 'admin':
            self.historybt.clicked.connect(self.adminAdded)

        if role == "hr":
            self.historybt.clicked.connect(self.hrApprove)

        self.accountButton = QPushButton(qta.icon("msc.account"), '')
        self.accountButton.setIconSize(QSize(35, 35))
        self.accountButton.setFixedSize(50, 50)
        self.accountButton.clicked.connect(self.account)

        self.logoutButton = QPushButton(qta.icon("ri.logout-box-r-line"), '')
        self.logoutButton.setIconSize(QSize(35, 35))
        self.logoutButton.setFixedSize(50, 50)
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
        self.sidemenu.addLayout(self.sidemenuheader, 1)
        self.sidemenu.addLayout(self.sidemenucontent, 100)
        self.sidemenu.addLayout(self.sidemenufooter, 1)
        self.sidemenu.addStretch()

        # whole window
        self.layout = QHBoxLayout()
        self.layout.addLayout(self.sidemenu, 1)
        self.layout.addLayout(self.content, 100)

        self.widget.setLayout(self.layout)
        self.setCentralWidget(self.widget)

    def loadDashboard(self):
        dashboard = QLabel("Dashboard")
        self.dashboardwindow.addWidget(dashboard)

    def loadTraining(self):
        training = QLabel("Training")
        self.trainingwindow.addWidget(training)

    def hrApprove(self):
        self.current.setText("History")
        self.approvebt.show()
        self.rejectbt.show()

        HistoryNoTitle = QLabel("No.")
        HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingTitle = QLabel("Training Title")
        HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryDateList = QLabel("Date")
        HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryParticipantName = QLabel("Participant Name")
        HistoryParticipantName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryHRName = QLabel("HR Name")
        HistoryHRName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        approveParticipantDetails = QGridLayout()
        approveParticipantDetails.addWidget(HistoryNoTitle, 0, 0)
        approveParticipantDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        approveParticipantDetails.addWidget(HistoryTrainingTitle, 0, 2)
        approveParticipantDetails.addWidget(HistoryDateList, 0, 3)
        approveParticipantDetails.addWidget(HistoryParticipantName, 0, 4)
        approveParticipantDetails.addWidget(HistoryHRName, 0, 5)

        approveParticipantData = []

        for temp in self.approveddata:
            for tempa in self.tempdata:
                if temp[0] == tempa[1]:
                    approveParticipantData.append([tempa[0], tempa[1], tempa[2], temp[1], temp[2]])

        for temp in self.approveddata:
            for tempa in self.ongoing:
                if temp[0] == tempa[1]:
                    approveParticipantData.append([tempa[0], tempa[1], tempa[2], temp[1], temp[2]])

        for temp in self.approveddata:
            for tempa in self.completed:
                if temp[0] == tempa[1]:
                    approveParticipantData.append([tempa[0], tempa[1], tempa[2], temp[1], temp[2]])

        count = 1

        for i in approveParticipantData:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Ttitle = QLabel(i[0])
            Date = QLabel(i[2])
            ParticipantName = QLabel(i[3])
            HRID = QLabel(i[4])
            approveParticipantDetails.addWidget(number, count, 0)
            approveParticipantDetails.addWidget(TID, count, 1)
            approveParticipantDetails.addWidget(Ttitle, count, 2)
            approveParticipantDetails.addWidget(Date, count, 3)
            approveParticipantDetails.addWidget(ParticipantName, count, 4)
            approveParticipantDetails.addWidget(HRID, count, 5)
            count += 1

        approveParticipantwid = QWidget()
        approveParticipantwindow = QVBoxLayout(approveParticipantwid)
        approveParticipantwindow.addLayout(approveParticipantDetails)
        approveParticipantwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        approveParticipantwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(approveParticipantwid)

    def hrReject(self):
        self.current.setText("History")
        self.approvebt.show()
        self.rejectbt.show()

        HistoryNoTitle = QLabel("No.")
        HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingTitle = QLabel("Training Title")
        HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryDateList = QLabel("Date")
        HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryParticipantName = QLabel("Participant Name")
        HistoryParticipantName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryHRName = QLabel("HR Name")
        HistoryHRName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        rejectParticipantDetails = QGridLayout()
        rejectParticipantDetails.addWidget(HistoryNoTitle, 0, 0)
        rejectParticipantDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        rejectParticipantDetails.addWidget(HistoryTrainingTitle, 0, 2)
        rejectParticipantDetails.addWidget(HistoryDateList, 0, 3)
        rejectParticipantDetails.addWidget(HistoryParticipantName, 0, 4)
        rejectParticipantDetails.addWidget(HistoryHRName, 0, 5)

        rejectParticipantData = []

        for temp in self.rejecteddata:
            for tempa in self.tempdata:
                if temp[0] == tempa[1]:
                    rejectParticipantData.append([tempa[0], tempa[1], tempa[2], temp[1], temp[2]])

        for temp in self.rejecteddata:
            for tempa in self.ongoing:
                if temp[0] == tempa[1]:
                    rejectParticipantData.append([tempa[0], tempa[1], tempa[2], temp[1], temp[2]])

        for temp in self.rejecteddata:
            for tempa in self.completed:
                if temp[0] == tempa[1]:
                    rejectParticipantData.append([tempa[0], tempa[1], tempa[2], temp[1], temp[2]])

        count = 1

        for i in rejectParticipantData:
            number = QLabel(str(count))
            TID = QLabel(i[1])
            Ttitle = QLabel(i[0])
            Date = QLabel(i[2])
            ParticipantName = QLabel(i[3])
            HRID = QLabel(i[4])
            rejectParticipantDetails.addWidget(number, count, 0)
            rejectParticipantDetails.addWidget(TID, count, 1)
            rejectParticipantDetails.addWidget(Ttitle, count, 2)
            rejectParticipantDetails.addWidget(Date, count, 3)
            rejectParticipantDetails.addWidget(ParticipantName, count, 4)
            rejectParticipantDetails.addWidget(HRID, count, 5)
            count += 1

        rejectParticipantwid = QWidget()
        rejectParticipantwindow = QVBoxLayout(rejectParticipantwid)
        rejectParticipantwindow.addLayout(rejectParticipantDetails)
        rejectParticipantwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        rejectParticipantwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(rejectParticipantwid)

    def adminAdded(self):
        self.current.setText("History")
        self.addedbt.show()
        self.modifiedbt.show()
        self.removebt.show()

        HistoryNoTitle = QLabel("No.")
        HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingTitle = QLabel("Training Title")
        HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryDateList = QLabel("Date")
        HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryAdminName = QLabel("Admin")
        HistoryAdminName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        addDetails = QGridLayout()
        addDetails.addWidget(HistoryNoTitle, 0, 0)
        addDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        addDetails.addWidget(HistoryTrainingTitle, 0, 2)
        addDetails.addWidget(HistoryDateList, 0, 3)
        addDetails.addWidget(HistoryAdminName, 0, 4)

        addeddata = []

        for temp in self.addedtrainingdata:
            for tempa in self.tempdata:
                if temp[1] == tempa[1]:
                    addeddata.append([tempa[0], temp[0], temp[1], temp[2]])

        count = 1

        for i in addeddata:
            number = QLabel(str(count))
            TID = QLabel(i[2])
            Title = QLabel(i[0])
            Date = QLabel(i[3])
            Admin = QLabel(i[1])
            addDetails.addWidget(number, count, 0)
            addDetails.addWidget(TID, count, 1)
            addDetails.addWidget(Title, count, 2)
            addDetails.addWidget(Date, count, 3)
            addDetails.addWidget(Admin, count, 4)
            count += 1

        addwid = QWidget()
        addwindow = QVBoxLayout(addwid)
        addwindow.addLayout(addDetails)
        addwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        addwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(addwid)

    def adminModify(self):
        self.current.setText("History")
        self.addedbt.show()
        self.modifiedbt.show()
        self.removebt.show()

        HistoryNoTitle = QLabel("No.")
        HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingTitle = QLabel("Training Title")
        HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryDateList = QLabel("Date")
        HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryAdminName = QLabel("Admin")
        HistoryAdminName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        editDetails = QGridLayout()
        editDetails.addWidget(HistoryNoTitle, 0, 0)
        editDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        editDetails.addWidget(HistoryTrainingTitle, 0, 2)
        editDetails.addWidget(HistoryDateList, 0, 3)
        editDetails.addWidget(HistoryAdminName, 0, 4)

        editdata = []

        for temp in self.edittrainingdata:
            for tempa in self.tempdata:
                if temp[1] == tempa[1]:
                    editdata.append([tempa[0], temp[0], temp[1], temp[2]])


        count = 1

        for i in editdata:
            number = QLabel(str(count))
            TID = QLabel(i[2])
            Title = QLabel(i[0])
            Date = QLabel(i[3])
            Admin = QLabel(i[1])
            editDetails.addWidget(number, count, 0)
            editDetails.addWidget(TID, count, 1)
            editDetails.addWidget(Title, count, 2)
            editDetails.addWidget(Date, count, 3)
            editDetails.addWidget(Admin, count, 4)
            count += 1

        editwid = QWidget()
        editwindow = QVBoxLayout(editwid)
        editwindow.addLayout(editDetails)
        editwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        editwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(editwid)

    def adminRemove(self):
        self.current.setText("History")
        self.addedbt.show()
        self.modifiedbt.show()
        self.removebt.show()

        HistoryNoTitle = QLabel("No.")
        HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingIDTitle = QLabel("Training ID")
        HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryTrainingTitle = QLabel("Training Title")
        HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryDateList = QLabel("Date")
        HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        HistoryAdminName = QLabel("Admin")
        HistoryAdminName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        removeDetails = QGridLayout()
        removeDetails.addWidget(HistoryNoTitle, 0, 0)
        removeDetails.addWidget(HistoryTrainingIDTitle, 0, 1)
        removeDetails.addWidget(HistoryTrainingTitle, 0, 2)
        removeDetails.addWidget(HistoryDateList, 0, 3)
        removeDetails.addWidget(HistoryAdminName, 0, 4)

        removedata = []

        for temp in self.removetrainingdata:
            removedata.append([temp[0], temp[1], temp[2], temp[3]])

        count = 1

        for i in removedata:
            number = QLabel(str(count))
            TID = QLabel(i[3])
            Title = QLabel(i[2])
            Date = QLabel(i[1])
            Admin = QLabel(i[0])
            removeDetails.addWidget(number, count, 0)
            removeDetails.addWidget(TID, count, 1)
            removeDetails.addWidget(Title, count, 2)
            removeDetails.addWidget(Date, count, 3)
            removeDetails.addWidget(Admin, count, 4)
            count += 1

        removewid = QWidget()
        removewindow = QVBoxLayout(removewid)
        removewindow.addLayout(removeDetails)
        removewindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        removewindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(removewid)

    def staffcomplete(self):
        self.current.setText("History")
        self.completedbt.show()
        self.rejectedbt.show()

        HistoryNoTitle = QLabel("No.")
        HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        HistoryTrainingID = QLabel("Training ID")
        HistoryTrainingID.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        HistoryDateList = QLabel("Date")
        HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        completedetails = QGridLayout()
        completedetails.addWidget(HistoryNoTitle, 0, 0)
        completedetails.addWidget(HistoryTrainingID, 0, 1)
        completedetails.addWidget(HistoryTrainingTitle, 0, 2)
        completedetails.addWidget(HistoryDateList, 0, 3)

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
            completedetails.addWidget(number, count, 0)
            completedetails.addWidget(TID, count, 1)
            completedetails.addWidget(Ttitle, count, 2)
            completedetails.addWidget(Date, count, 3)
            count += 1

        completewid = QWidget()
        completewindow = QVBoxLayout(completewid)
        completewindow.addLayout(completedetails)
        completewindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        completewindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(completewid)

    def staffreject(self):
        HistoryNoTitle = QLabel("No.")
        HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        HistoryTrainingID = QLabel("Training ID")
        HistoryTrainingID.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        HistoryTrainingTitle = QLabel("Training Title")
        HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        HistoryDateList = QLabel("Date")
        HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")

        rejectdetails = QGridLayout()
        rejectdetails.addWidget(HistoryNoTitle, 0, 0)
        rejectdetails.addWidget(HistoryTrainingID, 0, 1)
        rejectdetails.addWidget(HistoryTrainingTitle, 0, 2)
        rejectdetails.addWidget(HistoryDateList, 0, 3)

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
            rejectdetails.addWidget(number, count, 0)
            rejectdetails.addWidget(TID, count, 1)
            rejectdetails.addWidget(Ttitle, count, 2)
            rejectdetails.addWidget(Date, count, 3)
            count += 1

        rejectwid = QWidget()
        rejectwindow = QVBoxLayout(rejectwid)
        rejectwindow.addLayout(rejectdetails)
        rejectwindow.setAlignment(Qt.AlignmentFlag.AlignTop)
        rejectwindow.addStretch()

        # set scroll area widget
        self.windowscroll.setWidget(rejectwid)

    def dashboard(self):
        self.current.setText("DashBoard")
        if role == 'staff':
            self.completedbt.hide()
            self.rejectedbt.hide()
        if role == 'admin':
            self.addedbt.hide()
            self.modifiedbt.hide()
            self.removebt.hide()
        if role == 'hr':
            self.approvebt.hide()
            self.rejectbt.hide()

        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loadDashboard()
        self.windowscroll.setWidget(self.dashboardwid)
        print("Dashboard")

    def trainingListStatus(self):
        self.current.setText("Training List Status")
        self.completedbt.hide()
        self.rejectedbt.hide()
        self.trainingwid = QWidget()
        self.trainingwindow = QVBoxLayout(self.trainingwid)
        self.loadTraining()
        self.windowscroll.setWidget(self.trainingwid)
        print("Training List Status")

    def training(self):
        self.current.setText("Training")
        print("test")

    def account(self):
        self.current.setText("Account")
        print("test")

    def logout(self):
        self.hideall()
        self.current.setText("Logout")
        print("test")

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
        if role == "hr":
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
    role = input("Enter Role: ")
    app = QApplication(sys.argv)
    window = Main_window(role)
    window.show()
    sys.exit(app.exec())
