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
        self.current = QLabel("History")
        self.current.setStyleSheet("QLabel{font-size: 18pt;}")

        # history
        self.Historymenu = QHBoxLayout()
        self.Historymenu.setAlignment(Qt.AlignmentFlag.AlignRight)

        #history menu
        if role == 'admin':
            self.addedbt = QPushButton('Added Training')
            self.addedbt.setFixedSize(100,25)
            self.modifiedbt =QPushButton('Modified Training')
            self.removebt = QPushButton('Remove Training')

            self.Historymenu.addWidget(self.addedbt)
            self.Historymenu.addWidget(self.modifiedbt)
            self.Historymenu.addWidget(self.removebt)
        if role == 'hr':
            self.dropbt = QPushButton('Drop')
            self.dropbt.clicked.connect(self.show_popup)
            self.dropbt.setStyleSheet("QPushButton { background-color:red;border-style: outset;border-width: 1px;border-color:black;font:bold;width:60px;color:white;}")
            self.Historymenu.addWidget(self.dropbt)
        if role == 'staff':
            self.completedbt = QPushButton('Completed Training')
            self.rejectedbt = QPushButton('Rejected Request')

            self.Historymenu.addWidget(self.completedbt)
            self.Historymenu.addWidget(self.rejectedbt)

        #History Content
        
        self.HistoryNo = QVBoxLayout()
        self.HistoryNoTitle = QLabel("No.")
        self.HistoryNo.addWidget(self.HistoryNoTitle)

        self.HistoryTraining = QVBoxLayout()
        self.HistoryTrainingTitle = QLabel("Training Title")
        self.HistoryTraining.addWidget(self.HistoryTrainingTitle)

        self.HistoryTrainingID= QVBoxLayout()
        self.HistoryTrainingIDTitle= QLabel("Training ID")
        self.HistoryTrainingID.addWidget(self.HistoryTrainingIDTitle)

        self.HistoryRejected= QVBoxLayout()
        self.HistoryRejectedReason = QLabel("Rejected Reason")
        self.HistoryRejected.addWidget(self.HistoryRejectedReason)

        self.HistoryDate = QVBoxLayout()
        self.HistoryDateList= QLabel("Date")
        self.HistoryDate.addWidget(self.HistoryDateList)

        self.HistoryParticipant= QVBoxLayout()
        self.HistoryParticipantName= QLabel("Participant Name")
        self.HistoryParticipant.addWidget(self.HistoryParticipantName)


        #History Table
        self.HistoryTable = QHBoxLayout()
        self.HistoryTable.addLayout(self.HistoryNo)
        self.HistoryTable.addLayout(self.HistoryTrainingID)
        self.HistoryTable.addLayout(self.HistoryTraining)
        self.HistoryTable.addLayout(self.HistoryDate)

        if role == 'hr':
            self.HistoryTable.addLayout(self.HistoryParticipant)
            self.HistoryTable.addLayout(self.HistoryRejected)

        #History Main Window
        self.HistoryWindow = QVBoxLayout()
        self.HistoryWindow.addLayout(self.Historymenu)
        self.HistoryWindow.addLayout(self.HistoryTable)
        self.loadhistory(role)

        # content
        self.content = QVBoxLayout()
        self.content.addWidget(self.current)
        self.content.addLayout(self.HistoryWindow)
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
            self.trainingbt.clicked.connect(self.training)

        if role == "hr":
            self.dropbt = QPushButton(qta.icon("mdi.account-remove"), '')
            self.dropbt.setIconSize(QSize(35, 35))
            self.dropbt.setFixedSize(50, 50)
            self.dropbt.clicked.connect(self.drop)

        self.historybt = QPushButton(qta.icon("msc.history"), '')
        self.historybt.setIconSize(QSize(35, 35))
        self.historybt.setFixedSize(50, 50)
        self.historybt.clicked.connect(self.history)

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

    def loadhistory(self, role):
        print('bill')

    def hideall(self):
        print("Bill")

    def dashboard(self):
        self.hideall()
        self.current.setText("DashBoard")
        print("Bill")

    def training(self):
        self.hideall()
        self.current.setText("Training")
        print("Bill")

    def show_popup(self):
        popup = QMessageBox()
        popup.setWindowTitle("Drop participant")
        popup.setText("Participant Dropped!")
        popup.exec()

    def drop(self):
        self.hideall()
        self.current.setText("Drop")
        print("Bill")

    def history(self):
        self.hideall()
        self.current.setText("History")
        print("Bill")

    def account(self):
        self.hideall()
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
            self.dropbt.setText("Drop")
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
