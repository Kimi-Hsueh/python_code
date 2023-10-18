import json
import csv

with open('./台積電.csv','r',encoding='utf-8') as file:
    reader=csv.DictReader(file)
    for row in reader:
        #print(row)
        with open('test3.json','w',encoding='utf-8') as file2:
            jsonStr = json.dumps(row,ensure_ascii=False)
            #print(type(jsonStr))
            #print(jsonStr)
            file2.write(jsonStr)