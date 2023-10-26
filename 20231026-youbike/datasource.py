import requests

def download_youbike_data():
    '''
    下載youbike資料
    2.0資料來源：https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json
    '''
    url ='https://tcgbusf.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'
    response=requests.get(url)
    if response.status_code == 200:
        print('資料下載成功')
    else:
        raise Exception('下載失敗')