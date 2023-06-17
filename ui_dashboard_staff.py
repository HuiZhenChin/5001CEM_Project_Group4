# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_dashboard_staffIDECiQ.ui'
##
## Created by: Qt User Interface Compiler version 6.4.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

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
        MainWindow.resize(1328, 1103)
        MainWindow.setStyleSheet(u"background-color: rgb(199, 199, 199)")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(320, 80, 961, 711))
        font = QFont()
        font.setPointSize(4)
        self.frame.setFont(font)
        self.frame.setCursor(QCursor(Qt.ArrowCursor))
        self.frame.setStyleSheet(u"background-color: rgb(232, 232, 232);\n"
"border-color: rgb(0, 0, 0);\n"
"border-width: 1px;\n"
"border-style:solid;\n"
"")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(60, 80, 311, 241))
        self.widget.setStyleSheet(u"background-color: rgb(133, 157, 195)")
        self.line = QFrame(self.widget)
        self.line.setObjectName(u"line")
        self.line.setGeometry(QRect(0, 130, 311, 111))
        self.line.setStyleSheet(u"background-color: rgb(242, 250, 249);")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 150, 181, 31))
        font1 = QFont()
        font1.setFamilies([u"Times New Roman"])
        font1.setPointSize(22)
        self.label.setFont(font1)
        self.label.setStyleSheet(u"background-color: rgb(242, 250, 249);\n"
"border-color: rgb(242, 250, 249);\n"
"")
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(30, 200, 101, 31))
        font2 = QFont()
        font2.setFamilies([u"Times New Roman"])
        font2.setPointSize(14)
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
        self.pushButton_3 = QPushButton(self.widget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(190, 200, 101, 31))
        self.pushButton_3.setFont(font2)
        self.pushButton_3.setStyleSheet(u"\n"
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
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(860, 10, 71, 91))
        self.pushButton.setCursor(QCursor(Qt.PointingHandCursor))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"border-color: rgb(232, 232, 232);\n"
"\n"
"}\n"
"\n"
"\n"
"")
        icon = QIcon()
        icon.addFile(u"C:/Users/Hui Zhen/AppData/Local/Programs/Python/Python311/Lib/site-packages/qt6_applications/Qt/bin/filter.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QSize(50, 50))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1328, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Training Title", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"Register", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"Details", None))
        self.pushButton.setText("")
    # retranslateUi

