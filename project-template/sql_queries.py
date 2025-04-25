# DROP TABLES

songplay_table_drop = (" DROP TABLE IF EXISTS songplays;")
user_table_drop = (" DROP TABLE IF EXISTS users;")
song_table_drop = (" DROP TABLE IF EXISTS songs;")
artist_table_drop = (" DROP TABLE IF EXISTS artists;")
time_table_drop = (" DROP TABLE IF EXISTS time;")


# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS songplays (
  songplay_id SERIAL PRIMARY KEY,
  start_time TIMESTAMP NOT NULL,
  user_id INT NOT NULL REFERENCES users(user_id), 
  level VARCHAR(100) NOT NULL,
  song_id INT NOT NULL REFERENCES songs(song_id),
  artist_id INT NOT NULL REFERENCES artists(artist_id),
  session_id INT NOT NULL,
  location float NOT NULL,
  user_agent varchar(255)
);
""")

user_table_create = ("""
Create TABLE IF NOT EXISTS users (
  user_id SERIAL PRIMARY KEY, 
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  gender VARCHAR(20),
  level VARCHAR(100) NOT NULL
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS songs (
  song_id SERIAL PRIMARY KEY,
  title VARCHAR(255) NOT NULL,
  artist_id INT REFERENCES artists(artist_id),
  year INT,
  duration INTERVAL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS artists (
  artist_id SERIAL PRIMARY KEY, 
  name VARCHAR(255) NOT NULL,
  location VARCHAR(255) NOT NULL,
  latitude FLOAT CHECK (latitude >= -90 AND latitude <= 90),
  longitude FLOAT CHECK (longitude >= -180 AND longitude <= 180)
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS time (
  start_time TIMESTAMP PRIMARY KEY, 
  hour INT NOT NULL, 
  day INT NOT NULL, 
  week INT NOT NULL, 
  month INT NOT NULL,
  year INT NOT NULL,
  weekday VARCHAR(10)

);
""")

# INSERT RECORDS

songplay_table_insert = ("""
""")

user_table_insert = ("""
""")

song_table_insert = ("""
""")

artist_table_insert = ("""
""")


time_table_insert = ("""
""")

# FIND SONGS

song_select = ("""
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]