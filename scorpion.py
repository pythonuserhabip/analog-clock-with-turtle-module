from turtle import Turtle

scorpion = [12, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

class Scorpion(Turtle):

     def __init__(self):
         super().__init__()
         self.hour = 0
         self.color("white")
         self.penup()

