#!python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs, sys 
sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
import cgi
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
<title>購物車倉庫管理端功能表 </title>
</head>
<body>
<center><H2>購物車倉庫管理端功能表 </H2></center>
""")

product_list = cart.get_in_stock_product_list()

print("<h4>倉庫貨品清單</h4><table board=1><tr><td>貨品編號</td><td>名稱</td><td>單價</td><td>庫存量</td><td></td></tr>")
for ( product_id, name, price, quantity, updated_at, created_at ) in product_list:
    print( f"<tr><td>{product_id}</td><td>{name}</td><td>{price}</td><td>{quantity}</td>" )
    print( f"<td><a href=EditProductInStock.py?product_id={product_id}>編修</td>" )    
    print( f"<td><a href=DeleteProductInStock.py?product_id={product_id}>刪除</td></tr>" )

print("</table><br><hr><br><br>" )

order_list = cart.query_not_shipped_order()

print("<h4>未出貨訂單明細</h4><table board=1><tr><td>訂單編號</td><td>用戶id</td><td>訂單金額</td></td><td>下訂時間</td></tr>")
for ( order_id, user_id, total_price, created_at, updated_at ) in order_list:
    print( f"<tr><td>{order_id}</td><td>{user_id}</td><td>{total_price}</td><td>{created_at}</td>" )
    print( f"<td><a href=ship_order.py?order_id={order_id}>出貨</td>" )    


print("""</table><hr>
<a href='addNewProductForm.html'>新貨品建檔作業</a><hr>
</body></html>""")

