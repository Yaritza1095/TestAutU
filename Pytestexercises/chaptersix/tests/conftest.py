import pytest

from Pytestexercises.chaptersix.stuff.accum import Accumulator
'''
There are a few advanced tricks you can do with fixtures as well. 
If you want to share fixtures between multiple test modules, you can move it to a module in the tests features named conftest.py. 
conftest.py modules share test code for pytest. The name of the module is important. 
Pytest will automatically pick up any fixtures here.
'''
@pytest.fixture
def accum():
  return Accumulator()

@pytest.fixture
def accum2():
  return Accumulator()

def test_accumulator_init(accum, accum2):
  assert accum.count == 0
'''
 fixtures can handle both setup _and _cleanup. 
 If you use a yield statement instead of a return statement in a fixture, 
 the fixture function becomes something known in Python as a generator
 Basically, everything before the fixture's yield statement will be the "setup" steps, 
 and everything after the fixture's yield statement will be the "cleanup" steps. 
 The fixture will resume execution after the yield statement when the test case function completes, regardless of whether or not the test passed.

You can also change the scope of the fixture, or when the fixture is run. 
By default, the scope is set to "function", meaning that the fixture will run once for each function that needs it. 
However, if you change the scope to "session", then the fixture runs only one time for the entire test suite.

If multiple tests use the fixture, then the fixture will run only for the first test. 
pytest will then store its return value and simply inject the return value into each subsequent test that needs it.

Session scope would not be appropriate for these Accumulator tests, but it would be appropriate for a fixture that needs to read data from an external file. 
Other scope levels include "class", "module", and "package".

Finally, pytest provides several fixtures out of the box:

monkeypatch can be used for modifying classes, functions, and other objects
request provides test case metadata
tmpdir and tmp_path provide temporary directories
pytest plugins may also provide additional fixtures.
'''
@pytest.fixture
def accum():
    yield Accumulator()
    print('DONE-ZO')

@pytest.fixture
def accum(scope="session"):
  return Accumulator()