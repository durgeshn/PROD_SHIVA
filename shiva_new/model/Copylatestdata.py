import sys
import os
import shutil
from PySide.QtGui import QMessageBox
from PySide import QtGui
from model.dbhelper import dbhelper
import subprocess
import smtplib


class Copylatestdata(object):

    def __init__(self, src, localdrive, project, filetype, shotGeneric, c2, c3, c4, fileext):

        """
        set arguments to variable set destination path
        :param src: file source path
        :param localdrive: file local path
        :param project: project name
        :param filetype: filetype(*.ma)
        :param shotGeneric: to check shot name is proper
        :param c2: sequence combobox
        :param c3: shot combobox
        :param c4: department combobox
        :param fileext: file extension
        """
        print "in copylatestdata init"
        self.dst = localdrive
        self.project = project
        self.filetype = filetype
        self.shotGeneric = shotGeneric
        self.sequence = c2.currentText()
        self.shot = c3.currentText()
        self.dept = 'anim' if not c4.currentText() == 'lay' else c4.currentText()
        self.copy_dept = c4.currentText()

        # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
        # print self.sequence,self.shot,self.dept
        self.fileext = fileext
        self.dst = os.path.join(self.dst, self.project)
        self.src = src
        self.copyop()
        
    def copyop(self):

        """
        Check path exists if not create path for file on local data
        Check latest file on local drive
        :return: None
        """
        sourcepath = self.src.split("\\")
        # print "!!!!!!!!!!!!!!!!!!!!!!!!",self.dst
        for i in sourcepath[2:]:
            self.dst = os.path.join(self.dst, i)
            if os.path.exists(self.dst):
                pass
                # print "exists"
            else:
                # print "nothing"
                # os.mkdir(self.dst)
                os.makedirs(self.dst)
        # print "$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$"
        # print self.src
        self.latest_file_server = self.get_latest_file(self.src, self.filetype)
        self.latest_file_local = self.get_latest_file(self.dst, self.filetype)
        # print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@",self.latest_file_local
        self.checkFilegeneric_server(self.latest_file_server)
            
    def checkFilegeneric_server(self, tempfile):

        """
        Verify filename with filegeneric
        :param tempfile: Current filename
        :return: None
        """
        filecheck = tempfile.split('_')
        temp = filecheck[-1].split('.')
        filecheck.pop(-1)
        for i in temp:
            filecheck.append(i)
        # print "##################",filecheck
        self.src = os.path.join(self.src, tempfile)
        shotGeneric_server = self.shotGeneric
        # print "$$$$$$$$$$$$$$$$$$",shotGeneric_server
        if len(filecheck) == 5:
            shotGeneric_server = shotGeneric_server.replace('$PROJ', filecheck[0])
            shotGeneric_server = shotGeneric_server.replace('$SHOTNAME', filecheck[1])
            shotGeneric_server = shotGeneric_server.replace('$DEPT', filecheck[2])
            shotGeneric_server = shotGeneric_server.replace('$VERSION', filecheck[3])
            shotGeneric_server = shotGeneric_server.replace('$FILEEXT', filecheck[4])
            # print "##################",shotGeneric_server
            self.checkFilegeneric_local()
            # shutil.copy(self.src,self.dst)
            # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ copy done"
        else:
            print "Invalid filename"
            
    def checkFilegeneric_local(self):

        """
        Copy file from server to local drive
        Check status of the shot,change shot status and session status
        :return: None
        """
        print "in checklocalgeneric"
        msgbox = QMessageBox()
        dh = dbhelper(self.project)
        self.conn = dh.connection()
        cur = self.conn.cursor()
        shotGeneric_local = self.shotGeneric
        cur.execute("SELECT `Session_status`,`" + self.dept + "_status` FROM `" + self.sequence + "` WHERE `shots` = '" + self.shot + "'")
        status = cur.fetchall()
        # print "status", status
        if status[0][0] == 'CLOSED' and (status[0][1] == 'NYS' or status[0][1] == 'TWIP' or status[0][1] == 'CWIP'):
            # print "in session status if"
            if self.latest_file_local != None:
                filecheck = self.latest_file_local.split('_')
                temp = filecheck[-1].split('.')
                filecheck.pop(-1)
                for i in temp:
                    filecheck.append(i)
                # print "##################",filecheck
                version = str(int(filecheck[3])+1)
                shotGeneric_local = shotGeneric_local.replace('$PROJ', filecheck[0])
                shotGeneric_local = shotGeneric_local.replace('$SHOTNAME', filecheck[1])
                shotGeneric_local = shotGeneric_local.replace('$DEPT', filecheck[2])
                shotGeneric_local = shotGeneric_local.replace('$VERSION', version.zfill(3))
                shotGeneric_local = shotGeneric_local.replace('$FILEEXT', filecheck[4])
                # print "##################",shotGeneric_local
                self.dst = os.path.join(self.dst, shotGeneric_local)
                print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                print self.src
                print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                print self.dst
                shutil.copy(self.src, self.dst)
                f1 = open(self.dst, 'r')
                f2 = open('D:\\project\\tmp.ma', 'w')
                for line in f1:
                    f2.write(line.replace('R:', '$PROD_SERVER'))
                f1.close()
                f2.close()

                shutil.move('D:\\project\\tmp.ma', self.dst)
                print "done"
                # print "done"
                # f3 = open('D:\\tmp.ma', 'r')
                # f4 = open(self.dst, 'w')
                # for line in f3:
                #     f4.write(line)
                # # print "done writing to original file"
                # f3.close()
                # f4.close()

                if status[0][1] == 'NYS':
                    cur.execute("UPDATE `"+self.sequence+"` SET `" + self.dept + "_status`='TWIP',`Session_status`='OPEN' WHERE `shots`='"+self.shot+"'")
                    self.conn.commit()
                    # print "UPDATE `"+self.sequence+"` SET `" + self.dept + "_status`='TWIP',`Session_status`='OPEN' WHERE `shots`='"+self.shot+"'"
                    # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ copy done in if-upgrade version for current version"
                    # subprocess.Popen("C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe self.dst")
                    os.environ['PROD_SERVER'] = 'P:/badgers_and_foxes'
                    subprocess.Popen(["C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe", self.dst])
                    msgbox.setText('Latest file has been copied to local folder')
                    ret = msgbox.exec_()
                else:
                    # print ")))))))))))))))))))))) in status else"
                    cur.execute("UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='"+status[0][1]+"',`Session_status`='OPEN' WHERE `shots`='" + self.shot + "'")
                    self.conn.commit()
                    # print "UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='"+status[0][1]+"',`Session_status`='OPEN' WHERE `shots`='" + self.shot + "'"
                    # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ copy done in if-upgrade version for current version"
                    # subprocess.Popen("C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe self.dst")
                    os.environ['PROD_SERVER'] = 'P:/badgers_and_foxes'
                    subprocess.Popen(["C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe", self.dst])
                    msgbox.setText('Latest file has been copied to local folder')
                    ret = msgbox.exec_()
            else:
                print "no file present create 1st version"
                shotGeneric_local = shotGeneric_local.replace('$PROJ', self.sequence.upper())
                shotGeneric_local = shotGeneric_local.replace('$SHOTNAME', self.shot.strip('sh'))
                shotGeneric_local = shotGeneric_local.replace('$DEPT', self.copy_dept)
                shotGeneric_local = shotGeneric_local.replace('$VERSION', '001')
                shotGeneric_local = shotGeneric_local.replace('$FILEEXT', self.fileext)
                # print "##################",shotGeneric_local
                self.dst = os.path.join(self.dst, shotGeneric_local)
                print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                print self.src
                print "^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^"
                print self.dst
                shutil.copy(self.src, self.dst)
                f1 = open(self.dst, 'r')
                f2 = open('D:\\project\\tmp.ma', 'w')
                for line in f1:
                    f2.write(line.replace('R:', '$PROD_SERVER'))
                f1.close()
                f2.close()

                shutil.move('D:\\project\\tmp.ma', self.dst)
                print "done"
                # print "done"
                # f3 = open('D:\\tmp.ma', 'r')
                # f4 = open(self.dst, 'w')
                # for line in f3:
                #     f4.write(line)
                # # print "done writing to original file"
                # f3.close()
                # f4.close()

                if status[0][1] == 'NYS':
                    cur.execute("UPDATE `"+self.sequence+"` SET `" + self.dept + "_status`='TWIP',`Session_status`='OPEN' WHERE `shots`='"+self.shot+"'")
                    self.conn.commit()
                    # print "UPDATE `"+self.sequence+"` SET `" + self.dept + "_status`='TWIP',`Session_status`='OPEN' WHERE `shots`='"+self.shot+"'"
                    # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ copy done in else-first version"
                    # subprocess.Popen("C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe self.dst")
                    os.environ['PROD_SERVER'] = 'P:/badgers_and_foxes'
                    subprocess.Popen(["C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe", self.dst])
                    msgbox.setText('Latest file has been copied to local folder')
                    ret = msgbox.exec_()
                else:
                    # print ")))))))))))))))))))))) in status else"
                    cur.execute("UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='"+status[0][1]+"',`Session_status`='OPEN' WHERE `shots`='" + self.shot + "'")
                    self.conn.commit()
                    # print "UPDATE `" + self.sequence + "` SET `" + self.dept + "_status`='"+status[0][1]+"',`Session_status`='OPEN' WHERE `shots`='" + self.shot + "'"
                    # print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ copy done in else-first version"
                    # subprocess.Popen("C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe self.dst")
                    os.environ['PROD_SERVER'] = 'P:/badgers_and_foxes'
                    subprocess.Popen(["C:\\Program Files\\Autodesk\\Maya2015\\bin\\maya.exe", self.dst])
                    msgbox.setText('Latest file has been copied to local folder')
                    ret = msgbox.exec_()

            # body1 = 'Hi ,\n'
            # body2 = 'combobox selected items - {0},{1},{2} \n' \
                    # 'source path - {3} \n' \
                    # 'destination path - {4}'.format(self.sequence, self.shot, self.dept, self.src, self.dst)
            # body3 = '\nThanks,\nShiva Admin'
            # body = body1 + body2 + body3
            # subject = 'copymail'
            # print send_mail(mail_sub=subject, mail_body=body, receivers=['support@pcgi.com', 'bala.k@pcgi.com', 'rnd@pcgi.com'], sender='durgesh.n@pcgi.com')
            # print self.send_mail(mail_sub=subject, mail_body=body, receivers=['durgesh.n@pcgi.com', 'prafull.s@pcgi.com'],
                            # sender='shiva.admin@pcgi.com')

        else:
            print "session or anim status is not ready"
            msgbox.setText('Session or anim status is not ready')
            ret = msgbox.exec_()
        self.conn.close()

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
        filename = [i for i in list_of_files if i.endswith('.ma') and not i.endswith('_D:\\tmp.ma')][-1]
        return filename

    def send_mail(self, mail_sub='', mail_body='', sender='', receivers=[], mail_server='192.168.0.10'):
        # we need the receivers.
        if not receivers:
            return 'No receivers found, aborting mailing process.'
        # if no senders specified then take the local user as the sender.
        if not sender:
            user_name = os.environ['USERNAME']
            sender = '%s@pcgi.com' % user_name
        if not mail_sub or not mail_body:
            return 'No Subject or the mail body provided, aborting mailing process.'

        message = 'From: %s\nTo: %s\nSubject: %s\n%s.' % (sender, receivers[0], mail_sub, mail_body)

        try:
            smtp_obj = smtplib.SMTP(mail_server)
            smtp_obj.sendmail(sender, receivers, message)
            smtp_obj.quit()
            print "Successfully sent email"
        except smtplib.SMTPException:
            print "Error: unable to send email"
