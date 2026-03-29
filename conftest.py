import pytest
import yaml
import os
from utils.api_client import APIClient


@pytest.fixture(scope="session")
def client():
    """Shared API client instance across all tests."""
    return APIClient()


@pytest.fixture(scope="session")
def config():
    """Load test config once per session."""
    config_path = os.path.join(os.path.dirname(__file__), 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def endpoints(config):
    return config['endpoints']


@pytest.fixture(scope="session")
def test_data(config):
    return config['test_data']
