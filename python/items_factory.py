from python.items import AgedBrieItem, BackStageItem, RagnarosItem, ConjuredItem
from python.exceptions import InvalidRepositoryException
from typing import Union


class ItemsFactory:
    """Generates correct item objects
    based on specified parameter
    """

    @staticmethod
    def create_item(
        text: str,
    ) -> Union[AgedBrieItem, BackStageItem, RagnarosItem, ConjuredItem]:
        """Creates correct item

        Args:
            text (str): [description]

        Returns:
            Item: [description]
        """
        if text == "Aged Brie":
            return AgedBrieItem
        elif text == "Backstage passes to a TAFKAL80ETC concert":
            return BackStageItem
        elif text == "Sulfuras, Hand of Ragnaros":
            return RagnarosItem
        elif text == "Conjured":
            return ConjuredItem
        else:
            raise InvalidRepositoryException(
                f"Repository of type {text} does not exist."
            )
