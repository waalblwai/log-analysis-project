
import psycopg2

conn = psycopg2.connect(database="news")
cursor = conn.cursor()
cursor.execute('''select articles.slug, count(log.path) as a from
articles join log on SUBSTRING( log.path, 10)=articles.slug
group by articles.slug order by a desc limit 3;''')
results = cursor.fetchall()
print('1. What are the most popular three articles of all time?')
for result in results:
    print(result[0], result[1])

cursor.execute('''select authors.name, articalsslug.a from authors, articles,
articalsslug where authors.id = articles.author and
articles.slug = articalsslug.slug;''')
results = cursor.fetchall()
print('2. Who are the most popular article authors of all time?')
for result in results:
    print(result[0], result[1])


cursor.execute('''select * from (select (nfstatus/ sum( okstatus + nfstatus)
* 100) as Error, date from days group by date, nfstatus) as Error
 where Error > 1;''')
results = cursor.fetchall()
print('3. On which days did more than 1% of requests lead to errors?')
for result in results:
    print(result[0], result[1])


conn.close()
