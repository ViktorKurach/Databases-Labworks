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
        self.cursor.execute("select artist.name, album.name, album.year,\
        genre.name, album.tracks, album.duration, label.name\
        from album, artist, genre, label\
        where (album.artist_id = artist.artist_id)\
            and (artist.genre_id = genre.genre_id)\
            and (album.label_id = label.label_id);")
        for x in self.cursor.fetchall():
            print "Artist: %s" % (x[0])
            print "Album name: %s" % (x[1])
            print "Year: %s" % (x[2])
            print "Genre: %s" % (x[3])
            print "Tracks: %s" % (x[4])
            print "Duration: %s" % (x[5])
            print "Label: %s\n" % (x[6])

    def add_album(self):
        artist = str(raw_input("Artist: "))
        album_name = str(raw_input("Album name: "))
        year = int(raw_input("Year: "))
        genre = str(raw_input("Genre: "))
        tracks = int(raw_input("Tracks: "))
        duration = str(raw_input("Duration (HH:MM:SS): "))
        label = str(raw_input("Label: "))
        artist_id, genre_id, label_id = self.artist_id(artist, genre), self.genre_id(genre), self.label_id(label)
        self.cursor.execute("insert into album (artist_id, label_id, name, year, tracks, duration)\
         values ("+str(artist_id)+", "+str(label_id)+", '"+album_name+"', "+str(year)+", "+str(tracks)+",\
        '"+duration+"')")
        self.connection.commit()
        print "Album added successfully!\n"

    def genre_id(self, genre):
        self.cursor.execute("select name from genre")
        exists = 0
        for x in self.cursor.fetchall():
            if genre in x:
                exists = 1
                break
        if exists == 0:
            self.cursor.execute("insert into genre (name) values ('" + genre + "')")
            self.connection.commit()
        self.cursor.execute("select genre_id, name from genre")
        for x in self.cursor.fetchall():
            if genre == x[1]:
                return x[0]

    def artist_id(self, artist, genre):
        self.cursor.execute("select name from artist")
        exists = 0
        for x in self.cursor.fetchall():
            if artist in x:
                exists = 1
                break
        if exists == 0:
            genre_id = self.genre_id(genre)
            self.cursor.execute("insert into artist (name, genre_id)\
                values ('" + artist + "', " + str(genre_id) + ")")
            self.connection.commit()
        self.cursor.execute("select artist_id, name from artist")
        for x in self.cursor.fetchall():
            if artist == x[1]:
                return x[0]

    def label_id(self, label):
        self.cursor.execute("select name from label")
        exists = 0
        for x in self.cursor.fetchall():
            if label in x:
                exists = 1
                break
        if exists == 0:
            self.cursor.execute("insert into label (name) values ('" + label + "')")
            self.connection.commit()
        self.cursor.execute("select label_id, name from label")
        for x in self.cursor.fetchall():
            if label == x[1]:
                return x[0]

    def edit_album(self):
        print "Here album is edited"

    def delete_album(self):
        print "Here album is deleted"

    def search(self):
        print "Here is a search"
