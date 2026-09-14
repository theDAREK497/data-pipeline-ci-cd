from pathlib import Path

import pandas as pd
from matplotlib.figure import Figure


def generate_plot(summary: pd.DataFrame, output_path: str | Path) -> Path:
    """Render the processed sales summary as a PNG chart."""
    required_columns = {"category", "total_sales"}
    missing = required_columns.difference(summary.columns)
    if missing:
        missing_columns = ", ".join(sorted(missing))
        raise ValueError(f"Cannot visualize data; missing columns: {missing_columns}")

    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)

    figure = Figure(figsize=(8, 5))
    axis = figure.subplots()
    axis.bar(summary["category"], summary["total_sales"])
    axis.set_title("Sales by Category")
    axis.set_xlabel("Category")
    axis.set_ylabel("Total sales")
    axis.tick_params(axis="x", rotation=30)
    figure.tight_layout()
    figure.savefig(path, dpi=144)
    return path
