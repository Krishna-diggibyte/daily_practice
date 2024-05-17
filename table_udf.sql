create function select_gender(@gender as varchar(10))
returns table
as
return
(
select * from new_table where gender=@gender
)

select * from dbo.select_gender('M')
select * from dbo.select_gender('F')
