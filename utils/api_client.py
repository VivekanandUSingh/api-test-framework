import requests
import yaml
import os


def load_config():
    config_path = os.path.join(os.path.dirname(__file__), '..', 'config', 'config.yaml')
    with open(config_path, 'r') as f:
        return yaml.safe_load(f)


config = load_config()
BASE_URL = config['base_url']
TIMEOUTS = (config['timeouts']['connect'], config['timeouts']['read'])


class APIClient:
    """
    Reusable API client wrapping requests library.
    Handles base URL, headers, timeouts, and response logging.
    """

    def __init__(self):
        self.base_url = BASE_URL
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Accept": "application/json",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        })

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.get(url, params=params, timeout=TIMEOUTS)
        self._log_response(response)
        return response

    def post(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.post(url, json=payload, timeout=TIMEOUTS)
        self._log_response(response)
        return response

    def put(self, endpoint, payload=None):
        url = f"{self.base_url}{endpoint}"
        response = self.session.put(url, json=payload, timeout=TIMEOUTS)
        self._log_response(response)
        return response

    def delete(self, endpoint):
        url = f"{self.base_url}{endpoint}"
        response = self.session.delete(url, timeout=TIMEOUTS)
        self._log_response(response)
        return response

    def _log_response(self, response):
        print(f"\n{'='*50}")
        print(f"URL     : {response.url}")
        print(f"Method  : {response.request.method}")
        print(f"Status  : {response.status_code}")
        print(f"Time    : {response.elapsed.total_seconds():.3f}s")
        try:
            print(f"Response: {response.json()}")
        except Exception:
            print(f"Response: {response.text}")
        print(f"{'='*50}")
