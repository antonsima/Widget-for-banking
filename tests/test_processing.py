from src.processing import filter_by_state, get_category_count, get_transactions_by_pattern, sort_by_date


def test_filter_by_state(test_operations, executed_operations, canceled_operations):
    assert filter_by_state(test_operations, 'EXECUTED') == executed_operations
    assert filter_by_state(test_operations, 'CANCELED') == canceled_operations
    assert filter_by_state(test_operations, 'Что-то другое') == []
    assert filter_by_state([], 'CANCELED') == []
    assert filter_by_state(test_operations, '') == []


def test_sort_by_date(test_operations, direct_sort, reversed_sort, problem_dates_of_operations):
    assert sort_by_date(test_operations, True) == reversed_sort
    assert sort_by_date(test_operations, False) == direct_sort
    assert sort_by_date(problem_dates_of_operations) == []
    assert sort_by_date([]) == []


def test_get_transactions_by_pattern(test_transactions):
    assert get_transactions_by_pattern(test_transactions, 'перевод') == test_transactions
    assert get_transactions_by_pattern(test_transactions, 'открытие') == []


def test_get_category_count(test_transactions):
    assert get_category_count(test_transactions,
                              ['Перевод организации',
                               'Перевод со счета на счет']) == {'Перевод организации': 2,
                                                                'Перевод со счета на счет': 2}
    assert get_category_count(test_transactions,
                              ['Открытие вклада']) == {}
