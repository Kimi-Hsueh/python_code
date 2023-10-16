import dataSource #匯入已建立download method的py檔案
import tkinter as Tk #匯入視窗化tkinter模組
from tkinter import ttk

class Winodwset(Tk.Tk):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title('111年度人口統計') #使用tk模組命名視窗名稱
        self.configure(background='red') #設定視窗內的背景色
        #這邊請注意，誰先被pack，就會先被執行，在視窗的顯示下就是從上到下的排列
        topFrame=Tk.Frame(self,background='#86C166') #設定視窗上部欄位底色
        label=Tk.Label(topFrame,text="111年度人口統計",font=('Helvetica', '30')) #設定視窗內文字內容及文字格式
        label.pack(padx=20,pady=20) #設定文字的間隔，x是寬度，y是高度
        topFrame.pack()

        bottomFrame=Tk.Frame(self,background='#8B81C3') #設定視窗下部欄位
        choies = dataSource.cityNames() #去dataSource呼叫cityNames()method
        choiesvar=Tk.StringVar(value=choies) #設定選單變數“choiesvar”
        self.listbox=Tk.Listbox(bottomFrame,listvariable=choiesvar,width=12) #設定下拉選單變數“listbox”在視窗的下部欄位，選單內容以“choiesvar”為內容，選單寬度為12px
        self.listbox.pack(pady=20) #設定與視窗上、下欄位的間隔
        bottomFrame.pack(expand=True,fill='x')
        
        resultFrame=Tk.Frame(self)
        Tk.Label(resultFrame,text='年度').grid(column=0,row=0,sticky='W',pady=5)
        Tk.Label(resultFrame,text='地區').grid(column=0,row=1,sticky='W',pady=5)
        Tk.Label(resultFrame,text='人口數').grid(column=0,row=2,sticky='W',pady=5)
        Tk.Label(resultFrame,text='土地面積').grid(column=0,row=3,sticky='W',pady=5)
        Tk.Label(resultFrame,text='人口密度').grid(column=0,row=4,sticky='W',pady=5)
        self.yearVar=Tk.StringVar()
        Tk.Label(resultFrame,textvariable=self.yearVar).grid(column=1,row=0,sticky='E',pady=5)
        self.cityVar=Tk.StringVar()
        Tk.Label(resultFrame,textvariable=self.cityVar).grid(column=1,row=1,sticky='E',pady=5)
        self.poplation=Tk.StringVar()
        Tk.Label(resultFrame,textvariable=self.poplation).grid(column=1,row=2,sticky='E',pady=5)
        self.areaVar=Tk.StringVar()
        Tk.Label(resultFrame,textvariable=self.areaVar).grid(column=1,row=3,sticky='E',pady=5)
        self.densityVar=Tk.StringVar()
        Tk.Label(resultFrame,textvariable=self.densityVar).grid(column=1,row=4,sticky='E',pady=5)
        resultFrame.pack()

        self.listbox.bind('<<ListboxSelect>>',self.user_selected) #設定listbox綁定“user_selected”method
    
    def user_selected(self,event): #定義“user_selected”method
        selectedIndex=self.listbox.curselection()[0] 
        cityName=self.listbox.get(selectedIndex)
        datalist=(dataSource.info(cityName))
        self.yearVar.set(datalist[0])
        self.cityVar.set(datalist[1])
        self.poplation.set(datalist[2])
        self.areaVar.set(datalist[3])
        self.densityVar.set(datalist[4])
        


        

def main():
    window = Winodwset() #inital 視窗化tkinter模組
    window.mainloop() #讓視窗一直保持運行，一直到按下“x”按鈕關閉它
    
if __name__ == '__main__':
    main()