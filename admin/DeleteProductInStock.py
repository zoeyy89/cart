#!python.exe
import sys
import cgi
import cgitb
cgitb.enable()

import cart 
#連線DB
from dbConfig import conn, cur

print("Content-type: text/html; charset: utf-8\n")
sys.stdout.flush()

# 讀取編輯的貨品編號 
form = cgi.FieldStorage()
product_id = form.getvalue('product_id')

# 用貨品編號查詢倉庫貨品詳細資料
record = cart.query_product_in_stock( product_id )
product_id = record[0]
name = record[1]
price = record[2] 
quantity = record[3]

#讀取刪除貨品資料畫面樣板
with open("DeleteProductInStockForm.html",'rb') as fp:
    st=fp.read()
    st=st.replace(b"###product_id###",str(product_id).encode())
    st=st.replace(b"###name###",name.encode())
    st=st.replace(b"###price###",str(price).encode())
    st=st.replace(b"###quantity###",str(quantity).encode())
    sys.stdout.buffer.write(st)
    
sys.stdout.flush()

