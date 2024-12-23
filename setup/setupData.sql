INSERT or ignore INTO user (ID, name, userName, hashedPassword) VALUES
(1, 'Alice', 'alice01', 4911055567749929105),
(2, 'Bob', 'bob02', 4911055567749929105),
(3, 'Charlie', 'charlie03', 4911055567749929105),
(4, 'David', 'david04', 4911055567749929105),
(5, 'Eve', 'eve05', 4911055567749929105),
(6, 'Frank', 'frank06', 4911055567749929105),
(7, 'Grace', 'grace07', 4911055567749929105),
(8, 'Hannah', 'hannah08', 4911055567749929105),
(9, 'Ivy', 'ivy09', 4911055567749929105),
(10, 'Jack', 'jack10', 4911055567749929105),
(15, 'Vo Bang Kieu', 'vbk1212', 4911055567749929105),
(20, 'Tran Huynh Thien', 'thientranhhh', 4911055567749929105);

INSERT or ignore INTO category (id, name, describtion) VALUES
(1, 'Fiction', 'Books with fictional stories'),
(2, 'Science', 'Books about science topics'),
(3, 'History', 'Historical books'),
(4, 'Technology', 'Books about technology'),
(5, 'Art', 'Books about art and design'),
(6, 'Travel', 'Travel guides and stories'),
(7, 'Biography', 'Biographical books'),
(8, 'Health', 'Books about health and wellness'),
(9, 'Education', 'Educational books'),
(10, 'Cooking', 'Cookbooks and recipes');

INSERT or ignore INTO book (bookCode, name, categoryId, quantity) VALUES
(1, 'The Great Gatsby', 1, 15),
(2, 'Physics Fundamentals', 2, 20),
(3, 'World War II', 3, 10),
(4, 'Artificial Intelligence', 4, 8),
(5, 'Modern Art', 5, 12),
(6, 'Europe Travel Guide', 6, 7),
(7, 'Steve Jobs Biography', 7, 5),
(8, 'Healthy Living', 8, 18),
(9, 'Mathematics for Beginners', 9, 25),
(10, 'The Chef’s Table', 10, 14);

INSERT or ignore INTO administrator (id, userId) VALUES
(1, 15),
(2, 20);


commit;
