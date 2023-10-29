import password #匯入並執行password.py檔
import requests #匯入並執行requests
import sqlite3 #匯入sqlite3模組
import json

def get_air_data():
    url=f'https://data.moenv.gov.tw/api/v2/aqx_p_319?api_key={password.apikey}'
    #print(url) #驗證url是否正確
    res=requests.get(url)
    data=res.json()['records']
    return data
    
    


def create_table_air(conn:sqlite3.Connection):
#conn=sqlite3.Connection(database='air.db') #測試建立db
    cursor=conn.cursor()
    cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS AIR(
    "ID"    INTEGER,
    "監測站名"  TEXT NOT NULL,
    "空品分區"  TEXT NOT NULL,
    "縣市行政區"    TEXT NOT NULL,
    "監測站地址"    TEXT NOT NULL,
    "監測站類型"    TEXT NOT NULL,
    "監測站編號"    TEXT NOT NULL,
    PRIMARY KEY("ID" AUTOINCREMENT)
    );
    '''
)
    conn.commit()
    #conn.close() #將測試的db關閉

def insert_data_air(conn:sqlite3.Connection,values:list[any])->None:
    cursor=conn.cursor()
    sql='''
    INSERT INTO AIR(監測日期,監測站編號,監測站名,縣市行政區,監測項目名稱,監測數值,監測單位)
    values(?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,values)
    conn.commit()

def insert_data(conn:sqlite3.Connection,  values:list[any]) ->None :
    data=get_air_data()
    conn=sqlite3.Connection('air.db')
    create_table_air(conn)
    for item in data:
        #print(type(item))
        insert_data_air(conn,[item['monitordate'],item['siteid'],item['sitename'],item['county'],item['itemname'],item['concentration'],item['itemunit']])
    conn.close()




