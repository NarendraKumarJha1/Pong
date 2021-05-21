from turtle import Turtle


class Paddle(Turtle):
    def __init__(self,Position):
        self.flag = 0
        super().__init__()
        self.shape("square")
        if self.flag == 0:
            self.color("green")
            self.flag += 1
        elif self.flag == 1:
            self.color("blue")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(Position)

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)







# paddle.shapesize(stretch_wid=5, stretch_len=1)
# paddle.penup()
# paddle.goto(380, 0)