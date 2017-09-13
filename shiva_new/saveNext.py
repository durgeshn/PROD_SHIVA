# General imports.
import os
import sys

import pymel.core as pm

# TODO : Remove the hardcoded module paths.
# sys.path.insert(0, r'\\stor\data\python_packages\repo\pathGenerator\v001')

# Qt imports.
from PySide import QtGui

# Custom imports.
from myui import saveNextUI


# from path_generator import ProjectpathGenerator


class SaveNextVersion(QtGui.QMainWindow, saveNextUI.Ui_MainWindow):
    def __init__(self, project, workFilePth=str(pm.sceneName()), prnt=None):
        super(SaveNextVersion, self).__init__(prnt)
        self.setupUi(self)
        self.project = project
        self.workFilePath = workFilePth
        self.workAreaLocation = os.path.dirname(self.workFilePath)
        self.workFileName = os.path.basename(self.workFilePath)
        # self.pathGen = ProjectpathGenerator.ProjectpathGenerator(self.project)
        self.connections()
        self.setWindowTitle('Save Next Window')
        self.version_sb.setEnabled(False)

    def connections(self):
        self.fillUI()
        self.save_pb.clicked.connect(self.saveNext)
        self.cancel_pb.clicked.connect(self.cancel)

    def fillUI(self):
        fileName, ext = os.path.splitext(self.workFileName)
        seq, sh, dept, ver = fileName.split('_')

        if dept == 'lay':
            dept = 'layout'
        if dept == 'ani':
            dept = 'animation'

        self.workAreaPath_l.setText(self.workAreaLocation)
		
        list_of_files = os.listdir(self.workAreaLocation)
        if not list_of_files:
            return None
        filenameForVer = [i for i in list_of_files if i.endswith('.ma') and not i.endswith('_tmp.ma')][-1].replace('.ma', '')
        verFinal = filenameForVer.split('_')[3]
        self.version_sb.setValue(int(verFinal) + 1)
        self.fileNamePre_l.setText('_'.join([seq, sh, dept, '%03d' % (int(verFinal) + 1)]))

    def cancel(self):
        self.close()

    def saveNext(self):
        fileName, ext = os.path.splitext(self.workFileName)
        seq, sh, dept, ver = fileName.split('_')
        finaleFile = os.path.join(self.workAreaLocation,
                                  '%s.ma' % '_'.join([seq, sh, dept, '%03d' % int(self.version_sb.value())]))
        pm.saveAs(finaleFile)
        self.close()


if __name__ == '__main__':
    qApp = QtGui.QApplication(sys.argv)
    proj = 'badgers_and_foxes'
    path = r'D:\project\badgers_and_foxes\01_SAISON_1\13_PRODUCTION\04_EPISODES\02_Fabrication_3D\BDG100\sh001\lay\maya\work\BDG100_001_lay_001.ma'
    saveUI = SaveNextVersion(project=proj, workFilePth=path)
    saveUI.show()
    qApp.exec_()
