import sys
import pandas as pd

def min_max_scaling(series):
    """Scale values to the range [0,1]."""
    return (series - series.min()) / (series.max() - series.min())

def z_score_normalization(series):
    """Standardize values to mean 0 and std 1."""
    return (series - series.mean()) / series.std()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 bin/normalize.py <csv_file>")
        sys.exit(1)

    # Read CSV from argument
    input_file = sys.argv[1]
    df = pd.read_csv(input_file)

    print("Original data (first 5 rows):")
    print(df.head())

    # Apply normalization on numeric columns
    for col in df.select_dtypes(include='number').columns:
        df[col + "_minmax"] = min_max_scaling(df[col])
        df[col + "_zscore"] = z_score_normalization(df[col])

    # Save new normalized data
    output_file = input_file.replace(".csv", "_normalized.csv")
    df.to_csv(output_file, index=False)

    print(f"\nNormalized data saved to {output_file}")
