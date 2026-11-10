
import requests

API_BASE_URL = "http://127.0.0.1:8000"


def get_health():
    try:
        response = requests.get(
            f"{API_BASE_URL}/api/health",
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None


def get_dashboard_stats():
    try:
        response = requests.get(
            f"{API_BASE_URL}/api/dashboard/stats",
            timeout=5
        )
        response.raise_for_status()
        return response.json()
    except requests.RequestException:
        return None
