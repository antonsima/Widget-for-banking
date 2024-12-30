def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает номер карты и возвращает ее маску
    """

    card_number_to_list = []
    temporary_card_number = str(card_number)

    if len(temporary_card_number) >= 16:
        while len(temporary_card_number) != 0:
            card_number_to_list.append(temporary_card_number[0:4])
            temporary_card_number = temporary_card_number[4:]

        card_number_to_list[1] = card_number_to_list[1][:2] + "**"

        for i in range(2, len(card_number_to_list) - 2):
            card_number_to_list[i] = "****"

        two_last_indexes = card_number_to_list.pop(-2) + card_number_to_list.pop(-1)
        last_stars = ''.join(['*' for i in range(len(two_last_indexes[:-4]))])
        two_last_indexes = last_stars + two_last_indexes[-4:]
        two_last_indexes = two_last_indexes[0:4] + ',' + two_last_indexes[4:]
        two_last_indexes = two_last_indexes.split(',')

        card_number_to_list.extend(two_last_indexes)

        hidden_card_number = " ".join(card_number_to_list)

        return hidden_card_number

    return 'Номер карты должен состоять из 16 цифр и более'


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает номер счета и возвращает его маску
    """

    temporary_account_number = str(account_number)

    if len(temporary_account_number) > 7:
        hidden_account_number = "**" + temporary_account_number[-4:]

        return hidden_account_number

    return 'Номер счета должен содержать больше 7 цифр'
