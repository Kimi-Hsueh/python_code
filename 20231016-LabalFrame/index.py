import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Window(tk.Tk):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("images")
        self.geometry('300x200')
        self.configure(background='#CA7853')



class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.aligement = tk.StringVar(value='left')
        ttk.Radiobutton(self,text="左邊",value='left',variable=self.aligement,command=self.choised).grid(column=0,row=0,padx=10)
        ttk.Radiobutton(self,text="中間",value='center',variable=self.aligement,command=self.choised).grid(column=1,row=0,padx=10)
        ttk.Radiobutton(self,text="右邊",value='right',variable=self.aligement,command=self.choised).grid(column=2,row=0,padx=10)
        self.pack(expand=1,fill='x',padx=10,pady=10)

    def choised(self):
        print(self.aligement.get())

def main():    
    window = Window()
    myFrame = MyFrame(window,'文字對齊方式')
    window.mainloop()

if __name__ == "__main__":
    main()
