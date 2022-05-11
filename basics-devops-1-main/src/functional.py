from typing import Union, Any


def process(first_numb: Any, second_numb: Any, operator: str) -> Any:

    if str(first_numb).replace('-', '', 1).replace('.', '', 1).isnumeric() and str(second_numb).replace('-', '', 1).replace('.', '', 1).isnumeric(): # noqa
        if operator == '*':
            return multiplication(first_numb, second_numb)
        elif operator == '/':
            return division(first_numb, second_numb)
        elif operator == '+':
            return addition(first_numb, second_numb)
        elif operator == '-':
            return subtraction(first_numb, second_numb)
        else:
            return "Неверный операнд"
    else:
        return "Неверный тип данных"


def multiplication(first_numb: Union[int, float], second_numb: Union[int, float]) -> Union[int, float]: # noqa
    return first_numb * second_numb


def addition(first_numb: Union[int, float], second_numb: Union[int, float]) -> Union[int, float]: # noqa
    return first_numb + second_numb


def subtraction(first_numb: Union[int, float], second_numb: Union[int, float]) -> Union[int, float]: # noqa
    return first_numb - second_numb


def division(first_numb: Union[int, float], second_numb: Union[int, float]) -> Any: # noqa
    if second_numb != 0:
        return first_numb / second_numb
    else:
        return "Деление на ноль"


def number_prep(number: str) -> Any:

    if number.isdigit():
        return int(number)
    elif number.replace('.', '', 1).replace('-', '', 1).isnumeric() == True: # noqa
        return float(number)
    else:
        return number