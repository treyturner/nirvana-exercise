# -*- coding: utf-8 -*-
from util import apply_delta


class Item:
    def __init__(self, name, sell_in, quality, quality_delta=-1, perishable=False, evergreen=False):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality
        # daily change in quality (positive or negative)
        self.quality_delta = quality_delta 
        # True will set quality to 0 once sell_in is negative
        self.perishable = perishable 
        # True will cause sell_in to not decrement
        self.evergreen = evergreen 

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def __eq__(self, other):
        if isinstance(other, Item):            
            for key in ["name", "sell_in", "quality"]:
                if getattr(self, key) != getattr(other, key):
                    return False
            return True
        else:
            return NotImplemented        

    def update_quality(self, delta=None):
        # Applies a delta to quality, ensuring the result stays within bounds.        
        # Use quality_delta if one isn't supplied.
        delta = delta if delta is not None else self.quality_delta
        self.quality = apply_delta(self.quality, delta, 0, 50)

    def daily_maintenance(self):
        # Currently, sell_in and quality are modified based on business rules.
        # Generally, sell_in is reduced by 1 (day), and quality is modified by
        # quality_delta (default -1). Once sell_in is negative, quality
        # deterioration doubles, or in some cases may immediately become zero.

        if self.quality_delta != 0:            
            self.update_quality()

            # special handling for backstage passes
            if "Backstage pass" in self.name:
                if self.sell_in < 11:
                    demand_adj = 2 if self.sell_in < 6 else 1
                    self.update_quality(demand_adj)

        if not self.evergreen:                
            self.sell_in -= 1

            # handle negative sell_in
            if self.sell_in < 0:
                if self.perishable:
                    self.quality = 0
                else:
                    # it's super effective!
                    self.update_quality()

        return self            
