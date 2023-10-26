import requests
import sqlite3

def __download_youbike_data() ->list[dict]:
    '''
    下載youbike資料
    2.0資料來源：https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    url ='https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response=requests.get(url)
    response.raise_for_status()
    print('下載成功')
    return response.json()

def __create_table(conn:sqlite3.Connection):
	conn=sqlite3.connect('Youbike.db') #建立一個名叫“Youbike.db”的資料庫(如果存在，則連線此資料庫)
	cursor=conn.cursor()
	cursor.execute(
    '''
    CREATE TABLE IF NOT EXISTS 台北市youbike(
        "id"	INTEGER,
	    "站點名稱"	TEXT NOT NULL,
	    "行政區"	TEXT NOT NULL,
	    "更新時間"	TEXT NOT NULL,
	    "地址"	TEXT,
	    "總車輛數"	INTEGER,
	    "可借數量"	INTEGER,
	    "可還車"	INTEGER,
	    PRIMARY KEY("id" AUTOINCREMENT)
    );
    '''
)
	conn.commit()



def update_sqlite_data(): #將json檔匯入到資料庫
    '''
    下載/更新資料庫
    '''
    data= __download_youbike_data() #呼叫method
    conn = sqlite3.connect("youbike.db")
    print(type(conn))
    __create_table(conn)


