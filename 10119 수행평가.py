import turtle as t
import random as ra
import turtle
t.bgcolor("black")
t.set(1000,800)
def sp():
    t.color("white")
    x=t.textinput("x좌표를 입력하세요.")
    y=t.textinput("y좌표를 입력하세요.")
    크기=t.textinput("도형의 크기를 말해주세요")
    t.goto(x,y)
    temp=t.textinput("그리고 싶은 도형은 무엇이가요?","(원,사각형)")
    
    if temp=="원":
        t.circle(크기)
        
        
    elif temp =="사각형":
        t.begin_fill()
        for x in range(4):
            t.forward(크기)
            t.left(90)
            
sp()

