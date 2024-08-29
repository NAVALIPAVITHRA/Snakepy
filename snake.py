from turtle import Turtle


STARTING_POSITIONS  = [(0,0),(-20,0),(-40,0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
class Snake(Turtle):
    def __init__(self):
        self.segment = []#empty list to make the snake in one list instead of blocks
        self.create_snake()
        self.head = self.segment[0]

    # creating the snake body
    def create_snake(self):
        for value in STARTING_POSITIONS: #the positions 0,-20,-40
           self.add_segment(value)#the parameter is passed
    def add_segment(self,value):#the parameter taken as argument
        new_phase = Turtle("square")  # creating the square by turtle module
        new_phase.color("white")  # color
        new_phase.penup()  # the while line disappears
        new_phase.goto(value)  # the white block places to the value specified
        self.segment.append(new_phase)  # appending to a list forms a snake instead a 3 blocks

    def extend(self):

       self.add_segment(self.segment[-1].position())#the position of last block is taken as value argumemnt and new block added to the list.


# move the snake#creates illusion as snake moving by replacing blocks to its previous block place.

    def move(self):
        for seg_num in range(len(self.segment) - 1, 0, -1):  # seg=3 0,1,2 len=2(start) ,stop=0,decrement=-1
            new_x = self.segment[seg_num - 1].xcor()  # segment[1].xcor() =whiteblock with position[1] is -20 update to new_x.
            new_y = self.segment[seg_num - 1].ycor()  # y is 0
            self.segment[seg_num].goto(new_x, new_y)  # segemnt[2] last block goes to previous block place.
        self.head.forward(MOVE_DIST)  # first block moves forward with 20 units.


#control of snake
    def up(self):
        if self.head.heading()!= DOWN:
          self.head.setheading(UP)
    def down(self):
        if self.head.heading() != UP:
         self.head.setheading(DOWN)
    def left(self):
        if self.head.heading() != RIGHT:
         self.head.setheading(LEFT)
    def right(self):
        if self.head.heading() != LEFT:
         self.head.setheading(RIGHT)