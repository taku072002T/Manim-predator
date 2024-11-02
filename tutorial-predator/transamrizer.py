# ここでは、解析学2で学んだ重積分の概念を解説するようなアニメーションを作成します。
from manim import * 
import numpy as np
import sympy as sb
import math 
import matplotlib.pyplot as plt

# 三角関数の出力確認
print(np.sin(np.pi/2))

# 1pi = 180°。よって1/180pi = 1°
# 今回は1°ごとのラジアン値数列を作りたい。
# 4pi = 720°。よって1/720*4*pi = 1°
# xへ、0~4piまでの微小間隔行列を代入
x = np.linspace(-2*np.pi,2*np.pi,721)
print(x)

# yへ、x内の値それぞれについて、sin値を算出した配列を代入
y = np.sin(x)
print(y)

# これをmanimによって、サインカーブを書く。

class CreateSin(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-8,8,1],
            y_range=[-1.5,1.5,1],
            x_length=10,
            axis_config={"color":GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-8,8.1,2),
                "numbers_with_elongated_ticks": np.arange(-8, 8.01, 2),
                
            },
            tips=False
        )
        axis_labels = axes.get_axis_labels()
        func = lambda x: np.sin(x)
        sin_graph = axes.plot(func,color=BLUE)
        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=8, direction=UP
        )
        area = axes.get_area(sin_graph, x_range=(0,2*np.pi), color = YELLOW, opacity=0.3)
        plot = VGroup(axes,sin_graph)
        labels = VGroup(axis_labels, sin_label)
        self.add(plot,labels,area)
        

