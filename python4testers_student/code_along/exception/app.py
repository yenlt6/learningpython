from random import randint


class Error(Exception):
    """Base Class"""
    pass


class ValueOutOfRangeError(Error):
    """Lỗi khi số đoán đoán nằm ngoài phạm vi"""
    pass


class SmallValueError(Error):
    """Lỗi số đoán nhỏ hơn kết quả"""
    pass


class LargeValueError(Error):
    """Lỗi số đoán lớn hơn kết quả"""
    pass


number = randint(0, 50)
count = 3

while count > 0:
    try:
        guess = int(input("Đoán một số (nguyên) bất kỳ trong khoảng 0 - 50: "))
        count -= 1

        if guess < 0 or guess > 50:
            raise ValueOutOfRangeError
        if guess < number:
            raise SmallValueError
        elif guess > number:
            raise LargeValueError
        else:
            print("Chúc mừng, số chính xác là:", number)
            break

    except ValueError:
        print("Nhập một số hợp lệ!")
    except ValueOutOfRangeError:
        print("Con số chính xác nằm trong khoảng 0-50")
    except SmallValueError:
        print("Số đoán nhỏ hơn con số chính xác")
    except LargeValueError:
        print("Số đoán lớn hơn con số chính xác")
    except Exception as e:
        print(e)
else:
    print("Đã hết số lượt đoán")
    print("Con số chính xác là:", number)
