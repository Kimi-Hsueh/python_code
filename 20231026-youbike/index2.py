import tkinter as tk
from tkinter import ttk
#從youbikeTreeView.py檔讀取treeview的內容
from youbikeTreeView import YoubikeTreeView
from tkinter import messagebox
from threading import Timer
import datasource1

class Window(tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        #-----更新資料庫-----#
        try:
            datasource1.update_sqlite_data()
        except Exception:
            messagebox.showerror("錯誤",'網路不正常\n將關閉應用程式\n請稍後再試')
            self.destroy()
        
        #-----建立界面-----#
        #設定視窗的第一個區塊
        #設定框架樣式
        topFrame=tk.Frame(self,relief=tk.RAISED,borderwidth=1)
        #設定內文樣式
        tk.Label(topFrame,text='台北市youbike及時資料',font=('arial,20'),bg='#86C166',fg='black',padx=20,pady=20).pack(padx=10,pady=10)
        #將框架及內文設定打包
        topFrame.pack(pady=30)

        #設定視窗的第二個區塊
        bottomFrame=tk.Frame(self)
        #-----建立treeview表格-----#        
        self.youbikeTreeView=YoubikeTreeView(bottomFrame,show='headings',columns=('sna','mday','sarea','ar','tot','sbi','bemp')) #定義資料欄位
        self.youbikeTreeView.pack(side='left')
        vsb = ttk.Scrollbar(bottomFrame, orient="vertical", command=self.youbikeTreeView.yview)
        vsb.pack(side='left')
        self.youbikeTreeView.configure(yscrollcommand=vsb.set)
        bottomFrame.pack(pady=30)

   
def main():    
    def update_data(w:Window)->None:
        datasource1.update_sqlite_data()
        #-----更新treeView資料-----#
        lastest_data = datasource1.lastest_datetime_data()
        w.youbikeTreeView.update_content(lastest_data)
        window.after(60*1000,update_data,w)
          
    window = Window()
    window.title('台北市youbike2.0')
    #window.geometry('600x300')
    window.resizable(width=False,height=False)
    update_data(window)          
    window.mainloop()

if __name__ == '__main__':
    main()