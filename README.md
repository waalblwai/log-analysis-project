# log-analysis-project
Log Analysis
The project is answering three questions about newspaper articles. The code will answer questions about the site's user activity. You can run the program using the command line. The program is connected to the newsDB using the SQL queries to log data, and print the QUESTIONS and ANSWERS.

Getting Started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Prerequisites
You have to download: 
- Psycopg2 v2.7.5  (http://initd.org/psycopg/download/)
- PostgreSQL v9.5.14  (https://www.postgresql.org/download/)
- Vagrant v2.2.0  (https://www.vagrantup.com/downloads.html) 
- VirtualBox v5.1.38  (https://www.virtualbox.org/wiki/Download_Old_Builds_5_1)
 You will also need a Unix-style terminal program. On Mac or Linux systems, you can use the built-in Terminal. On Windows, we recommend Git Bash, which is installed with the Git version control software. 

Installing
Once you get the above software installed, follow the following instructions USING THE COMMAND LINE : 
cd vagrant vagrant up vagrant ssh cd /vagrant mkdir log-analysis-project cd log-analysis-project 


Running the tests
After you successfully installations, you can run this code by:
```sh
$ python3 LogAnalysis.py
```
The output results should be below:
1. What are the most popular three articles of all time?
candidate-is-jerk 338647
bears-love-berries 253801
bad-things-gone 170098
2. Who are the most popular article authors of all time?
Rudolf von Treppenwitz 338647
Ursula La Multa 253801
Anonymous Contributor 170098
Ursula La Multa 84906
Rudolf von Treppenwitz 84810
Markoff Chaney 84557
Ursula La Multa 84504
Ursula La Multa 84383
3. On which days did more than 1% of requests lead to errors?
2.26268624680272595600 2016-07-17

You may want to see the views that I create for:

 Question #1
create view articalsslug as select articles.slug, count(log.path) as a from articles join log on SUBSTRING( log.path, 10)=articles.slug group by articles.slug order by a desc;

Question #2
create view days as select count(case when status='200 OK' then 1 ELSE NULL END) as OkStatus,count(case when status= '404 NOT FOUND' then 1 ELSE NULL end) as NFStatus, date(time) as date from log group by date;

Break down into end to end tests
When you finish tuning the program and see the result. You can close the the VM using the command line, as we start it, printing q OR control+d.

And coding style tests
This test to insure that the code is written correctly no whitespaces, long lines, and doublespaces. You can test the code in using the command line too. Just print ..
$ pycodestyle LogAnalysis.py


Built With
	•	Virtual Machine: https://www.virtualbox.org/wiki/Downloads 
	•	Vagrant: https://www.vagrantup.com/downloads.html 

Versioning
This project use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/waalblwai/log-analysis-project). 

Authors
	•	Walaa alblwai [waalblwai]- (https://github.com/waalblwai)

License
This project is licensed under the MIT License - see the LICENSE.md file for details

