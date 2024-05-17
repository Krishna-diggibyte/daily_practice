create Procedure emp_dynamic
@dept_id varchar(10)='d007'
as
begin
select * from new_table where new_table.dept_no=@dept_id;
END

EXEC emp_dynamic 'd001'
EXEC emp_dynamic 'd002'
EXEC emp_dynamic
