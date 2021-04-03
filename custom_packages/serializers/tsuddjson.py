import re

GLOBAL_OBJ_REGEX = "^{([\w\W]*}$)"
GLOBAL_ARRAY_REGEX = "^\[([\w\W]*)\]$"

CLASS_TYPE_REGEX = "\'([\w\W]+)\'"
META_METHOD = "__[\w]+__"

FILE_ENCODING = 'UTF-8'

JSON_TRUE = "true"
JSON_FALSE = "false"
JSON_NAN = "null"

FIELDS_SEPARATOR = ","
FIELDS_VALUE_SEPARATOR = ":"
OBJECT_START = "{"
OBJECT_END = "}"
ARRAY_START = "["
ARRAY_END = "]"


class BadJSONException(Exception, BaseException):
    def __init__(self, message=None):
        super().__init__(self)

        if not message is None:
            print(message)
            self.__str__()

    def __str__(self):
        return "Error while parsing: bad JSON."


def dump(obj, fp):
    s = dumps(obj)

    fp.write(s)


def dumps(obj):
    def dump_complex(complex_obj):
        ans = ""
        tp = type(complex_obj)
        if tp == dict:
            ans += f"{OBJECT_START} "
            for name, o in complex_obj.items():
                ans += f"\"{name}\": "
                ans += dump_obj(o)
                if list(complex_obj.keys())[-1] != name:
                    ans += f"{FIELDS_SEPARATOR} "
            ans += f" {OBJECT_END}"
        elif tp == list or tp == tuple:
            ans += "[ "
            for o in complex_obj:
                ans += dump_obj(o)
                if o != complex_obj[-1]:
                    ans += f"{FIELDS_SEPARATOR} "
            ans += " ]"
        else:
            ans += f"{OBJECT_START} "
            ans += f"\"\": " + "\"" + re.search(CLASS_TYPE_REGEX, str(tp)).group(1) + f"{FIELDS_SEPARATOR} "
            fields = dir(complex_obj)


        return ans

    def dump_obj(o):
        string = ""
        tp = type(o)
        if tp == bool:
            if o:
                string += JSON_TRUE
            else:
                string += JSON_FALSE
        elif o is None:
            string += JSON_NAN
        elif tp == int or tp == float:
            string += str(o)
        elif tp != str:
            string += dump_complex(o)
        else:
            string += "\"" + str(o) + "\""

        return string

    s = dump_complex(obj)
    return s


def load(fp):
    if fp.encoding != FILE_ENCODING:
        raise ValueError

    s = fp.read()
    fp.close()

    return loads(s)


def loads(s):
    if not isinstance(s, str):
        raise ValueError

    ind = 0

    def parse_complex(s, index=-1):
        if not (isinstance(s, str) or isinstance(index, int)):
            raise ValueError

        nonlocal ind
        ind = index + 1
        ans = {}
        field_name = ""
        value = ""
        is_field = True
        is_value = False
        value_quotes = False
        quotes = False
        while ind < len(s):
            if not quotes and s[ind].isspace():
                ind += 1
                continue

            if s[ind] == '\"':
                if is_field and not quotes:
                    if len(field_name) != 0:
                        raise BadJSONException()
                    quotes = True
                elif is_field and quotes:
                    if s[ind - 1] == '\\':
                        field_name += s[ind]
                    else:
                        quotes = False
                elif is_value and not quotes:
                    if len(value) != 0:
                        raise Exception
                    else:
                        quotes = value_quotes = True
                elif is_value and quotes:
                    if s[ind - 1] == '\\':
                        value += s[ind]
                    quotes = False

            elif not quotes:
                if s[ind] == FIELDS_VALUE_SEPARATOR:
                    is_field = not is_field
                    is_value = not is_value

                elif s[ind] == ARRAY_START:
                    value = parse_array(s, ind)

                elif s[ind] == FIELDS_SEPARATOR and is_value:
                    if not value_quotes and isinstance(value, str):
                        value = try_parse(value)
                    ans[field_name] = value
                    field_name = ""
                    value = ""
                    value_quotes = False
                    is_field = True
                    is_value = False

                elif s[ind] == '.' and is_value:
                    if not s[ind + 1].isdigit() or '.' in value:
                        raise BadJSONException()
                    value += s[ind]

                elif s[ind] == OBJECT_START:
                    if len(value) != 0:
                        raise BadJSONException()
                    ans[field_name] = parse_complex(s, ind)
                    field_name = ""
                    value_quotes = False
                    is_value = False
                    is_field = True

                elif s[ind] == OBJECT_END:
                    if field_name != "":
                        if not value_quotes and isinstance(value, str):
                            value = try_parse(value)

                        ans[field_name] = value

                    ind += 1
                    break
                elif is_value:
                    value += s[ind]

            elif is_field:
                field_name += s[ind]
            elif is_value:
                value += s[ind]

            ind += 1

        return ans

    def parse_array(s, index=-1):
        if not (isinstance(s, str) or isinstance(index, int)):
            raise ValueError

        nonlocal ind
        ind = index + 1
        ans = []
        value = ""
        quotes = False
        value_quotes = False
        while ind < len(s):
            if not quotes and s[ind].isspace():
                ind += 1
                continue

            if s[ind] == '\"':
                if not quotes:
                    if len(value) != 0:
                        raise BadJSONException()
                    quotes = True
                    value_quotes = True
                elif quotes:
                    quotes = False

            elif not quotes:

                if s[ind] == '.':
                    if not s[ind + 1].isdigit() or '.' in value:
                        raise BadJSONException()
                    value += s[ind]

                elif s[ind] == FIELDS_VALUE_SEPARATOR:
                    if not value_quotes and isinstance(value, str):
                        value = try_parse(value)
                    ans.append(value)
                    value = ""
                    value_quotes = False

                elif s[ind] == OBJECT_START:
                    value = parse_complex(s, ind + 1)

                elif s[ind] == ARRAY_END:
                    if not value_quotes and isinstance(value, str):
                        value = try_parse(value)

                    ans.append(value)
                    break
                else:
                    value += s[ind]
            else:
                value += s[ind]

            ind += 1

        return ans

    def try_parse(value):
        val = ""

        try:
            if value == JSON_FALSE:
                val = False
            elif value == JSON_TRUE:
                val = True
            elif value == JSON_NAN:
                val = None
            elif isinstance(value, str) and value.isnumeric():
                val = int(value)
            else:
                val = float(value)
        except Exception:
            raise BadJSONException()

        return val

    match = re.search(GLOBAL_OBJ_REGEX, s.strip())
    ans = {}
    if not match is None:
        ans = parse_complex(match.group(1))
    else:
        match = re.search(GLOBAL_ARRAY_REGEX, s.strip())
        if not match is None:
            ans = parse_array(match.group(0))
        else:
            raise BadJSONException()

    return ans


def solve():
    pass


if __name__ == '__main__':
    solve()
