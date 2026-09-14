from pathlib import Path

import pandas as pd

REQUIRED_COLUMNS = {"category", "sales"}


class DataValidationError(ValueError):
    """Raised when an input dataset does not satisfy the pipeline data contract."""


def collect_data(input_path: str | Path) -> pd.DataFrame:
    """Load and validate the source CSV."""
    path = Path(input_path)
    if not path.is_file():
        raise FileNotFoundError(f"Input CSV does not exist: {path}")

    data = pd.read_csv(path)
    missing = REQUIRED_COLUMNS.difference(data.columns)
    if missing:
        missing_columns = ", ".join(sorted(missing))
        raise DataValidationError(f"Missing required columns: {missing_columns}")

    if data.empty:
        raise DataValidationError("Input dataset must contain at least one row.")

    validated = data.loc[:, ["category", "sales"]].copy()

    if validated["category"].isna().any():
        raise DataValidationError("Column 'category' must not contain null values.")

    validated["category"] = validated["category"].astype(str).str.strip()
    if validated["category"].eq("").any():
        raise DataValidationError("Column 'category' must not contain blank values.")

    try:
        validated["sales"] = pd.to_numeric(validated["sales"], errors="raise")
    except (TypeError, ValueError) as exc:
        raise DataValidationError("Column 'sales' must contain numeric values.") from exc

    if validated["sales"].isna().any():
        raise DataValidationError("Column 'sales' must not contain null values.")

    if (validated["sales"] < 0).any():
        raise DataValidationError("Column 'sales' must not contain negative values.")

    return validated
