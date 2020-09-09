#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    for j in range(len(mot)):
        l = ord(mot[j])
        if l > 96 and l <123:
            l = l - 32
            mot = mot[0:j] + chr(l) + mot[j+1:]
        elif l == 233:
            l = 144
            mot = mot[0:j] + chr(l) + mot[j+1:]
    return mot

print(ord('É'))
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
