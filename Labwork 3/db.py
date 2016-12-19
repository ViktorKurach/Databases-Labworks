import MySQLdb
import json
import models


class Database:
    connection = None
    cursor = None

    def __init__(self):
        self.connection = MySQLdb.connect(host='127.0.0.1', user='root', passwd='1234', db='music')
        self.cursor = self.connection.cursor()

    def __del__(self):
        self.connection.close()

    def show_albums(self):
        self.cursor.execute("select artist.name, album.name,\
        album.year, genre.name, album.tracks,\
        album.duration, label.name, artist.country\
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

    def parse_json(self):
        f = open("music.json", "rb")
        data = json.loads(f.read())
        f.close()
        self.clean_database()
        for x in data["Genre"]:
            style, genre_name = x["Style"], x["Name"]
            self.cursor.execute("insert into genre (name, style) values ('"+genre_name+"', '"+style+"')")
            self.connection.commit()
        for x in data["Artist"]:
            artist_name, country, genre_id = x["Name"], x["Country"], self.get_genre_id(x["Genre"])
            self.cursor.execute("insert into artist (name, country, genre_id)\
            values ('" + artist_name + "', '" + country + "', "+str(genre_id)+")")
            self.connection.commit()
        for x in data["Label"]:
            label_name, country, since = x["Name"], x["Country"], x["Since"]
            self.cursor.execute("insert into label (name, country, since)\
            values ('" + label_name + "', '" + country + "', "+str(since)+")")
            self.connection.commit()
        return 0

    def full_text_search(self, phrase, without=""):
        query = "select artist.name, s.name,\
            s.year, genre.name, s.tracks,\
            s.duration, label.name, artist.country\
            from artist inner join\
            (select * from album where match (name)\
            against ('+\""+phrase+"\""
        if without != "":
            query += " -"+without
        query += "' in boolean mode)) s\
            on (s.artist_id = artist.artist_id)\
            inner join genre on (artist.genre_id = genre.genre_id)\
            inner join label on (label.label_id = s.label_id)"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def search_by_artist(self, artist):
        self.cursor.execute("select artist.name, album.name,\
        album.year, genre.name, album.tracks,\
        album.duration, label.name, artist.country\
        from album, artist, genre, label\
        where (album.artist_id = artist.artist_id)\
            and (artist.genre_id = genre.genre_id)\
            and (album.label_id = label.label_id)\
            and (artist.name = '"+artist+"')")
        return self.cursor.fetchall()

    def search_by_genre(self, genre):
        self.cursor.execute("select artist.name, album.name,\
        album.year, genre.name, album.tracks,\
        album.duration, label.name, artist.country\
        from album, artist, genre, label\
        where (album.artist_id = artist.artist_id)\
            and (artist.genre_id = genre.genre_id)\
            and (album.label_id = label.label_id)\
            and (genre.name = '" + genre + "')")
        return self.cursor.fetchall()

    def search_by_year(self, frm, to):
        self.cursor.execute("select artist.name, album.name,\
        album.year, genre.name, album.tracks,\
        album.duration, label.name, artist.country\
        from album, artist, genre, label\
        where (album.artist_id = artist.artist_id)\
            and (artist.genre_id = genre.genre_id)\
            and (album.label_id = label.label_id)\
            and (album.year >= "+frm+") and (album.year <= "+to+")")
        return self.cursor.fetchall()

    def search_by_label(self, label):
        self.cursor.execute("select artist.name, album.name,\
        album.year, genre.name, album.tracks,\
        album.duration, label.name, artist.country\
        from album, artist, genre, label\
        where (album.artist_id = artist.artist_id)\
            and (artist.genre_id = genre.genre_id)\
            and (album.label_id = label.label_id)\
            and (label.name = '" + label + "')")
        return self.cursor.fetchall()

    def search_by_country(self, country):
        self.cursor.execute("select artist.name, album.name,\
        album.year, genre.name, album.tracks,\
        album.duration, label.name, artist.country\
        from album, artist, genre, label\
        where (album.artist_id = artist.artist_id)\
            and (artist.genre_id = genre.genre_id)\
            and (album.label_id = label.label_id)\
            and (artist.country = '" + country + "')")
        return self.cursor.fetchall()

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

    def clean_database(self):
        self.cursor.execute("delete from genre")
        self.cursor.execute("delete from artist")
        self.cursor.execute("delete from label")
        self.cursor.execute("delete from album")
        self.connection.commit()
