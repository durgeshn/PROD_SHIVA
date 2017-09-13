# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\user\durgesh.n\workspace\shiva\source\shiva\ui\loginUi.ui'
#
# Created: Wed Dec 21 16:14:42 2016
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_FormLogin(object):
    def setupUi(self, FormLogin):
        FormLogin.setObjectName("FormLogin")
        FormLogin.resize(370, 140)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/User-Login-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        FormLogin.setWindowIcon(icon)
        self.gridLayout = QtGui.QGridLayout(FormLogin)
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonQuit = QtGui.QPushButton(FormLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonQuit.sizePolicy().hasHeightForWidth())
        self.pushButtonQuit.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/Logout-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonQuit.setIcon(icon1)
        self.pushButtonQuit.setIconSize(QtCore.QSize(16, 16))
        self.pushButtonQuit.setObjectName("pushButtonQuit")
        self.horizontalLayout.addWidget(self.pushButtonQuit)
        spacerItem = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButtonLogin = QtGui.QPushButton(FormLogin)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonLogin.sizePolicy().hasHeightForWidth())
        self.pushButtonLogin.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/Login-01-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButtonLogin.setIcon(icon2)
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.horizontalLayout.addWidget(self.pushButtonLogin)
        self.gridLayout.addLayout(self.horizontalLayout, 3, 0, 1, 1)
        self.lineEditUser = QtGui.QLineEdit(FormLogin)
        self.lineEditUser.setEchoMode(QtGui.QLineEdit.Normal)
        self.lineEditUser.setObjectName("lineEditUser")
        self.gridLayout.addWidget(self.lineEditUser, 1, 0, 1, 1)
        self.lineEditPassword = QtGui.QLineEdit(FormLogin)
        self.lineEditPassword.setEchoMode(QtGui.QLineEdit.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.gridLayout.addWidget(self.lineEditPassword, 2, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.option_tb = QtGui.QToolButton(FormLogin)
        self.option_tb.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icon/icons/setup_page_document_settings-512.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.option_tb.setIcon(icon3)
        self.option_tb.setObjectName("option_tb")
        self.horizontalLayout_2.addWidget(self.option_tb)
        self.gridLayout.addLayout(self.horizontalLayout_2, 0, 0, 1, 1)

        self.retranslateUi(FormLogin)
        QtCore.QMetaObject.connectSlotsByName(FormLogin)
        FormLogin.setTabOrder(self.lineEditPassword, self.pushButtonLogin)
        FormLogin.setTabOrder(self.pushButtonLogin, self.pushButtonQuit)

    def retranslateUi(self, FormLogin):
        FormLogin.setWindowTitle(QtGui.QApplication.translate("FormLogin", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonQuit.setText(QtGui.QApplication.translate("FormLogin", "Quit", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButtonLogin.setText(QtGui.QApplication.translate("FormLogin", "Login", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditUser.setPlaceholderText(QtGui.QApplication.translate("FormLogin", "User Name", None, QtGui.QApplication.UnicodeUTF8))
        self.lineEditPassword.setPlaceholderText(QtGui.QApplication.translate("FormLogin", "Enter Password", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
import login_rc