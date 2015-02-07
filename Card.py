#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pprint import pprint

class Card:
    """"""
    def __init__(self, json):
        """"""
        
        self._name = json['name']
        if not 'colors' in json:
            self._colors = None
        else:
            self._colors = json['colors']
        if not 'cmc' in json:
            raise TypeError('it is a land')
        else:
            self._cmc = json['cmc']

    def __str__(self):
        """"""
        ret = str(self._name)
        if self._colors:
            for c in self._colors:
                ret = ret+' '+c
        ret = ret+' '+str(self._cmc)
        return ret
            
    def sameColor(self, colors):
        """"""
        if self._colors:
            return any((True for x in colors if x in self._colors))            
        else:
            return True
            

