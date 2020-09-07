import turtle
import winsound

wn = turtle.Screen()
wn.title("2 Players Pong Game by Jeet @JxxT")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)


score_a = 0
score_b = 0


paddle_a = turtle.Turtle()
paddle_a.speed(10)
paddle_a.shape("square")
paddle_a.color("orange")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)


paddle_b = turtle.Turtle()
paddle_b.speed(10)
paddle_b.shape("square")
paddle_b.color("orange")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("cyan")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.65
ball.dy = 0.65


pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("light green")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("PLAYER-1:   0                   PLAYER-2:   0", align="center", font=("Comic Sans MS", 24, "normal"))


def paddle_a_up():
    y = paddle_a.ycor()
    y += 30
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 30
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 30
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 30
    paddle_b.sety(y)


wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


while True:
    wn.update()
    
    
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    

    
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)

    
    if ball.xcor() > 350:
        score_a += 1
        pen.clear()
        pen.write("PLAYER-1:   {}                   PLAYER-2:   {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        score_b += 1
        pen.clear()
        pen.write("PLAYER-1:   {}                   PLAYER-2:   {}".format(score_a, score_b), align="center", font=("Comic Sans MS", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    
    if ball.xcor() < -340 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50:
        ball.dx *= -1 
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
    
    elif ball.xcor() > 340 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50:
        ball.dx *= -1
        winsound.PlaySound("bounce.wav", winsound.SND_ASYNC)
