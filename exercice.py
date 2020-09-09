#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    for j in range(len(nom)):
        if j != 0 :
            l = ord(nom[j])
            if l > 64 and l <= 90:
                l = l + 32
                nom = nom[0:j] + chr(l) + nom[j+1:]

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
