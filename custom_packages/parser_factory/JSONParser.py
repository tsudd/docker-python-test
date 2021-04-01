from custom_packages.parser_factory.Parser import Parser
import custom_packages.serializers.tsuddjson as custom_json


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