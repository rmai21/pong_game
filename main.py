from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

# Screen Display
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600, startx=0, starty=0)
screen.title("My Pong Game")
screen.tracer(0)

# Add in paddle one to the screen
paddle_right = Paddle((350, 0))
paddle_left = Paddle((-350, 0))

# Paddle Movements
screen.listen()
screen.onkey(paddle_right.move_up, "Up")
screen.onkey(paddle_right.move_down, "Down")
screen.onkey(paddle_left.move_up, "w")
screen.onkey(paddle_left.move_down, "s")

# Adding in the ball
ball = Ball()

# Adding scoreboard
scoreboard = Score()

# Game play
game_is_on = True
while game_is_on:
    # Display Beginning
    time.sleep(ball.speed)
    screen.update()
    ball.move()

    # Bouncing it off the walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with right and left paddle
    if ball.distance(paddle_right) < 50 and ball.xcor() > 320 or ball.distance(paddle_left) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Score update when paddle misses the ball
    if ball.xcor() > 380:  # R paddle
        ball.reset_pos()
        scoreboard.left_point()

    if ball.xcor() < -380:  # L paddle
        ball.reset_pos()
        scoreboard.right_point()

    # Game end
    if scoreboard.l_score == 6:
        print("Left Paddle Wins!")
        game_is_on = False
        scoreboard.game_over()
    elif scoreboard.r_score == 6:
        print("Right Paddle Wins")
        game_is_on = False
        scoreboard.game_over()
    elif scoreboard.l_score == 6 and scoreboard.l_score == 6:
        print("It's a draw")
        game_is_on = False
        scoreboard.game_over()

# Exit Display Screen
screen.exitonclick()
