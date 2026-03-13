from datetime import timedelta

import pytest
from django.urls import reverse
from django.utils import timezone

from mailings.models import Newsletter, Message


@pytest.fixture
def test_message(test_user):
    """Создаем тестовое сообщение с полями topic и content"""

    return Message.objects.create(
        topic="Тема сообщения",
        content="Текст сообщения",
        owner=test_user
    )


@pytest.fixture
def test_newsletter(test_user, test_message):
    """Создаем рассылку со всеми обязательными полями для БД"""

    now = timezone.now()
    return Newsletter.objects.create(
        message=test_message,
        status="created",  # Техническое имя из твоего choices
        sending_date=now,  # Исправляем NotNullViolation
        end_date_of_send=now + timedelta(days=1),  # Исправляем NotNullViolation
        owner=test_user
    )


@pytest.mark.django_db
class TestMailings:
    def test_newsletter_list_authorized(self, auth_client):
        url = reverse("mailings:newsletter_list")
        response = auth_client.get(url)
        assert response.status_code == 200

    def test_newsletter_creation_logic(self, test_newsletter):
        assert test_newsletter.status == "created"
        assert Newsletter.objects.count() == 1

    def test_newsletter_unauthorized_access(self, client):
        """Проверка редиректа для анонима (код 302)"""

        url = reverse("mailings:newsletter_list")
        response = client.get(url)
        assert response.status_code == 302
