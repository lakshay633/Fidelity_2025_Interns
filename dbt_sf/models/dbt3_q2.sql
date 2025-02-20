SELECT c.customerName, c.phone, c.city, o.status, o.orderDate, p.productName
FROM db1.s1.orders o
INNER JOIN db1.s1.customers c ON o.customerNumber=c.customerNumber
INNER JOIN db1.s1.orderDetails od ON od.orderNumber=o.orderNumber
INNER JOIN db1.s1.products p ON od.productCode=p.productCode
where o.status = 'Pending'