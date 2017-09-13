import os
import pymysql
import subprocess
import glob
import platform
from PySide.QtGui import QMessageBox

# reading the config file
from ConfigParser import SafeConfigParser
from model.dbhelper import dbhelper


class Selectproject_Supervisior(object):
    
    def __init__(self, projectpath, c, c2, c3, c4):
        print("in init project selected")
        self.projectpath = projectpath
        self.c = c
        self.c2 = c2
        self.c3 = c3
        self.c4 = c4
        # print self.c.currentText()
        self.selectoperation()
        # print "#####################",self.c2
        
        #self.comboBoxSeq.activated.connect(self.updatecomboBoxShot)
        # self.c3.activated.connect(self.updateShotDept)
     
    def selectoperation(self):
        parser2 = SafeConfigParser()
        self.project = self.c.currentText()
        if self.project == '':
            pass
        else:
            parser2.read(self.project+'_config.ini')
            self.epfold = parser2.get('BASE_SHOT_TYPE', 'shots')
            self.layout = parser2.get('DEPT', 'layout')
            self.anim =  parser2.get('DEPT', 'anim')
            self.lighting = parser2.get('DEPT', 'lit')
            self.shf = parser2.get('DEPT', 'shf')
            self.subset = parser2.get('DEPT', 'subset')
            self.filepath = parser2.get('PATH', 'filepath')
            self.projectpath = parser2.get('PATH', 'projectroot')
            self.filetype = parser2.get('REPO', 'filetype')
            # print "&&&&&&&&&&&&&&&&&&&&&&&&&&&&done"
            
            if self.project != '':
                #self.updatecomboBoxEpisode()
                self.updateSequence()
                
    def updateSequence(self):
        # print "in update sequence"
        self.c2.clear()
        
        dh = dbhelper(self.project)
        self.conn = dh.connection()
        # print "%%%%%%%%%%%%%",self.conn
        cur = self.conn.cursor()
        #cur.execute("select `episode` from `shot_production`")
        cur.execute("show tables")
        ep = cur.fetchall()
        subassets = []
        # print ep
       
        for i in range(len(ep)):
            subassets.append(ep[i][0])
        # print "$$$$$$$$$$$$$$$$$$$$$$$$"
        if 'assets' in subassets:
            subassets.remove('assets')
        else:
            pass
            # print "assets not found"
        # print subassets
        # print ep, '<-------------------------'
        self.c2.addItems(subassets)
        # self.updateShot()
        
    def updateShot(self):
        
        # dh = dbhelper(self.project)
        # self.conn = dh.connection()
        
        print "in update shot"
        self.c3.clear()
        
        self.episode = self.c2.currentText()
        cur = self.conn.cursor()
        # conn=pymysql.connect(host='192.168.0.206', db='mar', user = 'users', passwd = 'users')
        #cur.execute("select `shot` from `shot_production` where `episode` = 'FTR01'")
        cur.execute("select shots from "+self.episode)
        
        sh = cur.fetchall()
        # print "###################", sh
        shots = []
        # shots = sh[0][0].split(',')
        for i in range(len(sh)):
            shots.append(sh[i][0])
        # print shots
        self.c3.addItems(shots)
        return self.episode
        
    def updateDept(self):

        msgbox = QMessageBox()
        print "in update dept"
        self.c4.clear()
        self.shotselected = self.c3.currentText()
        sourcepath = os.path.join(self.projectpath, self.project, self.epfold, self.episode, self.shotselected)
        if os.path.exists(sourcepath):
            self.c4.addItem(self.layout)
            self.c4.addItem(self.anim)
            self.c4.addItem(self.lighting)
            self.c4.addItem(self.shf)
            self.c4.addItem(self.subset)
        else:
            print "selected shot is not available on p drive"
            msgbox.setText('Selected shot is not available on p drive')
            ret = msgbox.exec_()

                
    def deptActivated(self):
        framecount = None
        description = None
        print "in dept activated"
        deptselected = self.c4.currentText()
        
        cur = self.conn.cursor()
        cur.execute("select `anim_artist_name`,`Start_Frame`,`End_Frame`,`Description` from "+self.episode+" where `shots` = '"+self.shotselected+"'")
        data = cur.fetchall()
        # print data
        name, startframe, endframe, desc = data[0]
        
        if startframe and endframe:
            framecount = endframe - startframe    
        else:
            framecount = 'NA'
        if desc:
            description = desc
        else:
            description = 'None'
        if name:
            anim_artist_name = name
        else:
            anim_artist_name = 'None'
        # print "###########",framecount
        # print "$$$$$$$$$$$",description
        # print "!@#$%^&*()"
        path = os.path.join(self.projectpath, self.project, self.epfold, self.episode, self.shotselected, deptselected, self.filepath)
        print path
        latest_file = self.get_latest_file(path, self.filetype)
        # print "@@@@@@@@@@@@@", latest_file
        if latest_file:
            print "got latest file"
        else:
            print "file not found or no file is available on location"
        return self.project, self.epfold, self.episode, self.shotselected, deptselected, description, framecount, path, latest_file, startframe, endframe, anim_artist_name
        
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