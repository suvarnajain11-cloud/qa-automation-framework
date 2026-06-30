import configparser
import os


class ConfigReader:
    _config = configparser.ConfigParser()

    config_path = os.path.join(
        os.path.dirname(os.path.dirname(__file__)),
        "config",
        "config.ini"
    )

    _config.read(config_path)

    @classmethod
    def get_browser(cls):
        return cls._config.get("DEFAULT", "browser")

    @classmethod
    def get_base_url(cls):
        return cls._config.get("DEFAULT", "base_url")

    @classmethod
    def get_implicit_wait(cls):
        return cls._config.getint("DEFAULT", "implicit_wait")

    @classmethod
    def get_explicit_wait(cls):
        return cls._config.getint("DEFAULT", "explicit_wait")

    @classmethod
    def get_username(cls):
        return cls._config.get("DEFAULT", "username")

    @classmethod
    def get_password(cls):
        return cls._config.get("DEFAULT", "password")

    @classmethod
    def is_headless(cls):
        return cls._config.getboolean("DEFAULT", "headless")

    @classmethod
    def should_maximize(cls):
        return cls._config.getboolean("DEFAULT", "maximize_window")