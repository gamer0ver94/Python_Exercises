def ft_filter(func, iterator):
    """Iterate a iterator and applies a function if it return true.
    Args:
        fuc: function that return true or false.
        iterator: iterator where the function will apply.
    Returns:
        return a new list with new that that were true in the func function.
        """
    new_list = [value for value in iterator if func(value)]
    return new_list
