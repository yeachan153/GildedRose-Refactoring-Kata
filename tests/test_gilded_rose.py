from python.gilded_rose import GildedRose
from python.items import Item
from python.items_factory import ItemsFactory
from python.operations import increment_by_n, decrement_by_n


def get_item_brie(sell_in: int, quality: int):
    name = "Aged Brie"
    item = Item(name=name, sell_in=sell_in, quality=quality)
    created_item = ItemsFactory.create_item(text=name)
    increment_by_1 = increment_by_n(1)
    decrement_by_1 = decrement_by_n(1)
    item = [
        created_item(item=item, incrementor=increment_by_1, decrementor=decrement_by_1)
    ]
    return item


def get_item_backstage(sell_in: int, quality: int):
    name = "Backstage passes to a TAFKAL80ETC concert"
    item = Item(name=name, sell_in=sell_in, quality=quality)
    created_item = ItemsFactory.create_item(text=name)
    increment_by_1 = increment_by_n(1)
    decrement_by_1 = decrement_by_n(1)
    item = [
        created_item(item=item, incrementor=increment_by_1, decrementor=decrement_by_1)
    ]
    return item


def get_item_ragnaros(sell_in: int, quality: int):
    name = "Sulfuras, Hand of Ragnaros"
    item = Item(name=name, sell_in=sell_in, quality=quality)
    created_item = ItemsFactory.create_item(text=name)
    increment_by_1 = increment_by_n(1)
    decrement_by_1 = decrement_by_n(1)
    item = [
        created_item(item=item, incrementor=increment_by_1, decrementor=decrement_by_1)
    ]
    return item


def get_item_conjured(sell_in: int, quality: int):
    name = "Conjured"
    item = Item(name=name, sell_in=sell_in, quality=quality)
    created_item = ItemsFactory.create_item(text=name)
    increment_by_1 = increment_by_n(1)
    decrement_by_1 = decrement_by_n(1)
    item = [
        created_item(item=item, incrementor=increment_by_1, decrementor=decrement_by_1)
    ]
    return item


def update(item: list):
    gilded_rose = GildedRose(item)
    gilded_rose.update_quality()
    return gilded_rose


def test_brie_quality_normal():
    item = get_item_brie(sell_in=4, quality=4)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Aged Brie"
    assert gilded_rose.items[0].sell_in == 3
    assert gilded_rose.items[0].quality == 5


def test_brie_quality_2():
    item = get_item_brie(sell_in=-2, quality=4)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Aged Brie"
    assert gilded_rose.items[0].sell_in == -3
    assert gilded_rose.items[0].quality == 6


def test_brie_quality_max():
    item = get_item_brie(sell_in=-2, quality=50)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Aged Brie"
    assert gilded_rose.items[0].sell_in == -3
    assert gilded_rose.items[0].quality == 50


def test_stage_quality_normal():
    item = get_item_backstage(sell_in=11, quality=4)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Backstage passes to a TAFKAL80ETC concert"
    assert gilded_rose.items[0].sell_in == 10
    assert gilded_rose.items[0].quality == 5


def test_stage_quality_2():
    item = get_item_backstage(sell_in=9, quality=4)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Backstage passes to a TAFKAL80ETC concert"
    assert gilded_rose.items[0].sell_in == 8
    assert gilded_rose.items[0].quality == 6


def test_stage_quality_3():
    item = get_item_backstage(sell_in=5, quality=4)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Backstage passes to a TAFKAL80ETC concert"
    assert gilded_rose.items[0].sell_in == 4
    assert gilded_rose.items[0].quality == 7


def test_stage_quality_drop():
    item = get_item_backstage(sell_in=0, quality=20)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Backstage passes to a TAFKAL80ETC concert"
    assert gilded_rose.items[0].sell_in == -1
    assert gilded_rose.items[0].quality == 0


def test_stage_quality_max():
    item = get_item_backstage(sell_in=2, quality=50)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Backstage passes to a TAFKAL80ETC concert"
    assert gilded_rose.items[0].sell_in == 1
    assert gilded_rose.items[0].quality == 50


def test_sul_quality_normal():
    item = get_item_ragnaros(sell_in=2, quality=30)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Sulfuras, Hand of Ragnaros"
    assert gilded_rose.items[0].sell_in == 2
    assert gilded_rose.items[0].quality == 30


def test_sul_quality_max():
    item = get_item_ragnaros(sell_in=-1, quality=50)
    gilded_rose = update(item)
    assert gilded_rose.items[0].name == "Sulfuras, Hand of Ragnaros"
    assert gilded_rose.items[0].sell_in == -1
    assert gilded_rose.items[0].quality == 50
