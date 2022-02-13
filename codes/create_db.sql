create database if not exists kafka_feed;
use kafka_feed;
create table students (
  name varchar(70),
  address varchar(200),
  email varchar(40),
  created_at int
);