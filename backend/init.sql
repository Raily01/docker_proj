CREATE TABLE products(
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    price INTEGER
);

--мои итемы, ладно еще есть наушники
INSERT INTO products(name, price)
VALUES
('MacBook', 1800),
('iPhone', 1200),
('Keyboard', 150);