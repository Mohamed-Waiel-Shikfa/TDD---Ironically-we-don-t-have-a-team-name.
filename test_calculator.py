"""
Test Module for String Calculator
----------------------------------
    @author: [student's name] - [student's email]
    @date: [date of creation]
    @description: This test module is designed to test the functionality of the string calculator
             defined in the calculator.py module. Using pytest for testing allows for more
             concise and powerful test capabilities, which is integrated into the GitHub
             workflow for continuous integration and testing.
"""

import pytest
from calculator import add
import random


def test_basic_add():
    """
        Tests addition. This test is written for you, extend it and add others!
    """
    assert add("5,2") == "7", "Failed on 5+2==7"
    assert add("") == "0", "Failed on empty string"
    assert add("1.1, 2.2") == "3.3", "Failed on 1.1+2.2==3.3"
    assert add("1,6,7") == "14", "Failed on 1+6+7==14"
    
def many_numbers():
    for i in range(15):
        val1= random.randint(0,5)
        val2 = random.randint(0,5)
        val3= random.randint(0,5)
        val4 = random.randint(0,5)
        val5 = random.randint(0,5)
        total = val1+val2+val3
        total1 = val1+val2+val3+val4
        total2 = val1+val2+val3+val4+val5
        assert add(f"{val1},{val2},{val3}") == f"{total}", f"Failed on {val1} + {val2} + {val3} == {total}"
        assert add(f"{val1},{val2},{val3},{val4}") == f"{total}", f"Failed on {val1} + {val2} + {val3} + {val4} == {total1}"
        assert add(f"{val1},{val2},{val3},{val4},{val5}") == f"{total}", f"Failed on {val1} + {val2} + {val3} + {val4} + {val5} == {total2}"
    
