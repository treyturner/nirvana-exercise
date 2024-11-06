# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import GildedRose
from item import Item

if __name__ == "__main__":
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=1, quality=0, quality_delta=1),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Elixir of the Mongoose", sell_in=1, quality=5),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=10, quality=30, quality_delta=0, evergreen=True),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80, quality_delta=0, evergreen=True),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80, quality_delta=0, evergreen=True),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20, quality_delta=1, perishable=True),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49, quality_delta=1, perishable=True),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49, quality_delta=1, perishable=True),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6, quality_delta=-2),  # <-- :O
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):
        print("-------- day %s --------" % day)
        print("name, sellIn, quality")
        for item in items:
            print(item)
        print("")
        GildedRose(items).daily_maintenance()
