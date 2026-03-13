import pytest

from users.models import User


@pytest.fixture
def test_user(db):
    """Создает тестового пользователя для использования в тестах"""

    user = User.objects.create(
        email="test@mailflow.pro",
        is_active=True
    )
    user.set_password("Qwerty12345!")
    user.save()
    return user


@pytest.fixture
def auth_client(client, test_user):
    """Возвращает клиента, который уже залогинен под нашим пользователем"""

    client.force_login(test_user)
    return client
