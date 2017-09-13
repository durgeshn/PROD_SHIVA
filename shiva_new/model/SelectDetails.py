# import neccessary libraries
import os
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
class SelectDetails(object):
    def __init__(self, projectpath, c, c2, c3):
        """
        :param projectpath: server path
        :param username: current username
        :param c: project combobox
        :param c2: sequence combobox
        :param c3: shot combobox
        """
        print("in init project selected")
        self.projectpath = projectpath
        self.c = c
        self.c2 = c2
        self.c3 = c3
        self.selectoperation()

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
                    parser2.read(self.project + '_config.ini')
                    self.epfold = parser2.get('BASE_SHOT_TYPE', 'shots')
                    self.layout = parser2.get('DEPT', 'layout')
                    self.anim = parser2.get('DEPT', 'anim')
                    self.lighting = parser2.get('DEPT', 'lit')
                    self.shf = parser2.get('DEPT', 'shf')
                    self.subset = parser2.get('DEPT', 'subset')
                    self.filepath = parser2.get('PATH', 'filepath')
                    self.shotGeneric = parser2.get('PATH', 'shotGeneric')
                    self.fileext = parser2.get('REPO', 'fileext')
                    self.movtype = parser2.get('REPO', 'movtype')
                    self.movGeneric = parser2.get('PATH', 'movGeneric')
                    # self.updateSequence()
                else:
                    print "please select project"
            elif osname == 'Linux':
                if self.project != '':
                    parser2.read(self.project + '_config.ini')
                    self.epfold = parser2.get('BASE_SHOT_TYPE', 'shots_linux')
                    self.layout = parser2.get('DEPT', 'layout')
                    self.anim = parser2.get('DEPT', 'anim')
                    self.lighting = parser2.get('DEPT', 'lit')
                    self.shf = parser2.get('DEPT', 'shf')
                    self.subset = parser2.get('DEPT', 'subset')
                    self.filepath = parser2.get('PATH', 'filepath_linux')
                    self.filetype = parser2.get('REPO', 'filetype')
                    self.shotGeneric = parser2.get('PATH', 'shotGeneric')
                    self.fileext = parser2.get('REPO', 'fileext')
                    self.movtype = parser2.get('REPO', 'movtype')
                    self.movGeneric = parser2.get('PATH', 'movGeneric')
                    # self.updateSequence()
                else:
                    print "please select project"
            else:
                print "Error - config file reading"
        except Exception as e:
            print e
            print "Error while loading project"

    def uploadepisodes(self):

        print "in select uploadepisodes"
        self.project = self.c.currentText()
        dh = dbhelper(self.project)
        self.conn = dh.connection()
        self.cur = self.conn.cursor()
        # cur.execute("select `episode` from `shot_production`")
        self.cur.execute("show tables")
        tablename = self.cur.fetchall()
        projectlist = []
        for i in range(len(tablename)):
            projectlist.append(tablename[i][0])
        # print projectlist, '<-------------------------'
        self.c2.addItem('select Episode')
        self.c2.addItems(projectlist)

    def uploaddept(self):

        msgbox = QMessageBox()
        print "upload dept"
        try:
            self.c3.clear()
            self.c3.addItem('Select Dept')
            self.shotselected = self.c2.currentText().upper()
            self.sourcepath = os.path.join(self.projectpath, self.project, self.epfold, self.shotselected)
            print "########################################", self.sourcepath
            if os.path.exists(self.sourcepath):
                self.c3.addItem(self.layout)
                self.c3.addItem(self.anim)
                self.c3.addItem(self.lighting)
                self.c3.addItem(self.shf)
                self.c3.addItem(self.subset)
            else:
                print "selected shot is not available on p drive"
                msgbox.setText('Selected shot is not available on p drive')
                ret = msgbox.exec_()
        except Exception as e:
            print e
            print "Error occured in source path or shot is not available on p drive"

    def uploadtablewdigetdetails(self):

        print "in loadtablewidget"
        deptselected = self.c3.currentText()
        # self.sourcepath
        print "@@@@@@@@@@@@", self.shotselected
        self.cur.execute("SELECT `shots`,`anim_artist_name`,`anim_status`,`Start_Frame`,`End_frame`,`Session_Status` FROM `"+self.shotselected+"`")
        statusdata = self.cur.fetchall()
        statuslist = [each for each in statusdata]
        list_file = [x for x in os.listdir(self.sourcepath) if x.startswith('sh')]
        print "############################################################################"
        print list_file
        print statuslist
        return list_file

