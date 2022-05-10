DROP DATABASE IF EXISTS SocialiApp;
CREATE DATABASE IF NOT EXISTS SocialiApp;
USE SocialiApp;

CREATE TABLE IF NOT EXISTS users (
	username_id INT AUTO_INCREMENT NOT NUll,
    firstname VARCHAR(255) NOT NULL,
    lastname VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    PRIMARY KEY (username_id)
);
CREATE TABLE IF NOT EXISTS replies (
	reply_num INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    users VARCHAR(255) NOT NULL,
    timeposted VARCHAR(255) NOT NULL,
    likes INT NOT NULL,
    PRIMARY KEY (reply_num)
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

CREATE TABLE IF NOT EXISTS userposts (
	Foreign Key (post_num), (username_id)
    PRIMARY KEY (post_num), (username_id) 
);

CREATE TABLE IF NOT EXISTS userreplies (
	Foreign Key (reply_num), (username_id)
    PRIMARY KEY (reply_num), (username_id) 
);

CREATE TABLE IF NOT EXISTS postlikes (
	Foreign Key (like_num), (username_id)
    PRIMARY KEY (like_num), (username_id) 
);

