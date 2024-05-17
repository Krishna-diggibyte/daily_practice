Create Procedure joinalltable
AS
BEGIN
select * from employee as e inner join dept_emp as de on e.emp_no=de.emp_no inner join department as d on de.dept_no=d.dept_no
END
EXEC joinalltable
