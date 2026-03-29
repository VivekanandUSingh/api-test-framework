import pytest


class TestLogin:
    """Test suite for POST /login endpoint."""

    def test_valid_login_returns_200(self, client, endpoints, test_data):
        """Verify valid credentials return HTTP 200."""
        response = client.post(endpoints['login'], payload=test_data['valid_user'])
        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

    def test_valid_login_returns_token(self, client, endpoints, test_data):
        """Verify successful login returns an auth token."""
        response = client.post(endpoints['login'], payload=test_data['valid_user'])
        body = response.json()
        assert "token" in body, "Login response missing 'token'"
        assert len(body["token"]) > 0, "Token should not be empty"

    def test_invalid_login_returns_400(self, client, endpoints, test_data):
        """Verify invalid credentials return HTTP 400."""
        response = client.post(endpoints['login'], payload=test_data['invalid_user'])
        assert response.status_code == 400, \
            f"Expected 400 but got {response.status_code}"

    def test_invalid_login_returns_error_message(self, client, endpoints, test_data):
        """Verify failed login returns a meaningful error message."""
        response = client.post(endpoints['login'], payload=test_data['invalid_user'])
        body = response.json()
        assert "error" in body, "Failed login should return an 'error' field"
        assert len(body["error"]) > 0, "Error message should not be empty"

    def test_login_missing_password_returns_400(self, client, endpoints):
        """Verify login with missing password returns HTTP 400."""
        payload = {"email": "eve.holt@reqres.in"}
        response = client.post(endpoints['login'], payload=payload)
        assert response.status_code == 400

    def test_login_missing_email_returns_400(self, client, endpoints):
        """Verify login with missing email returns HTTP 400."""
        payload = {"password": "pistol"}
        response = client.post(endpoints['login'], payload=payload)
        assert response.status_code == 400


class TestRegister:
    """Test suite for POST /register endpoint."""

    def test_valid_registration_returns_200(self, client, endpoints, test_data):
        """Verify valid registration returns HTTP 200."""
        response = client.post(endpoints['register'], payload=test_data['valid_user'])
        assert response.status_code == 200

    def test_valid_registration_returns_token(self, client, endpoints, test_data):
        """Verify successful registration returns a token."""
        response = client.post(endpoints['register'], payload=test_data['valid_user'])
        body = response.json()
        assert "token" in body, "Registration should return a token"

    def test_valid_registration_returns_id(self, client, endpoints, test_data):
        """Verify successful registration returns a user ID."""
        response = client.post(endpoints['register'], payload=test_data['valid_user'])
        body = response.json()
        assert "id" in body, "Registration should return an ID"

    def test_registration_missing_password_returns_400(self, client, endpoints):
        """Verify registration without password returns HTTP 400."""
        payload = {"email": "eve.holt@reqres.in"}
        response = client.post(endpoints['register'], payload=payload)
        assert response.status_code == 400

    def test_registration_returns_error_for_unknown_user(self, client, endpoints):
        """Verify registration for unknown email returns error message."""
        payload = {"email": "unknown@test.com", "password": "test123"}
        response = client.post(endpoints['register'], payload=payload)
        body = response.json()
        assert "error" in body
