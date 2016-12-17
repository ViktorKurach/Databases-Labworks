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
        return self.cursor.fetchall()

    def add_album(self, artist, album, year, genre, tracks, duration, label):
        artist_id = self.get_artist_id(artist, genre)
        label_id = self.get_label_id(label)
        self.cursor.execute("insert into album (artist_id, label_id, name, year, tracks, duration)\
         values ("+str(artist_id)+", "+str(label_id)+", '"+album+"', "+str(year)+", "+str(tracks)+",\
        '"+duration+"')")
        self.connection.commit()
        return 0

    def delete_album(self, artist, album, genre):
        self.cursor.execute("select album.name, artist.name, genre.name from album, artist, genre\
                where (album.artist_id = artist.artist_id) and (artist.genre_id = genre.genre_id)")
        exists = 0
        for x in self.cursor.fetchall():
            if artist == x[1] and album == x[0]:
                exists = 1
                break
        if exists == 0:
            return -1
        artist_id = self.get_artist_id(artist, genre)
        self.cursor.execute("delete from album where (name = '" + album + "')\
        and (artist_id = " + str(artist_id) + ")")
        self.connection.commit()
        return 0

    def get_genre_id(self, genre):
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

    def get_artist_id(self, artist, genre):
        self.cursor.execute("select name from artist")
        exists = 0
        for x in self.cursor.fetchall():
            if artist in x:
                exists = 1
                break
        if exists == 0:
            genre_id = self.get_genre_id(genre)
            self.cursor.execute("insert into artist (name, genre_id)\
                values ('" + artist + "', " + str(genre_id) + ")")
            self.connection.commit()
        self.cursor.execute("select artist_id, name from artist")
        for x in self.cursor.fetchall():
            if artist == x[1]:
                return x[0]

    def get_label_id(self, label):
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
