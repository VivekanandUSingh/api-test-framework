import pytest


class TestGetUsers:
    """Test suite for GET /users endpoint."""

    def test_get_users_status_code(self, client, endpoints):
        """Verify users list returns HTTP 200."""
        response = client.get(endpoints['users'])
        assert response.status_code == 200, \
            f"Expected 200 but got {response.status_code}"

    def test_get_users_returns_list(self, client, endpoints):
        """Verify response contains a data array."""
        response = client.get(endpoints['users'])
        body = response.json()
        assert "data" in body, "Response missing 'data' key"
        assert isinstance(body["data"], list), "'data' should be a list"
        assert len(body["data"]) > 0, "Users list should not be empty"

    def test_get_users_page_param(self, client, endpoints):
        """Verify pagination returns correct page number."""
        response = client.get(endpoints['users'], params={"page": 2})
        body = response.json()
        assert body["page"] == 2, f"Expected page 2 but got {body['page']}"

    def test_get_users_response_schema(self, client, endpoints):
        """Verify each user object has required fields."""
        response = client.get(endpoints['users'])
        users = response.json()["data"]
        required_fields = {"id", "email", "first_name", "last_name", "avatar"}
        for user in users:
            missing = required_fields - user.keys()
            assert not missing, f"User missing fields: {missing}"

    def test_get_single_user(self, client, endpoints):
        """Verify single user fetch returns correct ID."""
        response = client.get(f"{endpoints['users']}/2")
        assert response.status_code == 200
        body = response.json()
        assert body["data"]["id"] == 2

    def test_get_nonexistent_user_returns_404(self, client, endpoints):
        """Verify fetching unknown user returns HTTP 404."""
        response = client.get(f"{endpoints['users']}/9999")
        assert response.status_code == 404, \
            f"Expected 404 for unknown user but got {response.status_code}"

    def test_response_time_under_threshold(self, client, endpoints):
        """Verify API responds within 3 seconds."""
        response = client.get(endpoints['users'])
        elapsed = response.elapsed.total_seconds()
        assert elapsed < 3.0, f"Response too slow: {elapsed:.3f}s"


class TestCreateUser:
    """Test suite for POST /users endpoint."""

    def test_create_user_status_code(self, client, endpoints, test_data):
        """Verify user creation returns HTTP 201."""
        response = client.post(endpoints['users'], payload=test_data['new_user'])
        assert response.status_code == 201, \
            f"Expected 201 but got {response.status_code}"

    def test_create_user_returns_id(self, client, endpoints, test_data):
        """Verify newly created user has an ID assigned."""
        response = client.post(endpoints['users'], payload=test_data['new_user'])
        body = response.json()
        assert "id" in body, "Created user should have an 'id'"
        assert body["id"] is not None

    def test_create_user_returns_correct_name(self, client, endpoints, test_data):
        """Verify created user name matches request payload."""
        response = client.post(endpoints['users'], payload=test_data['new_user'])
        body = response.json()
        assert body["name"] == test_data['new_user']['name']

    def test_create_user_returns_correct_job(self, client, endpoints, test_data):
        """Verify created user job matches request payload."""
        response = client.post(endpoints['users'], payload=test_data['new_user'])
        body = response.json()
        assert body["job"] == test_data['new_user']['job']

    def test_create_user_returns_timestamp(self, client, endpoints, test_data):
        """Verify created user response includes a createdAt timestamp."""
        response = client.post(endpoints['users'], payload=test_data['new_user'])
        body = response.json()
        assert "createdAt" in body, "Response should include createdAt timestamp"
