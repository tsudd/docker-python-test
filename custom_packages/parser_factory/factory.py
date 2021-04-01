from custom_packages.parser_factory.JSONParser import JSONParser
from custom_packages.parser_factory.TOMLParser import TOMLParser
from custom_packages.parser_factory.YAMLParser import YAMLParser


EXTENSIONS = {
    "JSON": "json",
    "YAML": "yaml",
    "TOML": "toml",
}


class ParserFactory(object):
    """
    Factory class with pure parser_factory pattern< which creating parsers for specific data formats.
    """

    @staticmethod
    def get_parser(target_format: str):
        ft = target_format.lower()
        if ft == EXTENSIONS["JSON"]:
            return JSONParser()
        elif ft == EXTENSIONS["YAML"]:
            return YAMLParser()
        elif ft == EXTENSIONS["TOML"]:
            return TOMLParser()
        else:
            raise ValueError


