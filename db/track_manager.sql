DROP TABLE IF EXISTS notes;
DROP TABLE IF EXISTS tracks;

CREATE TABLE tracks (
  id SERIAL PRIMARY KEY,
  title VARCHAR(255),
  tempo INT
);

CREATE TABLE notes (
  id SERIAL PRIMARY KEY,
  pitch INT,
  duration FLOAT,
  location FLOAT,
  velocity FLOAT,
  track_id INT NOT NULL REFERENCES tracks(id)
);
