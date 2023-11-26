
CREATE TABLE IF NOT EXISTS peristorage (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    tour_name TEXT,
    quantity INTEGER,
    price REAL,
    FOREIGN KEY (userID) REFERENCES users (id),
    FOREIGN KEY (tour_name) REFERENCES tours (id)

);

CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY,
    userID INTEGER NOT NULL,
    username TEXT UNIQUE NOT NULL

);

CREATE TABLE IF NOT EXISTS tours (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    price REAL NOT NULL

);

