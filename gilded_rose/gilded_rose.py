# -*- coding: utf-8 -*-
class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def daily_maintenance(self):
        for item in self.items:
            item.daily_maintenance()
