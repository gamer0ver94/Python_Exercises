import sys
from ft_filter import ft_filter


def check_args(argv):
    """Checks if the arguments are valid, else throw an assertion Error
    Args:
        argv: List of arguments passed as input.
    """
    n_args = len(argv) - 1
    assert n_args == 2, "the arguments are bad"
    if len(argv) == 3:
        text: str = argv[1]
        n: str = argv[2]
    assert type(text) is str and str(n).isnumeric(), "the arguments are bad"


def parse_text(text: str, char: str) -> list:
    """Parse text by spliting it into a list of words
     based on the caracter passed.
    Args:
        text(str): text to be parsed.
        char(str): character used to parse text.
    Returns:
        Return a list of words."""
    return text.split(char)


def main() -> int:
    check_args(sys.argv)
    text = str()
    if len(sys.argv) == 3:
        text = sys.argv[1]
    else:
        print("bad arguments")
        return -1
    words = parse_text(text, " ")
    assert all(x.isalnum() and x.isprintable() for x in words), \
        "the arguments are bad"
    valid_words = ft_filter(lambda word: len(word) > int(sys.argv[2]), words)
    print(list(valid_words))


if __name__ == "__main__":
    main()
