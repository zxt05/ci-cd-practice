import requests
import pytest
import sqlite3
def test_get_product_normal():
    url="https://jsonplaceholder.typicode.com/posts/1"
    response=requests.get(url)
    assert response.status_code==200
    assert response.json()["id"]==1
def test_get_product_404():
    url="https://jsonplaceholder.typicode.com/posts/9999"
    response=requests.get(url)
    assert response.status_code==404
def test_datebase_consistency():
    url="https://jsonplaceholder.typicode.com/posts/1"
    response=requests.get(url)
    api_id=requests.json()["id"]
    conn=sqlite3.connect(":memory")
    cursor=conn.cursor()
    cursor.execute("CREATE TABLE product(id INTEGER,name TEXT)")
    cursor.execute("SELECT id FROM product WHERE name ='二手手机'")
    db_id=cursor.fetchone()[0]
    conn.close()
    assert api_id==db_id

    