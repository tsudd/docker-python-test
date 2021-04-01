from abc import ABC, abstractmethod
import local_packages.serializers.tsuddjson as custom_json
import local_packages.serializers.tsuddtoml as custom_toml
import local_packages.serializers.tsuddyaml as custom_yaml

EXTENSIONS = {
    "JSON": "json",
    "YAML": "yaml",
    "TOML": "toml",
}


class Parser(ABC):
    """
    Abstract class of a parser, which has all necessary methods to process different data formats.
    """
    @abstractmethod
    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put the result to file.
        """
        pass

    @abstractmethod
    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        pass

    @abstractmethod
    def load(self, fp):
        """
        Returns parsed object and data from the file.
        """
        pass

    @abstractmethod
    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        pass


class JSONParser(Parser):
    """
        Parser for ".json" format, which uses custom library.
    """

    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put the result to file.
        """
        return custom_json.dump(obj, fp)

    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        return custom_json.dumps(obj)

    def load(self, fp):
        """
        Returns parsed object and data from the file.
        """
        return custom_json.load(fp)

    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        return custom_json.loads(s)


class YAMLParser(Parser):
    """
        Parser for ".yaml" format, which uses custom library.
    """

    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put the result to file.
        """
        return custom_yaml.dump(obj, fp)

    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        return custom_yaml.dumps(obj)

    def load(self, fp):
        """
        Returns parsed object and data from the file.
        """
        return custom_yaml.load(fp)

    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        return custom_yaml.loads(s)


class TOMLParser(Parser):
    """
    Parser for ".toml" format, which uses custom library.
    """

    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put the result to file.
        """
        return custom_toml.dump(obj, fp)

    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        return custom_toml.dumps(obj)

    def load(self, fp):
        """
        Returns parsed object and data from the file.
        """
        return custom_toml.load(fp)

    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        return custom_toml.loads(s)


class ParserFactory:
    """
    Factory class with pure parser_factory pattern< which creating parsers for specific data formats.
    """

    def get_parser(self, target_format: str):
        ft = target_format.lower()
        if ft == EXTENSIONS["JSON"]:
            return JSONParser()
        elif ft == EXTENSIONS["YAML"]:
            return YAMLParser()
        elif ft == EXTENSIONS["TOML"]:
            return TOMLParser()
        else:
            raise ValueError


