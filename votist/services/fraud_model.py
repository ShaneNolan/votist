from typing import Any, List

from joblib import load as joblib_load


class FraudModel:

    def __new__(cls):
        attribute_instance = 'instance'

        if not hasattr(cls, attribute_instance):  # noqa: WPS421
            cls.instance = super().__new__(cls)

        return cls.instance

    def __init__(self):
        self._model = joblib_load('model.joblib')

    def score(self, encoded_payment: List[Any]) -> int:
        index_result = 0

        return self._model.predict([encoded_payment])[index_result]


_fraud_model = FraudModel()


async def get_fraud_model() -> FraudModel:
    return _fraud_model
