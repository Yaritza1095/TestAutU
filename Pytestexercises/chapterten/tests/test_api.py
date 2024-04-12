import pytest
import requests

@pytest.mark.api
@pytest.mark.duckduckgo
def test_duckduckgo_instant_answer_api():

  # Arrange
  url = 'https://api.duckduckgo.com/?q=python+programming&format=json'

  # Act
  response = requests.get(url)
  body = response.json()

  # Assert
  assert response.status_code == 200
  assert 'Python' in body['AbstractText']




