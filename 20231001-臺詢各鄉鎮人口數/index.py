import dataSource #匯入已建立download method的py檔案

def main():
    name=dataSource.cityNames()
    city = dataSource.info(name='台北市中和區')

    print(city)

if __name__ == '__main__':
    main()