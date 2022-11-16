DROP TABLE IF EXISTS bands CASCADE;
DROP TABLE IF EXISTS songs CASCADE;
DROP TABLE IF EXISTS setlists CASCADE;
DROP TABLE IF EXISTS setlist_songs CASCADE;

CREATE TABLE bands (
    id SERIAL PRIMARY KEY,
    band_name VARCHAR(255),
    band_type VARCHAR(255)
);

CREATE TABLE songs (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    artist VARCHAR(255),
    duration INT,
    song_key VARCHAR(255),
    structure VARCHAR(255),
    harmony VARCHAR(255),
    learned VARCHAR(255),
    notes VARCHAR(255),
    band_id INT REFERENCES bands(id) ON DELETE CASCADE
);

CREATE TABLE setlists (
    id SERIAL PRIMARY KEY,
    setlist_name VARCHAR(255),
    band_id INT REFERENCES bands(id) ON DELETE CASCADE
);

CREATE TABLE setlist_songs (
    id SERIAL PRIMARY KEY,
    setlist_id INT REFERENCES setlists(id) ON DELETE CASCADE,
    song_id INT REFERENCES songs(id) ON DELETE CASCADE
)
