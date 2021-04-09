from serilizer_lib.parser_factory.parser_objects.Parser import Parser
import serilizer_lib.parsers.json.tsuddjson as custom_json


class JSONParser(Parser):
    """
        Parser for ".json" format, which uses custom library.
    """

    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put the result to file.
        """
        simple = self.serializer.serialize_obj(obj)
        return custom_json.dump(simple, fp)

    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        simple = self.serializer.serialize_obj(obj)
        return custom_json.dumps(simple)

    def load(self, fp):
        """
        Returns parsed object and data from the file.
        """
        raw_object = custom_json.load(fp)
        return self.serializer.deserialize_obj(raw_object)

    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        raw_object = custom_json.loads(s)
        return self.serializer.deserialize_obj(raw_object)