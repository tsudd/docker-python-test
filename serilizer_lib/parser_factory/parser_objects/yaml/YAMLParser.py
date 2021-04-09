from serilizer_lib.parser_factory.parser_objects.Parser import Parser
import serilizer_lib.parsers.yaml.tsuddyaml as custom_yaml


class YAMLParser(Parser):
    """
        parser_objects for ".yaml" format, which uses custom library.
    """

    def dump(self, obj, fp):
        """
        Classic dump to serialize object and put the result to file.
        """
        simple = self.serializer.serialize_obj(obj)
        return custom_yaml.dump(simple, fp)

    def dumps(self, obj):
        """
        Returns string with serialized object.
        """
        simple = self.serializer.serialize_obj(obj)
        return custom_yaml.dumps(simple)

    def load(self, fp):
        """
        Returns parsed object and data from the file.
        """
        raw_input = custom_yaml.load(fp)
        return self.serializer.deserialize_obj(raw_input)

    def loads(self, s):
        """
        Returns parsed object and data from the string.
        """
        raw_input = custom_yaml.loads(s)
        return self.serializer.deserialize_obj(raw_input)
