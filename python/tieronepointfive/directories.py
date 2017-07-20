import os

import appdirs

APP_NAME = 'TierOnePointFive'


class DefaultDirectories:
    def __init__(self):
        if os.name == 'nt':
            self._config_directory = appdirs.user_config_dir(APP_NAME, roaming=True)
            self._data_directory = appdirs.user_data_dir(APP_NAME)
        else:
            self._config_directory = appdirs.site_config_dir(APP_NAME)
            self._data_directory = appdirs.site_data_dir(APP_NAME)

    @property
    def config_directory(self):
        return self._config_directory

    @property
    def data_directory(self):
        return self._data_directory
