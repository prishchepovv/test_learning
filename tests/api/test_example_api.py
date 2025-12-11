import pytest
@pytest.mark.api
def test_get_posts(api_session):
    """Проверяет успешный ответ от JSONPlaceholder API."""
    response = api_session.get("https://jsonplaceholder.typicode.com/posts/1")
    assert response.status_code == 200
    assert response.json()["id"] == 1