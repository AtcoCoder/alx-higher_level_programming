-- lists all the tables of a database in MySQL server.
SELECT table_name
FROM information_schema.tables
WHERE table_schema = DATABASE();
