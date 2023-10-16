import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk


class Window(tk.Tk):

    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.title("images")
        #self.geometry('300x200')
        #self.configure(background='#CA7853')



class MyFrame(tk.LabelFrame):
    def __init__(self,master,title,**kwargs):
        super().__init__(master,text=title,**kwargs)
        self.pack(expand=1,fill='both',padx=10,pady=10)

        self.tree=ttk.Treeview(self,columns=['#1','#2','#3'],show='headings')
        self.tree.heading('#1',text='第一欄')
        self.tree.heading('#2',text='第二欄')
        self.tree.heading('#3',text='第三欄')
        self.tree.pack()

        contacts = []
        for i in range(1,100):
            contacts.append([f'first{i}',f'last{i}',f'email{i}@example.com'])
        
        for contact in contacts:
            self.tree.insert('',tk.END,values=contact)

    def choised(self):
        print(self.aligement.get())

def main():    
    window = Window()
    myFrame = MyFrame(window,'文字對齊方式')
    window.mainloop()

if __name__ == "__main__":
    main()
