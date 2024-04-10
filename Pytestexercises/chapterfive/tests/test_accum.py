import pytest

from Pytestexercises.chapterfive.stuff.accum import Accumulator

#test_accumulator_init() verifies that the new instance of the Accumulator class has a starting count of zero.
def test_accumulator_init():
    accum = Accumulator()
    assert accum.count == 0

#test_accumulator_add_one() verifies that the add() method adds one to the internal count when it is called with no other arguments.
def test_accumulator_add_one():
    accum = Accumulator()
    accum.add()
    assert accum.count == 1

#test_accumulator_add_two() verifies that the count increases appropriately with multiple add() calls.
def test_accumulator_add_two():
    accum = Accumulator()
    accum.add()
    accum.add()
    assert accum.count == 2
#test_accumulator_add_three() verifies that the add() method adds 3 to the count when it is called with the argument of 3.
def test_accumulator_add_three():
    accum = Accumulator()
    accum.add(3)
    assert accum.count == 3
#Finally, test_accumulator_cannot_set_count_directly() verifies that the count attribute cannot be assigned directly because it is a read-only property.
# Notice how we use pytest.raises to verify the AttributeError.
def test_accumulator_cannot_set_count_directly():
  accum = Accumulator()
  with pytest.raises(AttributeError, match=r"property 'count' of 'Accumulator' object has no setter") as e:
    accum.count = 10

'''
This pattern is called "Arrange-Act-Assert". It is the classic three-step pattern for functional test cases.

1. Arrange assets for the test (like a setup procedure).
2. Act by exercising the target behavior.
3. Assert that expected outcomes happen.
'''