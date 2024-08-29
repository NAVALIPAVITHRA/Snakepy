from turtle import Screen
from snake import Snake
from food import food
from score import Score
import time
screen = Screen()  # setting up the screen
screen.setup(width = 600, height = 600) # defining the screen
screen.bgcolor("black")# setting up the bg
screen.title("snake game")# title specifier
screen.tracer(0)#the tracer turns off then the screen gonna be black no loops get activated no animation exceuted.

#objects
snake = Snake()
food = food()
score = Score()
screen.listen()3
26.

#event listeners
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:#while loop iterates till the value is true
    screen.update()#the update method refreshes the prgm against the tracer.
    time.sleep(0.1)
    snake.move()
 #detect the collosion of food and snake
    if snake.head.distance(food) < 15:
       food.refresh()
       snake.extend()
       score.increase_score()
#detect collosion with wall
    if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290 :
     score.game_over()
     game_is_on = False

#detect collision with tail
    for segment in snake.segment:
        if segment == snake.head:
            pass
        elif snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()
screen.exitonclick()# exites when clicked on screen
