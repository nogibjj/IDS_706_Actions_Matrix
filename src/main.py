"""
IDS706 Individual Project One

This module reads an NBA dataset, calculates statistics, generates visualizations,
and creates a PDF report with statistics on player performance.test
"""

from lib import read_dataset, statistics, generate_pdf, visualization


def main():
    """Entrance to functions."""
    dataset_path = "../NBA_2021.csv"

    df = read_dataset(dataset_path)

    statistics(df)

    visualization(df)

    generate_pdf(df)


if __name__ == "__main__":
    main()
