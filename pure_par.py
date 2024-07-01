from etc_pars import *  # clean3r, g2th3r1ng, d1g1t
import pandas as pd
import csv
from datetime import datetime
import tkinter as tk

""" закомментированный код ниже несет ознакомительный характер как происходило создание функций"""
# date = datetime.now()
# date = date.strftime(f"|Запись от {'%Y/%m/%d %H:%M:%S'}|:")

# d1g1tl1es = int(input('Введите цифру от 1 до 12 \n'))
# for i in range(d1g1tl1es):
#     for x1x in g2th3r1ng(i):
#         print(clean3r(x1x))

# for x1x in g2th3r1ng(1):
#     print(clean3r(x1x))

# print(clean3r(g2th3r1ng(1)[0]))

# i = 1
# # fgh = str(i) + '.csv'
# #
# columns = ['Время', 'Цена', 'Изменение', 'Изменение в процентах', 'Название']
#
# data = [date, clean3r(g2th3r1ng(i)[1]), clean3r(g2th3r1ng(i)[2]), clean3r(g2th3r1ng(i)[3]), clean3r(g2th3r1ng(i)[0])]
# #
# # df = pd.Series(data)
# # # df.to_csv('$.csv')
# #
# with open('13.csv', 'a', encoding='utf-8') as f:
#     data_w = csv.writer(f)
#     # data_w.writerow(columns)
#     data_w.writerow(data)
#
# # data1 = pd.read_csv('$.csv')
# # print(data1.info())
# # data1 = data1.dropna()
# # print(data1.info())
# #
# # print(data1['Время'])


def h1d3():
    button.destroy()


def p7r3_p2rs3r():
    date = datetime.now()
    date = date.strftime(f"|Запись от {'%Y/%m/%d %H:%M:%S'}|:")
    columns = ['Время', 'Цена', 'Изменение', 'Изменение в процентах', 'Название']
    for i in range(12):
        n2m3_csv = str(i) + '.csv'
        data = [date, clean3r(g2th3r1ng(i)[0]), clean3r(g2th3r1ng(i)[1]), clean3r(g2th3r1ng(i)[2]),
                pd.read_csv(n2m3_csv)['Название'][0]]  # после создания имя можно дублировать из файла
        df = pd.Series(data)
        with open(n2m3_csv, 'a', encoding='utf-8') as f:  # после создания 'w' было заменено на 'a'
            data_w = csv.writer(f)
            # data_w.writerow(columns)
            data_w.writerow(data)


root = tk.Tk()
root.title("Внимание!")
root.geometry("400x150")
root.resizable(False, False)

label = tk.Label(root, text="Точно ли прошел день с прошлого запроса?", height=5,
                 font="Arial 8 normal roman")
label.pack()

button = tk.Button(root, text="Да", command=lambda: (p7r3_p2rs3r(), h1d3()), background='red', padx=5)
button.pack()

root.mainloop()
