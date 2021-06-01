from typing import Any, List


class MockFraudModel:
    def score(self, encoded_payment: List[Any]) -> int:
        """If the amount (index 0) is over 1000 then declare it as fraud.

        Args:
            encoded_payment (List[Any]): The encoded payment.

        Returns:
            int: 1 if fraud else 0 (not fraud).
        """
        is_fraud, not_fraud = 1, 0

        amount_index = 0
        flag_fraud_amount = 1000

        if encoded_payment[amount_index] > flag_fraud_amount:
            return is_fraud

        return not_fraud


async def get_mock_fraud_model() -> MockFraudModel:
    return MockFraudModel()
