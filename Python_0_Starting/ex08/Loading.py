import os
from typing import Generator


def ft_tqdm(lst: range) -> Generator:
    terminal_col = int(os.get_terminal_size().columns) - 41
    for x in lst:
        percentage = int(x / len(lst) * 100 + 1)
        bar = "█" * (int(terminal_col * (percentage / 100)))
        spaces = " " * int(terminal_col - len(bar))
        print(f"\r{percentage}%|{bar} {spaces}| {x + 1}/{len(lst)}", end="")
        yield
