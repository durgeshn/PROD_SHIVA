import sys
import pymysql

from PySide import QtGui

import password_change


class ChangePassword(QtGui.QDialog, password_change.Ui_password_change_win):
    def __init__(self, user, parent=None, db=''):
        super(ChangePassword, self).__init__(parent)
        self.user = user
        self.db = db
        self.setupUi(self)

        # connections
        self.change_pb.clicked.connect(self.do_change_password)
        self.cacnle_pb.clicked.connect(self.close)

    def get_sql_data(self, msg='', update=False):
        conn = pymysql.connect(host=self.db, db='users', user='users', passwd='users')
        cur = conn.cursor()
        ret = cur.execute(msg)
        conn.commit()
        if not update:
            fetcheddata = cur.fetchall()
            cur.close()
            return fetcheddata
        cur.close()
        return ret

    def do_change_password(self):
        old_pass = str(self.old_password_le.text())
        new_pass = str(self.new_password_le.text())
        new_pass_01 = str(self.new_password_01_le.text())

        # check for old password is there.
        if not old_pass:
            self.prompt_dialog(status='critical', msg='Please Enter A Password.')
            return False
        # check for the old password in db.
        sql_query = 'SELECT `emppass` FROM `emp` WHERE `empname` = "%s"' % self.user
        current_pass = str(self.get_sql_data(sql_query)[0][0])
        print current_pass
        if old_pass != current_pass:
            self.prompt_dialog(status='critical', msg='Invalid password for user : %s.' % self.user)
            return False
        if new_pass != new_pass_01:
            self.prompt_dialog(status='critical', msg='New password and the retype new password not matching.')
            return False
        print 'changing password from %s to %s for user %s' % (old_pass, new_pass, self.user)

        update_sql_query = 'UPDATE `users`.`emp` SET `emppass` = "%s" WHERE `empname` = "%s"' % (new_pass, self.user)
        print update_sql_query
        # update_sql_query = 'UPDATE `emppass` = "%s" FROM `emp` WHERE `empname` = "%s"' % (new_pass, self.user)
        update_ret = self.get_sql_data(update_sql_query, update=True)
        print update_ret
        sql_query = 'SELECT `emppass` FROM `emp` WHERE `empname` = "%s"' % self.user
        current_pass = self.get_sql_data(sql_query)[0][0]
        print current_pass
        self.prompt_dialog(status='info', msg='Your password has been changed. Please Log in with you new password.')
        self.close()

    @staticmethod
    def prompt_dialog(status, msg):
        qt_status = QtGui.QMessageBox.Information
        if status == 'info':
            qt_status = QtGui.QMessageBox.Information
        if status == 'warning':
            qt_status = QtGui.QMessageBox.Warning
        if status == 'critical':
            qt_status = QtGui.QMessageBox.Critical
        if status == 'question':
            qt_status = QtGui.QMessageBox.Question
        msg_box = QtGui.QMessageBox()
        msg_box.setIcon(qt_status)
        msg_box.setText(status)
        msg_box.setInformativeText(msg)
        msg_box.exec_()


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    ChangePassword(user='durgesh.n', db='192.168.0.206').exec_()
