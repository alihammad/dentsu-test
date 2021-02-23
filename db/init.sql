DROP DATABASE IF EXISTS skillfinder;
CREATE DATABASE skillfinder;

USE skillfinder;

CREATE TABLE people (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `first_name` VARCHAR(100),
  `last_name` VARCHAR(100),
  `email` VARCHAR(100),
  `address` VARCHAR(1000),
  `skills` VARCHAR(2000)
);


CREATE TABLE project (
  `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
  `project_name` VARCHAR(100),
  `date_posted` VARCHAR(100), 
  `department`  VARCHAR(100),
  `description`  VARCHAR(5000),
  `skills`  VARCHAR(2000)
);

LOAD DATA INFILE '/data/people.csv' INTO TABLE people 
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;

LOAD DATA INFILE '/data/projects.csv' INTO TABLE project
FIELDS TERMINATED BY ',' 
ENCLOSED BY '"' 
LINES TERMINATED BY '\n' 
IGNORE 1 LINES;
