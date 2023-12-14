-- creates a database
-- and creates a table
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
	id INT UNIQUE NOT NULL AUTO-INCREMENT PRIMARY KEY,
	name VARCHAR(256)
	);
