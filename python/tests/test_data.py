from tieronepointfive.data import DataPickler


def test_fresh_data_is_valid():
    pickler = DataPickler(None)
    fresh_data = pickler._create_fresh_data()
    assert pickler._is_valid_data(fresh_data)

def test_error_parsing_data_is_valid():
    pickler = DataPickler(None)
    error_data = pickler._create_error_parsing_data()
    assert pickler._is_valid_data(error_data)
