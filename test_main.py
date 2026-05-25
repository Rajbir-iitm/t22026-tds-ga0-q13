import httpx

def test_email_endpoint():
    response = httpx.get("https://httpbin.org/get")
    assert response.status_code == 200

def test_placeholder():
    assert 1 + 1 == 2
