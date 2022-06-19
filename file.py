from tkinter import *
from tkinter import filedialog
import tkinter as tk
from tksheet import Sheet
import pandas as pd
import os

os.chdir("C:\\Users\\pkh\\Desktop\\객체지향 파이썬 코딩\\project")
class demo(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)
        self.frame = tk.Frame(self)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.sheet = Sheet(
            self.frame,
            data=pd.read_csv(
                "person.csv", names=['Name', 'Time']).values.tolist(),
        )
        self.sheet.enable_bindings()
        self.frame.grid(row=0, column=0, sticky="nswe")
        self.sheet.grid(row=0, column=0, sticky="nswe")
# 파일 열기


def open_file1():
    files = filedialog.askopenfilenames(title="이력서 파일을 넣으세요",filetypes=(("jpg 파일", "*.jpg"), ("PNG 파일", "*.png"), ("모든 파일", "*.*")),
                                        initialdir=r"C:\Users\pkh\Desktop\객체지향 파이썬 코딩\project\image")  # 시작할때 파일 경로
    for file in files:
        list_file.insert(END, file)


def open_file2():
    files = filedialog.askopenfilenames(title=" 얼굴사진을 넣으세요",filetypes=(("jpg 파일", "*.jpg"), ("PNG 파일", "*.png"), ("모든 파일", "*.*")),
                                        initialdir=r"C:\Users\pkh\Desktop\객체지향 파이썬 코딩\project\resume")  # 시작할때 파일 경로
    for file in files:
        list_file.insert(END, file)
