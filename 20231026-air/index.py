import tkinter as tk
from tkinter import ttk
import updata
from tkinter import messagebox
from threading import Timer


t=None
def main():
    def update_data():
        print('update data')
        global t
        t=timer(10,update_data.insert_data)
        t.start()


if __name__ =="__main__":
    main()