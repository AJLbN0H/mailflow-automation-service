import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestUsers:
    def test_user_str(self, test_user):
        assert str(test_user) == "test@mailflow.pro"

    def test_profile_redirect_for_anonymous(self, client, test_user):
        url = reverse("users:user_update", kwargs={"pk": test_user.pk})
        response = client.get(url)
        assert response.status_code == 302

    def test_profile_access_for_auth_user(self, auth_client, test_user):
        url = reverse("users:user_update", kwargs={"pk": test_user.pk})
        response = auth_client.get(url)
        assert response.status_code == 200
