# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login2IodHFf.ui'
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
from PySide6.QtWidgets import (QApplication, QFormLayout, QFrame, QGridLayout,
    QLabel, QMainWindow, QMenuBar, QPlainTextEdit,
    QPushButton, QSizePolicy, QStatusBar, QVBoxLayout,
    QWidget)
import logo - Copy_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1115, 775)
        MainWindow.setMinimumSize(QSize(0, 6))
        MainWindow.setMaximumSize(QSize(16777215, 16777215))
        MainWindow.setToolTipDuration(2)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(3, 28, 68);")
        self.widget_4 = QWidget(self.widget_2)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(40, 130, 0, 0))
        self.widget_4.setStyleSheet(u"background-color: rgb(212, 212, 212);")
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 150, 318, 51))
        self.label_2.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label = QLabel(self.widget_4)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 90, 318, 31))
        self.label.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.label_5 = QLabel(self.widget_4)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(70, 100, 318, 31))
        self.label_5.setStyleSheet(u"color: rgb(0, 0, 0)")
        self.frame = QFrame(self.widget_2)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(110, 260, 500, 401))
        self.frame.setMinimumSize(QSize(500, 80))
        font = QFont()
        font.setFamilies([u"Verdana Pro Semibold"])
        font.setPointSize(18)
        font.setBold(True)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"background-color: rgb(206, 206, 206)")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 40, 101, 21))
        font1 = QFont()
        font1.setFamilies([u"Copperplate Gothic Bold"])
        font1.setPointSize(18)
        font1.setBold(False)
        self.label_6.setFont(font1)
        self.plainTextEdit = QPlainTextEdit(self.frame)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(200, 140, 201, 31))
        self.plainTextEdit.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.plainTextEdit_2 = QPlainTextEdit(self.frame)
        self.plainTextEdit_2.setObjectName(u"plainTextEdit_2")
        self.plainTextEdit_2.setGeometry(QRect(200, 210, 201, 31))
        self.plainTextEdit_2.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.label_7 = QLabel(self.frame)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(70, 150, 121, 21))
        font2 = QFont()
        font2.setFamilies([u"Verdana Pro Cond Semibold"])
        font2.setPointSize(12)
        font2.setBold(True)
        self.label_7.setFont(font2)
        self.label_8 = QLabel(self.frame)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(70, 220, 121, 21))
        self.label_8.setFont(font2)
        self.pushButton = QPushButton(self.frame)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(320, 350, 75, 24))
        self.pushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout_2.addWidget(self.widget_2)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 1, 1, 1)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.widget = QWidget(self.centralwidget)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"background-color: rgb(227, 227, 227);")
        self.frame_2 = QFrame(self.widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(30, 20, 593, 70))
        self.frame_2.setMaximumSize(QSize(600, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.formLayout = QFormLayout(self.frame_2)
        self.formLayout.setObjectName(u"formLayout")
        self.label_3 = QLabel(self.frame_2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(600, 50))
        font3 = QFont()
        font3.setFamilies([u"Verdana Pro Black"])
        font3.setPointSize(36)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setTextFormat(Qt.RichText)
        self.label_3.setAlignment(Qt.AlignCenter)

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label_3)

        self.frame_3 = QFrame(self.widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(140, 90, 306, 46))
        self.frame_3.setMaximumSize(QSize(16777215, 100))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.gridLayout_2 = QGridLayout(self.frame_3)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_4 = QLabel(self.frame_3)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setEnabled(True)
        self.label_4.setMaximumSize(QSize(500, 50))
        self.label_4.setSizeIncrement(QSize(0, 0))
        self.label_4.setBaseSize(QSize(0, 0))
        font4 = QFont()
        font4.setFamilies([u"Verdana Pro Cond Semibold"])
        font4.setPointSize(16)
        font4.setBold(True)
        self.label_4.setFont(font4)
        self.label_4.setStyleSheet(u"")
        self.label_4.setAlignment(Qt.AlignCenter)

        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)

        self.frame_4 = QFrame(self.widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setGeometry(QRect(190, 310, 120, 80))
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(120, 280, 411, 391))
        icon = QIcon()
        icon.addFile(u":/logo/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(1000, 1000))

        self.verticalLayout.addWidget(self.widget)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1115, 22))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password: ", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Employee ID: ", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Employee ID: ", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"LOGIN", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Employee ID", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"Login", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"ALPHA ENTERPRISE", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Staff Training Tracking System", None))
        self.pushButton_2.setText("")
    # retranslateUi

