import os
from PIL import Image
os.chdir("image") #상대경로 설정

class calling():
    def callimg():
        while True:
            name = entry.get() #입력받은 문자를 name으로 받음
            image = Image.open(f'{name}.jpg') #name 문자를 받아서 이미 출력
            image.show() #이미지 창을 띄움
            break
