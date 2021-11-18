import turtle
import os

width = 800
height = 600


#
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=width, height=height)
wn.tracer(0)

#Score
score1 = 0
score2 = 0

#Paddle 1 a
paddle_1a = turtle.Turtle()
paddle_1a.speed(0)
paddle_1a.shape("square")
paddle_1a.color("white")
paddle_1a.shapesize(stretch_wid=5, stretch_len=1)
paddle_1a.penup()
paddle_1a.goto(-350, 0)

#Paddle 1 b
paddle_1b = turtle.Turtle()
paddle_1b.speed(0)
paddle_1b.shape("square")
paddle_1b.color("white")
paddle_1b.shapesize(stretch_wid=5, stretch_len=1)
paddle_1b.penup()
paddle_1b.goto(-175,150)

#Paddle 1 c
paddle_1c = turtle.Turtle()
paddle_1c.speed(0)
paddle_1c.shape("square")
paddle_1c.color("white")
paddle_1c.shapesize(stretch_wid=5, stretch_len=1)
paddle_1c.penup()
paddle_1c.goto(-175,-150)

#Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)
#Paddle 1 b
paddle_2b = turtle.Turtle()
paddle_2b.speed(0)
paddle_2b.shape("square")
paddle_2b.color("white")
paddle_2b.shapesize(stretch_wid=5, stretch_len=1)
paddle_2b.penup()
paddle_2b.goto(175,150)

#Paddle 2 c
paddle_2c = turtle.Turtle()
paddle_2c.speed(0)
paddle_2c.shape("square")
paddle_2c.color("white")
paddle_2c.shapesize(stretch_wid=5, stretch_len=1)
paddle_2c.penup()
paddle_2c.goto(175,-150)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .5
ball.dy = .5

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player 1: 0 Player 2: 0", align = "center", font = ("Courier", 24, "normal"))

#Functions
def paddle1Up():
    y = paddle_1a.ycor()
    if y < (height/2) - 60:
        y += 20
    paddle_1a.sety(y)

def paddle1Down():
    y = paddle_1a.ycor()
    if y > -(height/2) + 60:
        y -= 20
    paddle_1a.sety(y)

def paddle2Up():
    y = paddle_2.ycor()
    if y < (height/2) - 60:
        y += 20
    paddle_2.sety(y)

def paddle2Down():
    y = paddle_2.ycor()
    if y > -(height/2) + 60:
        y -= 20
    paddle_2.sety(y)

#Keyboard bindings
wn.listen()
wn.onkeypress(paddle1Up, "w")
wn.onkeypress(paddle1Down, "s")
wn.onkeypress(paddle2Up, "i")
wn.onkeypress(paddle2Down, "k")

#Main game loop
while True:
    wn.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #Border checking
    if ball.ycor() > height/2 or ball.ycor() < -(height/2):
        ball.dy *= -1
        os.system('aplay beep-sound-8333.wav&')
    if ball.xcor() > width/2:
        ball.goto(0, 0)
        ball.dx *= -1
        score1 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    if  ball.xcor() < -(width/2):
        ball.goto(0, 0)
        ball.dx *= -1
        score2 += 1
        pen.clear()
        pen.write("Player 1: {} Player 2: {}".format(score1, score2), align="center", font=("Courier", 24, "normal"))

    #Paddle Collision
    if (ball.xcor() == paddle_2.xcor())  and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.dx *= -1
        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_1a.xcor())  and (ball.ycor() < paddle_1a.ycor() + 50 and ball.ycor() > paddle_1a.ycor() - 50):
        ball.dx *= -1
        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_2.xcor() + 10 )  and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.dy *= -1
        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_1a.xcor() - 10)  and (ball.ycor() < paddle_1a.ycor() + 50 and ball.ycor() > paddle_1a.ycor() - 50):
        ball.dy *= -1
        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_1c.xcor())  and (ball.ycor() < paddle_1c.ycor() + 50 and ball.ycor() > paddle_1c.ycor() - 50):
        ball.dx *= -1
        paddle_1b.sety(paddle_1b.ycor() - 20)
        paddle_1c.sety(paddle_1c.ycor() + 20)

        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_1b.xcor())  and (ball.ycor() < paddle_1b.ycor() + 50 and ball.ycor() > paddle_1b.ycor() - 50):
        ball.dx *= -1
        paddle_1b.sety(paddle_1b.ycor() + 20)
        paddle_1c.sety(paddle_1c.ycor() - 20)

        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_1c.xcor() - 10 )  and (ball.ycor() < paddle_1c.ycor() + 50 and ball.ycor() > paddle_1c.ycor() - 50):
        ball.dy *= -1
        paddle_1b.sety(paddle_1b.ycor() - 20)
        paddle_1c.sety(paddle_1c.ycor() + 20)

        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_1b.xcor() - 10)  and (ball.ycor() < paddle_1b.ycor() + 50 and ball.ycor() > paddle_1b.ycor() - 50):
        ball.dy *= -1
        paddle_1b.sety(paddle_1b.ycor() + 20)
        paddle_1c.sety(paddle_1c.ycor() - 20)
        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_2c.xcor()) and (ball.ycor() < paddle_2c.ycor() + 50 and ball.ycor() > paddle_2c.ycor() - 50):
        ball.dx *= -1
        paddle_2b.sety(paddle_2b.ycor() - 20)
        paddle_2c.sety(paddle_2c.ycor() + 20)
        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_2b.xcor()) and (ball.ycor() < paddle_2b.ycor() + 50 and ball.ycor() > paddle_2b.ycor() - 50):
        ball.dx *= -1
        paddle_2b.sety(paddle_2b.ycor() + 20)
        paddle_2c.sety(paddle_2c.ycor() - 20)
        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_2c.xcor() + 10) and (ball.ycor() < paddle_2c.ycor() + 50 and ball.ycor() > paddle_2c.ycor() - 50):
        ball.dy *= -1
        paddle_2b.sety(paddle_2b.ycor() - 20)
        paddle_2c.sety(paddle_2c.ycor() + 20)
        os.system('aplay stone-dropping-6843.wav&')
    if (ball.xcor() == paddle_2b.xcor() + 10) and (ball.ycor() < paddle_2b.ycor() + 50 and ball.ycor() > paddle_2b.ycor() - 50):
        ball.dy *= -1
        paddle_2b.sety(paddle_2b.ycor() + 20)
        paddle_2c.sety(paddle_2c.ycor() - 20)
        os.system('aplay stone-dropping-6843.wav&')

