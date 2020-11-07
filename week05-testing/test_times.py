import times
import yaml
import pytest
from pytest import raises

with open("fixture.yml", 'r') as yamlfile:
    fixture = yaml.safe_load(yamlfile)
    print(fixture)

@pytest.mark.parametrize("test_name", fixture)
# fixture is a list of dictionaries [{'generic':...}, {'no_overlap':...}, ...]
 
# [
#    #base case
#    (
#        times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
#        times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
#        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#    ),
#    #test non overlap
#   (
#        times.time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"),
#        times.time_range("2010-01-12 14:30:00", "2010-01-12 14:45:00", 2, 60),
#        []
#    ),     
#    #test several intervals
#   (
#        times.time_range("2010-01-12 10:00:00", "2010-01-12 11:00:00", 2, 60),
#        times.time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60),
#        [('2010-01-12 10:30:30', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#   ) 
# ]
#)

def test_eval(test_name):
 # test_name will be a dictionary, e.g. for the first case: {'generic': {'time_range_1':..., 'time_range2':..., 'expected':...}
    properties = list(test_name.values())[0]
    first_range = times.time_range(*properties['time_range_1'])
    second_range = times.time_range(*properties['time_range_2'])
    expected = [(start, stop) for start, stop in properties['expected']]
    assert times.compute_overlap_time(first_range, second_range) == expected


def test_time_back():

    start_time = "2010-01-12 12:00:00"
    end_time = "2010-01-12 10:00:00"

    with raises(ValueError):
        times.time_range(start_time, end_time)
