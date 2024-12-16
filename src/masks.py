def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает номер карты и возвращает ее маску
    """

    card_number_to_list = []
    temporary_card_number = str(card_number)

    while len(temporary_card_number) != 0:
        card_number_to_list.append(temporary_card_number[0:4])
        temporary_card_number = temporary_card_number[4:]

    card_number_to_list[1] = card_number_to_list[1][:2] + "**"
    card_number_to_list[2] = "****"

    hidden_card_number = " ".join(card_number_to_list)

    return hidden_card_number


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает номер счета и возвращает его маску
    """

    temporary_account_number = str(account_number)

    hidden_account_number = "**" + temporary_account_number[-4:]

    return hidden_account_number
