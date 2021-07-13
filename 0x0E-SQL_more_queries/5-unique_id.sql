-- creates the table unique_id on mysql server
-- database name passed as an argument of the mysql command
CREATE TABLE IF NOT EXISTS unique_id (id INT DEFAULT 1 UNIQUE,
		name VARCHAR(256)
		);
