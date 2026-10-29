# Complete Course Practice Collection

This directory contains every meaningful source file from the original practice folder, reorganized by skill area. Files have clearer, lowercase names where needed, but their learning purpose is preserved.

## 01 WebDriver basics

- demowebdriver.py — browser launch, navigation, title, and current URL
- chrome_options.py — Chrome options and headless execution

## 02 Locators and controls

- locators.py — locator strategy notes and drop-down practice
- locator_extensions.py — explicit wait and password-reset locators
- find_elements.py — auto-suggest country selection
- ui_controls.py — checkboxes, radio buttons, visibility
- alert.py — JavaScript alert validation and acceptance

## 03 Waits and actions

- wait_demo.py — implicit wait and promotional-code workflow
- explicit_wait.py — explicit wait and cart-total validation
- action_demo.py — mouse hover and context-click actions

## 04 Browser context

- child_window.py — switching between browser windows
- frame_demo.py — frame interaction
- miscellaneous.py — scrolling, headless mode, and screenshots

## 05 E-commerce workflows

- e2e_test.py — product selection through purchase confirmation
- functional_assignment.py — product-list and total validation
- sorting_table.py — browser-side table-sort validation

## 06 Data and files

- excel_demo.py — Excel reads and data extraction with OpenPyXL
- upload.py — Excel update followed by file upload validation
- package_version_check.py — OpenPyXL version check

## 07 Pytest basics

- conftest.py — fixtures and parameterized browser data
- test_demo1.py and test_demo2.py — markers, assertions, skips, and fixtures
- test_fixture_data.py and test_fixture_demo.py — fixture-data patterns

## 08 Page Object Model framework

- pages/ — login, shop, and checkout Page Object classes
- data/test_e2eTestFramework.json — data-driven product cases with safe placeholders
- test_e2e_framework.py and conftest.py — framework-level test and browser fixture

## Evidence

The sibling evidence directory preserves the two original HTML reports, supporting CSS assets, and the browser screenshot.

The following original directories are deliberately excluded: .venv, __pycache__, .pytest_cache, and .idea. They are generated machine-specific files, not source work.
