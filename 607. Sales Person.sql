declare @RED_com_id int = (select top(1) com_id from Company where name = 'RED');
select
    name
from SalesPerson
where not(exists(select Orders.sales_id from Orders where SalesPerson.sales_id = Orders.sales_id and Orders.com_id = @RED_com_id))
