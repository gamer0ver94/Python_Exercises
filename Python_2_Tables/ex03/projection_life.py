from load_csv import load
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter
import pandas as pd


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


def projection_life():
    life_expec = load("life_expectancy_years.csv")
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

    life_expec = life_expec.melt(
        id_vars=["country"],
        var_name="Year",
        value_name="Life Expectancy")

    gdp = gdp.melt(
        id_vars=["country"],
        var_name="Year",
        value_name="Gdp")

    gdp["Year"] = gdp["Year"].astype(int)
    gdp["Gdp"] = gdp["Gdp"].apply(convert_population_values)
    life_expec["Year"] = life_expec["Year"].astype(int)

    merged = pd.merge(gdp, life_expec, on=["country", "Year"])

    data_year = merged[merged["Year"] == 1900]

    sb.scatterplot(
        data=data_year,
        x="Gdp",
        y="Life Expectancy",
        hue="country",
        legend=False
    ).xaxis.set_major_formatter(
            FuncFormatter(format_bi_numbers))
    plt.title("1900")
    plt.xlabel("Gross domesctic product")
    plt.ylabel("Life Expectancy")
    plt.xscale("log")
    plt.show()

    return


def main():
    projection_life()


if __name__ == "__main__":
    main()