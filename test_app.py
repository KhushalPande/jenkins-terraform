from app import app


def client():
    app.config["TESTING"] = True
    return app.test_client()


def test_health_endpoint():
    r = client().get("/health")
    assert r.status_code == 200
    assert r.get_json()["status"] == "ok"


def test_home_page():
    r = client().get("/")
    assert r.status_code == 200
    assert b"Jenkins" in r.data


def test_add_valid_numbers():
    r = client().get("/api/add?a=2&b=3")
    assert r.status_code == 200
    assert r.get_json()["result"] == 5


def test_add_invalid_input():
    r = client().get("/api/add?a=x&b=3")
    assert r.status_code == 400
