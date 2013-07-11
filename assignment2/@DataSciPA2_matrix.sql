
SELECT "row_num", "col_num", "value" 
	FROM "a"
GO


SELECT "row_num", "col_num", "value" 
	FROM "b"
GO


SELECT 
    a.row_num, 
   b.col_num,

sum( ifnull(a.value* b.value,0))
	FROM a, b
where a.col_num=b.row_num
group by a.row_num, b.col_num

GO

--(3,2) (row=2 column = 3) = 2874