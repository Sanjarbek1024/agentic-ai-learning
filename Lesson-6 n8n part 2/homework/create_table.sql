DROP TABLE IF EXISTS order_items CASCADE;
DROP TABLE IF EXISTS orders CASCADE;
DROP TABLE IF EXISTS products CASCADE;
DROP TABLE IF EXISTS users CASCADE;

CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    telegram_id BIGINT UNIQUE,
    full_name VARCHAR(100),
    username VARCHAR(100),
    phone VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    category VARCHAR(50),
    price NUMERIC(10,2),
    stock INTEGER
);

CREATE TABLE orders (
    id SERIAL PRIMARY KEY,
    user_id INTEGER REFERENCES users(id),
    status VARCHAR(30),
    total NUMERIC(10,2),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE order_items (
    id SERIAL PRIMARY KEY,
    order_id INTEGER REFERENCES orders(id) ON DELETE CASCADE,
    product_id INTEGER REFERENCES products(id),
    quantity INTEGER,
    price NUMERIC(10,2)
);

--------------------------------

INSERT INTO users (telegram_id, full_name, username, phone) VALUES
(10001,'Ali Valiyev','ali','+998901111111'),
(10002,'Vali Karimov','vali','+998902222222'),
(10003,'Sanjarbek Gulomjonov','sanjar','+998903333333'),
(10004,'Madina Xasanova','madina','+998904444444'),
(10005,'Aziza Sobirova','aziza','+998905555555');

INSERT INTO products (name, category, price, stock) VALUES
('MacBook Air M3','Laptop',1500,8),
('iPhone 16','Phone',1200,15),
('AirPods Pro','Accessory',250,40),
('Mechanical Keyboard','Accessory',120,20),
('27 inch Monitor','Monitor',350,12),
('Logitech MX Master 3S','Mouse',110,25);

INSERT INTO orders (user_id,status,total) VALUES
(1,'completed',1750),
(2,'pending',1200),
(3,'completed',470),
(4,'cancelled',250),
(5,'completed',1610);

INSERT INTO order_items (order_id,product_id,quantity,price) VALUES
(1,1,1,1500),
(1,3,1,250),
(2,2,1,1200),
(3,5,1,350),
(3,4,1,120),
(4,3,1,250),
(5,1,1,1500),
(5,6,1,110);


--------------------------------

SELECT * FROM users;

SELECT * FROM products;

SELECT * FROM orders;

SELECT
u.full_name,
SUM(o.total) AS total_spent
FROM users u
JOIN orders o ON u.id=o.user_id
WHERE o.status='completed'
GROUP BY u.full_name
ORDER BY total_spent DESC;

SELECT
p.name,
SUM(oi.quantity) sold
FROM products p
JOIN order_items oi ON p.id=oi.product_id
GROUP BY p.name
ORDER BY sold DESC;

SELECT
o.id,
u.full_name,
o.total,
o.status
FROM orders o
JOIN users u ON u.id=o.user_id;