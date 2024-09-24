from polars import DataFrame
from lib import (
    visualization,
    generate_pdf,
    read_dataset,
    calculate_statistics,
    _file_exists_and_not_empty,
)

df = read_dataset("../NBA_2021.csv")


def test_read_dataset():
    assert isinstance(df, DataFrame)
    assert len(df) > 0


def test_calculate_statistics():
    assert calculate_statistics(df, "PTS")[1] == 7.2
    assert calculate_statistics(df, "BLK")[1] == 0.3
    assert calculate_statistics(df, "AST")[1] == 1.4


def test_visualization():
    visualization(df)
    assert _file_exists_and_not_empty("pts_histogram.png")
    assert _file_exists_and_not_empty("ast_histogram.png")
    assert _file_exists_and_not_empty("blk_histogram.png")


def test_pdf_gen():
    generate_pdf(df, "NBA_2021_Report.pdf")
    assert _file_exists_and_not_empty("NBA_2021_Report.pdf")
