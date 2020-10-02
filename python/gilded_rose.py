from python.items_utils import (
    decrease_quality_normal,
    increase_item_quality_special,
    decrease_sell_in,
    negative_sell_action,
)


class GildedRose(object):
    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item, modified = decrease_quality_normal(item)
            if modified is False:
                item = increase_item_quality_special(item)
            item = decrease_sell_in(item)
            if item.sell_in < 0:
                item = negative_sell_action(item)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
