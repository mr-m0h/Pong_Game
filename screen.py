from turtle import Turtle


class GameScreen:

    def __init__(self):
        self.part = []
        self.creating_screen()

    def creating_screen(self):
        for _ in range(16):
            new_part = Turtle()
            new_part.shape("square")
            new_part.penup()
            new_part.color("white")
            new_part.shapesize(stretch_wid=1.5, stretch_len=0.2)
            new_part.speed("fastest")
            self.part.append(new_part)
            self.partition()

    def partition(self):
        y_cor = -390
        for every in self.part:
            x_cor = 0
            every.goto(x_cor, y_cor)
            y_cor += 55
