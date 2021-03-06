import pickle

from tieronepointfive.enums import State, Transition
from tieronepointfive.state_machine import StateMachineTick


class Data:
    def __init__(self, tick_list):
        self.tick_list = tick_list


class DataPickler:
    def __init__(self, config):
        self._config = config
        self._data_file = None

    def load(self):
        data_file = self._get_data_file()
        if data_file.exists():
            try:
                data = self._load_existing_data(data_file)
            except:
                data = self._create_error_parsing_data()
        else:
            data = self._create_fresh_data()

        return data

    def dump(self, data):
        data_file = self._get_data_file()
        with data_file.open('wb') as f:
            pickle.dump(data, f)

    def _get_data_file(self):
        if self._data_file is None:
            data_dir = self._config.data_directory
            self._data_file = data_dir / 'tieronepointfive.dat'

        return self._data_file

    def _load_existing_data(self, data_file):
        with data_file.open('rb') as f:
            data = pickle.load(f)

        if not self._is_valid_data(data):
            raise Exception('Invalid data object loaded')

        return data

    @staticmethod
    def _create_fresh_data():
        tick = StateMachineTick.create_completed(State.NO_DATA_FILE, Transition.DATA_FILE_CREATED, State.FRESH_DATA_FILE, True)
        data = Data([tick])

        return data

    @staticmethod
    def _create_error_parsing_data():
        tick = StateMachineTick.create_completed(State.BAD_DATA_FILE, Transition.DATA_FILE_CREATED, State.FRESH_DATA_FILE, True)
        data = Data([tick])

        return data

    @staticmethod
    def _is_valid_data(data):
        if not hasattr(data, 'tick_list'):
            return False

        try:
            length = len(data.tick_list)
        except TypeError:
            return False

        if length < 1:
            return False

        return True
