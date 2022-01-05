run:
	manim -pqk --fps 120 --renderer opengl ./presentations/$(PROBLEM).py Problem

build:
	manim -qk -o $(PROBLEM) --fps 120 ./presentations/$(PROBLEM).py Problem
	mv ./media/videos/$(PROBLEM)/2160p120/$(PROBLEM).mp4 ./videos/