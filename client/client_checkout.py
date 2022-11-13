#!python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
import cgitb
cgitb.enable()

import cart

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<style>
table, th, td {
  border:1px solid black;
}
</style>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>購物車使用者端功能表</title>
</head>
<body>
<center><H2>購物車使用者端 - 結帳 </H2></center>
<br>
USER ID: User001
<hr>
""")

print("""
<center><H2>購物車內容</H2></center>
""")

product_list = cart.user_get_cart_products_list( 'User001')
amount = 0
print("<h4>購物車內容</h4><table board=1><tr><td>貨品編號</td><td>名稱</td><td>單價</td><td>下訂數量</td><td>小計</td></tr>")
for ( product_id, name, price, quantity, updated_at, created_at ) in product_list:
    print( f"<tr><td>{product_id}</td><td>{name}</td><td>{price}</td><td>{quantity}</td><td>{price * quantity}</td></tr>" )
    amount += price * quantity     
print( "<tr><td>合計</td><td></td><td></td><td></td><td>", amount, "</td></tr>" )

print("""</table><hr>
<fieldset>
<form method="post" action="submit_checkout.py">
結帳金額：<input type="hidden" name='amount' 
""")

print( "value=" , amount, ">", amount )
print( 
"""
<br>
<input type="submit" value= "確認結帳">
</form>
</fieldset>
""" )

print( "<br><a href='client_main.py'>回用戶端功能表</a></body></html>" )

