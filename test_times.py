from times import compute_overlap_time, time_range
import pytest
import yaml


with open("fixture.yaml") as f:
    yaml_data = yaml.safe_load(f)

paramaterized_data = [[time_range(*yaml_data[key]['time_range_1']), time_range(*yaml_data[key]['time_range_2']), [tuple(arr) for arr in yaml_data[key]['expected']]] for key in yaml_data.keys()]


@pytest.mark.parametrize("input1, input2, expected", paramaterized_data)
def test_given_input(input1, input2, expected):
    result = compute_overlap_time(input1, input2) 
    assert result == expected

# def test_no_overlap():
#     """Testing no overlap between inputs."""
#     time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     time2 = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")
#     result = compute_overlap_time(time1, time2)
#     expected = []
#     assert result==expected

# def test_mult_intervals():
#     """Testing multiple intervals in input."""
#     time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 4, 60)
#     time2 = time_range("2010-01-12 11:00:00", "2010-01-12 12:00:00", 2, 60)
#     result = compute_overlap_time(time1, time2)
#     expected = [('2010-01-12 11:00:30', '2010-01-12 11:29:30'), ('2010-01-12 11:30:45', '2010-01-12 12:00:00')]
#     assert result==expected

# def test_start_end_same():
#     """Testing one input ending when another starts."""
#     time1 = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     time2 = time_range("2010-01-12 12:00:00", "2010-01-12 13:00:00")
#     result = compute_overlap_time(time1, time2)
#     expected = [('2010-01-12 12:00:00', '2010-01-12 12:00:00')]
#     assert result==expected

def test_backward_time():
    """Testing when the time goes backward"""
    with pytest.raises(ValueError):
        assert time_range("2010-01-12 12:00:00", "2010-01-12 10:00:00")
