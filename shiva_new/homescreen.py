# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\python\shiva_new\homescreen3.ui'
#
# Created: Fri Mar 03 15:02:40 2017
#      by: pyside-uic 0.2.15 running on PySide 1.2.2
#
# WARNING! All changes made in this file will be lost!
# THIS IS SO WE CAN USE ALL THE MODULES FROM THE BELLOW LOCATION..............................................
import sys
sys.path.insert(0, r'\\stor\py\Packages\site-packages')
# This path so we have access to the module from inside maya.

# import neccessary libraries
from PySide import QtCore, QtGui, QtUiTools
from PySide.QtGui import QApplication, QMainWindow, QFileDialog, QMessageBox, QDialog, QTextBrowser, QWidget
import sys
import os
import pymysql
import subprocess
import shutil
import datetime
import platform

from homeUI import homeUI
# import from model package
from core.login import LoginDialog
# from model.Selectproject import Selectproject
from model.Selectprojectnew import Selectproject
from model.Copydata import Copydata
from model.Copylatestdata import Copylatestdata
from model.CopyLocaldata import CopyLocaldata
from model.dbhelper import dbhelper

#reading the config file
from ConfigParser import SafeConfigParser
parser = SafeConfigParser()
parser = SafeConfigParser()

config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
parser.read(config_path)
dbhost = parser.get('settings', 'dbhost')

# global variables
filename = None
framecount = None
ffmpeg = None
startframe = None
total = None
ps = None
username = None

