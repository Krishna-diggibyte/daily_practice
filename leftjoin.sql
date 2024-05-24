-- # Write your MySQL query statement below
select  empuni.unique_id as unique_id, emp.name as name
from Employees emp left join EmployeeUNI empuni on emp.id = empuni.id
