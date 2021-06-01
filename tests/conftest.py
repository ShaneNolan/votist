from os import getenv

import pytest


@pytest.fixture
def base_url() -> str:
    return getenv('BASE_URL', 'http://127.0.0.1:8000/api/v1')
