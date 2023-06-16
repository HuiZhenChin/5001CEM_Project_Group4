import sys
from PySide6.QtWidgets import QApplication, QMainWindow

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QMenuBar, QPushButton, QSizePolicy, QStatusBar,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1240, 925)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(250, 110, 961, 711))
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"border-style:solid;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(30, 30, 251, 261))
        font = QFont()
        font.setKerning(False)
        self.pushButton.setFont(font)
        self.pushButton.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(232, 232, 232);\n"
"border-width: 1px;\n"
"border-style: solid;")
        icon = QPixmap("profile.png")
        self.pushButton.setIcon(QIcon(icon))
        self.pushButton.setIconSize(icon.size())
        self.pushButton.setIconSize(QSize(250, 250))
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(300, 80, 191, 51))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"border-color: rgb(232, 232, 232);")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(300, 150, 191, 51))
        self.label_2.setFont(font1)
        self.label_2.setStyleSheet(u"border-color: rgb(232, 232, 232);")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(300, 220, 191, 51))
        self.label_3.setFont(font1)
        self.label_3.setStyleSheet(u"border-color: rgb(232, 232, 232);")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(300, 290, 191, 51))
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"border-color: rgb(232, 232, 232);")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(300, 360, 191, 51))
        self.label_5.setFont(font1)
        self.label_5.setStyleSheet(u"border-color: rgb(232, 232, 232);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(300, 430, 191, 51))
        self.label_6.setFont(font1)
        self.label_6.setStyleSheet(u"border-color: rgb(232, 232, 232);")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(300, 500, 191, 51))
        self.label_7.setFont(font1)
        self.label_7.setStyleSheet(u"border-color: rgb(232, 232, 232);")
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(300, 570, 191, 51))
        self.label_8.setFont(font1)
        self.label_8.setStyleSheet(u"border-color: rgb(232, 232, 232);")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(740, 660, 111, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(16)
        self.pushButton_2.setFont(font2)
        self.pushButton_2.setStyleSheet(u"\n"
"QPushButton {\n"
"	background-color: rgb(12, 12, 12);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 3px;\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"	\n"
"	\n"
"	background-color: rgb(223, 223, 223);\n"
"	color: rgb(4, 4, 4);\n"
"\n"
"}")
        self.label_9 = QLabel(self.frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(540, 80, 311, 41))
        self.label_9.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.label_10 = QLabel(self.frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(540, 150, 311, 41))
        self.label_10.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.label_11 = QLabel(self.frame)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(540, 220, 311, 41))
        self.label_11.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.label_12 = QLabel(self.frame)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(540, 290, 311, 41))
        self.label_12.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.label_13 = QLabel(self.frame)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(540, 360, 311, 41))
        self.label_13.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.label_14 = QLabel(self.frame)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setGeometry(QRect(540, 430, 311, 41))
        self.label_14.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.label_15 = QLabel(self.frame)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setGeometry(QRect(540, 500, 311, 41))
        self.label_15.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        self.label_16 = QLabel(self.frame)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setGeometry(QRect(540, 570, 311, 41))
        self.label_16.setStyleSheet(u"color: rgb(0, 0, 0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-width:1px;\n"
"border-style: solid;\n"
"border-color: rgb(0, 0, 0);\n"
"border-radius: 3px;")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1240, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Employee ID: ", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Full Name: ", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Age:", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Phone Number:", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Gender:", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Email:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Department:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password: ", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Edit", None))
        self.label_9.setText("")
        self.label_10.setText("")
        self.label_11.setText("")
        self.label_12.setText("")
        self.label_13.setText("")
        self.label_14.setText("")
        self.label_15.setText("")
        self.label_16.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())

