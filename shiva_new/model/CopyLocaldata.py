
import os
import shutil
from PySide.QtGui import QMessageBox
from PySide import QtGui
from model.dbhelper import dbhelper
import glob

class CopyLocaldata(object):

    def __init__(self, server_path, local_path, project, filetype, currentFileName, shotGeneric, c2, c3, c4, fileext, movtype, movGeneric):

        """
        :param server_path: Server drive path
        :param local_path: local drive path
        :param project: project name
        :param filetype: filetype(*.ma)
        :param currentFileName: selected filename
        :param shotGeneric: to check shot name is proper
        :param c2: sequence combobox
        :param c3: shot combobox
        :param c4: department combobox
        :param fileext: file extension
        :param movtype: movtype(*.mov)
        :param movGeneric: to check mov name is proper
        """
        print "in CopyLocaldata init"
        self.dst = server_path
        self.project = project
        self.filetype = filetype
        self.movtype = movtype
        self.currentFileName = currentFileName
        self.shotGeneric = shotGeneric
        self.movGeneric = movGeneric
        self.sequence = c2.currentText()
        self.shot = c3.currentText()
        self.dept = 'anim' if not c4.currentText() == 'lay' else c4.currentText()
        # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        # print self.sequence,self.shot,self.dept
        self.fileext = fileext
        # self.dst = os.path.join(self.dst,self.project)
        # print self.dst
        # latest_file = self.get_latest_file(src,self.filetype)
        # print "@@@@@@@@@@@@@",latest_file
        # if latest_file:
            # print "got latest file"
        # else:
            # print "file not found or no file is available on location"
        # self.src = os.path.join(src,latest_file)
        self.src = os.path.join(local_path, self.currentFileName)
        self.latest_file = self.get_latest_file(self.dst, self.filetype)

        temp_path_local = self.src.split('maya')
        self.mov_path_local = os.path.join(temp_path_local[0], 'preview')
        # if os.path.exists(self.mov_path_local):
        #     pass
        # else:
        #     os.makedirs(self.mov_path_local)
        # print "~~~~~~~~~~~~~~", self.mov_path_local

    def copyop(self ,sfa=True):

        """
        Copy file from local to server drive
        Change status of the shot
        sfa = True (if user click on sfa shot status will change to sfa and sfa = False if user click on end session)
        :return:None
        """
        msgbox = QMessageBox()
        # if os.listdir(self.mov_path_local):

        # self.latest_mov = self.get_latest_file(self.mov_path_local, self.movtype)
        # self.mov_path_local = os.path.join(self.mov_path_local, self.latest_mov)
        # print "@@@@@@@@@@@@@", self.latest_mov
        # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        # print self.src
        # print self.dst
        dh = dbhelper(self.project)
        self.conn = dh.connection()
        cur = self.conn.cursor()

        cur.execute("SELECT `Session_status` FROM `" + self.sequence + "` WHERE `shots` = '" + self.shot + "'")
        status = cur.fetchall()
        # print "status", status
        shotGeneric_server = self.shotGeneric

        filecheck = self.latest_file.split('_')
        temp = filecheck[-1].split('.')
        filecheck.pop(-1)
        for i in temp:
            filecheck.append(i)
        # print "##################",filecheck
        version = str(int(filecheck[3])+1)
        shotGeneric_server = shotGeneric_server.replace('$PROJ', filecheck[0])
        shotGeneric_server = shotGeneric_server.replace('$SHOTNAME', filecheck[1])
        shotGeneric_server = shotGeneric_server.replace('$DEPT', filecheck[2])
        shotGeneric_server = shotGeneric_server.replace('$VERSION', version.zfill(3))
        shotGeneric_server = shotGeneric_server.replace('$FILEEXT', filecheck[4])
        #print "##################",shotGeneric_server
        self.dst = os.path.join(self.dst, shotGeneric_server)
        print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
        print self.src
        print self.dst
        if status[0][0] == 'OPEN':
            shutil.copy(self.src, self.dst)
            if sfa == True:
                cur.execute("UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='SFA',`Session_status`='CLOSED' WHERE `shots`='"+self.shot+"'")
                self.conn.commit()
                # print "UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='SFA',`Session_status`='CLOSED' WHERE `shots`='" + self.shot + "'"
                # print "done update``````````````````````````````"
                print 'File has been copied to server folder'
                msgbox.setText('File has been copied to server folder')
                ret = msgbox.exec_()
            else:
                cur.execute("UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='TWIP',`Session_status`='CLOSED' WHERE `shots`='" + self.shot + "'")
                self.conn.commit()
                # print "UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='TWIP',`Session_status`='CLOSED' WHERE `shots`='" + self.shot + "'"
                # print "done update``````````````````````````````"
                print 'File has been copied to server folder'
                msgbox.setText('File has been copied to server folder')
                ret = msgbox.exec_()
        else:
            msgbox.setText('Session is closed already You have to start session again ')
            ret = msgbox.exec_()
        self.conn.close()

        # movGeneric_local = self.movGeneric
        # movcheck = self.latest_mov.split('_')
        # temp2 = movcheck[-1].split('.')
        # movcheck.pop(-1)
        # for i in temp2:
        #     movcheck.append(i)
        # mov_version = str(int(movcheck[3])+1)
        #
        # movGeneric_local = movGeneric_local.replace('$PROJ', movcheck[0])
        # movGeneric_local = movGeneric_local.replace('$SHOTNAME', movcheck[1])
        # movGeneric_local = movGeneric_local.replace('$DEPT', movcheck[2])
        # movGeneric_local = movGeneric_local.replace('$VERSION', mov_version.zfill(3))
        # movGeneric_local = movGeneric_local.replace('$FILEEXT', movcheck[4])
        #
        # temp_path_server = self.dst.split('maya')
        # mov_path_server = os.path.join(temp_path_server[0], 'preview', movGeneric_local)
        #
        # print "**********************************"
        # print self.mov_path_local
        # print mov_path_server
        #
        # # shutil.copy(self.mov_path_local, mov_path_server)
        # msgbox.setText('File and mov has been copied to server folder')
        # ret = msgbox.exec_()

        # else:
        #     print "mov file not present."
        #     msgbox.setText('Mov file is not found create one')
        #     ret = msgbox.exec_()

    def getmov(self):
        pass

    def get_latest_file(self, path, *paths):

        """Returns the name of the latest (most recent) file 
        of the joined path(s)"""
        # print "%%%%%%%%%%%%%",path
        # fullpath = os.path.join(path, *paths)
        # # print "############",fullpath
        # list_of_files = glob.glob(fullpath)  # You may use iglob in Python3
        # if not list_of_files:                # I prefer using the negation
        #     return None                      # because it behaves like a shortcut
        # latest_file = max(list_of_files, key=os.path.getctime)
        # # print "@@@@@@@@@@@@",latest_file
        # _, filename = os.path.split(latest_file)
        # return filename
        list_of_files = os.listdir(path)
        if not list_of_files:
            return None
        filename = [i for i in list_of_files if i.endswith('.ma') and not i.endswith('_tmp.ma')][-1]
        return filename

    def shfcopy(self):

        """
        Check for status of shot and then copy it from local drive to server
        :return: None
        """
        msgbox = QMessageBox()
        print "in shf copy"
        dh = dbhelper(self.project)
        self.conn = dh.connection()
        cur = self.conn.cursor()
        cur.execute("SELECT ``" + self.dept + "_status` FROM `" + self.sequence + "` WHERE `shots` = '" + self.shot + "'")
        status = cur.fetchall()
        print "status", status
        if status[0][0] == 'CWIP':
            shotGeneric_server = self.shotGeneric
            filecheck = self.latest_file.split('_')
            temp = filecheck[-1].split('.')
            filecheck.pop(-1)
            for i in temp:
                filecheck.append(i)
            # print "##################",filecheck
            version = str(int(filecheck[3]) + 1)
            shotGeneric_server = shotGeneric_server.replace('$PROJ', filecheck[0])
            shotGeneric_server = shotGeneric_server.replace('$SHOTNAME', filecheck[1])
            shotGeneric_server = shotGeneric_server.replace('$DEPT', filecheck[2])
            shotGeneric_server = shotGeneric_server.replace('$VERSION', version.zfill(3))
            shotGeneric_server = shotGeneric_server.replace('$FILEEXT', filecheck[4])
            # print "##################",shotGeneric_server
            self.dst = os.path.join(self.dst, shotGeneric_server)
            print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
            print self.src
            print self.dst
            # shutil.copy(self.src, self.dst)
            cur.execute("UPDATE `bdg100` SET `" + self.dept + "_status`='SFC',`Session_status`='CLOSED' WHERE `shots`='" + self.shot + "'")
            self.conn.commit()
            print "UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='SFC',`Session_status`='CLOSED' WHERE `shots`='" + self.shot + "'"
            msgbox.setText('File has been copied to server folder')
            ret = msgbox.exec_()
            # print "done update``````````````````````````````"
        else:
            print "anim status should be CWIP"
            msgbox.setText('Anim status != CWIP')
            ret = msgbox.exec_()
        self.conn.close()
