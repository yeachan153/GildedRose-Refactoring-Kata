def decrease_quality_normal(item):
    """Decreases quality of normal
    items.

    Args:
        item ([type]): item object
    """
    modified = False
    if (
        item.name != "Aged Brie"
        and item.name != "Backstage passes to a TAFKAL80ETC concert"
    ):
        modified = True
        if item.quality > 0:
            if item.name != "Sulfuras, Hand of Ragnaros":
                item.quality = degrade_quality(item)
    return item, modified


def degrade_quality(item):
    if item.name == "Conjured":
        return item.quality - 2
    else:
        return item.quality - 1


def increase_item_quality_special(item):
    if item.quality < 50:
        item.quality = item.quality + 1
        if item.name == "Backstage passes to a TAFKAL80ETC concert":
            if item.sell_in < 11:
                if item.quality < 50:
                    item.quality = item.quality + 1
            if item.sell_in < 6:
                if item.quality < 50:
                    item.quality = item.quality + 1
    return item


def decrease_sell_in(item):
    if item.name != "Sulfuras, Hand of Ragnaros":
        item.sell_in = item.sell_in - 1
    return item


def negative_sell_action(item):
    if item.name != "Aged Brie":
        if item.name != "Backstage passes to a TAFKAL80ETC concert":
            if item.quality > 0:
                if item.name != "Sulfuras, Hand of Ragnaros":
                    item.quality = item.quality - 1
        else:
            item.quality = item.quality - item.quality
    else:
        if item.quality < 50:
            item.quality = item.quality + 1
    return item
