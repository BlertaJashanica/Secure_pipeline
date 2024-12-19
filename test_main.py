# test_main.py
# test_main.py
import pytest
from main import hello_world

def test_hello_world():
    assert hello_world() == "Hello, world!"

