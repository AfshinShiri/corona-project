import matplotlib.pyplot as plt 
import random

def random_color(number):
    import numpy as np
    colors = []
    i = 0
    while i<number:
        this_color = list(np.random.choice(range(100), size=3))
        tmp_color = []
        tmp_color.append(this_color[0]/100)
        tmp_color.append(this_color[1]/100)
        tmp_color.append(this_color[2]/100)
        colors.append(tmp_color)
        i = i+1
    return colors

def get_plot(Country, Total_Cases):
    ### Number of Contries :
    number_of_country = 10

    ### TotalCase to int(from string) : 
    Total_Cases_int = [] ### Total Case are String by default
    tmp_Country = []
    for i in range(0, number_of_country):
        string_number = Total_Cases[i]
        if "," in string_number:
            tmp_list = string_number.split(",")
            string_number = tmp_list[0] + tmp_list[1]

            Total_Cases_int.append(int(string_number))
        else:
            Total_Cases_int.append(int(string_number))
        
        tmp_Country.append(Country[i])
    Country = tmp_Country

    register = range(0, number_of_country)
    plt.figure(figsize = (8, number_of_country))
    b = plt.barh(register, Total_Cases_int, height = .8, color=tuple(random_color(number_of_country)))
    plt.yticks(register, Country)
    plt.title("Total case of coronavirus in top 10 countries")
    plt.legend(b, Country, fontsize = 14)
    plot_src = "static/DB/plot.png"
    plt.savefig(plot_src)

    return plot_src