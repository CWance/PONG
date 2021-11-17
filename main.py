import turtle

width = 800
height = 600

#
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("black")
wn.setup(width=width, height=height)
wn.tracer(0)

#Paddle 1
paddle_1 = turtle.Turtle()
paddle_1.speed(0)
paddle_1.shape("square")
paddle_1.color("white")
paddle_1.shapesize(stretch_wid=5, stretch_len=1)
paddle_1.penup()
paddle_1.goto(-350,0)

#Paddle 2
paddle_2 = turtle.Turtle()
paddle_2.speed(0)
paddle_2.shape("square")
paddle_2.color("white")
paddle_2.shapesize(stretch_wid=5, stretch_len=1)
paddle_2.penup()
paddle_2.goto(350,0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = .5
ball.dy = .5

#Functions
def paddle1Up():
    y = paddle_1.ycor()
    if y < (height/2) - 60:
        y += 20
    paddle_1.sety(y)

def paddle1Down():
    y = paddle_1.ycor()
    if y > -(height/2) + 60:
        y -= 20
    paddle_1.sety(y)

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
    if ball.xcor() > width/2 or ball.xcor() < -(width/2):
        ball.goto(0, 0)
        ball.dx *= -1

    #Paddle Collision
    if (ball.xcor() == paddle_2.xcor())  and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.dx *= -1
    if (ball.xcor() == paddle_1.xcor())  and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.dx *= -1
    if (ball.xcor() == paddle_2.xcor() + 10 )  and (ball.ycor() < paddle_2.ycor() + 50 and ball.ycor() > paddle_2.ycor() - 50):
        ball.dy *= -1
    if (ball.xcor() == paddle_1.xcor() - 10)  and (ball.ycor() < paddle_1.ycor() + 50 and ball.ycor() > paddle_1.ycor() - 50):
        ball.dy *= -1