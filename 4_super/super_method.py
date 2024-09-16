import turtle

class OrangeTurtle(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.color("orange")
        self.width(10)

# if __name__ == "__main__":
c = OrangeTurtle()
for n in range(4):
    c.forward(100)
    c.right(90)
