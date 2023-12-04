import requests

url = 'https://tcgbusfs.blob.core.windows.net/dotapp/youbike/v2/youbike_immediate.json'

try:
    response=requests.request('GET',url)
    response.raise_for_status()
except:
    print('網路下載失敗')
else:
    if response.status_code == 200:
        print('下載成功')
