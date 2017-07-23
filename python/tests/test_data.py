from tieronepointfive.data import DataPickler


def test_fresh_data_is_valid():
    pickler = DataPickler(None)
    fresh_data = pickler._create_fresh_data()
    assert pickler._is_valid_data(fresh_data)
