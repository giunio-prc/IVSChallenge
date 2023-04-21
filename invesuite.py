def number_of_digit(number: int | float | complex | str) -> int:
    """function that accepts a number and outputs the number of (base-10) digits

    Args:
        number (int | float | complex | str): input number can be a
        intgeter, float, complex or convertible string

    Returns:
        int: the number of digits
    """
    if isinstance(number, str):
        try:
            number = complex(number)
        except ValueError as err:  # TODO include binary/hexadecimal format numbers
            print(f"ERROR: cannot convert `{number}` into a number")
            raise err

    if isinstance(number, complex):
        number = number.real

    if isinstance(number, float):
        number = int(number)

    return len(str(number))
