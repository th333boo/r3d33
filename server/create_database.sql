CREATE TABLE user (
    id INTEGER PRIMARY KEY AUTO_INCREMENT,
    firstname VARCHAR(50),
    lastname VARCHAR(50),
    role
    username VARCHAR(50),
    mobile VARCHAR(15),
    email VARCHAR(50),
    passwordHash VARCHAR(32),
    lastlogin DATETIME,
    ip VARCHAR(10),
)