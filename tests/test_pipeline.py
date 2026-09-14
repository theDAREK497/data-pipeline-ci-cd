from pathlib import Path

import pandas as pd

from src.pipeline import run_pipeline


def test_pipeline_creates_all_artifacts(tmp_path: Path) -> None:
    source = tmp_path / "sales.csv"
    source.write_text("category,sales\nbooks,100\nbooks,50\ngames,75\n", encoding="utf-8")
    artifacts = run_pipeline(source, tmp_path / "artifacts")

    assert artifacts.raw_data.is_file()
    assert artifacts.processed_data.is_file()
    assert artifacts.plot.is_file()
    assert artifacts.plot.stat().st_size > 0

    processed = pd.read_csv(artifacts.processed_data)
    assert processed.to_dict(orient="records") == [
        {"category": "books", "total_sales": 150},
        {"category": "games", "total_sales": 75},
    ]
