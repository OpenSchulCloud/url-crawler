"""Test that the test cases work.
"""
import requests

def test_server_is_available(base_url):
    """Make sure the bottle server is started."""
    response = requests.get(base_url)
    assert response.status_code == 404

def test_url_starts_with_source_server_url(base_url, resource_url):
    """The resource url should be in the bottle server."""
    assert resource_url.startswith(base_url)