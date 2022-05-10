DROP DATABASE IF EXISTS SocialiApp;
CREATE DATABASE IF NOT EXISTS SocialiApp;
USE SocialiApp;

CREATE TABLE IF NOT EXISTS users (
	username_id INT AUTO_INCREMENT NOT NULL,
    first_name VARCHAR(255) NOT NULL,
    last_name VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
    PRIMARY KEY (username_id)
);
CREATE TABLE IF NOT EXISTS replies (
	reply_num INT AUTO_INCREMENT NOT NULL,
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
	post_num int NOT NULL, 
    username_id int NOT NULL,
    Foreign Key (post_num) REFERENCES posts(post_id), 
    Foreign Key (username_id) REFERENCES users(username_id),
    PRIMARY KEY (post_num, username_id) 
);

CREATE TABLE IF NOT EXISTS userreplies (
	reply_num int NOT NULL, 
    username_id int NOT NULL,
    Foreign Key (reply_num) REFERENCES replies(reply_num), 
    Foreign Key (username_id) REFERENCES users(username_id),
    PRIMARY KEY (reply_num, username_id) 
);

CREATE TABLE IF NOT EXISTS postlikes (
	like_num int NOT NULL, 
    username_id int NOT NULL,
    Foreign Key (like_num) REFERENCES likes(like_num), 
    Foreign Key (username_id) REFERENCES users(username_id),
    PRIMARY KEY (like_num, username_id)  
);

