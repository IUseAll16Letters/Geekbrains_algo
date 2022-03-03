"""3. Сформировать из введенного числа обратное по порядку входящих в него цифр и вывести на экран.
Например, если введено число 3486, то надо вывести число 6843."""


def argument_type_can_int(fnc):
    def wrapper(fnc_arg):
        try:
            if isinstance(fnc_arg, (str, int)):
                return fnc(fnc_arg)
            else:
                raise ValueError
        except ValueError:
            return f"Received value must be able to -> 'int', received {fnc_arg.__class__}"
    return wrapper


# Option 1
@argument_type_can_int
def intify(value: str) -> int:
    value = int(value)
    is_negative = 0
    if value < 0:
        is_negative = True
        value = -1 * value
    result = 0
    while value:
        result *= 10
        result += value % 10
        value //= 10
    return -1 * result if is_negative else result


# Option 2
@argument_type_can_int
def super_intify(value: str) -> int:
    return -1 * int(value[::-1][:-1]) if int(value) < 0 else int(value[::-1])


if __name__ == '__main__':
    user_int_input = input('Enter any integer: ')
    print(intify('asd'))
    print(intify(user_int_input))
    print(super_intify(user_int_input))

