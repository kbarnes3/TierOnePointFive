from appdirs import AppDirs


def get_app_dirs():
    dirs = AppDirs('TierOnePointFive')


class Config:
    def __init__(self, config_dir=None):
        if config_dir is None:
            config_dir = AppDirs.user_config_dir
        config_file_name =
