run:
	poetry run manimgl animations/$(PROBLEM).py $(PROBLEM) -c "#000"

video:
	poetry run manimgl animations/$(PROBLEM).py $(PROBLEM) -c "#000" -o --uhd
