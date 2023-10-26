import requests
import sqlite3

__all__ = ['update_sqlite_data'] #公開給其他人看的method

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
        UNIQUE(站點名稱,更新時間) ON CONFLICT REPLACE
    );
    '''
)
	conn.commit()

def __insert_data(conn:sqlite3.Connection,values:list[any]) ->None :
    cursor = conn.cursor()
    sql = '''
    REPLACE INTO 台北市youbike(站點名稱,行政區,更新時間,地址,總車輛數,可借數量,可還車)
        VALUES(?,?,?,?,?,?,?)
    '''
    cursor.execute(sql,values)
    conn.commit()



def update_sqlite_data(): #將json檔匯入到資料庫
    '''
    下載/更新資料庫
    '''
    data= __download_youbike_data() #呼叫method
    conn = sqlite3.connect("youbike.db")
    __create_table(conn)
    for item in data:
        __insert_data(conn,[item['sna'],item['sarea'],item['mday'],item['ar'],item['tot'],item['sbi'],item['bemp']])
    conn.close()


