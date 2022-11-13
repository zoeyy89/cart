#連線DB
from dbConfig import conn, cur

##################################################################
# 管理端    

#查詢貨品庫存資料清單
def get_in_stock_product_list():
    sql="select product_id, name, price, quantity, updated_at, created_at from in_stock_products order by product_id ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records

# 新增一筆新貨品至倉庫
def add_new_product_to_stock( name, price, quantity ):
    sql="insert into in_stock_products( name, price, quantity ) values ( %s, %s, %s );"
    cur.execute(sql,( name, price, quantity))
    conn.commit()
    return False
    
#查詢倉庫貸品資料
def query_product_in_stock( product_id ):
    sql="select product_id, name, price, quantity, updated_at, created_at from in_stock_products where product_id = %s ;"
    cur.execute(sql,(product_id,))
    record = cur.fetchone() #只抓一筆回來
    return record  
    
# 修改倉庫貸品資料
def update_product_in_stock( product_id, name, price, quantity ):
    sql="update in_stock_products set name = %s, price = %s, quantity = %s where product_id = %s ;"
    cur.execute(sql,( name, price, quantity, product_id))
    conn.commit()
    return False    
    
# 刪除倉庫一項貨品
def delete_product_from_stock( product_id ):
    sql="delete from in_stock_products where product_id = %s ;"
    cur.execute(sql,(product_id,))
    conn.commit()
    return False
    
#查詢未出貨訂單資料清單
def query_not_shipped_order():
    sql="select order_id, user_id, total_price, created_at, updated_at from orders where shipped = 'N'"
    cur.execute(sql)
    records = cur.fetchall() 
    return records    
    
##################################################################
# 使用者端    
    
   
#使用者查詢貨品庫存資料清單
def user_query_in_stock_product_list():
    sql="select product_id, name, price, quantity, updated_at, created_at from in_stock_products where quantity > 0 order by product_id ;"
    cur.execute(sql)
    records = cur.fetchall()
    return records    

#使用者查詢購物車資料清單
def user_get_cart_products_list( user_id ):
    sql="select product_id, name, price, quantity, updated_at, created_at from cart_products where user_id = %s order by product_id"
    cur.execute(sql, (user_id,))
    records = cur.fetchall()
    return records
    
#使用者查詢購物車中某項貨品資料
def user_get_cart_product( user_id, product_id ):
    sql="select product_id, name, price, quantity, updated_at, created_at from cart_products where user_id = %s and product_id = %s "
    cur.execute(sql, (user_id, product_id))
    record = cur.fetchone()
    return record
         
# 使用者新增一筆貨品至購物車, 相同貨品編號無法新增
def user_add_product_to_cart( user_id, product_id, name, price, quantity ):
    sql="select count(*) from cart_products where user_id = %s and product_id =%s ;"
    cur.execute(sql,(user_id, product_id))
    record = cur.fetchone() 
    if record[0] == 0:
        sql="insert into cart_products( user_id, product_id, name, price, quantity ) values (%s,%s,%s,%s,%s );"
        cur.execute(sql,(user_id, product_id, name, price, quantity))
        conn.commit()
        return True
    else:
        return False    

# 刪除購物車一項貨品
def user_delete_product_from_cart( user_id, product_id ):
    sql="delete from cart_products where user_id = %s and product_id = %s ;"
    cur.execute(sql,(user_id, product_id))
    conn.commit()
    return False

# 購物車內貨品轉訂單, 轉完必須將此人的購物車清空
def user_transfer_cart_to_order( user_id, total_price ):
    # 新增訂單資料 orders
    sql="insert into orders( user_id, total_price ) values (%s,%s )"
    cur.execute(sql,(user_id, total_price))
    conn.commit()     
    order_id = cur.lastrowid
    # 複製購物車貨品資料到訂單貨品細項資料
    sql2 = "INSERT INTO order_products ( order_id, product_id, name, price, quantity ) " + \
           "SELECT '" + str( order_id ) + "', product_id, name, price, quantity FROM cart_products where user_id = %s "
    cur.execute(sql2,(user_id,))
    conn.commit()    
    # 清空購物車
    sql3 ="delete FROM cart_products where user_id = %s "
    cur.execute(sql3,(user_id,))
    conn.commit()
    return order_id
    
#使用者查詢訂單明細
def user_query_order_detail_list( order_id ):
    sql="select order_id, product_id, name, price, quantity, updated_at, created_at from order_products where order_id = %s ;"
    cur.execute(sql, (order_id,))
    records = cur.fetchall()
    return records       
    
def user_calc_cart_checkout_amount( user_id ):
    sql="select sum( price * quantity ) as amount from cart_products where user_id = %s "
    cur.execute(sql,(user_id,))
    record = cur.fetchone()
    return record    

    




