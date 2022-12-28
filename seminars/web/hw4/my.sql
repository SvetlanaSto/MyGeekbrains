-- create
CREATE TABLE groupmates (
  id INTEGER PRIMARY KEY,
  name TEXT NOT NULL,
  age INTEGER NOT NULL,
  address TEXT NOT NULL
);

-- insert
INSERT INTO groupmates VALUES (1, 'Наталья', 30, 'Москва');
INSERT INTO groupmates VALUES (2, 'Антон', 29, 'Москва');
INSERT INTO groupmates VALUES (3, 'Арсений', 26, 'Улан-Удэ');
INSERT INTO groupmates VALUES (4, 'Андрей', 40, 'Мытищи');
INSERT INTO groupmates VALUES (5, 'Дарья', 30, 'Саратов');
INSERT INTO groupmates VALUES (6, 'Дмитрий', 40, 'Балашиха');
INSERT INTO groupmates VALUES (7, 'Екатерина', 25, 'Санкт-Петербург');
INSERT INTO groupmates VALUES (8, 'Марина', 31, 'Нефтеюганск');
INSERT INTO groupmates VALUES (9, 'Ярослав', 18, 'Москва');
INSERT INTO groupmates VALUES (10, 'Денис', 30, 'Новосибирск');

-- fetch 
SELECT name FROM groupmates WHERE address = 'Москва' AND age BETWEEN 18 AND 29;

