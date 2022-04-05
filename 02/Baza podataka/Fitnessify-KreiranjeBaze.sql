CREATE USER admin SUPERUSER WITH PASSWORD 'admin';
CREATE DATABASE fitnessify OWNER admin;

CREATE TYPE account_type AS ENUM ('admin', 'user');

CREATE TABLE account (id SERIAL PRIMARY KEY NOT NULL, username varchar(50) NOT NULL, email varchar(50) NOT NULL, password varchar(60) NOT NULL, acc_type account_type NOT NULL);
CREATE TABLE goals (id SERIAL PRIMARY KEY NOT NULL, user_id int references account(id) NOT NULL, calories int, time_spent_exercising int, steps int, weight numeric(1));
CREATE TABLE exercise (id SERIAL PRIMARY KEY NOT NULL, name varchar(100) NOT NULL, description varchar(1000) NOT NULL, spent_calories int);
CREATE TABLE account_exercise (account_id SERIAL references account(id) NOT NULL, exercise_id SERIAL references exercise(id) NOT NULL, date_of_exercise timestamp);
CREATE TABLE ingredient (id SERIAL PRIMARY KEY NOT NULL, name varchar(30) NOT NULL, calories int, nutrients varchar(200));
CREATE TABLE account_ingredient (account_id SERIAL references account(id) NOT NULL, ingredient_id SERIAL references ingredient(id) NOT NULL, date_consumed timestamp);
CREATE TABLE recipe (id SERIAL PRIMARY KEY NOT NULL, name varchar(200) NOT NULL, description varchar(1000) NOT NULL, calories int, nutrients varchar(200), prep_time int);
CREATE TABLE account_recipe (account_id SERIAL references account(id) NOT NULL, recipe_id SERIAL references recipe(id) NOT NULL);
CREATE TABLE ingredient_recipe (ingredient_id SERIAL references ingredient(id) NOT NULL, recipe_id SERIAL references recipe(id) NOT NULL, quantity int DEFAULT 1);
