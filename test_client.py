def test_get(api):
    r = api.get("/get")
    assert r.status_code == 200

def test_args(api):
    r = api.get("/get", params={"a": "1"})
    # print(r.json())
    assert r.json()["args"] == {"a": "1"}

def test_token_sent(api):
    r = api.get("/get")
    print(r.json())
    assert r.json()["headers"]["Authorization"] == "Bearer ken"  