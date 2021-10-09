# 1.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# Tập kết quả chứa các cột first_name, last_name, phone, address và points

#SELECT * FROM `customers` WHERE 1

Select first_name, last_name, phone, address,points from customers


# 2.
# Viết câu lệnh truy vấn lấy ra tất cả product trong bảng products:
# Tập kết quả chứa các cột name, unit_price, và promo
# promo = unit_price - 10%

SELECT * FROM `products`

SELECT name, unit_price,
unit_price*0.9 as promo
  
FROM products;


# 3.
# Viết câu lệnh truy vấn lấy ra tất cả product trong bảng products:
# Chỉ lấy các product có quantity_in_stock < 10
# Tập kết quả gồm các cột name, quantity_in_stock và unit_price

SELECT name, quantity_in_stock, unit_price FROM `products` WHERE quantity_in_stock<10


SELECT NAME,
    quantity_in_stock,
    unit_price
FROM
    `products`
WHERE
    quantity_in_stock < 10


# 4.
# Viết câu lệnh truy vấn lấy ra tất cả order trong bảng orders:
# Chỉ lấy các order có order_date trước 2018
# Tập kết quả gồm các cột order_id, customer_id và status
SELECT * FROM `orders` WHERE order_date<'2018-00-00'


# 5.
# Viết câu lệnh truy vấn lấy ra tất cả order trong bảng orders:
# Có order date trong năm 2018 và status = 2

SELECT * FROM orders WHERE YEAR(order_date) = 2018 and status = 2

# 6.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# Có state = MA hoặc CA và points > 2000

# 7.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# Có birth_date từ 1980 - 1990

# 8.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# Có state không phải TX, TN, VA hoặc CA

# 9.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# Có address chứa từ TRAIL hoặc AVENUE

# 10. 
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# Có phone bắt đầu hoặc kết thúc với số 9

# 11.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# Có first_name và last_name đều bắt đầu bằng ký tự R

# 12.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# first_name có độ dài 4 ký tự

# 13.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# first_name có chứa ký tự B, nhưng không bắt đầu bằng B

# 14.
# Viết câu lệnh truy vấn lấy ra tất cả customer
# Có birth_date từ 1980 - 1990
# Sắp xếp theo độ tuổi (năm sinh) tăng dần

# 15.
# Viết câu lệnh truy vấn lấy ra tất cả product trong bảng products:
# Sắp xếp theo total (quantity * unit_price)

SELECT *, quantity_in_stock * unit_price as total FROM `products` ORDER BY total

# 16.
# Viết câu lệnh truy vấn lấy ra tất cả item trong bảng order_items:
# Có order_id = 2
# Bao gồm các cột order_id, product_id, quantity, unit_price và total (quantity * unit_price)
# Sắp xếp theo total giảm dần

SELECT order_id, product_id, quantity, unit_price, (quantity * unit_price) as total  FROM `order_items` WHERE order_id=2 order by total desc




# 17.
# Viết câu lệnh truy vấn lấy ra 3 customer trong bảng customers
# Có points cao nhất

SELECT * FROM `customers` order by points desc limit 3


# 18.
# Viết câu lệnh truy vấn lấy ra 3 product trong bảng products
# Có total (quantity * unit_price) cao nhất

SELECT *,(quantity_in_stock * unit_price) as total FROM `products` order by total desc limit 3

SELECT quantity_in_stock, (quantity_in_stock*unit_price) as total  FROM `products` order by total DESC LIMIT 3



# 19.
# Viết câu lệnh truy vấn lấy ra tất cả customer trong bảng customers:
# Có tháng sinh là tháng 5
# Bao gồm các cột customer_id, birth_date, fullname (first_name, last_name), phone và class
# Nếu points >= 1000 thì class = Bronze
# Nếu points >= 2000 thì class = Silver
# Nếu points >= 3000 thì class = Gold
# Nếu points < 1000 thì class = Normal
# Sắp xếp theo points giảm dần

SELECT
    customer_id,
    birth_date,
    CONCAT(first_name, last_name) AS fullname,
    phone,
    points,
    CASE 
        WHEN points >= 3000 THEN 'Gold'
        WHEN points >= 2000 THEN 'Silver'
        WHEN points >= 1000 THEN 'Bronze'
        ELSE 'Normal'
END AS class
FROM customers order by points DESC
 


 SELECT
    customer_id,
    birth_date,
    CONCAT(first_name, last_name) AS fullname,
    phone,
    points,
    CASE 
        WHEN points >= 3000 THEN 'Gold'
        WHEN points >= 2000 THEN 'Silver'
        WHEN points >= 1000 THEN 'Bronze'
        ELSE 'Normal'
END AS class
FROM customers WHERE MONTH(birth_date) = 5 order by points DESC
 




SELECT
    customer_id,
    birth_date,
    CONCAT(first_name, last_name) AS fullname,
    phone,
    CASE
       WHEN points >= 3000 THEN 'Gold'
       WHEN points >= 2000 THEN 'Silver'
       WHEN points >= 1000 THEN 'Bronze'   
       WHEN points < 1000 THEN 'Normal'
   END class
FROM
    customers ORDER By POINT DESC
    