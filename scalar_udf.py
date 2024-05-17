create function add_five(@num as int)
returns int
AS
BEGIN
RETURN  (@num+5)
END

select dbo.add_five(4)

Drop function add_five;
