# -*- coding: utf-8 -*-
from item import Item
from util import Color, assert_test_results


def test__item__daily_maintenance():
    test_cases = [        
        {
            "name": "typical item (-1 delta)",
            "actual": Item(name=None, sell_in=5, quality=25, quality_delta=-1),
            "expected": Item(name=None, sell_in=4, quality=24),
        },        
        {
            "name": "default delta",
            "actual": Item(name=None, sell_in=5, quality=25),
            "expected": Item(name=None, sell_in=4, quality=24),
        },
        {
            "name": "aged item (1 delta)",
            "actual": Item(name=None, sell_in=5, quality=25, quality_delta=1),
            "expected": Item(name=None, sell_in=4, quality=26),
        },
        {
            "name": "zero delta",
            "actual": Item(name=None, sell_in=5, quality=25, quality_delta=0),
            "expected": Item(name=None, sell_in=4, quality=25),
        },
        {
            "name": "zero sell_in (-1 delta)",
            "actual": Item(name=None, sell_in=0, quality=25, quality_delta=-1),
            "expected": Item(name=None, sell_in=-1, quality=23),
        },
        {
            "name": "zero sell_in (-2 delta)",
            "actual": Item(name=None, sell_in=0, quality=25, quality_delta=-2),
            "expected": Item(name=None, sell_in=-1, quality=21),
        },
        {
            "name": "negative sell_in (-1 delta)",
            "actual": Item(name=None, sell_in=-3, quality=25, quality_delta=-1),
            "expected": Item(name=None, sell_in=-4, quality=23),
        },
        {
            "name": "negative sell_in (-2 delta)",
            "actual": Item(name=None, sell_in=-3, quality=25, quality_delta=-2),
            "expected": Item(name=None, sell_in=-4, quality=21),
        },
        {
            "name": "evergreen",
            "actual": Item(name=None, sell_in=5, quality=25, quality_delta=-1, evergreen=True),
            "expected": Item(name=None, sell_in=5, quality=24),
        },        
        {
            "name": "perishing soon",
            "actual": Item(name=None, sell_in=1, quality=25, quality_delta=1, perishable=True),
            "expected": Item(name=None, sell_in=0, quality=26),
        },
        {
            "name": "perishing",
            "actual": Item(name=None, sell_in=0, quality=25, quality_delta=1, perishable=True),
            "expected": Item(name=None, sell_in=-1, quality=0),
        },
        {
            "name": "perished (default delta)",
            "actual": Item(name=None, sell_in=-1, quality=0, perishable=True),
            "expected": Item(name=None, sell_in=-2, quality=0),
        },
        {
            "name": "perished (-2 delta)",
            "actual": Item(name=None, sell_in=-1, quality=0, quality_delta=-2, perishable=True),
            "expected": Item(name=None, sell_in=-2, quality=0),
        },
        {
            "name": "Backstage passes (15 day sell_in)",
            "actual": Item(name=None, sell_in=15, quality=25, quality_delta=1, perishable=True),
            "expected": Item(name=None, sell_in=14, quality=26),
        },
        {
            "name": "Backstage passes (10 day sell_in)",
            "actual": Item(name=None, sell_in=10, quality=25, quality_delta=1, perishable=True),
            "expected": Item(name=None, sell_in=9, quality=27),
        },
        {
            "name": "Backstage passes (5 day sell_in)",
            "actual": Item(name=None, sell_in=5, quality=25, quality_delta=1, perishable=True),
            "expected": Item(name=None, sell_in=4, quality=28),
        },
        # outside specifications: worth mentioning? currently clamped
        {
            "name": "starting quality above upper boundary",
            "actual": Item(name=None, sell_in=5, quality=75),
            "expected": Item(name=None, sell_in=4, quality=50)
        },
        {
            "name": "starting quality below lower boundary",
            "actual": Item(name=None, sell_in=5, quality=-75),
            "expected": Item(name=None, sell_in=4, quality=0)
        }
    ]

    successes = []
    failures = []
    for test_case in test_cases:
        name, actual, expected = test_case.values()
        # Set test case name into item names
        for target in [actual, expected]:
            setattr(target, "name", Color.CYAN + name + Color.END)            
        
        actual.daily_maintenance()
        try:
            assert actual == expected
            successes.append(f"{Color.GREEN}pass{Color.END}: {Color.YELLOW}{name}{Color.END} (expected: {expected.sell_in}, {expected.quality})")
        except:
            failures.append(f"{Color.RED}FAIL{Color.END}: {Color.YELLOW}{name}{Color.END} (actual: {actual.sell_in}, {actual.quality}. expected: {expected.sell_in}, {expected.quality})")        

    assert_test_results(successes, failures)


if __name__ == "__main__":
    test__item__daily_maintenance()
    
