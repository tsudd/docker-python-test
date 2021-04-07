from serilizer_lib.parser_factory.Parsers.Parser import Parser
import serilizer_lib.parsers.yaml.tsuddyaml as custom_yaml


class YAMLParser(Parser):
    """
        Parsers for ".yaml" format, which uses custom library.
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
