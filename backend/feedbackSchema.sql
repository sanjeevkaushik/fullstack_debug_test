DROP TABLE IF EXISTS feedback;
CREATE TABLE feedback (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    message TEXT NOT NULL ,
    rating TEXT NOT NULL,
    created_at DATE default current_timestamp

);

INSERT INTO feedback (message, rating) values ("Thanksgiving", "5");
INSERT INTO feedback (message, rating) values ("Yukon", "4");
INSERT INTO feedback (message, rating) values ("Kona", "3");
INSERT INTO feedback (message, rating) values ("Holiday Blend", "2");
INSERT INTO feedback (message, rating) values ("Sumatra", "1");
INSERT INTO feedback (message, rating) values ("Pike Place", "5");
INSERT INTO feedback (message, rating) values ("House", "4");
INSERT INTO feedback (message, rating) values ("Espresso Roast", "3");
INSERT INTO feedback (message, rating) values ("Christmas Blend", "2");
INSERT INTO feedback (message, rating) values ("Sunsera", "1");