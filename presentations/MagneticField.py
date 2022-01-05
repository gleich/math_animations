from manim import *
import math

PROTON = True  # False for electron
VELOCITY = 3e6  # meters per second
STRENGTH = 0.1  # teslas
MASS = 1.673e-27 if PROTON else 9.109e-31
CHARGE = 1.600e-19 if PROTON else 1.602e-19
WAIT_TIME = 2


def exponential_fmt(num) -> str:
    return "{:.3e}".format(num).replace("e", "\\times 10^{") + "}".replace("+", "")


class Problem(Scene):
    def construct(self):
        self.intro()
        self.vars()
        self.visualization()

    def intro(self):
        logo = SVGMobject("sticker.svg").scale(1.5).to_corner(UL).shift(DOWN * 0.5)
        title = (
            Tex("Charge in a Magnetic Field")
            .scale(1.75)
            .next_to(logo, DOWN, buff=1)
            .shift(RIGHT * 4)
        )
        name = Tex("By Matt Gleich").next_to(title, DOWN, buff=0.3).shift(LEFT * 2.65)
        self.play(Write(title), Write(name), DrawBorderThenFill(logo), run_time=2.5)
        self.wait(WAIT_TIME)
        self.play(FadeOut(title, name, logo))
        self.clear()

    def vars(self):
        # top
        title = Tex("Variables").to_corner(UL, buff=1).scale(1.5)
        eq = MathTex("R = \\frac{mv}{Bq}").to_corner(UR, buff=1).scale(1.5)
        eq_box = SurroundingRectangle(eq, color=GREEN, buff=0.2)
        self.play(Write(title))
        self.wait(WAIT_TIME)
        self.play(Write(eq), Create(eq_box))

        # variables
        mass_def = Tex(f"mass ($ m $) $ \\rightarrow $ $ {exponential_fmt(MASS)} $ kg")
        velocity_def = (
            Tex(
                f"velocity ($ V $) $ \\rightarrow $ $ {exponential_fmt(VELOCITY)} $ m/s "
            )
            .next_to(mass_def, DOWN)
            .shift(LEFT * 0.1)
        )
        strength_def = (
            Tex(f"strength ($ B $) $ \\rightarrow $ {STRENGTH} T ")
            .next_to(velocity_def, DOWN)
            .shift(LEFT * 1.45)
        )
        charge_def = (
            Tex(f"charge ($ q $) $ \\rightarrow $ $ {exponential_fmt(CHARGE)} $ C ")
            .next_to(strength_def, DOWN)
            .shift(RIGHT * 1.45)
        )
        self.play(Write(mass_def))
        self.play(Write(velocity_def))
        self.play(Write(strength_def))
        self.play(Write(charge_def))
        self.wait(WAIT_TIME)

        self.play(
            FadeOut(title, eq, eq_box, mass_def, velocity_def, strength_def, charge_def)
        )
        self.clear()

    def visualization(self):
        answer = (MASS * VELOCITY) / (STRENGTH * CHARGE)
        eq = MathTex(
            f"R = \\frac{{mv}}{{Bq}} = \\frac{{({exponential_fmt(MASS)}) \\cdot ({exponential_fmt(VELOCITY)})}}{{({STRENGTH}) \\cdot ({exponential_fmt(CHARGE)})}} = {round(answer, 3)}  \\text{{ m}}"
        ).to_edge(UP)
        self.play(Write(eq))

        circ = Circle(radius=answer, color="#e92741").scale(5).shift(DOWN * 0.5)
        point = Dot().shift(DOWN * 0.5)
        center = Dot().shift(DOWN * 0.5)
        line = always_redraw(lambda: Line(circ.get_center(), point.get_center()))
        b_field = Brace(circ)
        b_field_tex = b_field.get_tex("\\vec{B} \\text{ } \\otimes")
        self.play(GrowFromCenter(circ), FadeIn(center, line))
        self.wait(WAIT_TIME)
        self.play(Create(b_field), Write(b_field_tex))
        self.wait(WAIT_TIME)
        self.play(point.animate.next_to(circ, buff=0).shift(LEFT * 0.1))
        self.play(
            MoveAlongPath(
                point,
                circ if PROTON else circ.reverse_points(),
            ),
            run_time=((2 * math.pi * answer) / VELOCITY) / 1e-7,
            rate_func=linear,
        )

        self.play(FadeOut(eq, circ, point, center, line, b_field, b_field_tex))
        self.clear()
