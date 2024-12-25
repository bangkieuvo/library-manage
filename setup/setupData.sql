INSERT or ignore INTO user (ID, name, userName, hashedPassword) VALUES
(1, 'Alice', 'alice01', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(2, 'Bob', 'bob02', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(3, 'Charlie', 'charlie03', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(4, 'David', 'david04', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(5, 'Eve', 'eve05', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(6, 'Frank', 'frank06', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(7, 'Grace', 'grace07', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(8, 'Hannah', 'hannah08', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(9, 'Ivy', 'ivy09', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(10, 'Jack', 'jack10', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(15, 'Vo Bang Kieu', 'vbk1212', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92'),
(20, 'Tran Huynh Thien', 'thientranhhh', '8d969eef6ecad3c29a3a629280e686cf0c3f5d5a86aff3ca12020c923adc6c92');

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

INSERT or ignore INTO book (id, name, categoryId, quantity) VALUES
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

INSERT or ignore INTO administrator (id) VALUES
(1),
(15),
(20);

INSERT INTO borrowedBook (userId, bookId, borrowDate, isReturned)
VALUES
(1, 3, '2024-12-01', TRUE),
(5, 7, '2024-12-05', FALSE),
(3, 9, '2024-12-07', TRUE),
(8, 4, '2024-12-10', FALSE),
(4, 2, '2024-12-12', TRUE),
(2, 10, '2024-12-13', FALSE),
(9, 6, '2024-12-14', TRUE),
(7, 1, '2024-12-16', FALSE),
(10, 5, '2024-12-18', TRUE),
(6, 8, '2024-12-20', FALSE),
(1, 4, '2024-12-21', TRUE),
(8, 2, '2024-12-22', FALSE),
(3, 6, '2024-12-23', TRUE),
(9, 5, '2024-12-25', FALSE),
(5, 9, '2024-12-26', TRUE),
(2, 7, '2024-12-28', FALSE),
(7, 10, '2024-12-30', TRUE),
(6, 1, '2024-12-02', FALSE),
(4, 8, '2024-12-04', TRUE),
(1, 6, '2024-12-06', FALSE),
(5, 3, '2024-12-08', TRUE),
(3, 2, '2024-12-11', FALSE),
(8, 10, '2024-12-15', TRUE),
(9, 4, '2024-12-17', FALSE),
(2, 5, '2024-12-19', TRUE),
(7, 8, '2024-12-21', FALSE),
(10, 9, '2024-12-23', TRUE),
(6, 7, '2024-12-24', FALSE),
(4, 3, '2024-12-27', TRUE),
(1, 9, '2024-12-29', FALSE);



commit;
