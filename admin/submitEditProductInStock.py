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
<title>管理端功能 - 修改倉庫貨品資料
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
print("<br><br>貨品編號:", product_id, "貨品名稱:", name, "單價:", price, "庫存數量", quantity, "<br><br>" )

cart.update_product_in_stock( product_id, name, price, quantity)

print("修改貨品資料成功<br>")
print("<br><a href='admin.py'>回管理端功能表</a>")
print("</body></html>")

