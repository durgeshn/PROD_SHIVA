# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'homeUI.ui'
#
# Created: Mon Aug 21 14:05:36 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.4
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class homeUI(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1048, 549)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/homeicon/icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Form.setWindowIcon(icon)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(2, 2, 2, 2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.frame = QtGui.QFrame(Form)
        self.frame.setStyleSheet("QWidget\n"
        "{\n"
        "    color: #eff0f1;\n"
        "    background-color: #31363b;\n"
        "    outline: 0;\n"
        "}\n"
        "QWidget:item:hover\n"
        "{\n"
        "    background-color: #3D7848;\n"
        "\n"
        "}\n"
        "QWidget::item:selected {\n"
        "    background: #3D7848;\n"
        "}\n"
        "QAbstractButton:pressed {\n"
        "    background: #3D7848;\n"
        "}\n"
        "QComboBox\n"
        "{\n"
        "    selection-background-color: #3daee9;\n"
        "    border-style: solid;\n"
        "     border: 1px solid #76797C;\n"
        "     border-radius: 7px;\n"
        "     padding: 1px;\n"
        "    min-width: 7px;\n"
        "}\n"
        "QComboBox::drop-down {\n"
        "    border: 1px solid #5A5A5A;\n"
        "    background: #353535;\n"
        "}\n"
        "QComboBox::down-arrow:on, QComboBox::down-arrow:hover,\n"
        "QComboBox::down-arrow:focus\n"
        "{\n"
        "    image: url(:/images/rc/down_arrow.png);\n"
        "}\n"
        "QComboBox::down-arrow\n"
        "{\n"
        "    image: url(:/images/rc/down_arrow_disabled.png);\n"
        "}\n"
        "QAbstractItemView \n"
        "{\n"
        "    show-decoration-selected: 1;\n"
        "    selection-background-color: #3D7848;\n"
        "    alternate-background-color: #353535;\n"
        "    selection-color: #DDDDDD;\n"
        "}\n"
        "QLabel \n"
        "{\n"
        "    border: none;\n"
        "}\n"
        "QSplitter::handle \n"
        "{\n"
        "    border: 1px dashed #76797C;\n"
        "}\n"
        "QSplitter::handle:hover \n"
        "{\n"
        "    background-color: #787876;\n"
        "    border: 1px solid #76797C;\n"
        "}\n"
        "QSplitter::handle:horizontal \n"
        "{\n"
        "    width: 1px;\n"
        "}\n"
        "QSplitter::handle:vertical \n"
        "{\n"
        "    height: 1px;\n"
        "}\n"
        "QPushButton\n"
        "{\n"
        "    border-width: 1px;\n"
        "    border-style: solid;\n"
        "    padding: 5px;\n"
        "    outline: none;\n"
        "}\n"
        "QPushButton#pushButton,#pushButton_2,#pushButton_3,#pushButton_4\n"
        "{\n"
        "    border-radius: 14px;\n"
        "}\n"
        "QPushButton#pushButton_5,#pushButton_6\n"
        "{\n"
        "    border-radius: 10px;\n"
        "}\n"
        "QPushButton:hover\n"
        "{\n"
        "    border-color: #3D7848;\n"
        "    color: #3D7848;\n"
        "}\n"
        "QPushButton:disabled\n"
        "{\n"
        "    color:grey;\n"
        "}\n"
        "QLabel:disabled\n"
        "{\n"
        "    color:grey;\n"
        "}")
        self.frame.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.splitter = QtGui.QSplitter(self.frame)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.frame_2 = QtGui.QFrame(self.splitter)
        self.frame_2.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_2.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.gridLayout_2 = QtGui.QGridLayout(self.frame_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.horizontalLayout_10 = QtGui.QHBoxLayout()
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        self.label = QtGui.QLabel(self.frame_2)
        self.label.setObjectName("label")
        self.horizontalLayout_10.addWidget(self.label)
        self.label_2 = QtGui.QLabel(self.frame_2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_10.addWidget(self.label_2)
        spacerItem = QtGui.QSpacerItem(88, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.gridLayout_2.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_4 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.verticalLayout.addWidget(self.label_4)
        self.comboBox = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setObjectName("comboBox")
        self.verticalLayout.addWidget(self.comboBox)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)
        self.verticalLayout_20 = QtGui.QVBoxLayout()
        self.verticalLayout_20.setObjectName("verticalLayout_20")
        self.label_7 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_7.sizePolicy().hasHeightForWidth())
        self.label_7.setSizePolicy(sizePolicy)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_20.addWidget(self.label_7)
        self.comboBox_4 = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_4.sizePolicy().hasHeightForWidth())
        self.comboBox_4.setSizePolicy(sizePolicy)
        self.comboBox_4.setObjectName("comboBox_4")
        self.verticalLayout_20.addWidget(self.comboBox_4)
        self.gridLayout.addLayout(self.verticalLayout_20, 0, 1, 1, 1)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label_5 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_2.addWidget(self.label_5)
        self.comboBox_2 = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_2.sizePolicy().hasHeightForWidth())
        self.comboBox_2.setSizePolicy(sizePolicy)
        self.comboBox_2.setObjectName("comboBox_2")
        self.verticalLayout_2.addWidget(self.comboBox_2)
        self.gridLayout.addLayout(self.verticalLayout_2, 1, 0, 1, 1)
        self.verticalLayout_19 = QtGui.QVBoxLayout()
        self.verticalLayout_19.setObjectName("verticalLayout_19")
        self.label_6 = QtGui.QLabel(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setObjectName("label_6")
        self.verticalLayout_19.addWidget(self.label_6)
        self.comboBox_3 = QtGui.QComboBox(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.comboBox_3.sizePolicy().hasHeightForWidth())
        self.comboBox_3.setSizePolicy(sizePolicy)
        self.comboBox_3.setObjectName("comboBox_3")
        self.verticalLayout_19.addWidget(self.comboBox_3)
        self.gridLayout.addLayout(self.verticalLayout_19, 1, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 1, 0, 1, 1)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout_22 = QtGui.QVBoxLayout()
        self.verticalLayout_22.setObjectName("verticalLayout_22")
        self.label_8 = QtGui.QLabel(self.frame_2)
        self.label_8.setMinimumSize(QtCore.QSize(161, 0))
        self.label_8.setObjectName("label_8")
        self.verticalLayout_22.addWidget(self.label_8)
        self.listWidget = QtGui.QListWidget(self.frame_2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_22.addWidget(self.listWidget)
        self.gridLayout_4.addLayout(self.verticalLayout_22, 0, 0, 1, 1)
        self.verticalLayout_23 = QtGui.QVBoxLayout()
        self.verticalLayout_23.setObjectName("verticalLayout_23")
        self.label_9 = QtGui.QLabel(self.frame_2)
        self.label_9.setMinimumSize(QtCore.QSize(151, 0))
        self.label_9.setObjectName("label_9")
        self.verticalLayout_23.addWidget(self.label_9)
        self.listWidget_2 = QtGui.QListWidget(self.frame_2)
        self.listWidget_2.setEnabled(True)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_23.addWidget(self.listWidget_2)
        self.gridLayout_4.addLayout(self.verticalLayout_23, 0, 1, 1, 1)
        self.horizontalLayout_14 = QtGui.QHBoxLayout()
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.pushButton = QtGui.QPushButton(self.frame_2)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_14.addWidget(self.pushButton)
        self.pushButton_2 = QtGui.QPushButton(self.frame_2)
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_14.addWidget(self.pushButton_2)
        self.pushButton_3 = QtGui.QPushButton(self.frame_2)
        self.pushButton_3.setEnabled(True)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_14.addWidget(self.pushButton_3)
        self.pushButton_4 = QtGui.QPushButton(self.frame_2)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_14.addWidget(self.pushButton_4)
        self.gridLayout_4.addLayout(self.horizontalLayout_14, 1, 0, 1, 2)
        self.gridLayout_2.addLayout(self.gridLayout_4, 2, 0, 1, 1)
        self.frame_4 = QtGui.QFrame(self.splitter)
        self.frame_4.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.gridLayout_5 = QtGui.QGridLayout(self.frame_4)
        self.gridLayout_5.setContentsMargins(1, 1, 1, 1)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.textBrowser = QtGui.QTextBrowser(self.frame_4)
        self.textBrowser.setStyleSheet("")
        self.textBrowser.setLineWidth(2)
        self.textBrowser.setObjectName("textBrowser")
        self.gridLayout_5.addWidget(self.textBrowser, 0, 0, 1, 1)
        self.verticalLayout_4.addWidget(self.splitter)
        self.horizontalLayout_2.addWidget(self.frame)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Animator Home", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Welcome", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "User", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Select Project", None, QtGui.QApplication.UnicodeUTF8))
        self.label_7.setText(QtGui.QApplication.translate("Form", "Select Dept.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_5.setText(QtGui.QApplication.translate("Form", "Select Sequence", None, QtGui.QApplication.UnicodeUTF8))
        self.label_6.setText(QtGui.QApplication.translate("Form", "Select Shot", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Server Path Versions :", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Local Path Versions :", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton.setText(QtGui.QApplication.translate("Form", "Start session", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_2.setText(QtGui.QApplication.translate("Form", "SFA", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_3.setText(QtGui.QApplication.translate("Form", "Refresh", None, QtGui.QApplication.UnicodeUTF8))
        self.pushButton_4.setText(QtGui.QApplication.translate("Form", "End Session", None, QtGui.QApplication.UnicodeUTF8))

# import home_rc
