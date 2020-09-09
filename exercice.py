#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    for j in range(len(mot)):
        l = ord(mot[j])
        if l > 96 and l <123:
            l = l - 32
            mot = mot[0:j] + chr(l) + mot[j+1:]
        else :
            print (l)
        elif l == 130:
            l = 69
            mot = mot[0:j] + chr(l) + mot[j+1:]
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)
