#!/usr/bin/env python
# -*- coding: utf-8 -*-
def majuscule(mot):
    for j in range(len(mot)):
        al = ord(j) + 32
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
