from load_csv import load
import seaborn as sb
import matplotlib.pyplot as plt


def aff_life(path: str, countries: list):
    """Display graph of Life Expectancy"""
    path = "life_expectancy_years.csv"
    datafile = load(path)
    try:
        df_long = datafile.melt(
            id_vars=["country"],
            var_name="Year",
            value_name="Life Expectancy")

        df_long["Year"] = df_long["Year"].astype(int)
        country = df_long["country"].isin(countries)
        print(df_long[country])
        sb.lineplot(data=df_long[country],
                    x="Year", y="Life Expectancy",
                    hue="country",)
        plt.title("Life Expectancy Projections")
        plt.show()
    except Exception as err:
        print(err)


def main():
    path = ""
    countries = ["France"]
    aff_life(path, countries)


if __name__ == "__main__":
    main()
