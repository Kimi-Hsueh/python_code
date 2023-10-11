import requests
import io
import csv

__city = [] #設定一個序列變數“__city”

def __download()->list[list]: #定義list二維序列，並且不公開

    #到網站上拉資料下來
    url = 'https://data.moi.gov.tw/MoiOD/System/DownloadFile.aspx?DATA=CA18EE06-4A50-4861-9D97-7853353D7108' #定義連結變數
    response=requests.request('GET',url) #使用requests.request()method下載資料

    try:
        response.raise_for_status() #檢查是否連線錯誤
    except:
        raise Exception('發生連線錯誤','網路中斷')
    else:
        if not response.ok: #檢查下載是否成功
            raise Exception('下載失敗','伺服器錯誤')
        #將資料拉下來後的處理動作
        else:
            file=io.StringIO(response.text) #使用io.StringIO()method將資料存在☆記憶體☆
            csv_reader=csv.reader(file) #將檔案轉為二維序列
            next(csv_reader)
            return list(csv_reader)
        
def city_info() ->list[list]:
    if len(__city) ==0: #當序列變數__city長度相等於0時
        try:
            data_list = __download() #建立data_list變數，內容為匯入download()“method”
        except Exception as e: #如果傳出Exception錯誤
            print(f'錯誤:{e}') #要證明網路連線的中斷，就直接改成一個不存在的網址即可驗證
        else:
            for row in data_list:
                if row[0] == '111':
                    __city.append(row)
    return __city #此處不管if的條件，都會顯示結果

def cityName() ->list[str]:
    cities=city_info()
    names= []
    for row in cities:
        cityName=row[1]
        names.append[cityName]
        return names

