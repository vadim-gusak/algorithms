from algorithms.bubble_sort import sort_by_score
import pytest

sorted_users = [
    {'username': 'Theodore', 'score': 500001},
    {'username': 'Harper', 'score': 500000},
    {'username': 'Charlotte', 'score': 201000},
    {'username': 'Noah', 'score': 150000},
    {'username': 'Amelia', 'score': 100500},
    {'username': 'Bob', 'score': 95000},
    {'username': 'Mia', 'score': 55000},
    {'username': 'Lucas', 'score': 3000},
    {'username': 'Zoidberg', 'score': 1000},
    {'username': 'Sophia', 'score': 750},
    {'username': 'Olivia', 'score': 661},
    {'username': 'Isabella', 'score': 660},
    {'username': 'James', 'score': 11},
    {'username': 'Emma', 'score': 1}
]

sorted_users_reverse = [
    {'username': 'Emma', 'score': 1},
    {'username': 'James', 'score': 11},
    {'username': 'Isabella', 'score': 660},
    {'username': 'Olivia', 'score': 661},
    {'username': 'Sophia', 'score': 750},
    {'username': 'Zoidberg', 'score': 1000},
    {'username': 'Lucas', 'score': 3000},
    {'username': 'Mia', 'score': 55000},
    {'username': 'Bob', 'score': 95000},
    {'username': 'Amelia', 'score': 100500},
    {'username': 'Noah', 'score': 150000},
    {'username': 'Charlotte', 'score': 201000},
    {'username': 'Harper', 'score': 500000},
    {'username': 'Theodore', 'score': 500001},
]


@pytest.fixture
def users():
    users = [
        {'username': 'Amelia', 'score': 100500},
        {'username': 'Bob', 'score': 95000},
        {'username': 'Charlotte', 'score': 201000},
        {'username': 'Emma', 'score': 1},
        {'username': 'Olivia', 'score': 661},
        {'username': 'Harper', 'score': 500000},
        {'username': 'Isabella', 'score': 660},
        {'username': 'James', 'score': 11},
        {'username': 'Lucas', 'score': 3000},
        {'username': 'Mia', 'score': 55000},
        {'username': 'Noah', 'score': 150000},
        {'username': 'Sophia', 'score': 750},
        {'username': 'Theodore', 'score': 500001},
        {'username': 'Zoidberg', 'score': 1000}
    ]
    return users


def test_sort_by_score(users):
    result = sort_by_score(users)
    assert result == sorted_users


def test_sort_by_score_revers(users):
    result = sort_by_score(users, reverse=True)
    assert result == sorted_users_reverse


def test_sort_by_score_empty_list():
    result = sort_by_score([])
    assert result == []