
import matplotlib.pyplot as plt

class function:
    def __init__(self, derivitive) -> None:
        self.func = derivitive
    def illustrate(self, integrations, limits, graph_integral=False, integral=0):
        #if limits == int:
            #print("TypeError: The `limits` param. must be of type `tuple`. to learn more about the `limits` param. use `info.help`")
            #return
        #elif limits == str:
            #print("TypeError: The `limits` param. must be of type `tuple`. to learn more about the `limits` param. use `info.help`")
            #return
        #elif len(limits) != 2:
            #print("ShapeError: The 'len()' of the inputed 'limits' param. must be equal to two. to learn more about the `limits` param. use `info.help`")
            #return

        base = (limits[1]-limits[0])/integrations
        current_x = limits[0]
        x_values = []

        for i in range(integrations):
            x_values.append(current_x)
            current_x += base
            
        x_values.append(limits[1])
        y = self.func(x_values)

        fig, ax = plt.subplots()
        ax.plot(x_values, y, label="f(x)")

        if graph_integral == True:
            height=integral/(limits[1]-limits[0])
            ax.plot(limits,(integral,integral),label=f"absolute integral value ({round(integral,2)})")
            ax.plot(limits,(height,height), label="integral area illustration (x*y=inte.)")
            ax.legend()

        ax.set(xlabel='x (input value)', ylabel='y (output value)',title='y=f(x)')
        ax.grid()

        plt.show()
        