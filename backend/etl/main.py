import argparse

from etl.pipeline import run_pipeline


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--year",
        type=int,
        default=2024,
        help="Formula 1 season to ingest",
    )

    args = parser.parse_args()

    run_pipeline(args.year)


if __name__ == "__main__":
    main()