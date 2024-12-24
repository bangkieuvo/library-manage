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


commit;
