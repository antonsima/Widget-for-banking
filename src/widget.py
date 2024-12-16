from src.masks import get_mask_card_number, get_mask_account

def mask_account_card(type_and_account_or_card_number: str) -> str:
    """Возвращает строку с замаскированным номером"""

    tmp_list = type_and_account_or_card_number.split()

    type_account_or_card = tmp_list[0]
    account_or_card_number = int(tmp_list[-1])

    if type_account_or_card == 'Счет':
        tmp_list.pop()

        tmp_list.append(get_mask_account(account_or_card_number))
    else:
        tmp_list.pop()

        tmp_list.append(get_mask_card_number(account_or_card_number))

    masked_account_card = ' '.join(tmp_list)

    return masked_account_card
