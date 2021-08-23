INSERT INTO post (title, body, created)
VALUES
  ('test title', 'test' || x'0a' || 'body', '2018-01-01 00:00:00');


INSERT INTO customer (cust_number, name, address, postal_number, postal_address, created)
VALUES
  (42, 'Nisse', 'Gatan 2', '123 45', 'Staden', '2018-01-01 00:00:00');