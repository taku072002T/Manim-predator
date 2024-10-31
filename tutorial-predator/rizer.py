from manim import *

class CreateSquare(Scene):
    def construct(self):
        BackgroundColor = Rectangle(width=15.0, height=9.0, color=WHITE).set_fill(WHITE,1)
        self.add(BackgroundColor)
        square= Square()
        square.set_fill(PINK, opacity=0.5)
        circle = Circle()
        circle.set_fill(BLUE, opacity=0.5)
        self.play(Create(square))
        self.wait(1.0)
        self.play(Transform(square,circle))
        self.wait(1.0)
        square1= Square()
        square1.set_fill(PINK, opacity=0.5)
        self.play(Transform(square,square1))
        self.wait(1.0)
