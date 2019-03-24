# Log Analytics 
_*by Sameh Koleid*_
## The task
You've been hired onto a team working on a newspaper site. The user-facing newspaper site frontend itself, and the database behind it, are already built and running. You've been asked to build an internal reporting tool that will use information from the database to discover what kind of articles the site's readers like.
The database contains newspaper articles, as well as the web server log for the site. The log has a database row for each time a reader loaded a web page. Using that information, your code will answer questions about the site's user activity.
The task is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.
It does so by answering this 3 questions :-
1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

Note: The program doesn't take any user input, it just uses pre-programmed select statements.
## Content
* logs_analysis.py
* ex_output.txt (example output)
* README.md
### Dependencies
* [python 2](https://www.python.org/downloads/release/python-2712/)
* [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
* [Vagrant](https://www.vagrantup.com/downloads.html)
* the only library needed is the [psycopg2](http://initd.org/psycopg/docs/install.html) lib for connecting to the databse `pip install psycopg2`.
* [Git Bash](https://git-scm.com/downloads) (for windows users)
* This is the database code for the `view` that is used in this program:-
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
### Instructions
1. Download and Unzip the configuration file for the Vagrant VM [FSND-Virtual-Machine.zip](https://s3.amazonaws.com/video.udacity-data.com/topher/2018/April/5acfbfa3_fsnd-virtual-machine/fsnd-virtual-machine.zip).
2. inside the vagrant subdirectory, run the command `vagrant up` then `vagrant ssh` and then `cd \vagrant`.
3.  Download and Unzip [newsdata.zip](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip) in your `vagrant` subdirectory.
4.  Use the command `psql -d news -f newsdata.sql` to load the data from the `newsdata.sql` file.
5.  Clone or download this repository.
6. Finally, type `python logs_analysis.py` to run the program.
### Output Example
```
1. What are the most popular three articles of all time?
1- "Candidate is jerk, alleges rival" -- 338647 views
2- "Bears love berries, alleges bear" -- 253801 views
3- "Bad things gone, say good people" -- 170098 views


2. Who are the most popular article authors of all time?
1- Ursula La Multa -- 507594 views
2- Rudolf von Treppenwitz -- 423457 views
3- Anonymous Contributor -- 170098 views
4- Markoff Chaney -- 84557 views


3. On which days did more than 1% of requests lead to errors?
2016-07-17 -- 2.3%
```