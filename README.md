# Log Analytics
This project gets information about a news database that is built using PostgreSQL.
It does so by answering this 3 questions :-
- What are the most popular three articles of all time?
- Who are the most popular article authors of all time?
- On which days did more than 1% of requests lead to errors?

Note: The program doesn't take any user input it just uses pre-programmed select statements.
### Dependencies
the only library needed is the `psycopg2` lib for connecting to the databse.
`import psycopg2`

This is the database code for the `view` that is used in this program:-
```
create view mostpop as
select authors.name, popular.title, popular.num
from authors join (
    select articles.title, articles.author, count(log.id) as num
    from articles left join log
    on '/article/' || articles.slug = log.path
    group by articles.title, articles.author) as popular
on authors.id = popular.author
order by popular.num DESC;
```
Note: The view code is executed through `c.execute()` in the code.
### Usage
To run the code :
1. while in your vagrant dir, open your VM using `vagrant up` then `vagrant ssh`.
2. type `python logs_analysis.py`.