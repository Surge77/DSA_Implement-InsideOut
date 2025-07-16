## Running the test with pytest which is a popular, third-party testing framework for Python.

`python -m pytest Tests\file_name.py -v`

> Why use -v?

1. Without -v: Shows dots (.) for passed tests, F for failed tests - very concise output
2. With -v: Shows:
•  The name of each test function being run
•  The result of each test (PASSED or FAILED)
•  The progress percentage
•  More detailed information about the test environment

The verbose output is particularly useful when:
•  You want to see which specific tests are running
•  You want to identify which test is failing in a large test suite
•  You need more context about the test execution environment
•  You're debugging test issues

If you're just running tests and don't need the extra detail, you can omit the -v flag for a more concise output


## What does `python -m Tests.file_name` do?

This runs the file c as a standalone Python script/module using the standard Python interpreter.

It does not use any test framework—just runs whatever is in the file, including your run_all_tests() function if present.

You must explicitly call your test functions (as in the template I provided).


## What about `python file_name.py`?

This just runs file_name.py directly as a Python script, not as a module.

## `python -m unittest Tests/test_file_name.py`

Runs only the specific test file you mention.

## `python -m unittest` 

This will discover and run every test class and method in all files matching test*.py in your project and subdirectories.