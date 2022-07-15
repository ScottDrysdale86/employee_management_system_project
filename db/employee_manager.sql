DROP TABLE employees;
DROP TABLE levels;
DROP TABLE credentials;

CREATE TABLE employees (
  id SERIAL PRIMARY KEY,
  name VARCHAR(100),
  phone VARCHAR(15),
  email VARCHAR(100),
  contract INT,
  active BOOLEAN,
  start_date DATE,
  end_date DATE,
  credential_id INT IS NOT NULL REFERENCES credentials(id) ON DELETE CASCADE,
  level_id INT IS NOT NULL REFERENCES levels(id) ON DELETE CASCADE
);

CREATE TABLE levels (
  id SERIAL PRIMARY KEY,
  name VARCHAR(15)
);

CREATE TABLE credentials (
  id SERIAL PRIMARY KEY,
  pin INT,
  passcode INT,
  employee_id INT IS NOT NULL REFERENCES employee(id) ON DELETE CASCADE
);