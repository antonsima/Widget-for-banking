from src.processing import filter_by_state, sort_by_date


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
