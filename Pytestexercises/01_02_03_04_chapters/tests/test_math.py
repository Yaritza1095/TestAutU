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

'''
Parametrization
Sometimes, the behaviors we want to test can have different kinds of inputs and outputs. 
They may also have specific boundary cases that should be tested. 
In these cases, it may be appropriate to parameterize test cases to cover all the different input and output values.
. Using pytest.mark.parametrize, we can write one test function that takes multiple parameterized inputs.

Let's rewrite our multiplication tests using @pytest.mark.parametrize. 
Let's write a list of tuples in which each tuple represents an equivalent class of inputs and outputs. 
Write one tuple for each equivalence class.
'''
products = [
    (2, 3, 6),  #positive integers
    (1, 99, 99), #identity
    (0, 99, 0), #zero
    (3, -4, -12), # positive by negative
    (-5, -5, 25), #negative by negative
    (2.5, 6.7, 16.75) #floats
]
'''
@pytest.mark.parametrize is a decorator for the test_multiplication function.
In Python, a decorator is a special function that wraps around another function.
It is a simple form of aspect-oriented programming

For @pytest.mark.parametrize, the inner function is the test case. 
The outer function is the decorator itself, 
and it will call the inner test case once per input tuple.
We also need to pass two arguments to the decorator. 

The first argument is a string containing a comma-separated list of variable names. 
These names must match the parameter names for the test case function, a, b, and product. 
The second argument is the list of parameterized values. 
'''
@pytest.mark.parametrize('a, b, product', products)
def test_multiplication(a, b, product):
    assert  a*b == product

