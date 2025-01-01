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
    (9, 'Y học', 'Nghiên cứu về sức khỏe và chữa bệnh'),
(10, 'Khác', 'Các loại sách khác như Ngoại ngữ, sức khỏe, Âm nhạc,...');

INSERT OR IGNORE INTO Book (id, name, author, categoryId, quantity) VALUES
    (1, 'Lập trình Python', 'Đoàn Minh Phụng', 4, 15),
    (2, 'Thơ ca Việt Nam', 'Bùi Minh Nguyên_ Hà Minh Đức', 1, 20),
    (3, 'Lịch sử thế giới', 'Jane Chisholm', 3, 10),
    (4, 'Kinh tế vi mô', 'Lê Bảo Lâm', 5, 12),
    (5, 'Văn học phương Tây', 'Lê Nguyên Cẩn', 1, 13),
    (6, 'Nghệ thuật tranh sơn dầu', 'Nguyễn Đình Đăng', 8, 8),
    (7, 'Giáo dục hiện đại', 'Hồ Ngọc Đại', 10, 25),
    (8, 'Toán học cơ bản và nâng cao', 'Nguyễn Đức Tán_Tại Hồ Thị Dung', 2, 22),
    (9, 'Lịch sử Việt Nam', 'Đào Duy Anh', 3, 13),
    (10, 'Giáo trình huấn luyện sức mạnh', 'Bùi Trọng Toại', 10, 11),
    (11, 'Học tiếng Anh cơ bản', 'Elight', 10, 30),
    (12, 'Thơ Hàn Mặc Tử', 'Hàn Mạc Tử', 1, 17),
    (13, 'Y học cổ truyền', 'Đặng Minh Hằng_Nguyễn Thị Thu Hà', 9, 5),
    (14, 'Chuyên đề văn học', 'Nguyễn Thành Huân', 1, 21),
    (15, 'Trái đất và vũ trụ', 'Science Encyclopedia', 2, 18),
    (16, 'Nhạc cổ điển', 'Stacy', 10, 7),
    (17, 'Công nghệ blockchain', 'William', 4, 9),
    (18, 'Tâm lý trẻ em', 'Nguyễn Khắc Viện', 6, 16),
    (19, 'Nghệ thuật sân khấu', 'Trần Văn Khải', 10, 10),
    (20, 'Văn học dân gian', 'Đinh Gia Khánh', 1, 23),
    (21, 'Thế giới động vật', 'Science Encyclopedia', 2, 14),
    (22, 'Du lịch Việt Nam', 'Bùi Thị Hải Yến', 10, 8),
    (23, 'Học tiếng Pháp', 'Trần Sỹ Lan_Hoàng Lê Chính', 10, 12),
    (24, 'Kinh tế toàn cầu', 'Nguyễn Xuân Thắng', 5, 15),
    (25, 'Vật lý cơ bản', 'Hoàng Ngọc Long', 2, 19),
    (26, 'Kỹ thuật lập trình', 'Phạm Văn Ất', 4, 22),
    (27, 'Thơ hiện đại', 'Lã Nguyên', 1, 10),
    (28, 'Triết học phương Tây', 'Bernard Morichrer', 7, 9),
    (29, 'Y học hiện đại', 'Trần Đức Phấn_ Lương Thị Lan Anh', 9, 1);

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

