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
CREATE TABLE IF NOT EXISTS replies (
	reply_num INT AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL,
    user VARCHAR(255) NOT NULL,
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
	Foreign Key (post_num), (user_num)
    PRIMARY KEY (post_num), (user_num) 
);

CREATE TABLE IF NOT EXISTS userreplies (
	Foreign Key (reply_num), (user_num)
    PRIMARY KEY (reply_num), (user_num) 
);

CREATE TABLE IF NOT EXISTS postlikes (
	Foreign Key (like_num), (post_num)
    PRIMARY KEY (like_num), (post_num) 
);

