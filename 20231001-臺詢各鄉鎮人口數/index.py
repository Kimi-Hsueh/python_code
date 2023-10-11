import dataSource #匯入已建立download method的py檔案

def main():
    name=dataSource.cityName()
    print(name)

if __name__ == '__main__':
    main()