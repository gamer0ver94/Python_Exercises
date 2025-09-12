import sys


def is_args_valid(args) -> int:
    n_args = len(args) - 1

    assert n_args == 1, "the arguments are bad"
    assert all(char.isalnum() or char.isspace() for char in args[1]), \
        "the arguments are bad"
    return True if n_args == 1 else False


def getMorseCode() -> dict:
    return {
            "A": ".- ",
            "B": "-... ",
            "C": "-.-. ",
            "D": "-.. ",
            "E": ". ",
            "F": "..-. ",
            "G": "--. ",
            "H": ".... ",
            "I": ".. ",
            "J": ".--- ",
            "K": "-.- ",
            "L": ".-.. ",
            "M": "-- ",
            "N": "-. ",
            "O": "--- ",
            "P": ".--. ",
            "Q": "--.- ",
            "R": ".-. ",
            "S": "... ",
            "T": "- ",
            "U": "..- ",
            "V": "...- ",
            "W": ".-- ",
            "X": "-..- ",
            "Y": "-.-- ",
            "Z": "--.. ",
            "0": "----- ",
            "1": ".---- ",
            "2": "..--- ",
            "3": "...-- ",
            "4": "....- ",
            "5": "..... ",
            "6": "-.... ",
            "7": "--... ",
            "8": "---.. ",
            "9": "---- .",
            " ": "/ ",
    }


def encode_to_morse(text: str) -> str:
    NESTED_MORSE = getMorseCode()
    encoded_text = str()
    for char in text:
        code = NESTED_MORSE.get(char.upper() if char.isalpha else char)
        if code:
            encoded_text += code
        else:
            print("error trying to get code")
            return
    return encoded_text


def main() -> int:
    if is_args_valid(sys.argv):
        text = sys.argv[1]
        code = encode_to_morse(text)
        print(code)
    return 0


if __name__ == "__main__":
    main()
