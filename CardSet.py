#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from Card import Card
from copy import copy
import random

class CardSet:
    """"""
    def __init__(self, name, json):
        """"""
        self._name = name
        if not 'cards' in json:
            raise RuntimeError('no cards in set')
        self._cards = []
        for card in json['cards']:
            try:
                c = Card(card)
                self._cards.append(c)
            except TypeError:
                pass
            
        
    def size(self):
        """"""
        return len(self._cards)
        

    def getCard(self, index = 0):
        """"""
        return copy(self._cards[index])
    
    def getRandomCard(self, colors = []):
        """"""
        if not colors:
            return copy(random.choice(self._cards))
        else:
            lst = [card for card in self._cards if card.sameColor(colors)]
            return copy(random.choice(lst))

