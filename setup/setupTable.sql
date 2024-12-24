PRAGMA foreign_keys = ON;
CREATE TABLE if not exists user(
	id integer PRIMARY KEY,
	name varchar(255) not null,
	userName varchar(255) not null,
	hashedPassword varchar(255) not null
);
CREATE TABLE if not exists category(
	id integer primary key,
	name varchar(255) not null,
	describtion varchar(255)
);
CREATE table if not exists book(
	id integer primary key,
	name varchar(255) not null,
	categoryId integer,
	quantity integer not null,
	foreign key (categoryId) references category(id)
);
CREATE table if not exists administrator(
	id integer primary key,
	foreign key (id) references user(id) ON DELETE restrict
);