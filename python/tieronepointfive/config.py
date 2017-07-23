import json
from pathlib import Path
import shutil
import sys

from jsoncomment import JsonComment

from tieronepointfive.directories import DefaultDirectories


class Config:
    def __init__(self, config_dir=None):
        dirs = DefaultDirectories()
        if config_dir is None:
            config_dir = dirs.config_directory
        config_dir_path = Path(config_dir).resolve()
        config_file_path = config_dir_path / 'config.json'
        if not config_file_path.is_file():
            self._create_new_config_file(config_dir_path, config_file_path)

        self._load_config_file(config_file_path, dirs)

    @staticmethod
    def _create_new_config_file(config_dir_path, config_file_path):
        config_dir_path.mkdir(parents=True, exist_ok=True)
        example_config_file = Path(__file__).parent / 'data' / 'config.example.json'
        shutil.copy(example_config_file, config_file_path)

        print('A new config file was created at:\n{0}\nPlease ensure it is correct before running Tier 1.5'.format(str(config_file_path)))
        sys.exit(1)

    def _load_config_file(self, config_file, default_dirs):
        parser = JsonComment(json)
        with config_file.open() as f:
            config_root = parser.load(f)

        config = config_root['config']
        self._load_data_dir(config, default_dirs)
        self._load_cable_modem_switch(config)

    def _load_data_dir(self, config, default_dirs):
        data_dir_label = 'data_dir'
        if data_dir_label in config:
            data_dir = config[data_dir_label]
        else:
            data_dir = default_dirs.data_directory

        self._data_dir = Path(data_dir).resolve()
        self._data_dir.mkdir(parents=True, exist_ok=True)

    @property
    def data_directory(self):
        return self._data_dir

    def _load_cable_modem_switch(self, config):
        cable_modem_switch_label = 'cable_modem_switch'
        if cable_modem_switch_label in config:
            self._cable_modem_switch = config[cable_modem_switch_label]
        else:
            self._cable_modem_switch = None

    @property
    def cable_modem_switch(self):
        return self._cable_modem_switch

    @property
    def can_reboot_cable_modem(self):
        return self._cable_modem_switch is not None


