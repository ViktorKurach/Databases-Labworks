import MySQLdb


class Database:
    connection = None
    cursor = None

    def __init__(self):
        self.connection = MySQLdb.connect(host='127.0.0.1', user='root', passwd='1234', db='music')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def show_albums(self):
        print "Here albums are shown"

    def add_album(self):
        print "Here album is added"

    def edit_album(self):
        print "Here album is edited"

    def delete_album(self):
        print "Here album is deleted"

    def search(self):
        print "Here is a search"
