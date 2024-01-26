import pytest
from calc import square
from calc import is_valid_number

def main():
     test_positive()
     test_negative()

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_string():
     with pytest.raises(TypeError):
          square("cat")

def test_is_valid_number():
     assert is_valid_number("qwe") == False
     assert is_valid_number("123") == True

    #if square(2) != 4:
    #    print("Square of 2 was not 4")
    #if square(3) != 9:
    #    print("Square of 3 was not 9")
    

if __name__ == "__main__":
        main()