# class for animator homescreen
class Homescreen_Animator(QWidget, homeUI):

    def __init__(self):

        """
        Add project list from project path
        """
        super(Homescreen_Animator, self).__init__()
        print "in homescreen original"
        self.setupUi(self)

    # def setupUi(self, Form):

        """
        UI elements declaration and signals
        :param Form:
        :return:None
        """

        osname = platform.system()
        # ui_path = os.path.join(os.path.dirname(__file__), 'homescreen.ui')
        # self = QtUiTools.QUiLoader().load(ui_path)
        # QtUiTools.QUiLoader().load(ui_path)
        # self.show()
        if osname == 'Windows':
            # parser.read(r'\\stor\py\TESTTALKDEMO\shiva_new\config.ini')
            self.projectpath = parser.get('project_settings', 'projectpath')
            self.localdrive = parser.get('project_settings', 'localdrive')
            if not os.path.exists(self.projectpath):
                dialog = QMessageBox.critical(self, 'Network Connection Error',
                                              'Project path is not accessible please check your network connection\nApplication will now Quit',
                                              buttons=QMessageBox.Ok)
                if dialog == QMessageBox.Ok:
                    QApplication.quit()
        elif osname == 'Linux':
            # self = QtUiTools.QUiLoader().load("/media/prafulls/New Volume/python/pycharm-23-5-2017-2pm/shiva_new/homescreen5.ui")
            print "read config for linux"
            # parser.read('config_linux.ini')
            self.projectpath = parser.get('project_settings', 'projectpath_linux')
            self.localdrive = parser.get('project_settings', 'localdrive_linux')
            if not os.path.exists(self.projectpath):
                dialog = QMessageBox.critical(self, 'Network Connection Error',
                                              'Project path is not accessible please check your network connection\nApplication will now Quit',
                                              buttons=QMessageBox.Ok)
                if dialog == QMessageBox.Ok:
                    QApplication.quit()

        else:
            print "Error"
        projects = os.listdir(self.projectpath)
        self.comboBox.addItem('Select Project')
        self.comboBox.addItems(projects)

        self.label_2.setText(username)
        self.comboBox.activated.connect(self.projectselected)
        # self.comboBox_4.activated.connect(self.deptActivated)
        self.comboBox_4.activated.connect(self.updateSequence)
        self.comboBox_2.activated.connect(self.updateShot)
        self.comboBox_3.activated.connect(self.shotActivated)
        # self.comboBox_4.activated.connect(self.deptActivated)

        self.pushButton.setEnabled(False)
        self.pushButton.clicked.connect(self.startsession)

        self.listWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget.connect(self.listWidget, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.serverlistitemRightclicked)
        self.listWidget.itemClicked.connect(self.listWidgetItemClicked)

        self.listWidget_2.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.listWidget_2.connect(self.listWidget_2, QtCore.SIGNAL("customContextMenuRequested(QPoint)"), self.locallistitemRightclicked)
        self.listWidget_2.itemClicked.connect(self.listWidget2_ItemClicked)

        self.listWidget_2.itemDoubleClicked.connect(self.openfile_clicked)

        self.pushButton_2.hide()

        self.pushButton_3.setEnabled(False)
        self.pushButton_3.clicked.connect(self.shotActivated)
        self.pushButton_4.setEnabled(False)
        self.pushButton_4.clicked.connect(self.endsessionbuttonClicked)

        self.textBrowser.setReadOnly(True)
        self.textBrowser.setOpenExternalLinks(True)
        self.textBrowser.setOpenLinks(False)
        # self.closeEvent = self.closeEvent()
        # self.actionExit.triggered.connect(self.close)
        # self.projectselected()

    def projectselected(self):

        """
        Call selectproject class-send all combobox,listwidgets objects
        :return:None
        """
        global ps, username
        self.c = self.comboBox
        self.c2 = self.comboBox_2
        self.c3 = self.comboBox_3
        self.c4 = self.comboBox_4
        l1 = self.listWidget
        l2 = self.listWidget_2

        startsession = self.pushButton
        endsession = self.pushButton_4
        refresh = self.pushButton_3
        textbrowser = self.textBrowser
        if self.c.currentText() != '':
            ps = Selectproject(self.projectpath, username, self.c, self.c2, self.c3, self.c4, l1, l2, self.localdrive, endsession, startsession, textbrowser, refresh)
            # ps = Selectprojectnew(self.projectpath, username, self.c, self.c2, self.c3, self.c4, l1, l2, self.localdrive)
        else:
            pass

    def updateSequence(self):
        global ps
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.textBrowser.clear()
        ps.updateSequence()

    def updateShot(self):

        """
        Call selectproject class method updateShot()
        :return:None
        """
        global ps
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.textBrowser.clear()
        ps.updateShot()
        
    def shotActivated(self):

        """
        Call selectproject class method deptActivated()
        pass
        :return:None
        """
        try:
            global ps
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.textBrowser.clear()
            self.project, self.epfold, self.epselected, self.shotselected, self.deptselected, self.description, self.filecount,\
            self.server_path, self.filetype, self.shotGeneric, self.fileext, self.local_path, self.movtype, self.movGeneric, self.shotpath, self.preview_path, self.comments = ps.shotActivated()
            self.srcpath = os.path.join(self.projectpath, self.project, self.epfold, self.epselected, self.shotselected, self.deptselected)
            # print "***************************************************"
            # print self.srcpath
            # self.pushButton.setEnabled(True)
        except Exception as e:
            print e
            print "No shots available"
            QMessageBox.critical(self, 'Filename Error', "No shots available")
        
    def startsession(self):

        """
        Start Session buttonclick event copy latest file from server to local drive
        Call class Copylatestdata
        :return:None
        """
        print "start session copy data to local drive"
        # self.pushButton.setEnabled(False)
        try:
            cd = Copylatestdata(self.server_path, self.localdrive, self.project, self.filetype, self.shotGeneric, self.c2, self.c3, self.c4, self.fileext)
            # print "copy done"
        except Exception as e:
            print e
            print "Check input"
            QMessageBox.critical(self, 'Filename Error', "Check input")
        self.shotActivated()

    def serverlistitemRightclicked(self, QPos):

        """
        Rightclick menu for listwidget
        :param QPos:
        :return: None
        """

        self.list_menu = QtGui.QMenu()
        menu_item = self.list_menu.addAction("Start Session")
        self.connect(menu_item, QtCore.SIGNAL("triggered()"), self.server_menu_itemClicked)
        parentPosition = self.listWidget.mapToGlobal(QtCore.QPoint(0, 0))
        self.list_menu.move(parentPosition + QPos)
        self.list_menu.show()
        # self.shotActivated()

    def server_menu_itemClicked(self):

        """
        Rightclick menu click event on current selected item in listwidget
        Copy current selected file from server to local drive
        :return: None
        """
        if self.listWidget.currentItem():

            currentFileName = str(self.listWidget.currentItem().text())
            # print currentFileName
            currentfilelist = currentFileName.split('\t')
            print currentfilelist[0], "------------------------------------------------"
            # print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&"
            # print self.server_path
            # print self.localdrive
            # print self.project, self.filetype, currentFileName, self.shotGeneric, self.c2, self.c3, self.c4, self.fileext
            cd = Copydata(self.server_path, self.localdrive, self.project, self.filetype, currentfilelist[0], self.shotGeneric, self.c2, self.c3, self.c4, self.fileext)
            # print "############", cd
        else:
            print "Invalid filename"
            QMessageBox.critical(self, 'Filename Error', 'Invalid filename')
        self.shotActivated()

            # print "copy done"
        
    def locallistitemRightclicked(self, QPos):

        """
        Right click menu for listwidget_2
        :param QPos:
        :return: None
        """
        self.list_menu = QtGui.QMenu()
        menu_item_4 = self.list_menu.addAction("Open file")
        self.list_menu.addSeparator()
        menu_item_1 = self.list_menu.addAction("SFA")
        # menu_item_2 = self.list_menu.addAction("SFC")
        # menu_item_3 = self.list_menu.addAction("End Session")
        self.connect(menu_item_1, QtCore.SIGNAL("triggered()"), self.sfa_menu_itemClicked)
        # self.connect(menu_item_2, QtCore.SIGNAL("triggered()"), self.sfc_menu_itemClicked)
        # self.connect(menu_item_3, QtCore.SIGNAL("triggered()"), self.endsession_menu_itemClicked)
        self.connect(menu_item_4, QtCore.SIGNAL("triggered()"), self.openfile_clicked)
        parentPosition = self.listWidget_2.mapToGlobal(QtCore.QPoint(0, 0))
        self.list_menu.move(parentPosition + QPos)
        self.list_menu.show() 
        
    def sfa_menu_itemClicked(self):

        """
        Call class CopyLocaldata to copy local drive file to server
        :return: None
        """
        msgbox = QMessageBox()
        reply = msgbox.question(self, 'Message',
                  "Are you sure want to \nsend for approval?", QtGui.QMessageBox.Yes |
                  QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        if reply == QtGui.QMessageBox.No:
            return
        if self.listWidget_2.currentItem():
            currentFileName = str(self.listWidget_2.currentItem().text())
            currentfilelist = currentFileName.split('\t')
            print currentfilelist[0], "------------------------------------------------"
            # print(currentFileName)
            cld = CopyLocaldata(self.server_path, self.local_path, self.project, self.filetype, currentfilelist[0], self.shotGeneric, self.c2, self.c3, self.c4, self.fileext, self.movtype, self.movGeneric)
            cld.copyop()
        else:
            print "Invalid filename"
            QMessageBox.critical(self, 'Filename Error', 'Invalid filename')
        self.shotActivated()


    def openfile_clicked(self):

        if self.listWidget_2.currentItem():
            currentFileName = str(self.listWidget_2.currentItem().text())
            currentfilelist = currentFileName.split('\t')
            print currentfilelist[0], "------------------------------------------------"
            openfilepath = os.path.join(self.local_path, currentfilelist[0])
            os.environ['PROD_SERVER'] = 'P:/badgers_and_foxes'
            subprocess.Popen(["C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe", openfilepath])
            print "file open from drive"
        else:
            print "Invalid filename"
            QMessageBox.critical(self, 'Filename Error', 'Invalid filename')

    def endsessionbuttonClicked(self):

        """
        Call class CopyLocaldata to copy local drive file to server
        :return: None
        """
        if self.listWidget_2.currentItem():
            currentFileName = str(self.listWidget_2.currentItem().text())
            currentfilelist = currentFileName.split('\t')
            print currentfilelist[0], "------------------------------------------------"
            # print(currentFileName)
            cld = CopyLocaldata(self.server_path, self.local_path, self.project, self.filetype, currentfilelist[0], self.shotGeneric, self.c2, self.c3, self.c4, self.fileext, self.movtype, self.movGeneric)
            cld.copyop(False)
        else:
            print "Invalid filename"
            QMessageBox.critical(self, 'Filename Error', 'Invalid filename')
        self.shotActivated()
        
    def sfc_menu_itemClicked(self):
        """
        Call class CopyLocaldata to copy local drive file to server
        :return:None
        """
        if self.listWidget_2.currentItem():
            currentFileName = str(self.listWidget_2.currentItem().text())
            print(currentFileName)
            cld = CopyLocaldata(self.server_path, self.local_path, self.project, self.filetype, currentFileName, self.shotGeneric, self.c2, self.c3, self.c4, self.fileext, self.movtype, self.movGeneric)
            cld.shfcopy()
        else:
            print "Invalid filename"
            QMessageBox.critical(self, 'Filename Error', 'Invalid filename')
        
    def endsession_menu_itemClicked(self):
        """
        :return: None
        """
        if self.listWidget_2.currentItem():
            currentFileName = str(self.listWidget_2.currentItem().text())
            # print(currentFileName)
        else:
            print "Invalid filename"
            QMessageBox.critical(self, 'Filename Error', 'Invalid filename')

    def listWidgetItemClicked(self):
        """
        Single click on listwidget to display information regarding shot in text editor
        :return: None
        """
        # print "in listwidgetitemclicked"
        # print self.listWidget.currentItem().text()
        self.textBrowser.clear()
        self.previouspath_link = None
        self.nextpath_link = None
        format = "%a %b %d %Y %H:%M:%S"
        today = datetime.datetime.today()
        today_datetime = today.strftime(format)

        self.textBrowser.setText("<span>************************************************</span>")
        self.textBrowser.append("<span>\n" + today_datetime + "</span>")
        self.textBrowser.append("<span>\n\nProject Name :- " + self.project+ "</span>")
        self.textBrowser.append("<span>\n\nEpisode :- " + self.epselected+ "</span>")
        self.textBrowser.append("<span>\n\nShot :- " + self.shotselected+ "</span>")
        self.textBrowser.append("<span>\n\nDepartment :- " + self.deptselected+ "</span>")
        self.textBrowser.append("<span>\n\nServer Path :- " + self.server_path+ "</span>")
        self.textBrowser.append("<span>\n\nLocal Path :- " + self.local_path+ "</span>")
        self.textBrowser.append("<span>\n\nFile Name :- "+str(self.listWidget.currentItem().text())+ "</span>")
        self.textBrowser.append("<span>\n\nFrame Count :- " + str(self.filecount)+ "</span>")
        self.textBrowser.append("<span>\n\nDescription :- " + self.description+ "</span>")
        self.textBrowser.append("<span>\n\n************************************************"+ "</span>")
        self.textBrowser.append("<span>\n\nMOV file list link -"+ "</span>")

        # print "----------------------------------------"
        # print self.shotpath

        shots_list = os.listdir(str(self.shotpath))
        # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", shots_list
        try:
            current_shotindex = shots_list.index(self.shotselected)
            lastshot = len(shots_list)
            # print lastshot
            # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", current_shotindex
            if current_shotindex == 1:

                # print "no previous shot"
                # print "---------", shots_list[current_shotindex + 1]
                next_shot = os.path.join(self.shotpath, shots_list[current_shotindex + 1], self.deptselected, self.preview_path)
                if os.path.exists(next_shot):
                    self.textBrowser.append("<span>\nPrevious Shot - Not Available</span>")
                    self.nextpath_link = "<a style=color:#00FFFF href='"+next_shot+"'>NextshotPath</a>"
                    self.textBrowser.append("<span>\nNext Shot - </span>"+self.nextpath_link)
                    # print next_shot
                else:
                    print "preview not available for next shot"
                    self.textBrowser.append("<span>\nPrevious Shot - Not Available</span>")
                    self.textBrowser.append("<span>\nNext Shot - Not Available</span>")
            elif current_shotindex == lastshot - 1:

                print "no next shot"
                # print "---------", shots_list[current_shotindex - 1]
                previous_shot = os.path.join(self.shotpath, shots_list[current_shotindex - 1], self.deptselected, self.preview_path)
                if os.path.exists(previous_shot):
                    self.previouspath_link = "<a style=color:#00FFFF href='" + previous_shot + "'>PreviousshotPath</a>"
                    self.textBrowser.append("<span>\nPrevious Shot - </span>"+self.previouspath_link)
                    self.textBrowser.append("<span>\nNext Shot - Not Available</span>")
                    # print previous_shot
                else:
                    print "previous shot is not available"
                    self.textBrowser.append("<span>\nPrevious Shot - Not Available</span>")
                    self.textBrowser.append("<span>\nNext Shot - Not Available</span>")
            else:

                # print "---------", shots_list[current_shotindex - 1]
                previousshot = os.path.join(self.shotpath, shots_list[current_shotindex - 1], self.deptselected, self.preview_path)
                # previous_mov = os.listdir(previousshot)
                # previousshot = os.path.join(previousshot, previous_mov[-1])
                # print "---------", shots_list[current_shotindex + 1]
                nextshot = os.path.join(self.shotpath, shots_list[current_shotindex + 1], self.deptselected, self.preview_path)
                # next_mov = os.listdir(nextshot)
                # nextshot = os.path.join(nextshot, next_mov[-1])
                if os.path.exists(previousshot):
                    self.previouspath_link = "<a style=color:#00FFFF href='" + previousshot + "'>PreviousshotPath</a>"
                    self.textBrowser.append("<span>\nPrevious Shot - </span>"+self.previouspath_link)
                else:
                    print "previous shot is not available"
                    self.textBrowser.append("<span>\nPrevious Shot - Not Available</span>")
                if os.path.exists(nextshot):
                    self.nextpath_link = "<a style=color:#00FFFF href='" + nextshot + "'>NextshotPath</a>"
                    self.textBrowser.append("<span>\nNext Shot - </span>"+self.nextpath_link)
                else:
                    print "next shot is not available"
                    self.textBrowser.append("<span>\nNext Shot - Not Available</span>")
                # print "----------", previousshot
                # print "----------", nextshot

        except Exception as e:
            print e
            print "error occured"
        self.textBrowser.append("<span>\n\n************************************************</span>")
        self.textBrowser.append("<span>\n\nComments :-</span>")
        if self.comments:
            commentdata = self.comments.split('~')
        else:
            commentdata = ['no comments']
        for i in commentdata:
            self.textBrowser.append("<span>" + i + "</span>")
        # self.textBrowser.append(self.textlink)

    def listWidget2_ItemClicked(self):
        """
        Single click on listwidget_2 to display information regarding shot in text editor
        :return: None
        """
        self.textBrowser.clear()
        format = "%a %b %d %Y %H:%M:%S"
        today = datetime.datetime.today()
        today_datetime = today.strftime(format)

        self.textBrowser.setText("<span>************************************************</span>")
        self.textBrowser.append("<span>\n" + today_datetime + "</span>")
        self.textBrowser.append("<span>\n\nProject Name :- " + self.project+ "</span>")
        self.textBrowser.append("<span>\n\nEpisode :- " + self.epselected+ "</span>")
        self.textBrowser.append("<span>\n\nShot :- " + self.shotselected+ "</span>")
        self.textBrowser.append("<span>\n\nDepartment :- " + self.deptselected+ "</span>")
        self.textBrowser.append("<span>\n\nLocal Path :- " + self.local_path+ "</span>")
        self.textBrowser.append("<span>\n\nServer Path :- " + self.server_path+ "</span>")
        self.textBrowser.append("<span>\n\nFile Name :- "+str(self.listWidget_2.currentItem().text())+ "</span>")
        self.textBrowser.append("<span>\n\nFrame Count :- " + str(self.filecount)+ "</span>")
        self.textBrowser.append("<span>\n\nDescription :- " + self.description + "</span>")
        self.textBrowser.append("<span>\n\n************************************************" + "</span>")
        self.textBrowser.append("<span>\n\nMOV file list link -" + "</span>")

        shots_list = os.listdir(str(self.shotpath))
        # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", shots_list
        try:
            current_shotindex = shots_list.index(self.shotselected)
            lastshot = len(shots_list)
            # print lastshot
            # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$", current_shotindex
            if current_shotindex == 1:

                # print "no previous shot"
                # print "---------", shots_list[current_shotindex + 1]
                next_shot = os.path.join(self.shotpath, shots_list[current_shotindex + 1], self.deptselected,
                                         self.preview_path)
                if os.path.exists(next_shot):
                    self.textBrowser.append("<span>\nPrevious Shot - Not Available</span>")
                    self.nextpath_link = "<a style=color:#00FFFF href='" + next_shot + "'>NextshotPath</a>"
                    self.textBrowser.append("<span>\nNext Shot - </span>" + self.nextpath_link)
                    # print next_shot
                else:
                    print "preview not available for next shot"
                    self.textBrowser.append("<span>\nPrevious Shot - Not Available</span>")
                    self.textBrowser.append("<span>\nNext Shot - Not Available</span>")
            elif current_shotindex == lastshot - 1:

                print "no next shot"
                # print "---------", shots_list[current_shotindex - 1]
                previous_shot = os.path.join(self.shotpath, shots_list[current_shotindex - 1], self.deptselected,
                                             self.preview_path)
                if os.path.exists(previous_shot):
                    self.previouspath_link = "<a style=color:#00FFFF href='" + previous_shot + "'>PreviousshotPath</a>"
                    self.textBrowser.append("<span>\nPrevious Shot - </span>" + self.previouspath_link)
                    self.textBrowser.append("<span>\nNext Shot - Not Available</span>")
                    # print previous_shot
                else:
                    print "previous shot is not available"
                    self.textBrowser.append("<span>\nPrevious Shot - Not Available</span>")
                    self.textBrowser.append("<span>\nNext Shot - Not Available</span>")
            else:

                # print "---------", shots_list[current_shotindex - 1]
                previousshot = os.path.join(self.shotpath, shots_list[current_shotindex - 1], self.deptselected,
                                            self.preview_path)
                # previous_mov = os.listdir(previousshot)
                # previousshot = os.path.join(previousshot, previous_mov[-1])
                # print "---------", shots_list[current_shotindex + 1]
                nextshot = os.path.join(self.shotpath, shots_list[current_shotindex + 1], self.deptselected,
                                        self.preview_path)
                # next_mov = os.listdir(nextshot)
                # nextshot = os.path.join(nextshot, next_mov[-1])
                if os.path.exists(previousshot):
                    self.previouspath_link = "<a style=color:#00FFFF href='" + previousshot + "'>PreviousshotPath</a>"
                    self.textBrowser.append("<span>\nPrevious Shot - </span>" + self.previouspath_link)
                else:
                    print "previous shot is not available"
                    self.textBrowser.append("<span>\nPrevious Shot - Not Available</span>")
                if os.path.exists(nextshot):
                    self.nextpath_link = "<a style=color:#00FFFF href='" + nextshot + "'>NextshotPath</a>"
                    self.textBrowser.append("<span>\nNext Shot - </span>" + self.nextpath_link)
                else:
                    print "next shot is not available"
                    self.textBrowser.append("<span>\nNext Shot - Not Available</span>")
                    # print "----------", previousshot
                    # print "----------", nextshot

        except Exception as e:
            print e
            print "error occured"
        self.textBrowser.append("<span>\n\n************************************************</span>")
        self.textBrowser.append("<span>\n\nComments :-</span>")
        if self.comments:
            commentdata = self.comments.split('~')
        else:
            commentdata = ['no comments']
        for i in commentdata:
            self.textBrowser.append("<span>" + i + "</span>")

    def refresh_widgets(self):
        """
        Refresh button click event to clear all combobox, listwidget and textBrowser
        :return: None
        """
        # print "in refresh widget"
        # self.comboBox.clear()
        self.comboBox_2.clear()
        self.comboBox_3.clear()
        self.comboBox_4.clear()
        self.listWidget.clear()
        self.listWidget_2.clear()
        self.textBrowser.clear()

    def closeEvent(self, event):
        # reply = msgbox.question(self, 'Message',
        #                         "Are you sure want to \nsend for approval?", QtGui.QMessageBox.Yes |
        #                         QtGui.QMessageBox.No, QtGui.QMessageBox.No)

        print "close button click event clicked"
        project = self.comboBox.currentText()
        dept_artistname = 'anim' if not self.comboBox_4.currentText() == 'lay' else self.comboBox_4.currentText()
        msgbox = QMessageBox()
        if project != 'Select Project':
            # print username, project
            dh = dbhelper(project)
            conn = dh.connection()
            cur = conn.cursor()
            # cur.execute("select `episode` from `shot_production`")
            cur.execute("show tables")
            epdata = cur.fetchall()
            epi = [e[0] for e in epdata]
            print epi
            epi.sort()
            print epi
            opensessiondata = dict()
            for i in epi:
                cmd = "SELECT `shots` FROM `{0}` WHERE `{1}_artist_name`= '{2}' AND `Session_Status` = 'OPEN'".format(
                    i, dept_artistname, username)
                cur.execute(cmd)
                shotdata = cur.fetchall()
                if shotdata:
                    shot = [s[0] for s in shotdata]
                    print shot
                    opensessiondata[i] = shot
            if opensessiondata:
                print opensessiondata
                detailstr = ''
                for i in sorted(opensessiondata.iterkeys()):
                    print "{}: {}".format(i, opensessiondata[i])
                    detailstr += str(i)
                    detailstr += ' - '
                    detailstr += ','.join(opensessiondata[i])
                    detailstr += '\n'
                # self.setWindowState(QtCore.Qt.WindowMinimized)
                msgbox.setText('Some Sessions are still open.\nNeed to close them\n'
                    'Please click on below show details button')
                msgbox.setIcon(QMessageBox.Information)
                msgbox.setDetailedText("The details are as follows:")
                msgbox.setDetailedText(detailstr)
                ret = msgbox.exec_()
                event.ignore()
                # event.accept()
            else:
                print "all sessions are closed"
                event.accept()
        else:
            print "project not found"
            event.accept()


if __name__ == "__main__":
    
    app = QApplication(sys.argv)
    log_in_diag = LoginDialog()
    log_in_diag.lineEditUser.setText(os.environ.get('USERNAME'))
    # log_in_diag.lineEditPassword.setText('aaa')
    log_in_diag.exec_()
    username = log_in_diag.lineEditUser.text()
    if log_in_diag.granted:
        #print "$$$$$$$$$$",a
        ha = Homescreen_Animator()
        ha.show()
        sys.exit(app.exec_())
    else:
        pass
