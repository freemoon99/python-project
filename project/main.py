import os
from tkinter import *
from PIL import Image
import file, face

os.chdir("C:\\Users\\pkh\\Desktop\\객체지향 파이썬 코딩\\project")
# 경로확인이 필요할 시
path = os.getcwd()
print(path)
#os.chdir("../")  # 경로를 한단계 이전으로
def calling():
        while True:
            name = entry.get() #입력받은 문자를 name으로 받음
            image = Image.open(f'{name}.jpg') #name 문자를 받아서 이미 출력
            image.show() #이미지 창을 띄움
            break

root = Tk()
root.title("편한 면접")

file_frame = Frame(root)
file_frame.grid(row=0, column=0)

a = Button(file_frame, padx=5, pady=5, width=12, text="증명사진 추가", command=file.open_file1)
a.grid(row=0, column=0)

b = Button(file_frame, padx=5, pady=5, width=12, text="이력서 추가", command=file.open_file2)
b.grid(row=0, column=3)

c = Button(file_frame, padx=5, pady=5, width=12, text="명단", command=file.demo)
c.grid(row=1, column=0)

d = Button(file_frame, padx=5, pady=5, width=12, text="캠", command=face.face)
d.grid(row=1, column=3)

entry = Entry(root)
entry.insert(0, "이름을 입력하세요")
entry.grid(row=3, column=0)

button = Button(root, text="확인", command=calling)
button.grid(row=3, column=1)

root.mainloop()
