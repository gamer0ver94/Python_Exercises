from load_csv import load
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter


def format_bi_numbers(y, pos):
    """This function formats the value y into a representation of a thousand
    million or billion value.
    Args:
        y: the value
        pos: the position.
    Returns:
        Return a formated representation of y"""

    m = 1000000
    k = 1000
    b = 1000000000
    if y >= b:
        return f"{int(y / b)}B"
    elif y >= m:
        return f"{int(y / m)}M"
    elif y >= k:
        return f"{int(y / k)}k"


def convert_population_values(elem):
    """This function read a value and check the letter to
    covert it to a number based on the letter k,M,B
    Args:
        elem: element to convert
    Returns:
            return the converted value"""
    if isinstance(elem, str):
        elem = elem.strip()
        if "k" in elem:
            value = float(elem.replace("k", ""))
            elem = value * 1000
        elif "M" in elem:
            value = float(elem.replace("M", ""))
            elem = value * 1000000
        elif "B" in elem:
            value = float(elem.replace("B", ""))
            elem = value * 1000000000
    return elem


def aff_pop(path: str, countries: list):
    """Display graph of Life Expectancy of two countries"""
    path = "population_total.csv"
    datafile = load(path)
    try:
        df_long = datafile.melt(
            id_vars=["country"],
            var_name="Year",
            value_name="Population")
        df_long["Year"] = df_long["Year"].astype(int)

        mask = (
            (df_long["country"].isin(countries)) &
            (df_long["Year"] >= 1800) &
            (df_long["Year"] <= 2050))
        filter = df_long[mask].copy()

        filter["Population"] = filter["Population"].apply(
            convert_population_values)
        sb.lineplot(
            data=filter,
            x="Year", y="Population",
            hue="country",).yaxis.set_major_formatter(
                FuncFormatter(format_bi_numbers))

        plt.title("Population Projections")
        plt.show()
    except Exception as err:
        print(err)


def main():
    path = "population_total.csv"
    countries = ["France", "Portugal"]
    aff_pop(path, countries)


if __name__ == "__main__":
    main()
