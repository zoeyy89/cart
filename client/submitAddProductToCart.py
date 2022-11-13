#!python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cgitb
cgitb.enable()

import cart 

#連線DB
from dbConfig import conn, cur

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>使用者端功能 - 加入貨品到購物車
</title>
</head>
<body>
""")

# get form value
form = cgi.FieldStorage()
product_id = form.getvalue('product_id')
order_quantity = form.getvalue('quantity')
product_r = cart.query_product_in_stock( product_id ) 

print("<br><br>貨品編號:", product_id, "貨品名稱:", product_r[1], "單價:", product_r[2] , "庫存數量", product_r[3], "下訂數量", order_quantity, "<br><br>" )

if int( order_quantity ) > product_r[3]:
    print("抱歉，訂購數量超過庫存數量!!!<br>")    
else:    
    if cart.user_add_product_to_cart( 'User001', product_id, product_r[1], product_r[2], order_quantity):
        print("加入購物車成功<br>")
    else:
        print("抱歉，相同貨品編號的資料已存在購物車!!!<br>")     
    
print("<br><a href='client_main.py'>回用戶端功能表</a>")
print("</body></html>")

