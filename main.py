from turtle import Screen
from ball import Ball
from scoreboard import ScoreBoard
import time
from paddle import Paddle
from screen import GameScreen
screen = Screen()
screen.bgcolor("black")
screen.tracer(0)
screen.setup(width=800, height=600)
screen.title("My Pong Game")

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
player = GameScreen()
score = ScoreBoard()
ball = Ball()
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")
game_is_on = True

while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect when right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()
    # Detect when left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()

screen.exitonclick()
