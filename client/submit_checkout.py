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
<style>
table, th, td {
  border:1px solid black;
}
</style>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>使用者端功能 - 結帳
</title>
</head>
<body>
""")

# get form value
form = cgi.FieldStorage()
amount = form.getvalue('amount')
user_id = 'User001' 

order_id = cart.user_transfer_cart_to_order( user_id, amount ) 

print("<br><br>結帳金額", amount, " 結帳成功! 訂單編號:", order_id, "<br><br>" )

order_detail = cart.user_query_order_detail_list( order_id )

print("<h4>訂單明細內容</h4><table board=1><tr><td>訂單編號</td><td>貨品編號</td><td>名稱</td><td>單價</td><td>下訂數量</td><td>小計</td></tr>")
for ( order_id, product_id, name, price, quantity, updated_at, created_at ) in order_detail:
    print( f"<tr><td>{order_id}</td><td>{product_id}</td><td>{name}</td><td>{price}</td><td>{quantity}</td><td>{price * quantity}</td><tr>" )  


print("</table><hr>" )
 
    
print("<br><a href='client_main.py'>回用戶端功能表</a>")
print("</body></html>")

