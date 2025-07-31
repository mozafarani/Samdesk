# Advent of Code 2024 - Day 2: Red-Nosed Reports
# Author: Mohammed Alzafarani
# Description:
# This script reads a list of reports from standard input. Each report is a line
# of space-separated integers representing reactor levels. A report is considered
# "safe" if all levels are strictly increasing or decreasing, and each adjacent
# pair differs by 1 to 3 (inclusive).
#
# Example usage:
# python red_nosed_reports.py < input.txt

def is_safe(report):
    """Check if a given list of levels in the report is safe."""
    diffs = [b - a for a, b in zip(report, report[1:])]

    # All differences must be between -3 and -1 (decreasing)
    # or between 1 and 3 (increasing), and all must be same sign
    increasing = all(1 <= d <= 3 for d in diffs)
    decreasing = all(-3 <= d <= -1 for d in diffs)

    return increasing or decreasing


def main():
    import sys

    safe_count = 0

    for line in sys.stdin:
        if not line.strip():
            continue  # Skip empty lines
        report = list(map(int, line.strip().split()))
        if is_safe(report):
            safe_count += 1

    print(safe_count)


if __name__ == "__main__":
    main()
