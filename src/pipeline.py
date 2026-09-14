from __future__ import annotations

import argparse
from dataclasses import dataclass
from pathlib import Path

from src.data_collector import collect_data
from src.data_processor import process_data
from src.visualizer import generate_plot


@dataclass(frozen=True)
class PipelineArtifacts:
    raw_data: Path
    processed_data: Path
    plot: Path


def run_pipeline(
    input_path: str | Path = "data/sales_data.csv",
    output_dir: str | Path = "artifacts",
) -> PipelineArtifacts:
    """Run the complete pipeline and persist inspectable artifacts."""
    output = Path(output_dir)
    output.mkdir(parents=True, exist_ok=True)

    raw_data = collect_data(input_path)
    processed_data = process_data(raw_data)

    raw_path = output / "raw_data.csv"
    processed_path = output / "processed_data.csv"
    plot_path = output / "sales_plot.png"

    raw_data.to_csv(raw_path, index=False)
    processed_data.to_csv(processed_path, index=False)
    generate_plot(processed_data, plot_path)

    return PipelineArtifacts(raw_data=raw_path, processed_data=processed_path, plot=plot_path)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run the sales data pipeline.")
    parser.add_argument("--input", default="data/sales_data.csv", help="Path to the source CSV.")
    parser.add_argument(
        "--output-dir",
        default="artifacts",
        help="Directory for generated CSV and PNG artifacts.",
    )
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    artifacts = run_pipeline(args.input, args.output_dir)
    print(f"Raw data: {artifacts.raw_data}")
    print(f"Processed data: {artifacts.processed_data}")
    print(f"Plot: {artifacts.plot}")


if __name__ == "__main__":
    main()
