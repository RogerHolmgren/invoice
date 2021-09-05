DROP TABLE IF EXISTS post;
DROP TABLE IF EXISTS customer;

CREATE TABLE post (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  title TEXT NOT NULL,
  body TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE customer (
  cust_number INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  address TEXT NOT NULL,
  postal_number TEXT NOT NULL,
  postal_address TEXT NOT NULL,
  created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO customer (cust_number, name, address, postal_number, postal_address, created)
VALUES
  (42, 'Nisse', 'Gatan 2', '123 45', 'Staden', '2018-01-01 00:00:00');