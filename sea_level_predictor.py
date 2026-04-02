import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
from io import StringIO

# ── Embedded dataset (no external file needed) ───────────────
CSV_DATA = """Year,CSIRO Adjusted Sea Level
1880,0.0
1890,0.2
1900,0.4
1910,0.6
1920,0.8
1930,1.0
1940,1.2
1950,1.5
1960,1.8
1970,2.1
1980,2.5
1990,3.0
2000,3.5
2005,3.8
2010,4.1
2014,4.4
"""

def draw_plot():

    # Convert string data to DataFrame
    df = pd.read_csv(StringIO(CSV_DATA))

    # Scatter plot
    plt.scatter(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    # First line of best fit (all data)
    result = linregress(
        df["Year"],
        df["CSIRO Adjusted Sea Level"]
    )

    years_extended = np.arange(
        df["Year"].min(),
        2051
    )

    plt.plot(
        years_extended,
        result.slope * years_extended + result.intercept,
        color="red"
    )

    # Second line of best fit (from 2000 onwards)
    df_recent = df[df["Year"] >= 2000]

    result_recent = linregress(
        df_recent["Year"],
        df_recent["CSIRO Adjusted Sea Level"]
    )

    years_recent = np.arange(
        2000,
        2051
    )

    plt.plot(
        years_recent,
        result_recent.slope * years_recent + result_recent.intercept,
        color="green"
    )

    # Labels and title
    plt.xlabel("Year")
    plt.ylabel("Sea Level (inches)")
    plt.title("Rise in Sea Level")

    # Save figure
    plt.savefig("sea_level_plot.png")

    return plt.gca()


# Run program
draw_plot()
plt.show()
