from pathlib import Path
import shutil
import sys

from tieronepointfive.directories import DefaultDirectories


class Config:
    def __init__(self, config_dir=None):
        if config_dir is None:
            dirs = DefaultDirectories()
            config_dir = dirs.config_directory
        config_dir_path = Path(config_dir).resolve()
        config_file_path = config_dir_path / 'config.json'
        if not config_file_path.is_file():
            self._create_new_config_file(config_dir_path, config_file_path)

    @staticmethod
    def _create_new_config_file(config_dir_path, config_file_path):
        config_dir_path.mkdir(parents=True, exist_ok=True)
        example_config_file = Path(__file__).parent / 'data' / 'config.example.json'
        shutil.copy(example_config_file, config_file_path)

        print('A new config file was created at:\n{0}\nPlease ensure it is correct before running TierOnePointFive'.format(str(config_file_path)))
        sys.exit(1)
