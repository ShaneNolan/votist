from typing import Any, Dict

import pytest
from httpx import AsyncClient

from tests.mocks import get_mock_fraud_model
from votist.main import app
from votist.services.fraud_model import get_fraud_model

app.dependency_overrides[get_fraud_model] = get_mock_fraud_model


@pytest.mark.asyncio
@pytest.mark.parametrize(
    'transaction,is_fraud', [
        (
            {
                'amount': 0,
                'lat': 0,
                'long': 0,
                'merch_lat': 0,
                'merchant_long': 0,
                'age': 0,
                'category': 'entertainment',
            },
            False,
        ),
        (
            {
                'amount': 10000,
                'lat': 0,
                'long': 0,
                'merch_lat': 0,
                'merchant_long': 0,
                'age': 0,
                'category': 'entertainment',
            },
            True,
        ),
    ],
)
async def test_api_predict(
    base_url: str,
    transaction: Dict[str, Any],
    is_fraud: bool,
):
    status_code_success = 200

    async with AsyncClient(app=app, base_url=base_url) as ac:
        response = await ac.post('/predict', json=transaction)

    assert response.status_code == status_code_success
    assert response.json() == {'fraudulent': is_fraud}
