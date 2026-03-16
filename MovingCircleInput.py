import turtle

# Create screen
screen = turtle.Screen()
screen.title("Animated Circle with Keyboard")
screen.bgcolor("white")

# Create circle
circle = turtle.Turtle()
circle.shape("circle")
circle.color("red")
circle.penup()
circle.speed(0)

# Movement functions
def move_up():
    y = circle.ycor()
    circle.sety(y + 20)

def move_down():
    y = circle.ycor()
    circle.sety(y - 20)

def move_left():
    x = circle.xcor()
    circle.setx(x - 20)

def move_right():
    x = circle.xcor()
    circle.setx(x + 20)

# Keyboard bindings
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

# Keep window open
turtle.done()