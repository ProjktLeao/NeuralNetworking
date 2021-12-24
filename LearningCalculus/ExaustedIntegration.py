class function:
    def __init__(self, derivitive) -> None:
        self.func = derivitive
    def calculate_area(self, limits, integrations=10**7, illustrate=False):
        if len(limits) == 2:
            rate_of_change = (limits[1]-limits[0])/integrations
            minimum_area = 0
            maximum_area = 0
            current_X = limits[0]
            for i in range(integrations):
                minimum_area += max(self.func(current_X) * rate_of_change,0) #because Area = base*height and ROC is base
                current_X += rate_of_change
            current_X = limits[0] + rate_of_change
            for j in range(integrations - 1):
                maximum_area += max(self.func(current_X) * rate_of_change,0) #because Area = base*height and ROC is base
                current_X += rate_of_change
            integral = (minimum_area + maximum_area)/2
            if illustrate == True:
                import FunctionIllustration as illustration
                illustration.function(self.func).illustrate(integrations,limits,graph_integral=True,integral=integral)
            return integral

class example_functions:
    def function_X_squared(X):
        return X**2

    def function_linear_standard(X):
        return X

class library_info:
    def _help():
        print(
            "Getting started:\n\n",
            "   -make(or use the integrated ones located in 'example_functions') a new function with",
            "'def' with an(singular) input parameter that returns a value(float/int)."
            "let this equation be your mathematical function of your liking\n"
            "\n"
            "   -next, make a tuple((float,float)) or array ([float,float]) of size 2 with floats(or ints) inside them.\n"
            "let them be your range(A.K.A limits). To avoid issues, order your tuple's/array's value in acending order\n"
            "like so [smaller float/int, larger float/int]\n"
            "\n"
            "   -finnaly, assign the class 'function' to a variable and enter your mathematical function as a parameter.\n"
            "Then, in order to calculate, use the 'calculate_area' function inside your new variable containing the class of\n"
            "function. Next, add your tuple/array as your first parameter and the number of integrations(int) as your second.\n"
             "The 'integrations' parameter determines how many rectangles will be drawn inside your shape to determine area\n"
            "(ie. the higher integration is the higher the accuracy and the higher the cost to process. absurdly low(<10-20)\n"
            " and absurdly high(per machine basis) values are discouraged because of acuracy and performance issues respectfully\n"
            "\n"
            "\n"
            "I hope my late night project has helped you in any way, shape, or form. This is not the fastest program of its kind but I \n"
            "believe i've optimized it great despite the fact ive been awake for roughly 17-18 hours. Enjoy! "
        )
    def _misc_info():
        print("library name: Calculus Integration Calculator\n",
                "Made by: Arthur Leao De Souza \n",
                "Time made:12/3/2021(Dec) 9:06pm Sao Paulo time\n"
                "library function: testing and familiarization of the application",
                "of integration from calculus")
