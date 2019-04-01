import time
import math
import matplotlib.pyplot as plt

Ini_Pop = int(input("Starting number of your population"))

Area_Size = int(input("How much land does the population have in square meters?(This influence your growth rate!)"))

Area_Influence = int(input("How many people per square are allowed?"))

Pop_grow = float(input("Average birth rate per year?")) / 100

Death_rate = float(input("Your Average Death Rate per year?")) / 100

Timeline = int(input("How many years to monitor the population?"))

Pop_Density = 0

population = 0

x_plot = [0]

y_plot = [0]

t = 0

for Timeline in range(0, Timeline):
    time.sleep(0.915)
    while t <= Timeline:
        t += 1
        population = (Ini_Pop * (math.exp(1) ** (Pop_grow * t))) - (Ini_Pop/(1+ (math.exp(1) ** (Death_rate * t))))
        x_plot.append(population)
        y_plot.append(t)
        Pop_Density = (population*Area_Influence)/Area_Size
    if Pop_Density <= .10:
        Pop_grow = Pop_grow * .20
    elif Pop_Density >= .11:
        Pop_grow = Pop_grow * .40
    elif Pop_Density >= .26:
        Pop_grow = Pop_grow * .60
    elif Pop_Density >= .51:
        Pop_grow = Pop_grow * .80
    elif Pop_Density >= .76:
        Pop_grow = Pop_grow * 1
    elif Pop_Density >= 1 :
        Pop_grow = Pop_grow * 1.25
    elif Pop_Density >= 1.50:
        Pop_grow = Pop_grow * 1.5
    elif Pop_Density >= 2:
        Pop_grow = Pop_grow * 2
    else:
        Pop_grow = Pop_grow * 1
    print("Current Year is ", t, "with the total population of", format(population, ".1f"))


plt.plot(x_plot,y_plot)
plt.show()