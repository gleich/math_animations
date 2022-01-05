run:
	manim -pqk --fps 120 --renderer opengl ./presentations/$(PROBLEM).py Problem

build:
	manim -qk -o out --fps 120 ./presentations/$(PROBLEM).py Problem