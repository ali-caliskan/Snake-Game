import turtle
import time
import random


oyun_ekrani = turtle.Screen()
oyun_ekrani.title("Snake Game")
oyun_ekrani.setup(width=1400, height=800)
oyun_ekrani.bgcolor('orange')
oyun_ekrani.tracer(0) 

yilan_kafasi = turtle.Turtle()
yilan_kafasi.speed(0)
yilan_kafasi.color('black')
yilan_kafasi.shape('circle')
yilan_kafasi.penup()
yilan_kafasi.goto(0,0)
yilan_kafasi.direction = 'stop'

yilan_hizi = 0.1

yem = turtle.Turtle()
yem.speed(0)
yem.color('red')
yem.shape('circle')
yem.penup()
yem.goto(0,100)
yem.shapesize(0.80,0.80)


kuyruk = []
puan = 0
puan_tahtasi = turtle.Turtle()
puan_tahtasi.speed(0)
puan_tahtasi.color('white')
puan_tahtasi.shape('square')
puan_tahtasi.penup()
puan_tahtasi.goto(0,350)
puan_tahtasi.hideturtle()
puan_tahtasi.write('Score : {}'.format(puan),align='center',font=('Courier',30,'normal'))

def hareket():
    if yilan_kafasi.direction == 'up':
        y = yilan_kafasi.ycor()
        yilan_kafasi.sety(y + 10)
    if yilan_kafasi.direction == 'down':
        y = yilan_kafasi.ycor()
        yilan_kafasi.sety(y - 10)
    if yilan_kafasi.direction == 'right':
        x = yilan_kafasi.xcor()
        yilan_kafasi.setx(x + 10) 
    if yilan_kafasi.direction == 'left':
        x = yilan_kafasi.xcor()
        yilan_kafasi.setx(x - 10)          

def yukari_gidis():
    if yilan_kafasi.direction != 'down':
        yilan_kafasi.direction = 'up'

def asagi_gidis():
    if yilan_kafasi.direction != 'up':
        yilan_kafasi.direction = 'down'

def saga_gidis():
    if yilan_kafasi.direction != 'left':
        yilan_kafasi.direction = 'right'

def sola_gidis():
    if yilan_kafasi.direction != 'right':
        yilan_kafasi.direction = 'left'


oyun_ekrani.listen()
oyun_ekrani.onkey(yukari_gidis, 'Up')
oyun_ekrani.onkey(asagi_gidis, 'Down')
oyun_ekrani.onkey(sola_gidis, 'Left')
oyun_ekrani.onkey(saga_gidis, 'Right')



while True:
    oyun_ekrani.update()


    if yilan_kafasi.xcor() > 700 or  yilan_kafasi.xcor() < -700 or yilan_kafasi.ycor() > 400 or  yilan_kafasi.ycor() < -400:
    
        time.sleep(1)
        yilan_kafasi.goto(0,0)
        yilan_kafasi.direction = 'stop'

        for i in kuyruk:
            i.goto(5000,5000)
        
        kuyruk = []
        puan = 0
        puan_tahtasi.clear()
        puan_tahtasi.write('Score : {}'.format(puan),align='center',font=('Courier',30,'normal'))
        yilan_hizi = 0.1


    if yilan_kafasi.distance(yem) < 20:
        x = random.randint(-300,300)
        y = random.randint(-300,300)
        yem.goto(x,y)

        puan += 10
        puan_tahtasi.clear()
        puan_tahtasi.write('Score : {}'.format(puan),align='center',font=('Courier',30,'normal'))

        #Yedikçe Artan Hızı:
        yilan_hizi = yilan_hizi - 0.001
  
        ek_kuyruk = turtle.Turtle()
        ek_kuyruk.speed(0)
        ek_kuyruk.shape('circle')
        ek_kuyruk.color('black')
        ek_kuyruk.penup()
        kuyruk.append(ek_kuyruk)


    for i in range(len(kuyruk) - 1, 0, -1):
        x = kuyruk[i-1].xcor()
        y = kuyruk[i-1].ycor()

        kuyruk[i].goto(x,y)
    if len(kuyruk) > 0:
        x = yilan_kafasi.xcor()
        y = yilan_kafasi.ycor()
        kuyruk[0].goto(x,y)

    hareket()
    time.sleep(yilan_hizi)