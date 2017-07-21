from pathlib import Path

from tieronepointfive.directories import DefaultDirectories


class Config:
    def __init__(self, config_dir=None):
        if config_dir is None:
            dirs = DefaultDirectories()
            config_dir = dirs.config_directory
        config_dir_path = Path(config_dir)
        config_file_path = config_dir_path / 'config.json'
        if not config_file_path.is_file():
            config_dir_path.mkdir(parents=True, exist_ok=True)
            config_file_path.touch(exist_ok=True)
