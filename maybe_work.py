from mat_par_lib import *
import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Построение графика")
root.geometry("400x500")
root.resizable(True, False)


label = tk.Label(root, text="Выберете интересующий график и нажмите на кнопку ниже:", height=5,
                 font="Arial 8 normal roman")
label.pack()


l1st1k1 = ['Цена', 'Изменение', 'Изменение в процентах']
l1st1k2 = ['AMCEntertainment', 'Липецкаяэнергосбытоваякомпания', 'РБК', 'Варьеганнефтегаз', 'ГруппаАстра', 'ВУШХолдинг',
           'Тамбовскаяэнергосбытоваякомпания—привилегированные', 'Волгоградэнергосбыт', 'Яндекс',
           'Волгоградэнергосбыт—привилегированные', 'РуссНефть', 'Варьеганнефтегаз—привилегированные']


z = 'Цена'
izm = 'Изменение'
izm_p = 'Изменение в процентах'

p3r1 = tk.StringVar(value=z)  # по умолчанию будет выбран элемент с value=z
head3r1 = ttk.Label(textvariable=p3r1, padding=15)
head3r1.pack()

radiobutton = tk.Radiobutton(root, text="Цена акции", value=z, variable=p3r1)
radiobutton.pack()
radiobutton1 = tk.Radiobutton(root, text="Изменение акции", value=izm, variable=p3r1)
radiobutton1.pack()
radiobutton1 = tk.Radiobutton(root, text="Изменение акции в процентах", value=izm_p, variable=p3r1)
radiobutton1.pack()

p3r2 = tk.StringVar(value='AMCEntertainment')
head3r2 = ttk.Label(textvariable=p3r2, padding=20)
head3r2.pack()

combobox = ttk.Combobox(root, values=['AMCEntertainment', 'Липецкаяэнергосбытоваякомпания', 'РБК', 'Варьеганнефтегаз',
                                      'ГруппаАстра', 'ВУШХолдинг', 'Тамбовскаяэнергосбытоваякомпания—привилегированные',
                                      'Волгоградэнергосбыт', 'Яндекс', 'Волгоградэнергосбыт—привилегированные',
                                      'РуссНефть', 'Варьеганнефтегаз—привилегированные'], textvariable=p3r2, height=20)
combobox.pack()


def p1nt():
    print(p3r1.get(), p3r2.get())
    n2m3_1d = l1st1k2.index(p3r2.get())
    r1s0v2lk2(n2m3_1d, p3r1.get())


button = tk.Button(root, text="Нажми", command=p1nt, background='lightgreen')
button.pack()
# Главный цикл, окно будет активным, пока пользователь его не закроет

root.mainloop()
