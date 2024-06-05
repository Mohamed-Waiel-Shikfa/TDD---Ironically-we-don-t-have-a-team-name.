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



def test_basic_add():
    """
        Tests addition. This test is written for you, extend it and add others!
    """
    assert add("5,2") == "7", "Failed on 5+2==7"
    assert add("") == "0", "Failed on empty string"
    assert add("1.1, 2.2") == "3.3", "Failed on 1.1+2.2==3.3"
    assert add("1,6,7") == "14", "Failed on 1+6+7==14"


def test_newline_delimiter():
    """
        Tests newline delimiter
    """
    assert add("1\n2,3") == "6", "Failed on 1+2+3==6"
    assert add("1\n2\n3") == "6", "Failed on 1+2+3==6"
    assert add("1\n2,3\n4") == "10", "Failed on 1+2+3+4==10"
    assert add("1\n2\n3\n4") == "10", "Failed on 1+2+3+4==10"
    assert add("1.1\n2.2,3.3") == "6.6", "Failed on 1.1+2.2+3.3==6.6"
    assert add("1.1\n2.2\n3.3") == "6.6", "Failed on 1.1+2.2+3.3==6.6"
    assert add("1.1\n2.2,3.3\n4.4") == "11", "Failed on 1.1+2.2+3.3+4.4==11"
    assert add("1.1\n2.2\n3.3\n4.4") == "11", "Failed on 1.1+2.2+3.3+4.4==11"





