from ..config_reader import ConfigFileNameConstants, ConfigLocator, ConfigReader
import os
import pytest
from pytest import raises
from configparser import NoSectionError, NoOptionError


class TestConfigLocator:

    @pytest.mark.slow
    def test_get_config_path_for_file_existence(self):
        config_values = [value for constant, value in vars(ConfigFileNameConstants).items()
                         if not constant.startswith('__') and not constant.startswith('<')
                         and not constant.endswith('>') and not callable(getattr(ConfigFileNameConstants, constant))]
        for constant in config_values:
            assert os.path.isfile(ConfigLocator.get_config_path(constant)) is True, \
                'Config file specified in ConfigLocator does not exist.'


class TestConfigReader:

    @classmethod
    def setup_method(cls):
        cls.reader = ConfigReader()

    @pytest.mark.slow
    def test_read_key_section_and_key_present(self):
        assert self.reader.read_key('KEYWORDS_TO_WATCH_FOR', 'KEYWORDS') is not None

    @pytest.mark.slow
    def test_read_key_section_not_present(self):
        with raises(NoSectionError):
            self.reader.read_key('invalid_section_name', 'host')

    @pytest.mark.slow
    def test_read_key_key_not_present(self):
        with raises(NoOptionError):
            self.reader.read_key('KEYWORDS_TO_WATCH_FOR', 'invalid_key')

    @pytest.mark.slow
    def test_get_section_returns_dictionary(self):
        assert isinstance(self.reader.get_section('FILE_PATHS'), dict)
