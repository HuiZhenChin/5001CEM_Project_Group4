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
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1421, 862)
        MainWindow.setStyleSheet(u"QFrame {\n"
"\n"
"	border-width: 1px;\n"
"	border-color: black;\n"
"	border-style: solid;\n"
"\n"
"}")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(380, 110, 961, 711))
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
        self.plainTextEdit_2 = QPlainTextEdit(self.frame)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(540, 150, 311, 41))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(18)
        self.plainTextEdit_2.setFont(font2)
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 3, 3);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 3px;")
        self.pushButton_2 = QPushButton(self.frame)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(740, 660, 111, 41))
        font3 = QFont()
        font3.setFamilies([u"Times New Roman"])
        font3.setPointSize(16)
        self.pushButton_2.setFont(font3)
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
        self.plainTextEdit_3 = QPlainTextEdit(self.frame)
        self.plainTextEdit_3.setObjectName(u"plainTextEdit_3")
        self.plainTextEdit_3.setGeometry(QRect(540, 220, 311, 41))
        self.plainTextEdit_3.setFont(font2)
        self.plainTextEdit_3.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 3, 3);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 3px;")
        self.plainTextEdit_4 = QPlainTextEdit(self.frame)
        self.plainTextEdit_4.setObjectName(u"plainTextEdit_4")
        self.plainTextEdit_4.setGeometry(QRect(540, 290, 311, 41))
        self.plainTextEdit_4.setFont(font2)
        self.plainTextEdit_4.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 3, 3);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 3px;")
        self.plainTextEdit_5 = QPlainTextEdit(self.frame)
        self.plainTextEdit_5.setObjectName(u"plainTextEdit_5")
        self.plainTextEdit_5.setGeometry(QRect(540, 360, 311, 41))
        self.plainTextEdit_5.setFont(font2)
        self.plainTextEdit_5.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 3, 3);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 3px;")
        self.plainTextEdit_6 = QPlainTextEdit(self.frame)
        self.plainTextEdit_6.setObjectName(u"plainTextEdit_6")
        self.plainTextEdit_6.setGeometry(QRect(540, 430, 311, 41))
        self.plainTextEdit_6.setFont(font2)
        self.plainTextEdit_6.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 3, 3);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 3px;")
        self.plainTextEdit_7 = QPlainTextEdit(self.frame)
        self.plainTextEdit_7.setObjectName(u"plainTextEdit_7")
        self.plainTextEdit_7.setGeometry(QRect(540, 500, 311, 41))
        self.plainTextEdit_7.setFont(font2)
        self.plainTextEdit_7.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 3, 3);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 3px;")
        self.plainTextEdit_8 = QPlainTextEdit(self.frame)
        self.plainTextEdit_8.setObjectName(u"plainTextEdit_8")
        self.plainTextEdit_8.setGeometry(QRect(540, 570, 311, 41))
        self.plainTextEdit_8.setFont(font2)
        self.plainTextEdit_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-color: rgb(3, 3, 3);\n"
"border-width: 1px;\n"
"border-style: solid;\n"
"border-radius: 3px;")
        self.pushButton_3 = QPushButton(self.frame)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(590, 660, 111, 41))
        self.pushButton_3.setFont(font3)
        self.pushButton_3.setStyleSheet(u"\n"
"QPushButton {\n"
"	\n"
"	background-color: rgb(6, 56, 135);\n"
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
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1421, 22))
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
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Discard", None))
        self.label_9.setText("")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())