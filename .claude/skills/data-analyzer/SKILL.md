---
name: data-analyzer
description: Analyze data files, generate reports, and create visualizations. Use when working with CSV, JSON, or data analysis tasks.
allowed-tools: Read, Bash, Write
---

# Data Analyzer Skill

Use this skill when you need to analyze data files, generate reports, or create visualizations.

## Capabilities

- Parse and analyze CSV, JSON, and other data formats
- Generate statistical summaries
- Create data visualizations
- Export reports in various formats
- Clean and transform data

## When to Use

- User asks to analyze a data file
- Need to generate reports from data
- Creating charts or visualizations
- Data cleaning or transformation tasks
- Statistical analysis requests

## Available Scripts

### analyze_csv.py
Analyzes CSV files and generates summary statistics.

Usage:
```bash
python .claude/skills/data-analyzer/scripts/analyze_csv.py <input_file>
```

### generate_report.py
Creates formatted reports from data analysis.

Usage:
```bash
python .claude/skills/data-analyzer/scripts/generate_report.py <data_file> <output_file>
```

## Example Workflow

1. Read the data file to understand structure
2. Use appropriate script to analyze
3. Generate visualizations if needed
4. Create summary report
5. Present findings to user

## Data Formats Supported

- CSV (Comma-separated values)
- JSON (JavaScript Object Notation)
- TSV (Tab-separated values)
- Excel files (with pandas)

## Best Practices

- Always inspect data before analysis
- Handle missing values appropriately
- Validate data quality
- Provide clear, actionable insights
- Include visualizations where helpful

## Dependencies

Requires Python with these packages:
- pandas
- numpy
- matplotlib (for visualizations)

Install with: `pip install pandas numpy matplotlib`
