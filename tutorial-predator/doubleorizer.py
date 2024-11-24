from manim import *

class DoubledIntegularExplanation(ThreeDScene):
    def construct(self):
        axes = ThreeDAxes()
        self.add(axes)
        self.set_camera_orientation(theta=45*DEGREES,phi=45*DEGREES,gamma=0*DEGREES)