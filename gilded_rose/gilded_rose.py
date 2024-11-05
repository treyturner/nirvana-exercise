# -*- coding: utf-8 -*-

#observed behaviors:
#
#valid qualities range from 0 to 50 inclusive
#brie and backstage passes are the only items that ever increment in quality
#brie increments 1 quality every day, even past sell_in
#backstage passes increment 1 quality per day when sell_in > 10, 2 when sell_in is 6-10, and 3 when 0-5
#backstage passes immediately receive quality 0 when past sell_in
#sulfuras does not suffer sell_in or quality degredation

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name != "Aged Brie" and item.name != "Backstage passes to a TAFKAL80ETC concert":
                # everything but brie or backstage pass
                if item.quality > 0:
                    # quality is positive
                    if item.name != "Sulfuras, Hand of Ragnaros":
                        # everything but brie, backstage pass, and sulfuras
                        if item.name == "Conjured Mana Cake" and item.quality > 1:
                            # conjured mana cake with quality > 1 only
                            item.quality = item.quality - 2
                            # !!! quality decremented by 2                            
                        else:
                            # everything but brie, backstage pass, sulfuras, and conjured mana cake with quality > 1
                            item.quality = item.quality - 1
                            # !!! quality decremented by 1
            else:
                # brie or backstage pass
                if item.quality < 50:
                    # quality is < 50
                    item.quality = item.quality + 1
                    # !!! quality incremented
                    if item.name == "Backstage passes to a TAFKAL80ETC concert":
                        # backstage pass only
                        if item.sell_in < 11:
                            # sell_in is < 11
                            if item.quality < 50:
                                # quality is still < 50
                                item.quality = item.quality + 1
                                # !!! quality incremented again!
                        if item.sell_in < 6:
                            # sell_in is < 6
                            if item.quality < 50:
                                # quality is still < 50
                                item.quality = item.quality + 1
                                # !!! quality incremented a third time!
            if item.name != "Sulfuras, Hand of Ragnaros":
                # everything but sulfuras
                item.sell_in = item.sell_in - 1
                # !!! sell_in decremented by 1
            if item.sell_in < 0:
                # sell_in is negative
                if item.name != "Aged Brie":
                    # everything but brie
                    if item.name != "Backstage passes to a TAFKAL80ETC concert":
                        # everything but brie and backstage pass
                        if item.name != "Sulfuras, Hand of Ragnaros" and item.quality > 0:
                            # everything but brie, backstage pass, and sulfuras where quality is > 0
                            if item.name == "Conjured Mana Cake" and item.quality > 1:
                                # conjured mana cake with quality > 1 only
                                item.quality = item.quality - 2 
                            else:
                                # conjured mana cake where quality is 1, and everything but brie, backstage pass, and sulfuras where quality is > 0
                                item.quality = item.quality - 1
                                # !!! quality decremented "extra" point for being past sell_in
                    else:
                        # backstage pass only
                        item.quality = item.quality - item.quality # 'item.quality = 0' more intuitive? :)
                        # !!! backstage pass expired, no longer has value
                else:
                    # brie only
                    if item.quality < 50:
                        # quality is < 50
                        item.quality = item.quality + 1
                        # !!! quality incremented


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
