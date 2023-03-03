/* This is for illustrative purposes and needs to be converted into Django models. */

drop database if exists cuisine_critic;
create database cuisine_critic;
use cuisine_critic;

/* test */
create table user (
    user_id varchar(50) not null,
    forename varchar(50) not null,
    surname varchar(50) not null,
    email varchar(200) not null,
    avatar_src varchar(200) not null,
    password varchar(200) not null,
    primary key (user_id)
);

create table category (
    category_id varchar(50) not null,
    name varchar(200) not null,
    image_src varchar(200) not null, /* image to display with this category */
    primary key (category_id)
);

create table restaurant (
    restaurant_id varchar(50) not null,
    name varchar(200) not null,
    address varchar(200) not null,
    category varchar(200),
    foreign key (category) references category(category_id),
    primary key (restaurant_id)
);

create table restaurant_image (
    image_id varchar(50) not null,
    restaurant_id varchar(50) not null,
    image_src varchar(200) not null,
    primary key (image_id),
    foreign key (restaurant_id) references restaurant(restaurant_id)
);


create table review (
    review_id varchar(50) not null,
    user_id varchar(50) not null,
    restaurant_id varchar(50) not null,
    rating float not null check (rating >= 0 and rating <= 5),
    title varchar(200) not null,
    comment varchar(2000) not null,
    likes integer not null,
    image_src varchar(200),
    primary key (review_id),
    foreign key (user_id) references user(user_id),
    foreign key (restaurant_id) references restaurant(restaurant_id)
);