#載入模組
import turtle
import time
import datetime

#創建turtle
tur = turtle.Turtle()
tur.seth(90)
tur.speed(10)

#step1 時鐘刻度
def writenum(num):
    tur.penup()
    tur.forward(200)
    tur.write(num)
    tur.back(200)

for i in range(1,13):
    tur.right(30)
    writenum(i)
    
#step2 時針、分針、秒針
update = True #時針，分針
updateSecond = True #秒針

while True:
    now = datetime.datetime.now()
    h = now.hour % 12
    m = now.minute
    s = now.second
    
    if update:
        #時針
        hour = turtle.Turtle() 
        hour.seth(90)
        hour.right(h * 30 + m / 60 * 30)
        hour.forward(100)
        
        #分針
        minute = turtle.Turtle()
        minute.seth(90)
        minute.right(m * 6)
        minute.forward(140)
        
        update = False
        
    if updateSecond: 
        #秒針
        second = turtle.Turtle()
        second.seth(90)
        second.right(s*6)
        second.forward(175)
        updateSecond = False
        
#step3 讓秒針一直轉，指針會依據現在時間移動到正確位置
        
        time.sleep(1)
        
        new = datetime.datetime.now()
        mNew = new.minute
        updateSecond = True
        second.clear() #清除
        second.reset() #重畫       
        
        if mNew != m:
            update = True
            hour.clear()
            hour.reset()
            
            minute.clear()
            minute.reset()
        
turtle.done()
turtle.exitonclick()       
        