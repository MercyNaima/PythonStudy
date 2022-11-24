

def is_prime(*args: int) -> bool:

    """
    check if it is a prime num
    :param args: int num
    :return: bool
    """

    def _is_prime(num: int) -> bool:
        if num == 1 or num < 0:
            return False
        for x in range(2, num):
            if num % x == 0:
                return False
        else:
            return True

    for i in args:
        if not isinstance(i, int):
            raise TypeError("only int num can do is_prime!")
        if not _is_prime(i):
            return False
    else:
        return True


def get_fib(index: int = 8) -> list:

    """
    get a list of fibonacci number
    :param index: len of the fibonacci list
    :return: a list of fibonacci number
    """

    if index <= 0 or not isinstance(index, int):
        raise TypeError("Argument:[index] must be a int num!")
    result_list = []
    count = 0
    num1 = 0
    num2 = 1
    num3 = 0
    while count < index:
        num3 = num1 + num2
        num1 = num2
        num2 = num3
        result_list.append(num1)
        count += 1
    return result_list
