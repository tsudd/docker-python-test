from serilizer_lib.parser_factory.Parsers.JSONParser.JSONParser import JSONParser
from serilizer_lib.parser_factory.Parsers.TOMLParser.TOMLParser import TOMLParser
from serilizer_lib.parser_factory.Parsers.YAMLParser.YAMLParser import YAMLParser


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


