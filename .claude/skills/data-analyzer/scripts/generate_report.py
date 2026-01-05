#!/usr/bin/env python3
"""
Generate formatted reports from data files.
"""

import sys
import pandas as pd
from datetime import datetime


def generate_report(data_file, output_file):
    """Generate a formatted report from a data file."""
    try:
        # Read the data file
        if data_file.endswith('.csv'):
            df = pd.read_csv(data_file)
        elif data_file.endswith('.json'):
            df = pd.read_json(data_file)
        else:
            print(f"Error: Unsupported file format. Use .csv or .json", file=sys.stderr)
            sys.exit(1)

        # Generate report
        report = []
        report.append("=" * 80)
        report.append(f"DATA ANALYSIS REPORT")
        report.append(f"Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        report.append(f"Source: {data_file}")
        report.append("=" * 80)
        report.append("")

        # Basic info
        report.append("DATASET OVERVIEW")
        report.append("-" * 80)
        report.append(f"Total Rows: {len(df)}")
        report.append(f"Total Columns: {len(df.columns)}")
        report.append(f"Columns: {', '.join(df.columns.tolist())}")
        report.append("")

        # Missing values
        missing = df.isnull().sum()
        if missing.sum() > 0:
            report.append("MISSING VALUES")
            report.append("-" * 80)
            for col, count in missing[missing > 0].items():
                report.append(f"{col}: {count} ({count/len(df)*100:.1f}%)")
            report.append("")

        # Numeric summary
        numeric_cols = df.select_dtypes(include='number').columns
        if len(numeric_cols) > 0:
            report.append("NUMERIC COLUMN STATISTICS")
            report.append("-" * 80)
            report.append(df[numeric_cols].describe().to_string())
            report.append("")

        # Write report
        report_text = "\n".join(report)
        with open(output_file, 'w') as f:
            f.write(report_text)

        print(f"Report generated: {output_file}")
        print("\nPreview:")
        print(report_text[:500] + "..." if len(report_text) > 500 else report_text)

    except FileNotFoundError:
        print(f"Error: File '{data_file}' not found.", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"Error generating report: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python generate_report.py <data_file> <output_file>", file=sys.stderr)
        sys.exit(1)

    generate_report(sys.argv[1], sys.argv[2])
