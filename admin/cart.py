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
    record = cur.fetchone() 
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
    
