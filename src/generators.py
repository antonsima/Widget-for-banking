from typing import Any, Generator


def filter_by_currency(transactions: list[dict], currency: str) -> Generator[dict, Any, None]:
    return (transaction for transaction in transactions if transaction["operationAmount"]["currency"]["code"] == currency)


def transaction_descriptions(transactions: list[dict]) -> Generator[Any, Any, None]:
    return (transaction["description"] for transaction in transactions)


def card_number_generator(start: int, stop: int) -> Generator[str, Any, None]:
    return ('0' * (16 - len(str(number))) + str(number) for number in range(start, stop + 1))
