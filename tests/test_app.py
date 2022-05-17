def test_request_about(client):
    response = client.get("/about/")
    assert b"About page for the Visual Studio Code Flask tutorial" in response.data