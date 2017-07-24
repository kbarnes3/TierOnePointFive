class MockConfig:
    @property
    def can_reboot_cable_modem(self):
        return True

    @property
    def can_send_email(self):
        return False
