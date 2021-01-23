# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS fact_songplays"
user_table_drop = "DROP TABLE IF EXISTS dim_user"
song_table_drop = "DROP TABLE IF EXISTS dim_song"
artist_table_drop = "DROP TABLE IF EXISTS dim_artist"
time_table_drop = "DROP TABLE IF EXISTS dim_time"

# CREATE TABLES

songplay_table_create = (""" CREATE TABLE IF NOT EXISTS
    songplays (
        songplay_id serial PRIMARY KEY,
        start_time timestamp NOT NULL,
        user_id int REFERENCES users (user_id),
        level varchar,
        song_id varchar REFERENCES songs (song_id),
        artist_id varchar  REFERENCES artists (artist_id),
        session_id int,
        location varchar,
        user_agent text
        );
""")

user_table_create = (""" CREATE TABLE IF NOT EXISTS
    users (
        user_id int PRIMARY KEY,
        first_name varchar,
        last_name varchar,
        gender varchar,
        level varchar
        );
""")

song_table_create = (""" CREATE TABLE IF NOT EXISTS
    songs (
        song_id varchar PRIMARY KEY,
        title varchar,
        artist_id varchar,
        year int,
        duration numeric(10,5)
        );
""")

artist_table_create = (""" CREATE TABLE IF NOT EXISTS
    artists (
        artist_id varchar PRIMARY KEY,
        name varchar,
        location varchar,
        latitude numeric(8,5),
        longitude numeric(8,5)
        );
""")

time_table_create = (""" CREATE TABLE IF NOT EXISTS
    time (
        start_time timestamp PRIMARY KEY,
        hour smallint,
        day smallint,
        week smallint,
        month smallint,
        year smallint,
        weekday smallint
        );
""")

# INSERT RECORDS

songplay_table_insert = (""" INSERT INTO songplays
(start_time,  user_id, level, song_id, artist_id,
    session_id, location, user_agent)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
""")

# Take latest changes to users, including name
user_table_insert = (""" INSERT INTO users
(user_id, first_name, last_name, gender, level)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (user_id)
DO UPDATE
    SET first_name = EXCLUDED.first_name,
        last_name = EXCLUDED.last_name,
        gender = EXCLUDED.gender,
        level = EXCLUDED.level
""")

song_table_insert = (""" INSERT INTO songs
(song_id, title , artist_id , year , duration)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (song_id)
DO NOTHING
""")

# Take latest change to artist
artist_table_insert = (""" INSERT INTO artists
(artist_id, name, location, latitude, longitude)
VALUES (%s, %s, %s, %s, %s)
ON CONFLICT (artist_id)
DO UPDATE
    SET name = EXCLUDED.name,
        location = EXCLUDED.location,
        latitude = EXCLUDED.latitude,
        longitude = EXCLUDED.longitude
""")


time_table_insert = (""" 
    INSERT INTO time(start_time, 
        hour, day, week, month, year, weekday)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (start_time)
    DO NOTHING
""")

# FIND SONGS

song_select = (""" 
    SELECT s.song_id, s.artist_id FROM songs s
    JOIN artists a ON s.artist_id = a.artist_id 
    WHERE s.title=%s and a.name=%s and s.duration=%s
""")

# QUERY LISTS

create_table_queries = [
    user_table_create,
    song_table_create,
    artist_table_create,
    time_table_create,
    songplay_table_create
]

drop_table_queries = [
    songplay_table_drop,
    user_table_drop,
    song_table_drop,
    artist_table_drop,
    time_table_drop
]