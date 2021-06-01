from enum import Enum
from typing import Any, Dict, List

from pydantic import BaseModel


class CategoryEnum(str, Enum):  # noqa: WPS600
    entertainment = 'entertainment'
    food_dining = 'food_dining'
    gas_transport = 'gas_transport'
    grocery_net = 'grocery_net'
    grocery_pos = 'grocery_pos'
    health_fitness = 'health_fitness'
    home = 'home'
    kids_pets = 'kids_pets'
    misc_net = 'misc_net'
    misc_pos = 'misc_pos'
    personal_care = 'personal_care'
    shopping_net = 'shopping_net'
    shopping_pos = 'shopping_pos'
    travel = 'travel'

    def get_index(self) -> int:
        return self.category_index()[self.value]

    @classmethod
    def category_index(cls) -> Dict[str, int]:
        return {
            'entertainment': 6,
            'food_dining': 7,
            'gas_transport': 8,
            'grocery_net': 9,
            'grocery_pos': 10,
            'health_fitness': 11,
            'home': 12,
            'kids_pets': 13,
            'misc_net': 14,
            'misc_pos': 15,
            'personal_care': 16,
            'shopping_net': 17,
            'shopping_pos': 18,
            'travel': 19,
        }


class PaymentSchema(BaseModel):
    amount: float
    lat: float
    long: float
    merch_lat: float
    merchant_long: float
    age: int
    category: CategoryEnum

    def to_model_list(self) -> List[Any]:
        """Convert `PaymentSchema` to a model scoring list.

        For example::

            { "amount": 101.10, "lat": 22.2, "long": 22.2, "merch_lat": 33.0,
                "merchant_long": 33.0, "age": 55, "category": "entertainment" }

        Would return::
            [101.10, 22.2, 22.2, 33.0, 33.0, 55,
                1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        Where `1` in the list is for the `category` being `entertainment`.
        If the `category` was `travel` then the list would be::

            [101.10, 22.2, 22.2, 33.0, 33.0, 55,
                0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1]

        Returns:
            List[Any]: A scorable list.
        """
        feature_false, feature_true = 0, 1

        model_list = [
            self.amount,
            self.lat,
            self.long,
            self.merch_lat,
            self.merchant_long,
            self.age,
        ]
        model_list.extend(
            feature_false for _, _ in enumerate(
                CategoryEnum.category_index(),
            )
        )
        model_list[self.category.get_index()] = feature_true

        return model_list
