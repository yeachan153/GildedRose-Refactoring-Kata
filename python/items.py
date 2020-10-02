import attr
from attr import validators
from typing import Callable, Union


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)


@attr.s(frozen=True)
class AgedBrieItem(Item):
    item: Item = attr.ib(validator=[attr.validators.instance_of(Item)])
    incrementor: Callable[[Union[int, float]], Union[int, float]] = attr.ib(
        validators.is_callable()
    )
    decrementor: Callable[[Union[int, float]], Union[int, float]] = attr.ib(
        validators.is_callable()
    )

    @property
    def name(self) -> str:
        return self.item.name

    @property
    def sell_in(self) -> int:
        return self.item.sell_in

    @property
    def quality(self) -> int:
        return self.item.quality

    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality = self.incrementor(self.item.quality)
        self.item.sell_in = self.decrementor(self.item.sell_in)
        if self.item.sell_in < 0:
            if self.item.quality < 50:
                self.item.quality = self.incrementor(self.item.quality)
        return self.item


@attr.s(frozen=True)
class BackStageItem(Item):
    item: Item = attr.ib(validator=[attr.validators.instance_of(Item)])
    incrementor: Callable[[Union[int, float]], Union[int, float]] = attr.ib(
        validators.is_callable()
    )
    decrementor: Callable[[Union[int, float]], Union[int, float]] = attr.ib(
        validators.is_callable()
    )

    @property
    def name(self) -> str:
        return self.item.name

    @property
    def sell_in(self) -> int:
        return self.item.sell_in

    @property
    def quality(self) -> int:
        return self.item.quality

    def update_quality(self):
        if self.item.quality < 50:
            self.item.quality = self.incrementor(self.item.quality)
            if self.item.sell_in < 11:
                if self.item.quality < 50:
                    self.item.quality = self.incrementor(self.item.quality)
            if self.item.sell_in < 6:
                if self.item.quality < 50:
                    self.item.quality = self.incrementor(self.item.quality)
        self.item.sell_in = self.decrementor(self.item.sell_in)
        if self.item.sell_in < 0:
            self.item.quality = 0
        return self.item


@attr.s(frozen=True)
class RagnarosItem(Item):
    item: Item = attr.ib(validator=[attr.validators.instance_of(Item)])
    incrementor: Callable[[Union[int, float]], Union[int, float]] = attr.ib(
        validators.is_callable()
    )
    decrementor: Callable[[Union[int, float]], Union[int, float]] = attr.ib(
        validators.is_callable()
    )

    @property
    def name(self) -> str:
        return self.item.name

    @property
    def sell_in(self) -> int:
        return self.item.sell_in

    @property
    def quality(self) -> int:
        return self.item.quality

    def update_quality(self):
        return self.item


@attr.s(frozen=True)
class ConjuredItem(Item):
    item: Item = attr.ib(validator=[attr.validators.instance_of(Item)])
    incrementor: Callable[[Union[int, float]], Union[int, float]] = attr.ib(
        validators.is_callable()
    )
    decrementor: Callable[[Union[int, float]], Union[int, float]] = attr.ib(
        validators.is_callable()
    )

    @property
    def name(self) -> str:
        return self.item.name

    @property
    def sell_in(self) -> int:
        return self.item.sell_in

    @property
    def quality(self) -> int:
        return self.item.quality

    def update_quality(self):
        if self.item.quality > 0:
            self.item.quality = self.decrementor(self.decrementor(self.item.quality))
        self.item.sell_in = self.decrementor(self.item.sell_in)
        if self.item.sell_in < 0:
            if self.item.quality > 0:
                self.item.quality = self.decrementor(
                    self.decrementor(self.item.quality)
                )
        return self.item_quality
