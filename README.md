# Gilded Rose

Refactoring allowed me to express the shop's business logic more clearly and produced methods that are more testable.

`update_quality` was renamed to [`daily_maintenance`](gilded_rose/item.py#L35) and moved into the [`Item` class](gilded_rose/item.py#L5), since it's only concerned with properties within a single instance. This simplified the [`GildedRose` class](gilded_rose/gilded_rose.py#L2) such that it doesn't currently require testing.

I replaced the unwieldy component test which tracked many scenarios across multiple days using a single point of failure with discrete test cases around two methods: [`Item.daily_maintenance`](gilded_rose/item.py#L35) and a reusable method `apply_delta` which was extracted into [`util.py`](gilded_rose/util.py). After a bit of thought I was able to refactor `apply_delta` into [just one line](gilded_rose/util.py#L19) (so say the tests!), but I left [the original](gilded_rose/util.py#L5) in so you can see how it developed.

`Item.daily_maintenance` now has the following [18 test cases](gilded_rose/item.test.py#L7):
```
typical item (-1 delta)
default delta
aged item (1 delta)
zero delta
zero sell_in (-1 delta)
zero sell_in (-2 delta)
negative sell_in (-1 delta)
negative sell_in (-2 delta)
evergreen
expiring soon
expiring
expired (default delta)
expired (-2 delta)
Backstage passes (15 day sell_in)
Backstage passes (10 day sell_in)
Backstage passes (5 day sell_in)

# outside specifications: currently clamped
starting quality above upper boundary
starting quality below lower boundary
```

85 cases were created for `util.apply_delta`. For these [5 boundaries](gilded_rose/util.test.py#L39):

```
(-100, -50)
(-50, 0)
(-50, 50)
(0, 50)
(50, 100)
```

These [17 cases](gilded_rose/util.test.py#L8) are run:

```
# mid range
-5 delta
-1 delta
0 delta
1 delta
5 delta

# low boundary
low boundary achieved: -2 delta
low boundary achieved: -1 delta
low boundary isn't crossed: -2 delta
low boundary isn't crossed: -1 delta
low boundary isn't crossed: 0 delta
low boundary recovery: 1 delta

# high boundary
high boundary achieved: 2 delta
high boundary achieved: 1 delta
high boundary isn't crossed: 2 delta
high boundary isn't crossed: 1 delta
high boundary isn't crossed: 0 delta
high boundary recovery: -1 delta
```

I stopped short of implementing a proper test framework because there are nuanced options from which to choose, but I took a little time to improve the test runners in each test file.

- They now run all tests instead of bailing on the first error
- Output is colorized
- Any failures are focused in the output (including actual & expected values)
- Successes are shown if there weren't any failures (including expected values)

Thank you again for your time and consideration! I'm really excited about the prospect of building with the team.

Regards,

Trey
