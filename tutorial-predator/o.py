from manim import * 
import pandas as pd
import numpy as np

class RuledProbabilityExplanation(Scene):
    def construct(self):
        table=Table([["1","2","1"],["1","2","1"],],include_outer_lines=True)
        table.add_highlighted_cell((2,2), color=YELLOW)
        self.add(table)
        