'''test_fixture_basic.py
'''
import pytest


@pytest.fixture()
def before():
    print("\nBefore each test")


def test_1(before):
    print("test_1()")


def test_2(before):
    print("test_2")
    assert True
