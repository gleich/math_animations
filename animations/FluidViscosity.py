from manimlib import *
from datetime import datetime

text_font = "CMU Serif"


class FluidViscosity(Scene):
    CONFIG = {
        "camera_config": {
            "background_color": WHITE,
        },
    }

    def construct(self):
        self.intro()

    def intro(self):
        title = Text("Fluid & Viscosity Problem", font=text_font, font_size=80)
        by = Text(f"Matt Gleich {datetime.now().year}", font=text_font, font_size=60)
        VGroup(title, by).arrange(DOWN, buff=1)
        self.play(Write(title))
        self.play(Write(by))
        self.wait(3)
        self.clear()
