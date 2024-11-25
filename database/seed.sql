-- Insert Sample Data
INSERT INTO Users (username, email, password_harsh) VALUES
('Alice', 'alice@example.com', 'hash1'),
('Bob', 'bob@example.com', 'hash2');

INSERT INTO Movies (title, genre, release_year, description) VALUES
('Inception', 'Sci-Fi', 2010, 'A mind-bending thriller.'),
('The Matrix', 'Sci-Fi', 1999, 'Reality is not what it seems.');

INSERT INTO Ratings (user_id, movie_id, rating) VALUES
(1, 1, 5.0),
(2, 2, 4.5);