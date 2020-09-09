#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    pl = ord(nom[0])
    if pl >= 97 and pl <= 122: 
        pl = pl - 32
    for j in range(len(nom)):
        if j != 0 and isspace(nom[j]) = false:
            l = ord(nom[j])
            if l  

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
