from bs4 import BeautifulSoup
import requests

""" Данный файл запускать не нужно, функции из этого файла используются в файле "pure_par.py". Также я не стал удалять
закомментированные строчки кода, так как в случае того, если csv файлы будут отсутсвовать их можно будет снова создать
раскомментировав код """

url = 'https://www.banki.ru/investment/shares/'
response = requests.get(url)
# print(response)
# soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

# если что-то перестанет работать, возможно нужно будет проверить ответ сервера, то есть достаточно будет
# раскомментировать код выше

soup = BeautifulSoup(response.text, 'html.parser')
# print(soup)

""" закомментированный код снизу имеет скорее ознакомительный характер как происходил процесс написания функций """
# id_comp = 11  # 11=max
# table = str(soup.find_all('div', class_='TextResponsive__sc-hroye5-0 jKnrKA')[id_comp])[1:-1]
# # print(table[id_comp])
#
# s = ''
# flag = False
# for char in table:
#     if char == '>':
#         flag = True
#         continue
#     if char == '<':
#         flag = False
#         continue
#     if flag:
#         s += char
# # print(s)
#
# zena = str(soup.find_all('div', class_='TextResponsive__sc-hroye5-0 keyTWo')[id_comp])[1:-1]
# # print(zena[id_comp])
#
# d = ''
# flag = False
# for char in zena:
#     if char == '>':
#         flag = True
#         continue
#     if char == '<':
#         flag = False
#         continue
#     if flag:
#         d += char
# # print(d)
#
# izme_zena1 = str(soup.find_all('div', class_='TextResponsive__sc-hroye5-0 fgQYaA')[id_comp*2])[1:-1]
# izme_zena2 = str(soup.find_all('div', class_='TextResponsive__sc-hroye5-0 fgQYaA')[id_comp*2+1])[1:-1]
# # print(izme_zena[id_comp*2])
#
# g = ''
# flag = False
# for char in izme_zena1:
#     if char == '>':
#         flag = True
#         continue
#     if char == '<':
#         flag = False
#         continue
#     if flag:
#         g += char
# # print(g)
#
# # print(izme_zena[id_comp*2+1])
#
# h = ''
# flag = False
# for char in izme_zena2:
#     if char == '>':
#         flag = True
#         continue
#     if char == '<':
#         flag = False
#         continue
#     if flag:
#         h += char
# # print(h)


def clean3r(str0ka: str):
    cleaned = ''
    fl2g = False
    for ch2r in str0ka:
        if ch2r == '>':
            fl2g = True
            continue
        if ch2r == '<':
            fl2g = False
            continue
        if fl2g:
            if ch2r == ',':
                cleaned += '.'
            elif ch2r == ' ':
                continue
            else:
                cleaned += ch2r
    if cleaned[0] == '(' and cleaned[-1] == ')':
        cleaned = cleaned[1:-1]
    return cleaned


def g2th3r1ng(id11: int):
    # n2m3 = str(soup.find_all('div', class_='TextResponsive__sc-hroye5-0 jKnrKA')[id11])[1:-1]
    pr1c3 = str(soup.find_all('div', class_='TextResponsive__sc-hroye5-0 keyTWo')[id11])[1:-1]
    alt2r2t10n = str(soup.find_all('div', class_='TextResponsive__sc-hroye5-0 fgQYaA')[id11*2])[1:-1]
    alt2r2t10n_p = str(soup.find_all('div', class_='TextResponsive__sc-hroye5-0 fgQYaA')[id11*2+1])[1:-1]
    return [pr1c3, alt2r2t10n, alt2r2t10n_p]  # когда файлы уже созданы можно имя вовсе не вызывать


# for i in range(12):
#     for x1x in g2th3r1ng(i):
#         print(clean3r(x1x))


def d1g1t(d1g: int):
    for p3r in range(d1g):
        for x2x2 in g2th3r1ng(p3r):
            print(clean3r(x2x2))


# print(d1g1t(int(input("Введите цифру Dx \n"))))
