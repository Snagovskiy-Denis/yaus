import string


DIGITS_62 = ''.join(map(str, range(0, 10))) + string.ascii_letters


def convert_10_to_B(number: int, digits_map: dict, radix_B: int) -> str:
    '''Convert a base 10 number to a base B number

    To convert number z form the numeral system with base 10 to the numeral
    system with base B, we need to perform sequential divisiton of number z
    by B; reminders are base-B 'digits' for z

    arguments:

        number: int = number with radix 10 (number z in description above)
        digits_map: dict = map of base 10 digits to base B digits
        radix_B: int = numeral system base to convert (B in description above)
    '''
    reminders = []
    while number >= radix_B:
        reminders.append(number % radix_B)
        number //= radix_B
    reminders.append(number)

    digits_in_new_radix = [digits_map[digit] for digit in reminders[::-1]]
    return ''.join(digits_in_new_radix)


def convert_10_to_62(number_10_radix: int) -> str:
    '''Return base 62 representation of integer'''
    digits_map_10_to_62 = {
        digit_10: digit_62
        for digit_10, digit_62 in enumerate(DIGITS_62)
    }
    radix = len(digits_map_10_to_62)
    return convert_10_to_B(number_10_radix, digits_map_10_to_62, radix)


def convert_B_to_10(number: str, digits_map: dict, radix_B: int) -> int:
    '''Convert a base B number to a base 10 number

    z = a(n) * B ** (n) + a(n-1) * B ** (n-1) + ... a(1) * B + a(0)

    arguments:

        number: str = z in description above
        digits_map: dict = map of base B digits to base 10 digits
        radix_B: int = numeral system base to convert (B in description above)
    '''
    number_digits_10_radix = [digits_map[digit] for digit in number]
    number_of_digits_in_number = len(number)

    number_in_10_radix = 0
    for position, digit in enumerate(number_digits_10_radix):
        digit_index = number_of_digits_in_number - position - 1
        number_in_10_radix += digit * radix_B ** digit_index

    return number_in_10_radix


def convert_62_to_10(number_62_radix: str) -> int:
    '''Return the decimal representation of a base 62 integer'''
    digits_map_62_to_10 = {
        digit_62: digit_10
        for digit_10, digit_62 in enumerate(DIGITS_62)
    }
    radix = len(digits_map_62_to_10)
    return convert_B_to_10(number_62_radix, digits_map_62_to_10, radix)
