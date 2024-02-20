-- This script prepares a MySQL server for the project
-- Create database and user and grant them some privileges.


-- Create database `hbnb_test_db`
CREATE DATABASE IF NOT EXISTS `hbnb_test_db`;

-- Create user `hbnb_test` in localhost with password `hbnb_test_pwd`
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';

-- Grant all privileges to user on database `hbnb_test_db`
GRANT ALL PRIVILEGES ON `hbnb_test_db`.* TO 'hbnb_test'@'localhost';

-- Grant SELECT privileges to user on database `performance_schema`
GRANT SELECT ON `performance_schema`.* TO 'hbnb_test'@'localhost';
