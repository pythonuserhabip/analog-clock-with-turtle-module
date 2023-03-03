import turtle
from turtle import Screen
import time

screen = Screen()
screen.setup(450, 450)
screen.bgcolor("red")
screen.title("Analog Saat Uygulaması")
screen.tracer(0)

kalem = turtle.Turtle()
kalem.speed("fastest")
kalem.pensize(30)
def cizim(saat, dakika, saniye, kalem):

    kalem.begin_fill()
    kalem.color("black")
    kalem.up()
    kalem.goto(0, 210)
    kalem.setheading(180)
    kalem.color("black")
    kalem.pendown()
    kalem.circle(210)
    kalem.end_fill()

    kalem.penup()
    kalem.goto(0, 0)
    kalem.setheading(90)
    kalem.begin_fill()
    kalem.color("white")
    for i in range(12):
        kalem.fd(190)
        kalem.pendown()
        kalem.pensize(5)
        kalem.fd(20)
        kalem.penup()
        kalem.goto(0, 0)
        kalem.rt(30)
        kalem.end_fill()
    # saat
    kalem.penup()
    kalem.goto(0, 0)
    kalem.color("blue")
    kalem.setheading(90)
    bilgi = (saat/12) * 360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.forward(80)
    # dakika
    kalem.penup()
    kalem.goto(0, 0)
    kalem.color("gold")
    kalem.setheading(90)
    bilgi = (dakika / 60) * 360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.forward(100)
    # saniye
    kalem.penup()
    kalem.goto(0, 0)
    kalem.color("pink")
    kalem.setheading(90)
    bilgi = (saniye / 60) * 360
    kalem.rt(bilgi)
    kalem.pendown()
    kalem.forward(120)

while True:

    saat =int(time.strftime("%I"))
    dakika = int(time.strftime("%M"))
    saniye = int(time.strftime("%S"))

    cizim(saat, dakika, saniye, kalem)
    screen.update()














