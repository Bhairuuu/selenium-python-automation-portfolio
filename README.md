# Selenium Python Automation Portfolio

A focused portfolio of UI test automation practice using **Python**, **Selenium WebDriver**, and **Pytest**. It includes a maintainable end-to-end purchase flow built with the Page Object Model, plus small examples that demonstrate common web-testing interactions.

## What this project demonstrates

- Page Object Model (POM) for readable and reusable test code
- Pytest fixtures, parametrization, command-line options, and markers
- Data-driven testing with JSON data
- Explicit waits and resilient browser interaction patterns
- Alerts, frames, windows, drop-downs, mouse actions, web tables, file upload/download, and Excel updates
- Chrome and Firefox execution with optional headless mode

## Project structure

```text
selenium-python-automation-portfolio/
├── src/ui_automation/pages/    # Page Object Model classes
├── tests/                      # Pytest end-to-end test and JSON data
├── examples/                   # Focused Selenium learning examples
├── docs/                       # Resume-ready project summary
├── requirements.txt            # Python dependencies
└── pytest.ini                  # Pytest configuration and markers
```

## Setup

1. Create and activate a virtual environment:

   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```

2. Install dependencies:

   ```powershell
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and add the test-site credentials. Do not commit `.env`.

4. Run the test suite:

   ```powershell
   pytest -m e2e --browser chrome
   ```

   For CI or a background run:

   ```powershell
   pytest -m e2e --browser chrome --headless
   ```

Selenium Manager resolves a compatible browser driver automatically when Chrome or Firefox is installed.

## Examples

Each example is an independently runnable script. For example:

```powershell
python examples\interactions\alerts.py
python examples\workflows\sort_table.py
python examples\file_handling\excel_data_demo.py path\to\workbook.xlsx
```

The examples use public training applications and may need locator updates if those sites change.

## Responsible test automation

- Test only applications you own or are authorized to test.
- Store credentials in environment variables or a local `.env` file, never in source control.
- Generated reports, screenshots, downloaded files, IDE settings, and virtual environments are excluded from Git.

## Resume-friendly summary

See [docs/portfolio-summary.md](docs/portfolio-summary.md) for concise, truthful project bullets that can be adapted for a resume, LinkedIn, or GitHub profile.
