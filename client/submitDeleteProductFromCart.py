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
<title>使用者端功能 - 刪除購物車的貨品
</title>
</head>
<body>
""")

# get form value
form = cgi.FieldStorage()
product_id = form.getvalue('product_id')
name = form.getvalue('name')
price = form.getvalue('price')
quantity = form.getvalue('quantity')
user_id = 'User001' 

print("<br><br>刪除購物車貨品編號:", product_id, "貨品名稱:", name, "單價:",price , "下訂數量", quantity, " 成功!<br><br>" )

cart.user_delete_product_from_cart( user_id, product_id )   
    
print("<br><a href='client_main.py'>回用戶端功能表</a>")
print("</body></html>")

