import sys
import qtawesome as qta
from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *


class Main_window(QMainWindow):
    def __init__(self, role):
        QMainWindow.__init__(self)
        self.tempdata = ['Training 1', 'Training 2', 'Training 3', 'Training 4', 'Training 5', 'Training 6',
                         'Training 7']
        if role == "hr":
            self.setWindowTitle("HR Assistant")
        elif role == "admin":
            self.setWindowTitle("Admin")
        else:
            self.setWindowTitle("Staff")
        self.widget = QWidget(self)
        self.title = QLabel(role)
        self.title.setStyleSheet("QLabel{font-size: 18pt;}")
        self.current = QLabel("Dashboard")
        self.current.setStyleSheet("QLabel{font-size: 18pt;}")

        # history menu
        self.Historymenu = QHBoxLayout()
        self.Historymenu.setAlignment(Qt.AlignmentFlag.AlignRight)

        if role == 'admin':
            self.addedbt = QPushButton('Added Training')
            self.addedbt.setFixedSize(150, 35)
            self.addedbt.setStyleSheet(
                "QPushButton{background-color: #2B5336; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.addedbt.clicked.connect(self.adminAdded)
            self.addedbt.hide()
            self.modifiedbt =QPushButton('Modified Training')
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
            self.Historymenu.addWidget(self.addedbt)
            self.Historymenu.addWidget(self.modifiedbt)
            self.Historymenu.addWidget(self.removebt)
        if role == 'hr':
            self.droppedbt = QPushButton('Dropped Participant')
            self.droppedbt.setFixedSize(150, 35)
            self.droppedbt.setStyleSheet(
                "QPushButton{background-color: #063887; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                "QPushButton:hover { background-color: #959595; color: black;}")
            self.droppedbt.clicked.connect(self.hrDrop)
            self.droppedbt.hide()
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
            self.Historymenu.addWidget(self.droppedbt)
            self.Historymenu.addWidget(self.approvebt)
            self.Historymenu.addWidget(self.rejectbt)
        if role == 'staff':
            self.completedbt = QPushButton('Completed Training')
            self.completedbt.setFixedSize(150, 35)
            self.completedbt.setStyleSheet("QPushButton{background-color: #2B5336; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                                           "QPushButton:hover { background-color: #959595; color: black;}")
            self.completedbt.clicked.connect(self.staffcomplete)
            self.completedbt.hide()
            self.rejectedbt = QPushButton('Rejected Request')
            self.rejectedbt.setFixedSize(150, 35)
            self.rejectedbt.setStyleSheet("QPushButton{background-color: black; color: white; border-style: outset; border-width: 2px;border-color:black;font:bold;}"
                                          "QPushButton:hover { background-color: #959595; color: black;}")
            self.rejectedbt.clicked.connect(self.staffreject)
            self.rejectedbt.hide()
            self.Historymenu.addWidget(self.completedbt)
            self.Historymenu.addWidget(self.rejectedbt)

        #scroll area

        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loadDashboard()

        ##staff
        self.trainingwid= QWidget()
        self.trainingwindow= QVBoxLayout(self.trainingwid)
        self.loadTraining()

        #hr assistant
        self.dropwid= QWidget()
        self.dropwindow= QVBoxLayout(self.dropwid)
        self.loadDrop()

        self.windowscroll = QScrollArea()
        self.windowscroll.setMinimumSize(QSize(800,500))
        self.windowscroll.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.windowscroll.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
        self.windowscroll.setWidget(self.dashboardwid)
        self.windowscroll.setWidgetResizable(True)
        self.windowscroll.setWidget(self.trainingwid)
        self.windowscroll.setWidgetResizable(True)
        self.windowscroll.setWidget(self.dropwid)
        self.windowscroll.setWidgetResizable(True)

        # content
        self.content = QVBoxLayout()
        self.content.addWidget(self.current)
        self.content.addLayout(self.Historymenu)
        self.content.addWidget(self.windowscroll)
        self.content.addStretch()

        # side menu
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

        if role == "hr":
            self.dropbt = QPushButton(qta.icon("mdi.account-remove"), '')
            self.dropbt.setIconSize(QSize(35, 35))
            self.dropbt.setFixedSize(50, 50)
            self.dropbt.clicked.connect(self.dropParticipant)

        self.historybt = QPushButton(qta.icon("msc.history"), '')
        self.historybt.setIconSize(QSize(35, 35))
        self.historybt.setFixedSize(50, 50)

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
        if role == "hr":
            self.sidemenucontent.addWidget(self.dropbt)

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

    def loadDrop(self):
        dropped = QLabel("Drop Participants")
        self.dropwindow.addWidget(dropped)

    def hrApprove(self):
        self.current.setText("History")
        self.approvebt.show()
        self.rejectbt.show()
        self.droppedbt.show()

        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTrainingID = QVBoxLayout()
        self.HistoryTrainingIDTitle = QLabel("Training ID")
        self.HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList = QLabel("Date")
        self.HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.HistoryParticipant = QVBoxLayout()
        self.HistoryParticipantName= QLabel("Participant Name")
        self.HistoryParticipantName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryParticipant.addWidget(self.HistoryParticipantName)

        self.Historywid = QWidget()
        self.HistoryTable = QHBoxLayout(self.Historywid)
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)
        self.HistoryTable.addLayout(self.HistoryParticipant)
        self.HistoryTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.windowscroll.setWidget(self.Historywid)

    def hrDrop(self):

        self.current.setText("History")
        self.approvebt.show()
        self.rejectbt.show()
        self.droppedbt.show()

        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTrainingID = QVBoxLayout()
        self.HistoryTrainingIDTitle = QLabel("Training ID")
        self.HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList = QLabel("Date")
        self.HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.HistoryParticipant = QVBoxLayout()
        self.HistoryParticipantName = QLabel("Participant Name")
        self.HistoryParticipantName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryParticipant.addWidget(self.HistoryParticipantName)

        self.Historywid = QWidget()
        self.HistoryTable = QHBoxLayout(self.Historywid)
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)
        self.HistoryTable.addLayout(self.HistoryParticipant)
        self.HistoryTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.windowscroll.setWidget(self.Historywid)

    def hrReject(self):
        self.current.setText("History")
        self.approvebt.show()
        self.rejectbt.show()
        self.droppedbt.show()

        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTrainingID = QVBoxLayout()
        self.HistoryTrainingIDTitle = QLabel("Training ID")
        self.HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList = QLabel("Date")
        self.HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.HistoryParticipant = QVBoxLayout()
        self.HistoryParticipantName = QLabel("Participant Name")
        self.HistoryParticipantName.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryParticipant.addWidget(self.HistoryParticipantName)

        self.Historywid = QWidget()
        self.HistoryTable = QHBoxLayout(self.Historywid)
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)
        self.HistoryTable.addLayout(self.HistoryParticipant)
        self.HistoryTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.windowscroll.setWidget(self.Historywid)

    def adminAdded(self):
        self.current.setText("History")
        self.addedbt.show()
        self.modifiedbt.show()
        self.removebt.show()

        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTrainingID = QVBoxLayout()
        self.HistoryTrainingIDTitle = QLabel("Training ID")
        self.HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList = QLabel("Date")
        self.HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.Historywid = QWidget()
        self.HistoryTable = QHBoxLayout(self.Historywid)
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)
        self.HistoryTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.windowscroll.setWidget(self.Historywid)

    def adminModify(self):
        self.current.setText("History")
        self.addedbt.show()
        self.modifiedbt.show()
        self.removebt.show()

        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTrainingID = QVBoxLayout()
        self.HistoryTrainingIDTitle = QLabel("Training ID")
        self.HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList = QLabel("Date")
        self.HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.Historywid = QWidget()
        self.HistoryTable = QHBoxLayout(self.Historywid)
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)
        self.HistoryTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.windowscroll.setWidget(self.Historywid)

    def adminRemove(self):
        self.current.setText("History")
        self.addedbt.show()
        self.modifiedbt.show()
        self.removebt.show()

        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTrainingID = QVBoxLayout()
        self.HistoryTrainingIDTitle = QLabel("Training ID")
        self.HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList = QLabel("Date")
        self.HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.Historywid = QWidget()
        self.HistoryTable = QHBoxLayout(self.Historywid)
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)
        self.HistoryTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.windowscroll.setWidget(self.Historywid)

    def staffcomplete(self):
        self.current.setText("History")
        self.completedbt.show()
        self.rejectedbt.show()

        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTrainingID = QVBoxLayout()
        self.HistoryTrainingIDTitle = QLabel("Training ID")
        self.HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList = QLabel("Date")
        self.HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.Historywid = QWidget()
        self.HistoryTable = QHBoxLayout(self.Historywid)
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)
        self.HistoryTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.windowscroll.setWidget(self.Historywid)

    def staffreject(self):
        self.current.setText("History")
        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNoTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTrainingID = QVBoxLayout()
        self.HistoryTrainingIDTitle = QLabel("Training ID")
        self.HistoryTrainingIDTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTrainingTitle.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList = QLabel("Date")
        self.HistoryDateList.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.HistoryRejected = QVBoxLayout()
        self.HistoryRejectedReason = QLabel("Rejected Reason")
        self.HistoryRejectedReason.setStyleSheet("color: black; font-weight: bold; font-size: 16px;")
        self.HistoryRejected.addWidget(self.HistoryRejectedReason)

        self.Historywid = QWidget()
        self.HistoryTable = QHBoxLayout(self.Historywid)
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)
        self.HistoryTable.addLayout(self.HistoryRejected)
        self.HistoryTable.setAlignment(Qt.AlignmentFlag.AlignTop)

        self.windowscroll.setWidget(self.Historywid)


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
            self.droppedbt.hide()

        self.dashboardwid = QWidget()
        self.dashboardwindow = QVBoxLayout(self.dashboardwid)
        self.loadDashboard()
        self.windowscroll.setWidget(self.dashboardwid)
        print("Dashboard")

    def trainingListStatus(self):
        self.current.setText("Training List Status")
        self.completedbt.hide()
        self.rejectedbt.hide()
        self.trainingwid= QWidget()
        self.trainingwindow= QVBoxLayout(self.trainingwid)
        self.loadTraining()
        self.windowscroll.setWidget(self.trainingwid)
        print("Training List Status")

    def dropParticipant(self):
        self.current.setText("Drop Participant")
        self.approvebt.hide()
        self.rejectbt.hide()
        self.droppedbt.hide()
        self.dropwid = QWidget()
        self.dropwindow = QVBoxLayout(self.dropwid)
        self.loadDrop()
        self.windowscroll.setWidget(self.dropwid)
        print("Drop Participant")

    def training(self):
        self.current.setText("Training")
        print("Bill")

    def drop(self):
        self.current.setText("Drop")
        print("Bill")

    def account(self):
        self.current.setText("Account")
        print("Bill")

    def logout(self):
        self.hideall()
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
    role = input("Enter Role: ")
    app = QApplication(sys.argv)
    window = Main_window(role)
    window.show()
    sys.exit(app.exec())
