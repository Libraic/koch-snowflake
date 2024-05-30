from manim import *
import numpy as np
from math import *


class KochSnowflake(Scene):
    def construct(self):
        # Define the vertices of an equilateral triangle
        triangle_vertices = [
            np.array([1, 0, 0]),
            np.array([-0.5, np.sqrt(3) / 2, 0]),
            np.array([-0.5, -np.sqrt(3) / 2, 0])
        ]

        # Create an equilateral triangle
        initial_triangle = Polygon(*triangle_vertices, color=BLUE, fill_opacity=0)

        first_distance = 1.0 / 3.0
        second_distance = 2.0 / 3.0
        first_point_x = (1 - first_distance) * triangle_vertices[0][0] + first_distance * triangle_vertices[1][0]
        first_point_y = (1 - first_distance) * triangle_vertices[0][1] + first_distance * triangle_vertices[1][1]
        second_point_x = (1 - second_distance) * triangle_vertices[0][0] + second_distance * triangle_vertices[1][0]
        second_point_y = (1 - second_distance) * triangle_vertices[0][1] + second_distance * triangle_vertices[1][1]
        dx = first_point_x - second_point_x
        dy = first_point_y - second_point_y
        third_point_x = cos(PI/3) * dx - sin(PI/3) * dy + second_point_x
        third_point_y = sin(PI/3) * dx + cos(PI/3) * dy + second_point_y

        vertices = [
            np.array([first_point_x, first_point_y, 0]),
            np.array([second_point_x, second_point_y, 0]),
            np.array([third_point_x, third_point_y, 0])
        ]

        # Create an equilateral triangle
        new_triangle = Polygon(*vertices, color=RED, fill_opacity=0)

        self.play(Create(initial_triangle))
        self.play(Create(new_triangle), run_time=3)
        self.wait()

