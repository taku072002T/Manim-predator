from manim import *
import numpy as np

class DoubleIntegralVisualization(ThreeDScene):
    def construct(self):
        # Set up the axes
        axes = ThreeDAxes(
            x_range=[-3, 3, 1],
            y_range=[-3, 3, 1],
            z_range=[-1, 1, 0.5],
            x_length=6,
            y_length=6,
            z_length=4
        )
        axes_labels = axes.get_axis_labels()

        # Define the function sin(x)cos(y)
        def func(u, v):
            return np.sin(u) * np.cos(v)

        # Create the surface
        surface = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[-3, 3],
            v_range=[-3, 3],
            resolution=(30, 30),
            should_make_jagged=True,
        )
        surface.set_style(fill_opacity=0.7)
        surface.set_fill_by_value(axes=axes, colors=[(RED, -0.5), (BLUE, 0.5)], axis=2)

        # Create the volume to be integrated (yellow)
        volume = Surface(
            lambda u, v: axes.c2p(u, v, func(u, v)),
            u_range=[0, PI],
            v_range=[0, PI/2],
            resolution=(20, 20),
            should_make_jagged=True,
        )
        volume.set_style(fill_color=YELLOW, fill_opacity=0.5)

        # Set up the scene
        self.set_camera_orientation(phi=70 * DEGREES, theta=-45 * DEGREES)
        self.begin_ambient_camera_rotation(rate=0.1)

        # Add elements to the scene
        self.add(axes, axes_labels, surface, volume)
        self.wait(2)

        # Create and animate the pointers (red)
        x_pointer = always_redraw(lambda: Line(
            axes.c2p(0, 0, 0),
            axes.c2p(PI, 0, 0),
            color=RED
        ))
        y_pointer = always_redraw(lambda: Line(
            axes.c2p(PI, 0, 0),
            axes.c2p(PI, PI/2, 0),
            color=RED
        ))
        z_pointer = always_redraw(lambda: Line(
            axes.c2p(PI, PI/2, 0),
            axes.c2p(PI, PI/2, func(PI, PI/2)),
            color=RED
        ))

        # Animate the pointers
        self.play(Create(x_pointer), run_time=2)
        self.play(Create(y_pointer), run_time=2)
        self.play(Create(z_pointer), run_time=2)

        # Show the integration process with rectangles
        num_rectangles = 5
        rectangles = VGroup()
        for i in range(num_rectangles):
            for j in range(num_rectangles):
                x = i * PI / num_rectangles
                y = j * PI / (2 * num_rectangles)
                height = func(x, y)
                rect = Cube(
                    side_length=1,
                    fill_opacity=0.5,
                    fill_color=YELLOW,
                    stroke_width=0.5,
                    stroke_color=WHITE
                )
                rect.scale(
                    [PI/num_rectangles, PI/(2*num_rectangles), abs(height)]
                )
                rect.move_to(axes.c2p(
                    x + PI/(2*num_rectangles),
                    y + PI/(4*num_rectangles),
                    height/2 if height > 0 else 0
                ))
                rectangles.add(rect)

        self.play(Create(rectangles), run_time=3)
        self.wait(2)

        # ハイライトされた積分範囲の表示
        integration_area = Rectangle(
            width=PI,
            height=PI/2,
            fill_color=GREEN,
            fill_opacity=0.3,
            stroke_color=GREEN
        ).move_to(axes.c2p(PI/2, PI/4, 0))
        self.play(FadeIn(integration_area), run_time=2)
        self.wait(2)

        # 積分過程のアニメーション
        self.play(
            ApplyMethod(volume.set_fill, YELLOW, opacity=0.7),
            run_time=2
        )
        self.play(
            ApplyMethod(volume.set_fill, YELLOW, opacity=0.5),
            run_time=2
        )
        self.wait(2)

        # Remove the rectangles and show the final volume
        self.play(FadeOut(rectangles), FadeOut(integration_area), run_time=2)
        self.wait(2)

        # Stop the camera rotation and end the scene
        self.stop_ambient_camera_rotation()
        self.wait(2)

if __name__ == "__main__":
    scene = DoubleIntegralVisualization()
    scene.render()