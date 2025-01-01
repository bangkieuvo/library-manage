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

INSERT or ignore INTO category (id, name, description) VALUES
    (1, 'Văn học', 'Tìm hiểu về các tác phẩm văn học cổ điển và hiện đại'),
    (2, 'Khoa học', 'Nghiên cứu các phát minh và hiện tượng tự nhiên'),
    (3, 'Lịch sử', 'Tìm hiểu về các sự kiện và thời kỳ lịch sử'),
    (4, 'Công nghệ thông tin', 'Kiến thức về phần mềm, phần cứng và lập trình'),
    (5, 'Kinh tế', 'Phân tích thị trường và các lý thuyết kinh tế'),
    (6, 'Tâm lý học', 'Nghiên cứu hành vi và tâm lý con người'),
    (7, 'Triết học', 'Tư duy về các khái niệm cơ bản của cuộc sống'),
    (8, 'Nghệ thuật', 'Khám phá hội họa, điêu khắc và sáng tạo nghệ thuật'),
    (9, 'Âm nhạc', 'Tìm hiểu về nhạc lý và các thể loại âm nhạc'),
    (10, 'Y học', 'Nghiên cứu về sức khỏe và chữa bệnh'),
    (11, 'Thể thao', 'Tìm hiểu các môn thể thao và lợi ích sức khỏe'),
    (12, 'Du lịch', 'Khám phá văn hóa và địa danh trên thế giới'),
    (13, 'Giáo dục', 'Các phương pháp giảng dạy và học tập hiệu quả'),
    (14, 'Ngoại ngữ', 'Học tập và sử dụng ngôn ngữ nước ngoài'),
    (15, 'Thơ ca', 'Khám phá các tác phẩm thơ văn đặc sắc');

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
(10, 'The Chef’s Table', 10, 1);

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



INSERT INTO Books (BookName, CategoryID, Quantity) VALUES
    ('Lập trình Python',author here!, 4, 15),
    ('Thơ ca Việt Nam', 15, 20),
    ('Lịch sử thế giới', 3, 10),
    ('Kinh tế vi mô', 5, 12),
    ('Tâm lý học hành vi', 6, 18),
    ('Nghệ thuật tranh sơn dầu', 8, 8),
    ('Giáo dục hiện đại', 13, 25),
    ('Toán học cơ bản và nâng cao', 2, 22),
    ('Lịch sử Việt Nam', 3, 13),
    ('Giáo trình huấn luyện sức mạnh', 11, 11),
    ('Học tiếng Anh cơ bản', 14, 30),
    ('Thơ Hàn Mặc Tử', 15, 17),
    ('Y học cổ truyền', 10, 5),
    ('Chuyên đề văn học', 1, 21),
    ('Trái đất và vũ trụ', 2, 18),
    ('Nhạc cổ điển', 9, 7),
    ('Công nghệ blockchain', 4, 9),
    ('Tâm lý trẻ em', 6, 16),
    ('Nghệ thuật sân khấu', 8, 10),
    ('Văn học dân gian', 1, 23),
    ('Thế giới động vật', 2, 14),
    ('Du lịch Việt Nam', 12, 8),
    ('Học tiếng Pháp', 14, 12),
    ('Kinh tế toàn cầu', 5, 15),
    ('Vật lý cơ bản', 2, 19),
    ('Kỹ thuật lập trình', 4, 22),
    ('Thơ hiện đại', 15, 10),
    ('Triết học phương Tây', 7, 9),
    ('Y học hiện đại', 10, 11),
    ('Văn học phương Tây', 1, 13);
