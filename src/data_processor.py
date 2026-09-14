import pandas as pd


def process_data(data: pd.DataFrame) -> pd.DataFrame:
    """Aggregate validated sales rows into category totals."""
    required_columns = {"category", "sales"}
    missing = required_columns.difference(data.columns)
    if missing:
        missing_columns = ", ".join(sorted(missing))
        raise ValueError(f"Cannot process data; missing columns: {missing_columns}")

    return (
        data.groupby("category", as_index=False)
        .agg(total_sales=("sales", "sum"))
        .sort_values(["total_sales", "category"], ascending=[False, True])
        .reset_index(drop=True)
    )
