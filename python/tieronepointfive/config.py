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
        self._load_router_switch(config)
        self._load_email_settings(config)

    def _load_data_dir(self, config, default_dirs):
        data_dir_label = 'data_dir'
        if data_dir_label in config:
            data_dir = config[data_dir_label]
        else:
            data_dir = default_dirs.data_directory

        data_dir_path = Path(data_dir)
        data_dir_path.mkdir(parents=True, exist_ok=True)
        self._data_dir = data_dir_path.resolve()

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

    def _load_router_switch(self, config):
        router_switch_label = 'router_switch'
        if router_switch_label in config:
            self._router_switch = config[router_switch_label]
        else:
            self._router_switch = None

    @property
    def router_switch(self):
        return self._router_switch

    @property
    def can_reboot_router(self):
        return self.router_switch is not None

    def _load_email_settings(self, config):
        email_settings_label = 'email_settings'
        if email_settings_label in config:
            self._email_settings = EmailConfig(config[email_settings_label])
        else:
            self._email_settings = None

    @property
    def email_settings(self):
        return self._email_settings

    @property
    def can_send_email(self):
        return self._email_settings is not None


class EmailConfig:
    def __init__(self, email_settings):
        self._server_address = email_settings['server_address']
        self._server_port = email_settings['server_port']
        self._login = email_settings['login']
        self._password = email_settings['password']
        self._sender = self._load_email_address(email_settings['sender'])

        to_config = email_settings['to']
        if len(to_config) < 1:
            raise Exception('Must provide at least one To: email address')

        self._to = [self._load_email_address(address) for address in to_config]

    @staticmethod
    def _load_email_address(email_address_config):
        email_address = email_address_config['email']
        name_label = 'name'
        if name_label in email_address_config:
            name = email_address_config[name_label]
            return EmailAddressWithName(email_address, name)
        else:
            return EmailAddress(email_address)

    @property
    def server_address(self):
        return self._server_address

    @property
    def server_port(self):
        return self._server_port

    @property
    def login(self):
        return self._login

    @property
    def password(self):
        return self._password

    @property
    def sender(self):
        return self._sender

    @property
    def to(self):
        return self._to


class EmailAddress:
    def __init__(self, email_address):
        self._email = email_address

    @property
    def email(self):
        return self._email


class EmailAddressWithName(EmailAddress):
    def __init__(self, email_address, name):
        super().__init__(email_address)
        self._name = name

    @property
    def name(self):
        return self._name