class AnimatedSin(Scene):
    def construct(self):
        axes = Axes(
            x_range=[-8,8,1],
            y_range=[-1.5,1.5,1],
            x_length=10,
            axis_config={"color":GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-8,8.1,2),
                "numbers_with_elongated_ticks": np.arange(-8, 8.01, 2),
                
            },
            y_axis_config={
                "numbers_to_include":np.arange(-1,1.1,1),
            },
            tips=False
        )
        axis_labels = axes.get_axis_labels()
        func = lambda x: np.sin(x)
        sin_graph = axes.plot(func,color=BLUE)
        sin_label = axes.get_graph_label(
            sin_graph, "\\sin(x)", x_val=8, direction=UP
        )
        area = axes.get_area(sin_graph, x_range=(0,2*np.pi), color = YELLOW, opacity=0.3)
        area_labels = MathTex("\\int_0^{2\\pi} \\sin(x) dx =  ?", color=YELLOW)
        area_labels.move_to([2,-2.5,0])
        plot = VGroup(axes,sin_graph)
        labels = VGroup(axis_labels, sin_label)
        self.add(axes)
        self.wait(1.0)
        self.play(Write(axis_labels))
        self.wait(1.0)
        self.play(Create(sin_graph))
        self.wait(1.0)
        self.play(Write(sin_label))
        self.wait(1.0)
        self.play(FadeIn(area))
        self.wait(1.0)
        self.play(Write(area_labels))
        self.wait(5.0)
        self.play(FadeOut(area))
        new_axes = Axes(
            x_range=[-4,4,1],
            y_range=[-1.5,1.5,1],
            x_length=10,
            axis_config={"color":GREEN},
            x_axis_config={
                "numbers_to_include": np.arange(-4,4.1,2),
                "numbers_with_elongated_ticks": np.arange(-4, 4.01, 2),
                
            },
            y_axis_config={
                "numbers_to_include":np.arange(-1,1.1,1),
            },
            tips=False
        )
        new_sin_graph=new_axes.plot(func,color=BLUE)
        new_area = new_axes.get_area(new_sin_graph,x_range=(0,np.pi),color=YELLOW, opacity=0.3)
        new_area_labels = MathTex("\\int_0^{\\pi} \\sin(x) dx =  ?", color=YELLOW)
        new_area_labels.move_to([2,-2.5,0])
        
        self.play(Transform(axes,new_axes),Transform(sin_graph,new_sin_graph),FadeOut(sin_label),FadeOut(area_labels))
        self.wait(1.0)
        self.play(FadeIn(new_area))
        self.wait(1.0)
        self.play(Write(new_area_labels))
        self.wait(1.0)
        self.play(FadeOut(new_area_labels))
        self.play(FadeOut(new_area))
        self.wait(1.0)
        t = ValueTracker(0)
        initial_point = [new_axes.coords_to_point(t.get_value(),func(t.get_value()))]
        dot = Dot(point=initial_point)
        dot.add_updater(lambda x: x.move_to(new_axes.c2p(t.get_value(), func(t.get_value()))))
        vertical_line = always_redraw(
        lambda: Line(
        start=new_axes.c2p(np.pi/2, 0),
        end=new_axes.c2p(np.pi/2, func(np.pi/2)),
        color=RED
        )
        )
        point_at_pi_half = Dot(new_axes.c2p(np.pi/2, func(np.pi/2)), color=RED)
        value_label = MathTex(f"\\sin(\\frac{{\\pi}}{{2}}) = {func(np.pi/2):.2f}", color=RED)
        value_label.next_to(point_at_pi_half, UP)
        self.play(Create(dot))
        self.play(t.animate.set_value(np.pi/2))
        self.play(Create(vertical_line),Create(point_at_pi_half),Write(value_label))
        self.play(t.animate.set_value(np.pi))
        self.wait(1.0)
        point_at_pi = Dot(new_axes.c2p(np.pi, func(np.pi)), color=RED)
        self.play(Create(point_at_pi))
        self.play(FadeOut(dot))
        ver0tohalf = always_redraw(
            lambda: Line(
                start = new_axes.c2p(0,1),
                end=new_axes.c2p(np.pi/2,1),
                color=RED
            )
        )
        verhalftopi = always_redraw(
            lambda: Line(
                start = new_axes.c2p(np.pi/2,0),
                end=new_axes.c2p(np.pi,0),
                color=RED
            )
        )
        self.play(Create(ver0tohalf),Create(verhalftopi))
        
        self.wait(5.0)
        self.play(FadeOut(VGroup(vertical_line,point_at_pi_half,value_label,point_at_pi,ver0tohalf,verhalftopi)))
        self.wait(1.0)
        
        # 一巡後
        t = ValueTracker(0)
        initial_point = [new_axes.coords_to_point(t.get_value(),func(t.get_value()))]
        dot = Dot(point=initial_point)
        dot.add_updater(lambda x: x.move_to(new_axes.c2p(t.get_value(), func(t.get_value()))))
        vertical_line = always_redraw(
        lambda: Line(
        start=new_axes.c2p(np.pi/3, 0),
        end=new_axes.c2p(np.pi/3, func(np.pi/3)),
        color=RED
        )
        )
        vertical_line2 = always_redraw(
        lambda: Line(
        start=new_axes.c2p(np.pi/3*2, 0),
        end=new_axes.c2p(np.pi/3*2, func(np.pi/3*2)),
        color=RED
        )
        )
        point_at_pi_1third = Dot(new_axes.c2p(np.pi/3, func(np.pi/3)), color=RED)
        point_at_pi_2third = Dot(new_axes.c2p(np.pi/3*2, func(np.pi/3*2)), color=RED)
        self.play(Create(dot))
        self.play(t.animate.set_value(np.pi/3))
        self.play(Create(vertical_line),Create(point_at_pi_1third))
        self.play(t.animate.set_value(np.pi/3*2))
        self.play(Create(vertical_line2),Create(point_at_pi_2third))
        self.play(t.animate.set_value(np.pi))
        self.wait(1.0)
        point_at_pi = Dot(new_axes.c2p(np.pi, func(np.pi)), color=RED)
        self.play(Create(point_at_pi))
        self.play(FadeOut(dot))
        ver0to1third = always_redraw(
            lambda: Line(
                start = new_axes.c2p(0,func(np.pi/3)),
                end=new_axes.c2p(np.pi/3,func(np.pi/3)),
                color=RED
            )
        )
        ver1to2third = always_redraw(
            lambda: Line(
                start = new_axes.c2p(np.pi/3,func(np.pi/3*2)),
                end=new_axes.c2p(np.pi/3*2,func(np.pi/3*2)),
                color=RED
            )
        )
        ver2thirdtopi = always_redraw(
            lambda: Line(
                start = new_axes.c2p(np.pi/3*2,func(np.pi)),
                end=new_axes.c2p(np.pi,func(np.pi)),
                color=RED
            )
        )
        self.play(Create(ver0to1third),Create(ver1to2third),Create(ver2thirdtopi))
        
        self.wait(5.0)
        self.play(FadeOut(VGroup(vertical_line,vertical_line2,point_at_pi_1third,point_at_pi_2third,point_at_pi,ver0to1third,ver1to2third,ver2thirdtopi)))
        self.wait(1.0)

        # 36巡後
        t = ValueTracker(0)
        initial_point = [new_axes.coords_to_point(t.get_value(),func(t.get_value()))]
        dot = Dot(point=initial_point)
        dot.add_updater(lambda x: x.move_to(new_axes.c2p(t.get_value(), func(t.get_value()))))
        #　最初からVGroupしとけばよかった...
        vertical_lines_36 = VGroup(*[
            always_redraw(lambda i=i: Line(
                start=new_axes.c2p(np.pi*i/36, 0),
                end=new_axes.c2p(np.pi*i/36, func(np.pi*i/36)),
                color=RED
            )) for i in range(1, 36)
        ])
        
        points_36 = VGroup(*[
            Dot(new_axes.c2p(np.pi*i/36, func(np.pi*i/36)), color=RED)
            for i in range(1, 37)
        ])

        self.play(Create(dot))
        self.play(t.animate.set_value(np.pi))
        self.play(Create(vertical_lines_36), Create(points_36))
        self.play(FadeOut(dot))

        horizontal_lines_36 = VGroup(*[
            always_redraw(lambda i=i: Line(
                start=new_axes.c2p(np.pi*(i-1)/36, func(np.pi*i/36)),
                end=new_axes.c2p(np.pi*i/36, func(np.pi*i/36)),
                color=RED
            )) for i in range(1, 37)
        ])
        
        self.play(Create(horizontal_lines_36))
        self.wait(5.0)
        self.play(FadeOut(VGroup(vertical_lines_36, points_36, horizontal_lines_36)))
        self.wait(1.0)

        # 360巡後（ほぼ面積）
        t = ValueTracker(0)
        initial_point = [new_axes.coords_to_point(t.get_value(),func(t.get_value()))]
        dot = Dot(point=initial_point)
        dot.add_updater(lambda x: x.move_to(new_axes.c2p(t.get_value(), func(t.get_value()))))
        
        vertical_lines_360 = VGroup(*[
            always_redraw(lambda i=i: Line(
                start=new_axes.c2p(np.pi*i/360, 0),
                end=new_axes.c2p(np.pi*i/360, func(np.pi*i/360)),
                color=RED
            )) for i in range(1, 360)
        ])
        
        points_360 = VGroup(*[
            Dot(new_axes.c2p(np.pi*i/360, func(np.pi*i/360)), color=RED)
            for i in range(1, 361)
        ])

        self.play(Create(dot))
        self.play(t.animate.set_value(np.pi))
        self.play(Create(vertical_lines_360), Create(points_360))
        self.play(FadeOut(dot))

        horizontal_lines_360 = VGroup(*[
            always_redraw(lambda i=i: Line(
                start=new_axes.c2p(np.pi*(i-1)/360, func(np.pi*i/360)),
                end=new_axes.c2p(np.pi*i/360, func(np.pi*i/360)),
                color=RED
            )) for i in range(1, 361)
        ])
        
        self.play(Create(horizontal_lines_360))
        integral_label = MathTex("\\approx\\int_0^{\\pi} \\sin(x)dx", color=RED)
        integral_label.move_to([2,2.5,0])
        self.play(Write(integral_label))
        self.wait(5.0)
        self.play(FadeOut(VGroup(vertical_lines_360, points_360, horizontal_lines_360)))
        self.wait(1.0)
        
        #EndOfCode
