DROP TABLE employees;
DROP TABLE levels;
DROP TABLE credentials;

CREATE TABLE levels (
  id SERIAL PRIMARY KEY,
  name VARCHAR(255)
);

CREATE TABLE credentials (
  id SERIAL PRIMARY KEY,
  pin INT,
  passcode INT
);

CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  phone VARCHAR(15),
  email VARCHAR(100),
  contract INT,
  active BOOLEAN DEFAULT TRUE,
  start_date DATE,
  end_date DATE,
  credential_id INT NOT NULL REFERENCES credentials(id) ON DELETE CASCADE,
  level_id INT NOT NULL REFERENCES levels(id) ON DELETE CASCADE
);