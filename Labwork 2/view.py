import db


class Menu:
    database = db.Database()

    def show_menu(self):
        print "1. Show albums\n2. Add new album\n3. Edit album\n4. Delete album\n5. Search\n\
6. Parse data from .json file\n7. Exit"

    def show_albums(self):
        albums_list = self.database.show_albums()
        if not albums_list:
            print "No albums yet\n"
            return
        for x in albums_list:
            print "Artist: %s" % (x[0])
            print "Album name: %s" % (x[1])
            print "Year: %s" % (x[2])
            print "Genre: %s" % (x[3])
            print "Tracks: %s" % (x[4])
            print "Duration: %s" % (x[5])
            print "Label: %s\n" % (x[6])

    def add_album(self, p=1):
        artist = str(raw_input("Artist: "))
        album = str(raw_input("Album name: "))
        year = int(raw_input("Year: "))
        genre = str(raw_input("Genre: "))
        tracks = int(raw_input("Tracks: "))
        duration = str(raw_input("Duration (HH:MM:SS): "))
        label = str(raw_input("Label: "))
        if self.database.add_album(artist, album, year, genre, tracks, duration, label) == 0 and p == 1:
            print "Album added successfully!\n"

    def edit_album(self):
        if self.delete_album(0) == 0:
            print "New information about the album"
            self.add_album(0)
            print "Album edited successfully!\n"

    def delete_album(self, p=1):
        artist = str(raw_input("Artist: "))
        album = str(raw_input("Album name: "))
        genre = str(raw_input("Genre: "))
        res = self.database.delete_album(artist, album, genre)
        if res == -1:
            print "No such album in the database!\n"
        elif res == 0 and p == 1:
            print "Album deleted successfully!\n"
        return res

    def search(self):
        print "Here will be the search\n"

    def parse_json(self):
        print "All albums will be deleted. Press any key to continue"
        raw_input()
        if self.database.parse_json() == 0:
            print "Data parsed successfully!\n"
