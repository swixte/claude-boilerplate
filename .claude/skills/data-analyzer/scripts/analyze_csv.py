#!/usr/bin/env python3
"""
Analyze CSV files and generate summary statistics.
"""

import sys
import pandas as pd
import json


def analyze_csv(file_path):
    """Analyze a CSV file and return summary statistics."""
    try:
        # Read the CSV file
        df = pd.read_csv(file_path)

        # Generate summary statistics
        summary = {
            "file": file_path,
            "rows": len(df),
            "columns": len(df.columns),
            "column_names": df.columns.tolist(),
            "missing_values": df.isnull().sum().to_dict(),
            "data_types": df.dtypes.astype(str).to_dict(),
            "numeric_summary": df.describe().to_dict() if len(df.select_dtypes(include='number').columns) > 0 else {},
        }

        # Print summary as JSON
        print(json.dumps(summary, indent=2, default=str))

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error analyzing CSV: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python analyze_csv.py <input_file>", file=sys.stderr)
        sys.exit(1)

    analyze_csv(sys.argv[1])
