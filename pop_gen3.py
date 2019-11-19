import time
import math
import matplotlib.pyplot as plt

civ_count = int(input("How many civilizations do you wish to have?"))
civ_countdown = 0
civ_list = []

for civ_countdown in range(0, civ_count):
  civ_countdown += 1
  civ_list.append(input("Name of civ"))
  print(civ_list)

Pop_Density = 0

population = 0

x_plot = [0]

y_plot = [0]

t = 0

y = 0

civs_final = {}

for x in civ_list:
    Ini_Pop = int(input("Starting number of your population of + str(civ_list[0+y])")) 

    Area_Size = int(input("How much land does the population have in square meters?(This influence your growth rate!)"))

    Area_Influence = int(input("How many people per square are allowed?"))

    Pop_grow = float(input("Average birth rate per year for?")) / 100 

    Death_rate = float(input("Your Average Death Rate per year?")) / 100

    Timeline = int(input("How many years to monitor the population?"))

    t = Timeline
    population = (Ini_Pop * (math.exp(1) ** (Pop_grow * t))) - (Ini_Pop/(1+ (math.exp(1) ** (Death_rate * t))))
    print("Current Year is ", t, "with the total population of", format(population, ".1f"))
    civs_final[civ_list[0 + y]] = population
    y += 1
    print(civs_final[0+y])