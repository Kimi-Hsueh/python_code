import datasource #匯入抓取資料的功能
import psycopg2
import password as pw

def main():
    #-----測試連線是否正常-----#
    datasource.updata_render_data()
    datasource.updata_render_data()
    print('資料已完成匯入動作')


if __name__ == "__main__":
    main()