import sys
import pymysql
import os
from PySide import QtGui, QtCore
from ConfigParser import SafeConfigParser
from PySide.QtGui import QMessageBox

import loginUi
import change_password_main
# from shiva.core import manager
# from homescreen2 import Ui_Form

parser = SafeConfigParser()
config_path = os.path.join(os.path.dirname(__file__), 'config.ini')
parser.read(config_path)

dbhost = parser.get('settings', 'dbhost')
# versioninfo = parser.get('settings', 'versioninfopath')
# projectpath = parser.get('project_settings', 'projectpath')
# projectuncpath = parser.get('project_settings', 'projectuncpath')
# assettemplatepath = parser.get('project_settings', 'assettemplatepath')
# seqtemplatepath = parser.get('project_settings', 'seqtemplatepath')
# eptemplatepath = parser.get('project_settings', 'eptemplatepath')
# sctemplatepath = parser.get('project_settings', 'sctemplatepath')
# projectdrive = parser.get('project_settings', 'projectdrive')
# localdrive = parser.get('project_settings', 'localdrive')
# epfoldername = parser.get('project_settings', 'epfoldername')

print dbhost
# print versioninfo
# print projectpath
# print projectuncpath
# print assettemplatepath
# print seqtemplatepath
# print eptemplatepath
# print sctemplatepath
# print projectdrive
# print localdrive
# print epfoldername


class LoginDialog(QtGui.QDialog, loginUi.Ui_FormLogin):
    def __init__(self, parent=None):
        print "in login init"
        super(LoginDialog, self).__init__(parent)
        self.setupUi(self)
        self.all_users = list()
        completer = QtGui.QCompleter()
        self.lineEditUser.setCompleter(completer)
        model = QtGui.QStringListModel()
        completer.setModel(model)
        self.get_users_auto_complete(model)

        # add context menu to the option menu.
        self.option_tb.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.option_tb.customContextMenuRequested.connect(self.on_context_menu)
        # create the actions.
        self.popMenu = QtGui.QMenu(self)
        pass_reset = QtGui.QAction('Request Reset Password.', self)
        pass_change = QtGui.QAction('Change Password', self)

        self.popMenu.addAction(pass_reset)
        self.popMenu.addSeparator()
        self.popMenu.addAction(pass_change)

        # connections.
        self.pushButtonLogin.clicked.connect(self.do_login)
        self.pushButtonQuit.clicked.connect(self.closewindow)
        # noinspection PyUnresolvedReferences
        pass_reset.triggered.connect(self.pass_reset)
        # noinspection PyUnresolvedReferences
        pass_change.triggered.connect(self.pass_change)
        self.granted = False
        self.dept = None

    @staticmethod
    def pass_reset():
        print 'Put request for the password reset.'

    def pass_change(self):
        print 'Change the password.'
        user_name = self.lineEditUser.text()
        # print self.all_users

        if not user_name or user_name not in self.all_users:
            print "wrong input"
            dialog = QMessageBox.critical(self, 'Username Error', 'Please enter correct username', buttons=QMessageBox.Ok)
            if dialog == QMessageBox.Ok:
                pass
            return False    
        # self.hide()
        password_change_win = change_password_main.ChangePassword(user=user_name, db=dbhost)
        password_change_win.exec_()
        # self.exec_()
        
    def closewindow(self):
        sys.exit()

    def on_context_menu(self, point):
        self.popMenu.exec_(self.option_tb.mapToGlobal(point))

    @staticmethod
    def get_sql_data(msg='SELECT `empname` FROM `emp`', update=False):
        conn = pymysql.connect(host=dbhost, db='users', user='users', passwd='users')
        cur = conn.cursor()
        cur.execute(msg)
        conn.commit()
        if not update:
            fetcheddata = cur.fetchall()
            return fetcheddata
        return True

    def get_users_auto_complete(self, model):
        user_list = self.get_sql_data('SELECT `empname` FROM `emp`')
        user_list = [x[0] for x in user_list]
        self.all_users = user_list
        model.setStringList(user_list)

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
        
    # def reject(self):
        # self.close()

    def do_login(self):
        username = self.lineEditUser.text().rstrip()
        password = self.lineEditPassword.text()

        # check for the empty user name field.
        if username == 'Enter UserName' or username == '':
            self.prompt_dialog('info', 'Please provide a valid user name.')
            return False

        # check for the user.
        # if username not in self.all_users:
            # self.prompt_dialog('critical', 'Invalid user name.')
            # return False

        # check for empty password field.
        # if not len(password):
            # self.prompt_dialog('info', 'Please provide a valid password for the user.')
            # return False

        # now check for the password from database.
        try:
            ret = self.get_sql_data('SELECT `emppass`, `empdepts` FROM `emp` WHERE `empname` ="%s"' % username)
            db_password = ret[0][0]
            if db_password != password:
                self.prompt_dialog('critical', 'User name and Password not matching, please try again.')
                return False
            # print username
            # print db_password
            # print deptaccess
            print 'Proceeding to Main UI...'
            self.dept = ret[0][1]
            self.granted = True
            self.close()
            return True
        except Exception as e:
            print e
            print "Error in login.Please provide a valid username and password"
        # return username
        # uf = Ui_Form()
        # shiva_manager = manager.MainWindow(user=username, dept_access=deptaccess, parent=self)
        # ret = shiva_manager.show()
        # shiva_manager.show()
        
if __name__ == '__main__':
    import os
    log_in_app = QtGui.QApplication(sys.argv)
    log_in_diag = LoginDialog()
    log_in_diag.lineEditUser.setText(os.environ.get('USERNAME'))
    # log_in_diag.lineEditUser.setText('durgesh.n')
    # log_in_diag.lineEditPassword.setText('aaa')
    log_in_diag.show()
    sys.exit(log_in_app.exec_())
