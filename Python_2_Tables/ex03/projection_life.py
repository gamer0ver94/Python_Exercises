from load_csv import load
import seaborn as sb
import matplotlib.pyplot as plt


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
    #life_expec = load("life_expectancy_years.csv")
    gdp = load("income_per_person_gdppercapita_ppp_inflation_adjusted.csv")

#    life_expec = life_expec.melt(
#        id_vars=["country"],
#        var_name="Year",
#        value_name="Life Expectancy")
    gdp = gdp.melt(
        id_vars=["country"],
        var_name="Year",
        value_name="gdp")
    gdp["gdp"] = gdp["gdp"].apply(convert_population_values)
    country = gdp["country"].isin(["Portugal"])
    sb.lineplot(
        data=gdp[country],
        x="Year", y="gdp",
        hue="country",)
    plt.title("Life Expectancy Projections")
    plt.show()
    return


def main():
    projection_life()


if __name__ == "__main__":
    main()