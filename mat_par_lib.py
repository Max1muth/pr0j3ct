import pandas as pd
from matplotlib import pyplot as plt
import numpy as np


""" этот файл запускать не нужно, в нем также просто отдельно написаны функции, которые используются
 в файле "maybe_work" """


""" закомментированный код снизу имеет скорее ознакомительный характер как происходил процесс написания функций """
# data = pd.read_csv('13.csv')
#
# print(data.head())
# print(data['Цена'])
# print(data['Изменение'])
# print(data['Изменение в процентах'])
# print(data['Название'][0])
# print(len(data['Цена']))
#
# h = []
# e1 = ''
# val = str(data['Цена'][0])[-1:]
# for e in data['Цена']:
#     h.append(float(str(e)[:-1]))
# print(h)
# for i in range(2):
#
#     fig, ax = plt.subplots(figsize=(10, 6))
#     ax.plot(np.arange(len(data['Цена'])), h)
#
#     ax.set_title('График {}'.format(data['Название'][0]))
#     ax.set_ylabel(f'Значение {data['Название'][i]} {val}')
#     ax.set_xlabel('День')
#
#     plt.subplots_adjust(wspace=0.2, hspace=0.2)
#
#     plt.show()
#
#
# l1st1 = ['Цена', 'Изменение', 'Изменение в процентах']


def r1s0v2lk2(akz12: int, gr2f1k: str):
    f1l3 = str(akz12) + '.csv'
    l1st1k = ['Цена', 'Изменение', 'Изменение в процентах']
    zn14_l1 = []
    # if not (0 <= akz12 <= 11):
    #     return 'Беспредел'
    if gr2f1k in l1st1k:
        n2m3_1d = l1st1k.index(gr2f1k)
    else:
        return 'Ошибка'
    d2t2 = pd.read_csv(f1l3)
    for zn14 in d2t2[l1st1k[n2m3_1d]]:
        zn14_l1.append(float(str(zn14)[:-1]))
    v2l = str(d2t2['Цена'][0])[-1:]
    f1g, ax_ = plt.subplots(figsize=(10, 6))
    ax_.plot(np.arange(len(d2t2['Цена'])), zn14_l1)
    ax_.set_title(f'График {l1st1k[n2m3_1d]}')
    ax_.set_ylabel(f'Значение акции {d2t2['Название'][0]}, {v2l}')
    ax_.set_xlabel('День')

    plt.subplots_adjust(wspace=0.2, hspace=0.2)

    plt.show()


# r1s0v2lk2(13, 'Цена')
# h = []
# for i in range(12):
#     file = str(i) + '.csv'
#     with open(file, 'r', encoding='utf-8') as f:
#         drt = pd.read_csv(f)
#         drt = str(drt['Название'][0])
#         h.append(drt)
#
# print(h)
