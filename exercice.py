#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    pl = ord(nom[0])
    if pl >= 97 and pl <= 122:
        pl = pl - 32
    nom = chr(pl) + nom[1:]
    sc = 0
    for j in range(len(nom)):
        if nom[j].isspace():
            sc = sc + 1
        if j != 0 and sc !=2 :
            l = ord(nom[j])
            if l > 64 and l <= 90:
                l = l + 32
                nom = nom[0:j] + chr(l) + nom[j+1:]
        elif 
    return nom


if __name__ == '__main__':
    pays = [
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
