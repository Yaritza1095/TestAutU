'''
Markers are basically tags for test cases.
 Any test can have any number of markers.
 pytest has a few standard markers, but you can add your own custom markers too.

In fact, we've already used markers.
@pytest.mark.parameterize is a standard marker!

To add a marker to a test case function,
add a @pytest.mark decorator,
then add a suffix with a name for the marker.
'''
import pytest


@pytest.mark.math
def test_one_plus_two():
    a = 1
    b = 2
    c = 3
    assert a + b == c

@pytest.mark.math
def test_divide_by_zero():
    with pytest.raises(ZeroDivisionError) as e:
        num = 1 / 0
    assert 'division by zero' in str(e.value)