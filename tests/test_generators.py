import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


def test_filter_by_usd(test_transactions, usd_transactions):
    expected_result = usd_transactions
    result = list(filter_by_currency(test_transactions, 'USD'))

    assert result == expected_result


def test_filter_by_currency_empty_input():
    expected_result = []
    result = list(filter_by_currency([], 'USD'))

    assert result == expected_result


def test_filter_by_missed_currency(test_transactions):
    expected_result = []
    result = list(filter_by_currency(test_transactions, 'CNY'))

    assert result == expected_result


def test_transaction_all_descriptions(test_transactions):
    expected_result = ['Перевод организации',
                       'Перевод со счета на счет',
                       'Перевод со счета на счет',
                       'Перевод с карты на карту',
                       'Перевод организации']
    result = list(transaction_descriptions(test_transactions))

    assert result == expected_result


def test_transaction_usd_descriptions(usd_transactions):
    expected_result = ['Перевод организации',
                       'Перевод со счета на счет',
                       'Перевод с карты на карту',]
    result = list(transaction_descriptions(usd_transactions))

    assert result == expected_result


def test_transaction_descriptions_empty_input():
    expected_result = []
    result = list(transaction_descriptions([]))

    assert result == expected_result


@pytest.mark.parametrize("start, stop, expected",
                         [(0, 5, ['0000 0000 0000 0000',
                                  '0000 0000 0000 0001',
                                  '0000 0000 0000 0002',
                                  '0000 0000 0000 0003',
                                  '0000 0000 0000 0004',
                                  '0000 0000 0000 0005']),
                          (-1, 5, []),
                          (0, 99999999999999999, [])
                          ])
def test_card_number_generator(start, stop, expected):
    assert list(card_number_generator(start, stop)) == expected
