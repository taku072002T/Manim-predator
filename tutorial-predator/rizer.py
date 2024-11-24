from manim import *
import numpy as np

class CreateSquareundCircle(Scene):
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

        self.wait(2.0)


class CreateSinCurves(Scene):
    def construct(self):
        # //Copied from https://qiita.com/ymgc3/items/0b6179638a7166025c2f
                # ベクトル場を定義する関数。
        # この関数は、与えられた位置に基づいてベクトルを返します。
        # ここでは、sinとcos関数を使用して2D空間でのベクトル場を作成しています。
        func = lambda pos: np.cos(pos[1] / 2) * LEFT
        
        # StreamLinesオブジェクトを作成。
        # funcで定義されたベクトル場に沿った流線を生成します。
        stream_lines = StreamLines(func, stroke_width=2, max_anchors_per_line=30)
        
        # 生成された流線をシーンに追加します。
        self.add(stream_lines)
        
        # 流線のアニメーションを開始します。
        # warm_upをFalseに設定することで、アニメーションがすぐに開始されます。
        # flow_speedパラメータで流線の動きの速さを調整できます。
        stream_lines.start_animation(warm_up=False, flow_speed=1.5)
        
        # アニメーションが終了するまで待機します。
        # virtual_timeとflow_speedを使用してアニメーションの総時間を計算し、
        # その時間だけ待機することで、アニメーションが完了するのを確実にします。
        self.wait(stream_lines.virtual_time / stream_lines.flow_speed)