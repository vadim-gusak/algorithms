from algorithms.binary_search import search

phone_book = [
    {'name': 'Amelia', 'number': '99-999-99'},
    {'name': 'Bob', 'number': '98-989-98'},
    {'name': 'Charlotte', 'number': '89-898-89'},
    {'name': 'Emma', 'number': '78-789-78'},
    {'name': 'Harper', 'number': '77-777-77'},
    {'name': 'Isabella', 'number': '67-678-67'},
    {'name': 'James', 'number': '66-666-66'},
    {'name': 'Lucas', 'number': '52-546-13'},
    {'name': 'Mia', 'number': '55-546-55'},
    {'name': 'Noah', 'number': '91-111-19'},
    {'name': 'Olivia', 'number': '42-999-42'},
    {'name': 'Sophia', 'number': '33-333-33'},
    {'name': 'Theodore', 'number': '22-222-22'},
    {'name': 'Zoidberg', 'number': '01-001-01'}
]


def test_search():
    result = search(phone_book, 'Theodore')
    assert result == '22-222-22'


def test_search_phonebook_is_empty():
    result = search([], 'Theodore')
    assert result == 'Phonebook is empty!'


def test_search_not_found():
    result = search(phone_book, 'Gordon')
    assert result == 'Name not found!'
