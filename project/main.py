import os
from tkinter import *
from PIL import Image
import file, openimg
import face
#경로확인이 필요할 시
#path = os.getcwd() 
#print(path)
os.chdir("../") ##경로를 한단계 이전으로
def callimg():
    while True:
        name = entry.get() #입력받은 문자를 name으로 받음
        image = Image.open(f'{name}.jpg') #name 문자를 받아서 이미 출력
        image.show() #이미지 창을 띄움
        break

root = Tk()
root.title ("편한 면접")
    
file_frame = Frame(root)
file_frame.pack(fill="x", padx=5,pady=5)

a = Button(file_frame, padx=5,pady=5,width=12,text="증명사진 추가",command=file.open_file1)
a.pack(side="left")

b = Button(file_frame, padx=5,pady=5,width=12,text="이력서 추가",command=file.open_file2)
b.pack(side="right")

c = Button(file_frame, padx=5,pady=5,width=12,text="명단",command=file.demo)
c.pack()

d = Button(file_frame, padx=5,pady=5,width=12, text="캠", command=face.face)
d.pack()

entry = Entry(root)
entry.insert(0,"이름을 입력하세요")
entry.pack()

button = Button(root, text="확인", command=callimg)
button.pack()

root.mainloop()
