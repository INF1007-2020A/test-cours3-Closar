#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    for j in range(len(mot)):
        c = ord(j) - 32
        mot = mot[0:j] + chr(c) + mot[j+1:]
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
