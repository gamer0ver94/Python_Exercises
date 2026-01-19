def ft_median(lst: list):
    """Print mean result"""
    lenght = len(lst)
    middle = (lenght // 2)
    lst.sort()
    if lenght % 2 == 0:
        return (lst[middle] + lst[middle - 1]) / 2
    else:
        return lst[middle]


def ft_mean(lst: list):
    """Print mean result"""
    result = sum(lst)
    return result / len(lst)


def ft_quartile(lst: list):
    """Return Q1 (25%) and Q3 (75%) using linear interpolation"""
    if not lst:
        return None, None

    lst = sorted(lst)
    n = len(lst)

    def percentile(sorted_lst, percent):
        pos = (n - 1) * (percent / 100)
        k = int(pos)
        d = pos - k
        if k + 1 < n:
            return sorted_lst[k] + d * (sorted_lst[k + 1] - sorted_lst[k])
        else:
            return sorted_lst[k]

    Q1 = percentile(lst, 25)
    Q3 = percentile(lst, 75)
    return Q1, Q3


def ft_std(lst: list):
    """Print standart variation result"""
    variance = ft_variance(lst)
    return variance ** 0.5


def ft_variance(lst: list):
    """Print variance result"""
    tmp = []
    mean = ft_mean(lst)
    tmp = [(v - mean) ** 2 for v in lst]
    variance = sum(tmp) / len(lst)
    return variance


def ft_statistics(*args: any, **kwargs: any) -> None:
    """Print some data based on the input
        Args:
            *args(any): data to be processed
            **kwargs(any): (Optional) mean, median, quartile,
             std(standard variation
                and variance)"""
    operations = {
        "mean": ft_mean,
        "median": ft_median,
        "std": ft_std,
        "var": ft_variance,
        "quartile": ft_quartile,
    }
    for index, (key, value) in enumerate(kwargs.items()):
        if value in operations:
            if args:
                print(f"{value} : {operations[value](list(args))}")
            else:
                print("ERROR")
