import pytest
from main import fizzbuzz

def test_fizzbuzz_with_integer():
    # Test fizzbuzz with an integer to ensure it returns the correct string
    assert fizzbuzz(15) == "FizzBuzz"
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(2) == "2"

def test_fizzbuzz_with_non_integer():
    # Test fizzbuzz with a non-integer to ensure it raises an exception or fails
    with pytest.raises(TypeError):
        fizzbuzz("some string")
