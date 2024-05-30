from manim import *
from math import *


class KochSnowflake(Scene):
    FIRST_DISTANCE = 1.0 / 3.0
    SECOND_DISTANCE = 2.0 / 3.0

    @staticmethod
    def get_vertices(first_vertice, second_vertice):
        first_point_x = ((1 - KochSnowflake.FIRST_DISTANCE)
                         * first_vertice[0] +
                         KochSnowflake.FIRST_DISTANCE *
                         second_vertice[0])
        first_point_y = ((1 - KochSnowflake.FIRST_DISTANCE) *
                         first_vertice[1] +
                         KochSnowflake.FIRST_DISTANCE *
                         second_vertice[1])
        second_point_x = ((1 - KochSnowflake.SECOND_DISTANCE) *
                          first_vertice[0] +
                          KochSnowflake.SECOND_DISTANCE *
                          second_vertice[0])
        second_point_y = ((1 - KochSnowflake.SECOND_DISTANCE) *
                          first_vertice[1] +
                          KochSnowflake.SECOND_DISTANCE *
                          second_vertice[1])
        dx = first_point_x - second_point_x
        dy = first_point_y - second_point_y
        third_point_x = cos(PI / 3) * dx - sin(PI / 3) * dy + second_point_x
        third_point_y = sin(PI / 3) * dx + cos(PI / 3) * dy + second_point_y
        return [
            np.array([first_point_x, first_point_y, 0]),
            np.array([second_point_x, second_point_y, 0]),
            np.array([third_point_x, third_point_y, 0])
        ]

    def construct(self):
        self.camera.background_color = BLACK
        vertices = [
            [
                np.array([1, 0, 0]),
                np.array([-0.5, np.sqrt(3) / 2, 0]),
                np.array([-0.5, -np.sqrt(3) / 2, 0])
            ]
        ]

        drawing_depth = 5
        for depth in range(drawing_depth):
            vertices_number = len(vertices)
            for i in range(vertices_number):
                current_vertice = vertices.pop(0)
                k = 0
                length = len(current_vertice)
                temp_vertices = []
                while k < length:
                    first_vertice = current_vertice[k % length if depth == 0 else (k + 1) % length]
                    second_vertice = current_vertice[(k + 1) % length if depth == 0 else k % length]
                    triangle_vertices = KochSnowflake.get_vertices(first_vertice=first_vertice,
                                                                   second_vertice=second_vertice)
                    if depth == 0 or k != 0:
                        vertices.append(triangle_vertices)
                        temp_vertices.append([first_vertice, triangle_vertices[0]])
                        temp_vertices.append([triangle_vertices[1], second_vertice])
                    if length != 2:
                        line = Line(current_vertice[k % length], current_vertice[(k + 1) % length],
                                    color=BLUE if depth == 0 or k != 0 else BLACK)
                        self.play(Create(line), run_time=1)
                    k += 1
                vertices.extend(temp_vertices)
        self.wait()
