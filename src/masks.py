from src.logger import setup_logging

logger = setup_logging(__file__)


def get_mask_card_number(card_number: int) -> str:
    """
    Функция принимает номер карты и возвращает ее маску
    """

    logger.info('Начало работы функции get_mask_card_number')

    card_number_to_list = []
    temporary_card_number = str(card_number)

    if len(temporary_card_number) >= 16:
        while len(temporary_card_number) != 0:
            card_number_to_list.append(temporary_card_number[0:4])
            temporary_card_number = temporary_card_number[4:]

        card_number_to_list[1] = card_number_to_list[1][:2] + "**"

        for i in range(2, len(card_number_to_list) - 2):
            card_number_to_list[i] = "****"

        two_last_indexes_str = card_number_to_list.pop(-2) + card_number_to_list.pop(-1)
        last_stars = ''.join(['*' for i in range(len(two_last_indexes_str[:-4]))])
        two_last_indexes_str = last_stars + two_last_indexes_str[-4:]
        two_last_indexes_str = two_last_indexes_str[0:4] + ',' + two_last_indexes_str[4:]

        two_last_indexes = two_last_indexes_str.split(',')

        card_number_to_list.extend(two_last_indexes)

        hidden_card_number = " ".join(card_number_to_list)

        logger.info("Программа завершена успешно")
        return hidden_card_number

    logger.error("Номер карты должен состоять из 16 цифр и более")
    return 'Номер карты должен состоять из 16 цифр и более'


def get_mask_account(account_number: int) -> str:
    """
    Функция принимает номер счета и возвращает его маску
    """

    logger.info('Начало работы функции get_mask_account')

    temporary_account_number = str(account_number)

    if len(temporary_account_number) > 7:
        hidden_account_number = "**" + temporary_account_number[-4:]

        logger.info("Программа завершена успешно")
        return hidden_account_number

    logger.error("Номер счета должен содержать больше 7 цифр")
    return 'Номер счета должен содержать больше 7 цифр'
