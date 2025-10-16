import pandas as pd


def load(path: str) -> pd.DataFrame | None:
    """Load a csv file."""
    try:
        data_file = pd.read_csv(path)
    except Exception as error:
        print(error)
        return None
    print(f"Loading dataset of dimentions {data_file.shape}")
    return data_file
