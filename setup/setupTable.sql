PRAGMA foreign_keys = ON;
CREATE TABLE if not exists user(
	id integer PRIMARY KEY not null,
	name varchar(255) not null,
	userName varchar(255) not null,
	password integer not null
);
CREATE TABLE if not exists category(
	id integer primary key not null,
	name varchar(255) not null,
	describtion varchar(255)
);
CREATE table if not exists book(
	bookCode integer primary key not null,
	name varchar(255) not null,
	categoryId integer,
	quantity integer not null,
	foreign key (categoryId) references category(id)
);
CREATE table if not exists administrator(
	id integer primary key not null,
	userId integer not null unique,
	foreign key (userId) references user(id)
);