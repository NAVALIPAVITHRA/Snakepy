from turtle import Turtle
import random
class food(Turtle):#inherts the super class to create the food object using the turtle module
    def __init__(self):
        super().__init__()#dis constructor calls o it is super class init where the super class methods can be used
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len = 0.5,stretch_wid = 0.5)
        self.color("blue")
        self.speed("fastest")

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)





