import os
from configparser import ConfigParser


class ConfigFileNameConstants:
    """
    Configuration file name constants.
    """
    # Config file name constants. File must exist in the Config folder.
    # Warning : Class variables must be a configuration file in the Config folder. If not so, tests will fail.
    NOTIFIER_CONF = 'notifier.conf'

    def __init__(self):
        pass


class ConfigLocator:
    """
    Locates the specified config constant in the Config directory.
    """
    def __init__(self):
        pass

    @staticmethod
    def get_config_path(config_name):
        return os.path.join(os.path.abspath(os.path.dirname(__file__)), '../../config', config_name)


class ConfigReader:
    """
    Utility class which acts as a wrapper around SafeConfigParser to read configurations. Reads the configurations for
    UI Services.
    """
    def __init__(self, config_file_name=ConfigFileNameConstants.NOTIFIER_CONF):
        self._parser = ConfigParser()
        self._parser.read(ConfigLocator.get_config_path(config_file_name))

    def read_key(self, section, key):
        return self._parser.get(section, key)

    def get_section(self, section):
        """
        Returns the whole section as a dictionary object.
        :param section: The section in the Config file.
        :return: A dictionary for the specified section.
        """
        return dict(self._parser.items(section))

