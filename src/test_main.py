from main import main
from lib import _file_exists_and_not_empty


def test_main():
    main()
    assert _file_exists_and_not_empty("pts_histogram.png")
    assert _file_exists_and_not_empty("ast_histogram.png")
    assert _file_exists_and_not_empty("blk_histogram.png")
    assert _file_exists_and_not_empty("NBA_2021_Report.pdf")
