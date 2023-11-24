import pytest
from src.test.test_2.task_2 import *
from io import StringIO


def test_print_usage_statistics_exception(monkeypatch):
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    print_usage_statistics(without_spy)

    output = fake_output.getvalue()
    assert output == "This function haven't decorator spy\n"


def test_main_scenario(monkeypatch):
    fake_output = StringIO()
    monkeypatch.setattr("sys.stdout", fake_output)
    main()
    t = time.localtime()
    start_time = time.strftime("%H:%M:%S", t)

    output = fake_output.getvalue()
    assert (
        output
        == f"Function with_spy was called at {start_time} with parameters:\nn = 8, key = obed\n"
    )
