import pymysql

class dbhelper(object):
    def __init__(self, project):
        print "in db connection init"
        self.project = project
        self.connection()
    
    def connection(self):
        # print "in connection",self.project
        self.conn=pymysql.connect(host='192.168.0.21', db=self.project, user='users', passwd='users')
        # print "connection done"
        return self.conn
        
    def selectquery(self):
        cur = self.conn.cursor()
        print "cursor created"
	
    def insertquery(self):
        pass
        
    def updatequery(self):
        pass
        
    def connclose(self):
        print "close connection"
        self.conn.close()