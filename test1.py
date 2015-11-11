import os
import kinterbasdb
#
# this file opens the nwtest2.fdb database
# then it gets all the rows of the project table
# then it prints them
#
con=kinterbasdb.connect(dsn="c:\\python progs\\nwtestdb2.fdb", user='norm', password='norm')
cur=con.cursor()
cur.execute("select * from project")
print cur.fetchall()
print 
print 'project name and product'
print 
query = "select proj_name, product from project order by proj_name desc"
cur.execute(query)
for row in cur:
    print '%s is for %s.' % (row[0], row[1])
print 
print 'here are the languages'
print
SELECT = "select name, year_released from languages order by year_released"

# 1. Iterate over the rows available from the cursor, unpacking the
# resulting sequences to yield their elements (name, year_released):
cur.execute(SELECT)
for (name, year_released) in cur:
    print '%s has been publicly available since %d.' % (name, year_released)
print 
print 'add a language'
print 
insert = "insert into languages (name, year_released) values ('Lisp',1962)";
cur.execute(insert)
con.commit()
print 
print 'here are the languages'
print
SELECT = "select name, year_released from languages order by year_released"

# 1. Iterate over the rows available from the cursor, unpacking the
# resulting sequences to yield their elements (name, year_released):
cur.execute(SELECT)
for (name, year_released) in cur:
    print '%s has been publicly available since %d.' % (name, year_released)
