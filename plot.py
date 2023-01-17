import matplotlib.pyplot as plt
from datetime import datetime
"""Вставить ссылку на людей в suspect и указать рассматриваемый временной интервал"""
suspects = []
date_from = datetime(year=2023, month=1, day=16, hour=0, minute=00).strftime("%Y-%m-%d; %H:%M:%S")
date_to = datetime(year=2023, month=1, day=16, hour=23, minute=00).strftime("%Y-%m-%d; %H:%M:%S")

def drawing(suspects):
    color = ['r', 'b', 'g', 'm', 'y']
    for i, item in enumerate(suspects):
        fig, ax = plt.subplots(figsize=[24, 12])
        x_list = []
        pc_list = []
        mob_list = []
        with open(str(item[15:]) + '.txt', "r") as file:
            for line in file:
                if date_from <= line[:17] <= date_to:
                    line_list = line.split(',')
                    x_list.append(line_list[0][12:])
                    pc_list.append(int(line_list[1]))
                    mob_list.append(int(line_list[2])+0.02)

        ax.plot(x_list, pc_list, 's', label=item[15:], color=color[i])
        ax.plot(x_list, mob_list, 'd', color=color[i])
        ax.set_xlabel('$date$', fontsize=16)
        ax.set_ylabel('$status$', fontsize=16)
        ax.grid(which='major', color='k', linewidth=0.1)
        plt.ylim((0, 1.2))
        ax.legend(fontsize=10)
    plt.show()

drawing(suspects)
