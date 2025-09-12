import sys


def main() -> None:
    """Prints the number of characters in a string and print the
    number of lowers, uppers, digit, space characters.
    Args:
        argv:Input text used to count the characters and their types.
    """
    n_args = len(sys.argv) - 1
    arg = "" if n_args == 0 else sys.argv[1]
    assert n_args < 2, "Too many arguments"
    if arg == "":
        arg = input("Write something:\n")

    upper_char = 0
    lower_char = 0
    ponctuation_char = 0
    space_char = 0
    digit_char = 0
    for char in arg:
        if char.isdigit():
            digit_char += 1
        elif char.isspace():
            space_char += 1
        elif char.isupper():
            upper_char += 1
        elif char.islower():
            lower_char += 1
        else:
            ponctuation_char += 1
    print(f"The text contains {len(arg)} characters:")
    print(f"{upper_char} upper letters")
    print(f"{lower_char} lower letters")
    print(f"{ponctuation_char} pontuation marks")
    print(f"{space_char} spaces")
    print(f"{digit_char} digits")


if __name__ == "__main__":
    main()
