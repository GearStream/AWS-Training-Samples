create database gearstream;
	\connect gearstream;
create schema gearstream;

create table gearstream.user_table(
	user_name text PRIMARY KEY,
	password text,
	first_name text,
	last_name text,
	token text
);