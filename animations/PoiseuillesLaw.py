from manimlib import *
from datetime import datetime

text_font = "CMU Serif"
title_font_size = 80
subtitle_font_size = 50
play_kw = {"run_time": 3, "rate_func": smooth}

raw_equation = "Q = \\frac{\\pi r^4 \\Delta P}{8 \\eta L}"


class PoiseuillesLaw(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):
        self.setup()
        self.intro()
        self.equation()
        self.variable_defs()
        self.assumptions()
        self.problem()
        self.variables()
        self.do_problem()

    def setup(self):
        dummy_text = Text(".")
        self.play(Write(dummy_text))
        self.clear()
        input()

    def intro(self):
        self.clear()
        title = Text("Poiseuille's Law", font=text_font, font_size=title_font_size)
        class_text = Text("AP Physics 2", font=text_font, font_size=subtitle_font_size)
        by = Text(
            f"Matt Gleich {datetime.now().year}",
            font=text_font,
            font_size=subtitle_font_size,
        )
        VGroup(title, class_text, by).arrange(DOWN, buff=0.5)
        self.play(Write(title), **play_kw)
        self.play(Write(class_text), Write(by), **play_kw)
        input()
        self.play(
            FadeOut(title, shift=LEFT), Uncreate(class_text), FadeOut(by, shift=RIGHT)
        )
        self.clear()

    def equation(self):
        eq = Tex(raw_equation, font_size=title_font_size)
        textbook_eq = Tex(
            raw_equation.replace("\\Delta P", "(P_2 - P_1)").replace("r^4", "R^4"),
            font_size=title_font_size,
        )
        name = Text("Poiseuille's Law", font=text_font, font_size=subtitle_font_size)
        VGroup(eq, name).arrange(DOWN, buff=1)
        self.play(Write(eq), Write(name), **play_kw)
        self.wait()
        input()
        self.play(TransformMatchingTex(eq, textbook_eq))
        input()
        self.play(Uncreate(textbook_eq), FadeOut(name, DOWN))
        self.clear()

    def variable_defs(self):
        eq = Tex(raw_equation, font_size=60)
        eq.to_corner(RIGHT + UP)
        variables = VGroup(
            Tex("Q = \\text{flow rate} \\rightarrow \\frac{\\text{m$^3$}}{\\text{s}}"),
            Tex("r = \\text{radius of pipe} \\rightarrow \\text{m}"),
            Tex(
                "\\Delta P = \\text{pressure gradient} \\rightarrow \\frac{\\text{N}}{\\text{m$^2$}} \\equiv \\text{Pa}"
            ),
            Tex("\\eta = \\text{viscosity} \\rightarrow \\text{Pa} \\cdot \\text{s}"),
            Tex("L = \\text{length of pipe} \\rightarrow \\text{m}"),
        )
        variables.arrange(DOWN)
        self.play(FadeIn(eq, DOWN + LEFT), Write(variables, **play_kw))
        input()
        self.play(Uncreate(variables), FadeOut(eq, UP + RIGHT))
        self.clear()

    def assumptions(self):
        title = Text("Assumptions", font_size=title_font_size, font=text_font)
        title.to_corner(LEFT + UP)
        assumptions = Text(
            "Fluid is Laminar\nSystem is Closed",
            font_size=subtitle_font_size,
            font=text_font,
        )
        self.play(FadeIn(title, DOWN + RIGHT), Write(assumptions, **play_kw))
        input()
        self.play(Uncreate(assumptions), FadeOut(title, UP + LEFT))
        self.clear()

    def problem(self):
        title = Text("Problem", font_size=title_font_size, font=text_font)
        title.to_corner(LEFT + UP)
        problem = Text(
            "Calculate the volumetic flow rate of laminar fluid in a pipe with a radius of 2 meters\nand change gradient of 2 Pa. This viscosity of the liquid is 3 Pa x s and the length\nof the pipe is 3 meters.",
            font_size=30,
            font=text_font,
        )
        self.play(FadeIn(title, DOWN + RIGHT), Write(problem, **play_kw))
        input()
        self.play(Uncreate(problem), FadeOut(title, UP + LEFT))
        self.clear()

    def variables(self):
        title = Text("Variables", font_size=title_font_size, font=text_font)
        title.to_corner(LEFT + UP)
        eq = Tex(raw_equation, font_size=60)
        variables = VGroup(
            Tex("Q = \\text{? } \\frac{\\text{m}^3}{\\text{s}}"),
            Tex("r = 2 \\text{ m}"),
            Tex("\\Delta P = 2 \\text{ Pa}"),
            Tex("\\eta = 3 \\text{ Pa} \\times \\text{s}"),
            Tex("L = 3 \\text{ meters}"),
        )
        variables.arrange(DOWN)
        eq.next_to(variables, LEFT)
        self.play(
            FadeIn(title, DOWN + RIGHT),
            Write(variables, **play_kw),
            Write(eq, **play_kw),
        )
        input()
        self.play(
            FadeOut(title, UP + LEFT), FadeOut(eq, LEFT), FadeOut(variables, RIGHT)
        )
        self.clear()

    def do_problem(self):
        title = Text("Solve", font_size=title_font_size, font=text_font)
        title.to_corner(LEFT + UP)

        steps = {
            "Insert": "Q = \\frac{\\pi \\cdot 2^4 \\cdot 2}{8 \\cdot 3 \\cdot 3}",
            "Combine Like Terms (Top)": "Q = \\frac{\\approx 100.53}{8 \\cdot 3 \\cdot 3}",
            "Combine Like Terms (Bottom)": "Q = \\frac{\\approx 100.53}{72}",
            "Combine Like Terms": "Q \\approxeq 1.396",
            "Final Answer": "Q \\approxeq 1.396 \\frac{\\text{m}^3}{\\text{s}}",
        }
        past_math = None
        past_description = None
        for key, value in steps.items():
            description = Text(key, font_Size=30, font=text_font)
            math = Tex(value, font_size=subtitle_font_size)
            VGroup(math, description).arrange(DOWN, buff=1)
            if past_math is None and past_description is None:
                past_math = math
                past_description = description
                self.play(Write(math, **play_kw), FadeIn(description, UP))
            else:
                self.play(
                    Transform(past_math, math),
                    Transform(past_description, description),
                )
            input()
