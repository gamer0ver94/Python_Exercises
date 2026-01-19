def square(x: int | float) -> int | float:
    """Return the square of a value"""
    return x ** 2


def pow(x: int | float) -> int | float:
    """Return the pow of the value"""
    return x ** x


def outer(x: int | float, function) -> object:
    count = 0

    def inner() -> float:
        nonlocal count
        count += 1
        res = x
        for i in range(count):
            res = function(res)
        return res
    return inner
