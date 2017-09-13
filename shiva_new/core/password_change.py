# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\user\durgesh.n\workspace\shiva\source\shiva\ui\password_change.ui'
#
# Created: Wed Dec 21 18:26:49 2016
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui


class Ui_password_change_win(object):

    def setupUi(self, password_change_win):
        password_change_win.setObjectName("password_change_win")
        password_change_win.resize(240, 141)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(password_change_win.sizePolicy().hasHeightForWidth())
        password_change_win.setSizePolicy(sizePolicy)
        password_change_win.setMaximumSize(QtCore.QSize(16777215, 500000))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icon/icons/User-Login-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        password_change_win.setWindowIcon(icon)
        self.verticalLayout = QtGui.QVBoxLayout(password_change_win)
        self.verticalLayout.setObjectName("verticalLayout")
        self.old_password_le = QtGui.QLineEdit(password_change_win)
        self.old_password_le.setEchoMode(QtGui.QLineEdit.Password)
        self.old_password_le.setObjectName("old_password_le")
        self.verticalLayout.addWidget(self.old_password_le)
        spacerItem = QtGui.QSpacerItem(20, 10, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.new_password_le = QtGui.QLineEdit(password_change_win)
        self.new_password_le.setEchoMode(QtGui.QLineEdit.Normal)
        self.new_password_le.setObjectName("new_password_le")
        self.verticalLayout.addWidget(self.new_password_le)
        self.new_password_01_le = QtGui.QLineEdit(password_change_win)
        self.new_password_01_le.setEchoMode(QtGui.QLineEdit.Normal)
        self.new_password_01_le.setObjectName("new_password_01_le")
        self.verticalLayout.addWidget(self.new_password_01_le)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cacnle_pb = QtGui.QPushButton(password_change_win)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cacnle_pb.sizePolicy().hasHeightForWidth())
        self.cacnle_pb.setSizePolicy(sizePolicy)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icon/icons/Logout-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.cacnle_pb.setIcon(icon1)
        self.cacnle_pb.setIconSize(QtCore.QSize(16, 16))
        self.cacnle_pb.setObjectName("cacnle_pb")
        self.horizontalLayout.addWidget(self.cacnle_pb)
        spacerItem1 = QtGui.QSpacerItem(20, 20, QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.change_pb = QtGui.QPushButton(password_change_win)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.change_pb.sizePolicy().hasHeightForWidth())
        self.change_pb.setSizePolicy(sizePolicy)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icon/icons/Login-01-48.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.change_pb.setIcon(icon2)
        self.change_pb.setObjectName("change_pb")
        self.horizontalLayout.addWidget(self.change_pb)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(password_change_win)
        QtCore.QMetaObject.connectSlotsByName(password_change_win)
        password_change_win.setTabOrder(self.new_password_01_le, self.change_pb)
        password_change_win.setTabOrder(self.change_pb, self.cacnle_pb)

    def retranslateUi(self, password_change_win):
        password_change_win.setWindowTitle(QtGui.QApplication.translate("password_change_win", "Change Password", None, QtGui.QApplication.UnicodeUTF8))
        self.old_password_le.setPlaceholderText(QtGui.QApplication.translate("password_change_win", "OLD PASSWORD", None, QtGui.QApplication.UnicodeUTF8))
        self.new_password_le.setPlaceholderText(QtGui.QApplication.translate("password_change_win", "NEW PASSWORD", None, QtGui.QApplication.UnicodeUTF8))
        self.new_password_01_le.setPlaceholderText(QtGui.QApplication.translate("password_change_win", "RETYPE NEW PASSWORD", None, QtGui.QApplication.UnicodeUTF8))
        self.cacnle_pb.setText(QtGui.QApplication.translate("password_change_win", "Cancel", None, QtGui.QApplication.UnicodeUTF8))
        self.change_pb.setText(QtGui.QApplication.translate("password_change_win", "Change", None, QtGui.QApplication.UnicodeUTF8))

import res_rc
import login_rc
