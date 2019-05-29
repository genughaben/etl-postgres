# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays"
user_table_drop = "DROP TABLE IF EXISTS users"
song_table_drop = "DROP TABLE IF EXISTS songs"
artist_table_drop = "DROP TABLE IF EXISTS artists"
time_table_drop = "DROP TABLE IF EXISTS time"

# CREATE TABLES

songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (
                                songplay_id SERIAL PRIMARY KEY,
                                start_time VARCHAR NOT NULL,
                                user_id INTEGER NOT NULL,
                                song_id VARCHAR,
                                artist_id VARCHAR,
                                session_id INTEGER,
                                location VARCHAR,
                                user_agent VARCHAR);""")

user_table_create = ("""CREATE TABLE IF NOT EXISTS users (
                            user_id INTEGER PRIMARY KEY,
                            first_name VARCHAR NOT NULL, 
                            last_name VARCHAR NOT NULL,
                            gender VARCHAR NOT NULL,
                            level VARCHAR NOT NULL);""")

song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (
                            song_id VARCHAR PRIMARY KEY, 
                            title VARCHAR NOT NULL,
                            artist_id VARCHAR NOT NULL, 
                            year INTEGER,
                            duration NUMERIC NOT NULL);""")

artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (
                            artist_id VARCHAR PRIMARY KEY,
                            name VARCHAR NOT NULL,
                            location VARCHAR,
                            latitude NUMERIC,
                            longitude NUMERIC);""")

time_table_create = ("""CREATE TABLE IF NOT EXISTS time (
                            start_time VARCHAR NOT NULL,
                            hour INTEGER NOT NULL CHECK (hour > -1 AND hour < 24),
                            day INTEGER NOT NULL,
                            week INTEGER NOT NULL,
                            month INTEGER NOT NULL,
                            year INTEGER NOT NULL,
                            weekday INTEGER NOT NULL);""")


# INSERT RECORDS


songplay_table_insert = ("""INSERT INTO songplays (start_time, user_id, song_id, artist_id, 
                            session_id, location, user_agent)
                                VALUES (%s, %s, %s, %s, %s, %s, %s);""")

user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)
                            VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO UPDATE set level=excluded.level, last_name = excluded.last_name, gender = excluded.gender;""")

song_table_insert = ("""INSERT INTO songs as so (song_id, title, artist_id, year, duration) 
                            VALUES (%s, %s, %s, %s, %s) ON CONFLICT (song_id) DO UPDATE set year=excluded.year WHERE so.year = 0;""")

artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)
                            VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO UPDATE set location=excluded.location, latitude=excluded.latitude, longitude=excluded.longitude;""")

time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)
                            VALUES (%s, %s, %s, %s, %s, %s, %s);""")

# FIND SONGS

song_select = ("""SELECT s.song_id, a.artist_id FROM songs as s JOIN artists as a ON s.artist_id = a.artist_id WHERE s.title = %s and a.name = %s and s.duration = %s ;""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]