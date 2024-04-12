import pytest

from Pytestexercises.chaptereight.stuff.accum import Accumulator
'''
Fixtures are special functions that pytest uses for setup and cleanup.
Any test case can call fixtures, making them very reusable. 
Fixtures are special functions that pytest can call before test case functions. 
They're the best way to handle "Arrange" steps shared by multiple tests in the context of the Arrange-Act-Assert pattern.
'''
#test_accumulator_init() verifies that the new instance of the Accumulator class has a starting count of zero.

@pytest.fixture
def accum():
    return Accumulator()

@pytest.mark.accumulator

def test_accumulator_init(accum):
    assert accum.count == 0

#test_accumulator_add_one() verifies that the add() method adds one to the internal count when it is called with no other arguments.
@pytest.mark.accumulator

def test_accumulator_add_one(accum):
    accum.add()
    assert accum.count == 1

#test_accumulator_add_two() verifies that the count increases appropriately with multiple add() calls.
@pytest.mark.accumulator

def test_accumulator_add_two(accum):
    accum.add()
    accum.add()
    assert accum.count == 2
#test_accumulator_add_three() verifies that the add() method adds 3 to the count when it is called with the argument of 3.
@pytest.mark.accumulator

def test_accumulator_add_three(accum):
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3
#Finally, test_accumulator_cannot_set_count_directly() verifies that the count attribute cannot be assigned directly because it is a read-only property.
# Notice how we use pytest.raises to verify the AttributeError.
@pytest.mark.accumulator

def test_accumulator_cannot_set_count_directly(accum):
  accum = Accumulator()
  with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
    accum.count = 10


'''
How does the fixture work? It's pytest magic! 
When pytest discovers a test case function, it looks at the function's parameter list. 
If the function has parameters, then it will search for fixtures to match each parameter's name.

In our case, the test function has a parameter named accum, so pytest looks for a fixture named accum which it will find in the same module. 
pytest will then execute the fixture and pass the fixture's return value into the test case function. 
Thus, in our test case, the accum variable will refer to the new Accumulator object created by the accum fixture. Nifty.

This is a clever form of dependency injection. The test case doesn't set up or "arrange" the test objects itself. 
Instead, the fixture handles setup and injects the required objects as dependencies into the test function. 
This separation of concerns makes test cases more readable, more consistent, and more maintainable. 
It also makes new test cases easier to write.
'''