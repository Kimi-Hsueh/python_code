import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from threading import Timer
import datasource

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #-----更新資料庫-----#
        try:
            datasource.update_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()
        
        #-----建立界面-----#
        topFrame=tk.Frame(self,relief=tk.RAISED,borderwidth=1,width=300,height=200) #設定按鈕樣式
        tk.Label(topFrame,text='台北市youbike及時資料',font=('arial,20'),bg='#86C166',fg='black',padx=20,pady=20).pack(padx=10,pady=10)
        topFrame.pack(pady=30)

        bottomFrame=tk.Frame(self)
        #-----建立treeview表格-----#        
        self.treeview=ttk.Treeview(bottomFrame,columns=('sna','mday','sarea','ar','tot','sbi','bemp')) #定義資料欄位
        self.treeview.heading('sna',text='站點名稱')
        self.treeview.heading('mday',text='更新時間')
        self.treeview.heading('sarea',text='行政區')
        self.treeview.heading('ar',text='地址')
        self.treeview.heading('tot',text='總車輛數')
        self.treeview.heading('sbi',text='可借數量')
        self.treeview.heading('bemp',text='可還車')
        self.treeview.pack()
        bottomFrame.pack(pady=30)

   
def main():    
    def update_data(w:Window)->None:
        datasource.update_sqlite_data()
        window.after(60*1000,update_data,w)
          
    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)          
    window.mainloop()

if __name__ == '__main__':
    main()