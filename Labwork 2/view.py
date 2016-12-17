import db


class Menu:
    database = db.Database()

    def show_menu(self):
        print "1. Show all albums\n2. Add new album\n3. Edit album\n4. Delete album\n5. Search albums by name\n\
6. Search albums by attribute\n7. Parse data from .json file\n8. Exit"

    def print_album(self, album):
        print "Artist: %s" % album[0]
        print "Album name: %s" % album[1]
        print "Year: %s" % album[2]
        print "Genre: %s" % album[3]
        print "Tracks: %s" % album[4]
        print "Duration: %s" % album[5]
        print "Label: %s" % album[6]
        print "Country: %s\n" % album[7]

    def show_all_albums(self):
        albums_list = self.database.show_albums()
        print ""
        if not albums_list:
            print "No albums yet\n"
        for x in albums_list:
            self.print_album(x)

    def add_album(self, message=1):
        artist = str(raw_input("Artist: "))
        album = str(raw_input("Album name: "))
        year = int(raw_input("Year: "))
        genre = str(raw_input("Genre: "))
        tracks = int(raw_input("Tracks: "))
        duration = str(raw_input("Duration (HH:MM:SS): "))
        label = str(raw_input("Label: "))
        if self.database.add_album(artist, album, year, genre, tracks, duration, label) == 0 and message == 1:
            print "Album added successfully!\n"

    def edit_album(self):
        if self.delete_album(0) == 0:
            print "New information about the album"
            self.add_album(0)
            print "Album edited successfully!\n"

    def delete_album(self, message=1):
        artist = str(raw_input("Artist: "))
        album = str(raw_input("Album name: "))
        genre = str(raw_input("Genre: "))
        res = self.database.delete_album(artist, album, genre)
        if res == -1:
            print "No such album in the database\n"
        elif res == 0 and message == 1:
            print "Album deleted successfully!\n"
        return res

    def full_text_search(self):
        phrase = str(raw_input("Search a phrase: "))
        without = str(raw_input("Search without (optional): "))
        result = self.database.full_text_search(phrase, without)
        print ""
        if not result:
            print "Nothing found\n"
        for x in result:
            self.print_album(x)

    def attribute_search(self):
        print "Search album by artist (A), genre (G), year (Y), label (L), country (C)"
        attr = ""
        result = None
        while attr not in ["A", "G", "Y", "L", "C"]:
            attr = str(raw_input()).capitalize()
        if attr == "A":
            artist = str(raw_input("Artist: "))
            result = self.database.search_by_artist(artist)
        elif attr == "G":
            genre = str(raw_input("Genre: "))
            result = self.database.search_by_genre(genre)
        elif attr == "Y":
            frm = str(raw_input("From: "))
            to = str(raw_input("To: "))
            result = self.database.search_by_year(frm, to)
        elif attr == "L":
            label = str(raw_input("Label: "))
            result = self.database.search_by_label(label)
        else:
            country = str(raw_input("Country: "))
            result = self.database.search_by_country(country)
        print ""
        if not result:
            print "Nothing found\n"
        for x in result:
            self.print_album(x)

    def parse_json(self):
        print "All albums will be deleted!\nPress X to cancel or any other key to continue"
        if str(raw_input()).capitalize() == 'X':
            return
        if self.database.parse_json() == 0:
            print "Data parsed successfully!\n"
