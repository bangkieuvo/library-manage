CREATE TABLE if not exists user(
	ID INTERGER PRIMARYKEY not null,
	name varchar(255),
	userName varchar(255),
	password interger
);
CREATE TABLE if not exists category(
	id interger primarykey not null,
	name varchar(255)
);