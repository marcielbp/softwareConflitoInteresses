__author__ = 'andremeireles'

from difflib import SequenceMatcher

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()


# print similar('Andre Andrade', 'Andre Souza Andrade')