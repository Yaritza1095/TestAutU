import pytest
def test_one_plus_one():
    assert 1 + 1 == 2

#A failing test case example
def test_one_plus_two():
    a = 1
    b = 2
    c = 0
    assert a + b == c


'''
In Python, with is a special statement for automatically handling extra "enter" and "exit" logic for a caller. 
It is most commonly used for file input and output. 
However, f or pytest.raises, the "enter" logic makes the code catch any exceptions, 
and the "exit" logic asserts if the desired exception type was actually raised.

In our case, one divided by zero should raise a ZeroDivisionError. 
So pytest.raises should catch the exception and keep running the test as if there were no problems.

Furthermore, pytest.raises looks for an exception of a specific type. 
If the steps within the statement's body do not raise the desired exception, then it will raise an assertion error to fail the test. 
Using pytest.raises makes the test code more concise and avoids repetitive try/except blocks.

In addition to verifying that the code raises an exception, we can also verify attributes of the raised exception. 
Notice how the with statement stores the exception object as a variable named e. 
We can verify the exception's message with the following line:

assert 'division by zero' in str(e.value)


'''
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1/0
    assert 'division by zero' in str(e.value)