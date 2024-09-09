# test_api_utils.py

import pytest
from unittest.mock import patch
from api_utils import fetch_data

@patch('api_utils.requests.get')
def test_fetch_data(mock_get):
    # Define mock response data
    mock_get.return_value.json.return_value = {'key': 'value'}

    url = "http://test.com/api"
    result = fetch_data(url)

    # Assertions
    assert result == {'key': 'value'}
    mock_get.assert_called_once_with(url)