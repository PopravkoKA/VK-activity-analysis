import matplotlib.pyplot as plt
from datetime import datetime
#вставить значение online полученное из data

# suspects = [] #вставить ссылки людей
# actual = suspects[1]
# x = list(online[actual].keys())
# PC = []
# MOB = []
# y = list(online[actual].values())
# for D in y:
#     PC.append(D['pc_status'])
#     MOB.append(D['mobile_status'])
# plt.plot(x, PC, '*', color='blue')
# plt.plot(x, MOB, '*', color='red')
# plt.title(actual)
# plt.show()

suspects = ['https://vk.com/reshwhat']
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

#
# # for i, ti in enumerate(np.linspace(3600/3600, 3600000/3600, 5)):
# for i, ti in enumerate(np.logspace(1, 6, 6)):
#     ax.plot(rd_1, (np.squeeze([soln1_inv_lapl_numpy(ti, r=ri) for ri in rd_1])+p01)/101325, label=f'$t={round(ti)}, сек$', color=color[i])
#     ax.plot(rd_2, (np.squeeze([soln2_inv_lapl_numpy(ti, r=ri) for ri in rd_2])+p01)/101325, color=color[i])
#
# plt.axvline(x=r_w,  linewidth=1, color='y', linestyle='--', label='радиус скважины')
# plt.axvline(x=r_c,  linewidth=1, color='g', linestyle='--', label='граница зон')
# ax.set_xlabel('$r, м$', fontsize=16)
# ax.set_ylabel('$p, атм$', fontsize=16)
# ax.set_title('Зависимость давления от радиуса для пласта с зональной неоднородностью', fontsize=15)
# ax.grid(which='major', color='k', linewidth=0.1)
# ax.legend(fontsize=10)
# # plt.ylim((180, None))
# # plt.xlim((0, r_c + 10))
# plt.show()