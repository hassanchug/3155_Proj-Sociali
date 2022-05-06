DROP DATABASE IF EXISTS SocialiApp;
CREATE DATABASE IF NOT EXISTS SocialiApp;
USE SocialiApp;

CREATE TABLE IF NOT EXISTS user (
	user_id INT AUTO_INCREMENT,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    PRIMARY KEY (username_id)
);

CREATE TABLE IF NOT EXISTS posts (
	post_id INT AUTO_INCREMENT NOT NULL,
    title VARCHAR(255) NOT NULL,
    replies VARCHAR(255) NOT NULL,
    likes VARCHAR(255) NOT NULL,
    PRIMARY KEY (post_id)
);

CREATE TABLE IF NOT EXISTS likes (
	like_num INT AUTO_INCREMENT NOT NULL,
    post VARCHAR(255) NOT NULL,
    PRIMARY KEY (like_num)
);

