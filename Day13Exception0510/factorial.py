class Error(Exception):
    """Base class cho các exception trong module"""
    pass

class NotIntegerError(Error):
    """Ném ra khi giá trị đầu vào không phải integer"""

    def __init__(self, value):
        message = f"Không phải số nguyên: {value}"
        self.value = value
        self.message = message

class NegativeError(Error):
    """Ném ra khi giá trị số là số âm"""
    
    def __init__(self, value):
        message = f"Không phải số nguyên dương: {value}"
        self.value = value
        self.message = message


def factorial(number):
    if type(number) != int: raise NotIntegerError(number)

    if number < 0: raise NegativeError(number)

    result = number

    if number == 0:
        return 1

    for i in range(2, number):
        result *= i

    return result

# int(input())

# print(factorial("abc"))

list_ = ["hello", 0, 1, -2, 3,6]

for value in list_:
    try:
        print(f"{value}! =", factorial(value))
    except (NotIntegerError,NegativeError) as e:
        print("lay ra thuoc tinh message của exception: ", e.message,"\nvalue của exception có có ý nghĩa sử dụng:-------value:",e.value )
        print()