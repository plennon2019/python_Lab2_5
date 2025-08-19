def test_get_users_initially_empty(client):
    r = client.get('/api/users')
    assert r.status_code == 200
    assert r.json() == []

def test_post_user(client):
    user = {'user_id': 1, 'name': 'Mary', 'email': 'mary@atu.ie', 'age': 22}
    r = client.post('/api/users', json=user)
    assert r.status_code == 201
    body = r.json()
    assert body['name'] == 'Mary'
    assert body['user_id'] == 1
