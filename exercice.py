#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    for j in range(len(mot)):
        if j != 0 :
            l = ord(mot[j])
            if l > 64 and l <= 90:
                l = l + 32
                nom = nom[0:j] + chr(l) + nom[j+1:]
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
