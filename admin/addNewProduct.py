#!python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
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
<title>管理端功能 - 新貨品至倉庫
</title>
</head>
<body>
""")

# get form value
form = cgi.FieldStorage()
name = form.getvalue('name')
price = form.getvalue('price')
quantity = form.getvalue('quantity')
print("<br><br>貨品:", name, "單價:", price, "庫存數量", quantity, "<br><br>" )

cart.add_new_product_to_stock(name, price, quantity)

print("新增新貨品至倉庫資料已存入!<br>")
print("<br><a href='admin.py'>回管理端功能表</a>")
print("</body></html>")

