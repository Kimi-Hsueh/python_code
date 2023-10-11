import dataSource #匯入已建立download method的py檔案

def main():
    f= dataSource.city_info()
    f1= dataSource.city_info() #進行第二次的method呼叫
    for i in f:
        print(i)

if __name__ == '__main__':
    main()