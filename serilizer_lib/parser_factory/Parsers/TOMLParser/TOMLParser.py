from serilizer_lib.parser_factory.Parsers.Parser import Parser
import serilizer_lib.parsers.toml.tsuddtoml as custom_toml


class TOMLParser(Parser):
    """
    Parsers for ".toml" format, which uses custom library.
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

