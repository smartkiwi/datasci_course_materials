select sum(count) from Frequency where docid='10398_txt_earn'
go


SELECT "docid", "term", "count" 
	FROM "Frequency"
GO

--Problem 1
--a ?docid=10398_txt_earn(frequency)  
select count(*) from Frequency where docid='10398_txt_earn'
--138
go

--b ¹term( ?docid=10398_txt_earn and count=1(frequency))
select count(*) from Frequency where docid='10398_txt_earn' and count=1
go
--110

--c ¹term( ?docid=10398_txt_earn&count=1(frequency)) U ¹term( ?docid=925_txt_trade&count=1(frequency))
select count(*) from
(

select term from Frequency where docid='10398_txt_earn' and count=1
union
select term from Frequency where docid='925_txt_trade' and count=1
)
go
--324

--(d) count: Write a SQL statement to count the number of documents containing the word ÒparliamentÓ
select count(distinct(docid)) from Frequency where term='parliament'
go
--15


--(e) big documents Write a SQL statement to find all documents that have more than 300 total terms, including duplicate terms. 
--(Hint: You can use the HAVING clause, or you can use a nested query. Another hint: Remember that the count column contains the term frequencies, and you want to consider duplicates.) (docid, term_count)
select docid,sum(count) from Frequency 
group by docid
having sum(count)>300
go
--107


select *
from ( 
select docid,sum(count) terms_count  from Frequency 
group by docid
)
where terms_count >300
go
--107

--(f) two words: Write a SQL statement to count the number of unique documents that contain both the word 'transactions' and the word 'world'.
--What to turn in: Run your query against your local database and determine the number of records returned as described above. In your browser, turn in a text file, two_words.txt, which states the number of records.
select distinct(docid) from Frequency where term='transactions'
intersect
select distinct(docid) from Frequency where term='world'
go
--3

select * from Frequency a,Frequency b 
where a.term='transactions' and b.term='world' and a.docid=b.docid
go


---h
select a.docid, b.docid,sum(a.count*b.count) from Frequency a, Frequency b
where a.term=b.term
and a.docid='10080_txt_crude' and b.docid='17035_txt_earn'
and a.docid<b.docid
group by a.docid, b.docid
go
--19



create view freq_with_query as
SELECT * FROM frequency
UNION
SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION
SELECT 'q' as docid, 'taxes' as term, 1 as count
UNION 
SELECT 'q' as docid, 'treasury' as term, 1 as count
go

select count(*) from freq_with_query
go

select b.docid,sum(a.count*b.count) similarity 
from freq_with_query a, freq_with_query b
where a.term=b.term
and a.docid='q'
--and a.docid>b.docid
group by a.docid, b.docid
order by similarity desc
go

--6