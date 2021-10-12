-- 1.
-- Viết câu lệnh truy vấn lấy dữ liệu từ 2 bảng orders và shippers:
-- Kết quả bao gồm: order_id, shipped_date và shipper_name

SELECT order_id, shipped_date, name FROM `orders` as o left JOIN shippers as s on o.shipper_id =s.shipper_id


-- 2.
-- Viết câu lệnh truy vấn lấy ra dữ liệu từ tất cả các bảng trong CSDL sql_invoicing:
-- Kết quả bao gồm: payment_id, client_name, client_address, invoice_number, payment_method và amount

SELECT payment_id, name, address, number, payment_method, amount 
FROM `payments` as p left JOIN invoices as i on p.invoice_id=i.invoice_id left JOIN clients as c on p.client_id=c.client_id

SELECT *
FROM payments AS p
JOIN clients AS c USING(client_id)
JOIN invoices AS i USING(invoice_id)
JOIN payment_methods AS m ON p.payment_method = m.payment_method_id;


-- 3.
-- Viết câu lệnh truy vấn lấy ra dữ liệu từ 4 bảng orders, customers, order_statuses trong CSDL sql_store, và bảng products trong CSDL sql_inventory:
-- Kết quả bao gồm: order_id, full_name, status_name, và product_name
-- Sắp xếp tập kết quả theo order_id

SELECT payment_id, name, address, number, payment_method, amount FROM `payments` as p left JOIN invoices as i on p.invoice_id=i.invoice_id left JOIN clients as c on p.client_id=c.client_id

-- 4.
-- Viết câu lệnh truy vấn lấy ra các records từ 2 bảng employees và offices:
-- Các cột bao gồm: Employee ID, Full Name, Report To, Office Address
-- Report To là full_name của employee tương ứng
-- Chỉ lấy ra các records với office_id là 1
-- Sắp xếp kết quả theo Employee ID
SELECT e.employee_id AS 'Employee ID',
		CONCAT(e.first_name, ' ', e.last_name) AS 'Full Name',
        CONCAT(ee.first_name, ' ', ee.last_name) AS 'Report To',
		address AS 'Office Address'
FROM sql_hr.employees AS e
LEFT JOIN sql_hr.employees AS ee ON e.reports_to = ee.employee_id
JOIN sql_hr.offices AS o ON e.office_id = o.office_id;

-- 5.
-- Viết câu lệnh truy vấn lấy ra các records từ 2 bảng products và order_items:
-- Chứa các cột Product ID, Product Name, Quantity (trong bảng order_items)
-- Tập kết quả phải bao gồm cả các products chưa có (không tồn tại) trong order_items

-- 6.
-- Viết câu lệnh truy vấn lấy ra các records từ bảng employees:
-- Chứa các cột Employee ID, Employee Name, và Report To (Employee Name)
-- Tập kết quả bao gồm cả các records mà Report To là NULL
-- Nếu Report To là NULL, hiển thị text thay thế là 'Big Boss'


SELECT 
    e.employee_id,
    e.first_name,
    e.last_name,
    IF(e.reports_to IS NULL,
        'Big Boss',
        CONCAT(ee.first_name, ee.last_name))
FROM
    sql_hr.employees AS e
        LEFT JOIN
    sql_hr.employees AS ee ON e.reports_to = ee.employee_id;



cua Mai:

ex5: 
select 
od.product_id,
pd.name,
od.quantity
from sql_inventory.products pd 
left join sql_store.order_items od on pd.product_id = od.product_id
EX6:
select
       employee_id
     , concat (first_name,' ', last_name) as employee_full_name
     , case
              when reports_to is null
                     then 'Big Boss'
                     else reports_to
       end as report_to_name
from
       employees
where
       reports_to is null




-- 7 .
-- Viết câu lệnh truy vấn lấy ra các records từ 4 bảng orders, customers, order_statuses và shippers:
-- Chứa các cột Order ID, Customer Full Name, Ship Status và Shipper Name
-- Bao gồm tất cả records trong orders, bất kể có shiper_id hay không
-- Sắp xếp dữ liệu theo order_id

Mai:
EX7: 
select 
order_id,
concat (first_name, ' ',last_name ) as full_name,
odst.name as ship_status,
sp.name as shipper_name

from orders od
left join customers ct on od.customer_id = ct.customer_id
left join order_statuses odst on od.order_id = odst.order_status_id
left join shippers sp on od.shipper_id = sp.shipper_id

order by order_id DESC;