from times import compute_overlap_time, time_range

def test_given_input():
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
    result = compute_overlap_time(large, short) 
    expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
    assert result == expected

def test_no_overlap():
    """Testing no overlap between inputs."""
    large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
    short = time_range("2010-01-12 13:00:00", "2010-01-12 14:00:00")
    result = compute_overlap_time(large, short)
    expected = []
    assert result==expected

def test_mult_intervals():
    """Testing multiple intervals in input."""
    time = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00", 4, 60)
    result = compute_overlap_time(time, time)
    expected = [('2010-01-12 10:00:00', '2010-01-12 10:29:15'), ('2010-01-12 10:30:15', '2010-01-12 10:59:30'), ('2010-01-12 11:00:30', '2010-01-12 11:29:45'), ('2010-01-12 11:30:45', '2010-01-12 12:00:00')]
    assert result==expected