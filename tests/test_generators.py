from src.generators import filter_by_currency


def test_filter_by_usd(test_transactions, usd_transactions):
    expected_result = usd_transactions
    result = list(filter_by_currency(test_transactions, 'USD'))

    assert result == expected_result


def test_filter_by_currency_empty(test_transactions, usd_transactions):
    expected_result = usd_transactions
    result = list(filter_by_currency(test_transactions, 'USD'))

    assert result == expected_result