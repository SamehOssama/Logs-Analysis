#!/usr/bin/env python
import psycopg2

db = psycopg2.connect("dbname=news")
c = db.cursor()

c.execute("""create view mostpop as
select authors.name, popular.title, popular.num
from authors join (
    select articles.title, articles.author, count(log.id) as num
    from articles left join log
    on '/article/' || articles.slug = log.path
    group by articles.title, articles.author) as popular
on authors.id = popular.author
order by popular.num DESC;""")

print("1. What are the most popular three articles of all time?")
query1 = "select title, num from mostpop limit 3;"
c.execute(query1)
data = c.fetchall()
i = 0
while i < len(data):
    print('{}- "{}" -- {} views'.format(i+1, data[i][0], data[i][1]))
    i += 1
print('\n')

print("2. Who are the most popular article authors of all time?")
query2 = """select name, sum(num) as total
    from mostpop group by name order by total DESC;"""
c.execute(query2)
data = c.fetchall()
i = 0
while i < len(data):
    print('{}- {} -- {} views'.format(i+1, data[i][0], data[i][1]))
    i += 1
print('\n')

print("3. On which days did more than 1% of requests lead to errors?")
query3 = """select date(time), round(errors.error*100::numeric/count(status),1)
from log, (select date(time) as date2, count(status) as error
    from log where status != '200 OK'
    group by date(time)) as errors
where errors.date2 = date(log.time)
group by date(log.time), error
having ((errors.error*100)::numeric/count(status)) > 1 limit 5;"""
c.execute(query3)
data = c.fetchall()
i = 0
while i < len(data):
    print('{} -- {}%'.format(data[i][0], data[i][1]))
    i += 1
c.close()
