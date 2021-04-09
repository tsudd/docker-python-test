from serilizer_lib.parser_factory.parser_objects.json.JSONParser import JSONParser
from serilizer_lib.parser_factory.parser_objects.toml.TOMLParser import TOMLParser
from serilizer_lib.parser_factory.parser_objects.yaml.YAMLParser import YAMLParser


EXTENSIONS = {
    "JSON": "json",
    "YAML": "yaml",
    "TOML": "toml",
}


class ParserFactory(object):
    """
    Factory class with pure parser_factory pattern< which creating parser_objects for specific data formats.
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


