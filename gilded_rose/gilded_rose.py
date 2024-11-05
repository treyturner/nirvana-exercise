# -*- coding: utf-8 -*-
import operator

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def apply_delta(self, item):
        boundary = 0 if item.quality_delta < 0 else 50
        comp = operator.ge if item.quality_delta < 0 else operator.le
        if (comp(item.quality + item.quality_delta, boundary)):
            item.quality += item.quality_delta
        else:
            item.quality = boundary

    def update_quality(self):
        for item in self.items:
            if item.quality_delta != 0:
                # handle quality delta
                self.apply_delta(item)

                # special handling for backstage passes
                if "Backstage passes" in item.name:
                    if item.sell_in < 11:
                        demand_adj = 2 if item.sell_in < 6 else 1
                        if (item.quality + demand_adj <= 50):
                            item.quality += demand_adj
                        else:
                            item.quality = 50

            if not item.evergreen:                
                item.sell_in -= 1

                # handle items past sell_in
                if item.sell_in < 0:
                    if "Backstage passes" in item.name:
                        item.quality = 0
                    else:
                        self.apply_delta(item)

class Item:
    def __init__(self, name, sell_in, quality, quality_delta=-1, expires=False, evergreen=False):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        self.quality_delta = quality_delta # daily quality delta (positive or negative)
        self.expires = expires # true if quality should become 0 once sell_in is negative
        self.evergreen = evergreen # true if sell_in should not decrement

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
