import argparse
from pathlib import Path

import openpyxl


def read_row_by_test_case(workbook_path: Path, test_case: str) -> dict[str, object]:
    """Return a header-to-value mapping for the requested spreadsheet row."""
    workbook = openpyxl.load_workbook(workbook_path, data_only=True)
    sheet = workbook.active
    headers = [cell.value for cell in sheet[1]]

    for row in sheet.iter_rows(min_row=2, values_only=True):
        if row[0] == test_case:
            return dict(zip(headers, row, strict=True))

    raise ValueError(f"Test case '{test_case}' was not found in {workbook_path}.")


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Read a test-data row from an Excel workbook."
    )
    parser.add_argument("workbook", type=Path, help="Path to the .xlsx test-data file.")
    parser.add_argument("test_case", help="Value in the first column to find.")
    arguments = parser.parse_args()

    print(read_row_by_test_case(arguments.workbook, arguments.test_case))


if __name__ == "__main__":
    main()
