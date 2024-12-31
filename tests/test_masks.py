import pytest

from src.masks import get_mask_account, get_mask_card_number


@pytest.mark.parametrize("number, expected",
                         [(7000792289606361, '7000 79** **** 6361'),
                          (700079, 'Номер карты должен состоять из 16 цифр и более'),
                          (None, 'Номер карты должен состоять из 16 цифр и более'),
                          (70007922896063617325, '7000 79** **** **** 7325'),
                          (7000792289606361732566, '7000 79** **** **** **25 66'),
                          (700079228960636173256666, '7000 79** **** **** **** 6666')])
def test_get_mask_card_number(number, expected):
    assert get_mask_card_number(number) == expected


@pytest.mark.parametrize("number, expected",
                         [(73654108430135874305, '**4305'),
                          (7365410, 'Номер счета должен содержать больше 7 цифр'),
                          (73654108430135, '**0135'),
                          (736541084301358743059235094567934590, '**4590'),
                          (None, 'Номер счета должен содержать больше 7 цифр')])
def test_get_mask_account(number, expected):
    assert get_mask_account(number) == expected
