# import neccessary libraries
import os
import datetime
import pymysql
import subprocess
import glob
import platform
from PySide.QtGui import QMessageBox

# reading the config file and import from model package
from ConfigParser import SafeConfigParser
from model.dbhelper import dbhelper
from PySide import QtCore, QtGui


# Selectproject and other operations
class Selectproject(object):
    
    def __init__(self, projectpath, username, c, c2, c3, c4, l1, l2, localdrive, endsession, startsession, textbrowser, refresh):

        """
        :param projectpath: server path
        :param username: current username
        :param c: project combobox
        :param c2: sequence combobox
        :param c3: shot combobox
        :param c4: department combobox
        :param l1: listwidget for server drive files
        :param l2: listwidget for local drive files
        :param localdrive: local drive path
        """
        print("in init project selected")
        self.projectpath = projectpath
        self.username = username
        self.c = c
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        self.listWidget = l1
        self.listWidget_2 = l2
        self.localdrive = localdrive
        self.endsession = endsession
        self.startsession = startsession
        self.textbrowser = textbrowser
        self.refresh = refresh
        self.selectoperation()
        # print self.c.currentText()
        # print "#####################",self.c2 
        # self.comboBoxSeq.activated.connect(self.updatecomboBoxShot)
        # self.c3.activated.connect(self.updateShotDept)
     
    def selectoperation(self):

        """
        Read config file for selected project
        :return: None
        """
        parser2 = SafeConfigParser()
        self.project = self.c.currentText()
        osname = platform.system()
        try:
            if osname == 'Windows':
                if self.project != '':

                    projectconfig_path = os.path.join(os.path.dirname(__file__), self.project + '_config.ini')
                    parser2.read(projectconfig_path)
                    # parser2.read('\\\\stor\\py\\TESTTALKDEMO\\shiva_new\\' + self.project + '_config.ini')
                    self.epfold = parser2.get('BASE_SHOT_TYPE', 'shots')
                    self.filepath = parser2.get('PATH', 'filepath')

                    # self.updateSequence()
                else:
                    print "please select project"
            elif osname == 'Linux':
                if self.project != '':
                    projectconfig_path = os.path.join(os.path.dirname(__file__), self.project + '_config.ini')
                    parser2.read(projectconfig_path)
                    self.epfold = parser2.get('BASE_SHOT_TYPE', 'shots_linux')
                    self.filepath = parser2.get('PATH', 'filepath_linux')
                    # self.updateDept()
                    # self.updateSequence()
                else:
                    print "please select project"
            else:
                print "Error - config file reading"
            self.layout = parser2.get('DEPT', 'layout')
            self.anim = parser2.get('DEPT', 'anim')
            self.lighting = parser2.get('DEPT', 'lit')
            self.shf = parser2.get('DEPT', 'shf')
            self.subset = parser2.get('DEPT', 'subset')
            self.filetype = parser2.get('REPO', 'filetype')
            self.shotGeneric = parser2.get('PATH', 'shotGeneric')
            self.fileext = parser2.get('REPO', 'fileext')
            self.movtype = parser2.get('REPO', 'movtype')
            self.movGeneric = parser2.get('PATH', 'movGeneric')
            self.preview_path = parser2.get('PATH', 'preview_path')
            self.updateDept()
        except Exception as e:
            print e
            print "Error while loading project"

    def updateDept(self):

        """
        Add departments to the department combobox
        :return: None
        """
        msgbox = QMessageBox()
        print "in update dept"
        try:
            self.listWidget.clear()
            self.listWidget_2.clear()
            self.textbrowser.clear()
            self.c4.clear()
            self.c4.addItem('Select Dept')
            # self.shotselected = self.c3.currentText()
            # sourcepath = os.path.join(self.projectpath, self.project, self.epfold, self.episode, self.shotselected)
            # print "########################################", sourcepath
            # if os.path.exists(sourcepath):
            self.c4.addItem(self.layout)
            self.c4.addItem(self.anim)
            self.c4.addItem(self.lighting)
            self.c4.addItem(self.shf)
            self.c4.addItem(self.subset)
            self.c2.clear()
            self.c2.addItem('Select Sequence')
            self.c3.clear()
            self.c3.addItem('Select Shot')
            # else:
            #     print "selected shot is not available on p drive"
            #     msgbox.setText('Selected shot is not available on p drive')
            #     ret = msgbox.exec_()
        except Exception as e:
            print e
            print "Error occured in selecting department"
            # print "Error occured in source path or shot is not available on p drive"

    def updateSequence(self):

        """
        Get sequence data from database and add to sequence combobox
        :return: None
        """
        print "in update sequence"
        try:
            self.c2.clear()
            self.c3.clear()
            dh = dbhelper(self.project)
            conn = dh.connection()
            cur = conn.cursor()
            #cur.execute("select `episode` from `shot_production`")
            cur.execute("show tables")
            ep = cur.fetchall()
            sequence = []
            for i in range(len(ep)):
                sequence.append(ep[i][0])
            # print ep, '<-------------------------'
            self.c2.addItem('Select Sequence')
            self.c2.addItems(sequence)
            self.c3.addItem('Select Shot')
            # self.updateShot()
        except Exception as e:
            print e
            print "Error while loading sequence details from database"
        conn.close()
        
    def updateShot(self):

        """
        Get shots from database and add it to shot combobox
        :return: None
        """
        # dh = dbhelper(self.project)
        # self.conn = dh.connection()
        print "in update shot"
        self.c3.clear()
        self.deptselected = self.c4.currentText()
        if self.c4.currentText() == 'ani':
            dept = 'anim'
        else:
            dept = self.c4.currentText()
        try:
            self.episode = self.c2.currentText().upper()
            dh = dbhelper(self.project)
            sourcepath = os.path.join(self.projectpath, self.project, self.epfold, self.episode)
            conn = dh.connection()
            cur = conn.cursor()
            #cur.execute("select `shot` from `shot_production` where `episode` = 'FTR01'")
            # print "########################################", sourcepath
            if os.path.exists(sourcepath):
                cmd = "select shots from {0} where `{1}_artist_name` = '{2}'".format(self.episode, dept, self.username)
                cur.execute(cmd)
                sh = cur.fetchall()
                shots = []
                for i in range(len(sh)):
                    shots.append(sh[i][0])
                # print shots
                self.c3.addItem('Select Shot')
                self.c3.addItems(shots)
            else:
                print "selected episode is not available on p drive"
                msgbox.setText("selected episode is not available on p drive")
                ret = msgbox.exec_()
        except Exception as e:
            print e
            print "Error while loading shot details from database"
        conn.close()
                
    def shotActivated(self):

        """
        Get information of shot from database check files on path(both serverside and local side) add it to listwidgets
        :return: All information regarding shot
        """
        framecount = None
        desc = None
        startframe = None
        endframe = None
        session_status = None
        if self.c4.currentText() == 'ani':
            dept = 'anim'
        else:
            dept = self.c4.currentText()
        print "in shot activated"
        try:
            self.shotselected = self.c3.currentText()
            dh = dbhelper(self.project)
            conn = dh.connection()
            cur = conn.cursor()
            # cmd2 = "select `Start_Frame`,`End_Frame`,`Description`,`Session_Status` from {0} where `shots` = '{1}'".format(self.episode,self.shotselected)
            cmd2 = "select `Start_Frame`,`End_Frame`,`Description`,`Session_Status`, {0}_comments from {1} where `shots` = '{2}'".format(dept, self.episode, self.shotselected)
            cur.execute(cmd2)
            data = cur.fetchall()
            # print data
            startframe, endframe, desc, session_status, comments = data[0]
            print "Session status", session_status
            # print "+++++++++++++++++++++++++++++++++++++++++++++", comments
        except Exception as e:
            print e
            print "Error occured while loading details of shot from database"
        
        if startframe and endframe:
            framecount = endframe - startframe    
        else:
            framecount = 'NA'
        if desc:
            description = desc
        else:
            description = 'None'
        if session_status == 'CLOSED':
            self.startsession.setEnabled(True)
            self.listWidget.setEnabled(True)
            self.listWidget_2.setEnabled(False)
            self.endsession.setEnabled(False)
        else:
            self.startsession.setEnabled(False)
            self.listWidget.setEnabled(False)
            self.listWidget_2.setEnabled(True)
            self.endsession.setEnabled(True)
        self.refresh.setEnabled(True)
            # pass
        # print "###########",framecount
        # print "$$$$$$$$$$$",description
        path = os.path.join(self.projectpath, self.project, self.epfold, self.episode, self.shotselected, self.deptselected, self.filepath)
        shotpath = os.path.join(self.projectpath, self.project, self.epfold, self.episode)
        local_path = os.path.join(self.localdrive, self.project, self.epfold, self.episode, self.shotselected, self.deptselected, self.filepath)
        print "server path-", path
        print "local path-", local_path
        if os.path.exists(path):
            path_listwidget = os.path.join(path, self.filetype)
            path_listwidget2 = os.path.join(local_path, self.filetype)
            list_files = glob.glob(path_listwidget)
            local_list_files = glob.glob(path_listwidget2)
            # print list_files
            list_files.sort()
            local_list_files.sort()
            for i in list_files:
                _, temp = os.path.split(str(i))
                item = QtGui.QListWidgetItem()
                # print "-------------------------",i
                serverfiledate = datetime.datetime.fromtimestamp(os.path.getmtime(i)).strftime("%d-%m-%y    %H:%M:%S")
                serverfilesize = self.convert_bytes(os.stat(i).st_size)
                item.setText(QtGui.QApplication.translate("Form", temp+"\t"+serverfiledate+"\t"+serverfilesize, None, QtGui.QApplication.UnicodeUTF8))
                self.listWidget.addItem(item)

            for i in local_list_files:
                _, temp = os.path.split(str(i))
                item = QtGui.QListWidgetItem()
                localfiledate = datetime.datetime.fromtimestamp(os.path.getmtime(i)).strftime("%d-%m-%y    %H:%M:%S")
                localfilesize = self.convert_bytes(os.stat(i).st_size)
                item.setText(QtGui.QApplication.translate("Form", temp+"\t"+localfiledate+"\t"+localfilesize, None, QtGui.QApplication.UnicodeUTF8))
                self.listWidget_2.addItem(item)

            # return self.project,self.epfold,self.episode,self.shotselected,deptselected,description,framecount,path,latest_file
            return self.project, self.epfold, self.episode, self.shotselected, self.deptselected, description, framecount, path, self.filetype, self.shotGeneric, self.fileext, local_path, self.movtype, self.movGeneric, shotpath, self.preview_path, comments
        else:
            print "Error occured in source path or shot is not available on p drive"
        conn.close()
        
    def get_latest_file(self, path, *paths):

        """Returns the name of the latest (most recent) file 
        of the joined path(s)"""
        # print "%%%%%%%%%%%%%", path
        fullpath = os.path.join(path, *paths)
        # print "############", fullpath
        list_of_files = glob.glob(fullpath)  # You may use iglob in Python3
        if not list_of_files:                # I prefer using the negation
            return None                      # because it behaves like a shortcut
        latest_file = max(list_of_files, key=os.path.getctime)
        # print "@@@@@@@@@@@@", latest_file
        _, filename = os.path.split(latest_file)
        return filename

    def convert_bytes(self, num):
        """
        this function will convert bytes to MB.... GB... etc
        """
        for x in ['bytes', 'KB', 'MB', 'GB', 'TB']:
            if num < 1024.0:
                # print num, x, "---------------------------"
                return "%3.1f %s" % (num, x)
            num /= 1024.0
