import pandas as pd

from src.data_processor import process_data


def test_process_data_aggregates_and_sorts_categories() -> None:
    data = pd.DataFrame(
        {"category": ["books", "games", "books", "music"], "sales": [100, 75, 50, 200]}
    )
    result = process_data(data)
    assert result.to_dict(orient="records") == [
        {"category": "music", "total_sales": 200},
        {"category": "books", "total_sales": 150},
        {"category": "games", "total_sales": 75},
    ]
