DROP TABLE employees;
DROP TABLE levels;
DROP TABLE credentials;

CREATE TABLE levels (
  id SERIAL UNIQUE PRIMARY KEY,
  job_title VARCHAR(255) UNIQUE
);

CREATE TABLE credentials (
  id SERIAL PRIMARY KEY,
  pin INT UNIQUE,
  passcode INT
);

CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  phone VARCHAR(15),
  email VARCHAR(100),
  contract INT,
  start_date DATE,
  end_date DATE,
  credential_id INT NOT NULL REFERENCES credentials(id) ON DELETE CASCADE,
  level_id INT NOT NULL REFERENCES levels(id) ON DELETE CASCADE
);

CREATE TABLE clocks (
  id SERIAL PRIMARY KEY,
  day DATE,
  clock_in TIME,
  clock_out TIME,
  employee_id INT NOT NULL REFERENCES employees(id) ON DELETE CASCADE
);