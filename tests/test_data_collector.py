from pathlib import Path

import pandas as pd
import pytest

from src.data_collector import DataValidationError, collect_data


def write_csv(path: Path, content: str) -> Path:
    path.write_text(content, encoding="utf-8")
    return path


def test_collect_data_accepts_valid_sales_data(tmp_path: Path) -> None:
    source = write_csv(tmp_path / "sales.csv", "category,sales\nbooks,100\nbooks,50\ngames,75\n")
    data = collect_data(source)
    assert list(data.columns) == ["category", "sales"]
    assert len(data) == 3
    assert pd.api.types.is_numeric_dtype(data["sales"])


def test_collect_data_rejects_missing_columns(tmp_path: Path) -> None:
    source = write_csv(tmp_path / "sales.csv", "category\nbooks\n")
    with pytest.raises(DataValidationError, match="sales"):
        collect_data(source)


@pytest.mark.parametrize(
    "content,error",
    [
        ("category,sales\nbooks,not-a-number\n", "numeric"),
        ("category,sales\nbooks,-1\n", "negative"),
        ("category,sales\n,10\n", "null|blank"),
    ],
)
def test_collect_data_rejects_invalid_rows(tmp_path: Path, content: str, error: str) -> None:
    source = write_csv(tmp_path / "sales.csv", content)
    with pytest.raises(DataValidationError, match=error):
        collect_data(source)
