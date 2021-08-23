import pytest
from app.db import get_db


@pytest.mark.parametrize('path', (
    '/2/update',
    '/2/delete',
))
def test_exists_required(client, path):
    assert client.post(path).status_code == 404

def test_create(client, app):
    assert client.get('/customers/create').status_code == 200
    client.post('/customers/create', data={ 'cust_number': '22',
                                            'name': 'Arne', 
                                            'address': 'roadhouse',
                                            'postal_number': '123 45',
                                            'postal_address': 'Lilla Byn'
                                            })

    with app.app_context():
        db = get_db()
        count = db.execute('SELECT COUNT(id) FROM customer').fetchone()[0]
        assert count == 2


# def test_update(client, app):
#     assert client.get('/1/update').status_code == 200
#     client.post('/1/update', data={'title': 'updated', 'body': ''})

#     with app.app_context():
#         db = get_db()
#         post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
#         assert post['title'] == 'updated'


# @pytest.mark.parametrize('path', (
#     '/create',
#     '/1/update',
# ))
# def test_create_update_validate(client, path):
#     response = client.post(path, data={'title': '', 'body': ''})
#     assert b'Title is required.' in response.data

# def test_delete(client, app):
#     response = client.post('/1/delete')
#     assert response.headers['Location'] == 'http://localhost/'

#     with app.app_context():
#         db = get_db()
#         post = db.execute('SELECT * FROM post WHERE id = 1').fetchone()
#         assert post is None