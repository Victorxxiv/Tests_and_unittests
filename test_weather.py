# test_weather.py
from unittest.mock import patch
from .weather import get_weather

@patch('weather.requests.get')
def test_get_weather(mock_get):
    mock_get.return_value.json.return_value = {"temperature": "20°C"}

    result = get_weather("London")

    assert result == {"temperature": "20°C"}
    mock_get.assert_called_once_with("http://api.weather.com/London")