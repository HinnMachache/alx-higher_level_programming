-- creates the table unique_id on your MySQL server.
CREATE IF NOT EXISTS (
	id INT DEFAULT 1 UNIQUE,
	name VARCHAR(256));
