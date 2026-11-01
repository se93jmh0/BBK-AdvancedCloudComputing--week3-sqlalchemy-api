# Courses API

A simple Courses API based on FastAPI, Pydantic, and SQLAlchemy.

# Test Results

    $ date; python -m pytest -v | cat; ls -l courses.db
    Sun Nov  1 19:01:52 GMT 2026
    ============================= test session starts ==============================
    platform linux -- Python 3.14.4, pytest-9.1.1, pluggy-1.7.0 -- /home/jhorns01/Uni/BBK/DataAnalyticsAndAI/AdvancedCloudComputing/week3-sqlalchemy-api/.venv/bin/python
    cachedir: .pytest_cache
    rootdir: /home/jhorns01/Uni/BBK/DataAnalyticsAndAI/AdvancedCloudComputing/week3-sqlalchemy-api
    plugins: anyio-4.15.1
    collecting ... collected 14 items

    tests/test_api.py::test_create_and_retrieve PASSED                       [  7%]
    tests/test_api.py::test_duplicate_does_not_add_row PASSED                [ 14%]
    tests/test_api.py::test_invalid_input_does_not_add_row PASSED            [ 21%]
    tests/test_api.py::test_missing_course PASSED                            [ 28%]
    tests/test_api.py::test_starts_empty PASSED                              [ 35%]
    tests/test_api.py::test_data_survives_new_application PASSED             [ 42%]
    tests/test_api.py::test_missing_title PASSED                             [ 50%]
    tests/test_api.py::test_valid_then_invalid_then_valid PASSED             [ 57%]
    tests/test_api.py::test_post_none_handling[code] PASSED                  [ 64%]
    tests/test_api.py::test_post_none_handling[title] PASSED                 [ 71%]
    tests/test_api.py::test_post_none_handling[lecturer] PASSED              [ 78%]
    tests/test_rules.py::test_enrolment_boundary[-1-True] PASSED             [ 85%]
    tests/test_rules.py::test_enrolment_boundary[0-False] PASSED             [ 92%]
    tests/test_rules.py::test_enrolment_boundary[1-False] PASSED             [100%]

    =============================== warnings summary ===============================
    .venv/lib/python3.14/site-packages/fastapi/testclient.py:1
    /home/jhorns01/Uni/BBK/DataAnalyticsAndAI/AdvancedCloudComputing/week3-sqlalchemy-api/.venv/lib/python3.14/site-packages/fastapi/testclient.py:1: StarletteDeprecationWarning: Using `httpx` with `starlette.testclient` is deprecated; install `httpx2` instead.
        from starlette.testclient import TestClient as TestClient  # noqa

    -- Docs: https://docs.pytest.org/en/stable/how-to/capture-warnings.html
    ======================== 14 passed, 1 warning in 0.17s =========================
    -rw-r--r-- 1 jhorns01 jhorns01 16384 Oct 22 20:34 courses.db
    (.venv)

# Limitations

There are no tests for fun failure scenarios, such as hitting an error condition
when talking to SQLite.
