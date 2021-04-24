import yaml
from serilizer_lib.parsers.yaml.yaml_config import *

#own parser
# def dumps(s):
#     pass
#
#
# def dump(s, fp):
#     pass
#
#
# def load(fp):
#     pass
#
#
# def loads(s):
#
#     strings = s.split("\n")
#     ind = 0
#     depth = 0
#     def parse_obj(dep):
#         ans = {}
#         nonlocal strings
#         nonlocal ind
#         while ind < len(strings):
#             if strings[ind].strip().startswith(COMMENT_SYMBOL):
#                 ind += 1
#                 continue
#             if depth > get_depth(strings[ind]):
#                 break
#             elif strings[ind].count(NAME_VALUE_MATCHER) == 1:
#                 key, value = strings[ind].split(NAME_VALUE_MATCHER)
#                 ans[slice_string_with_depth(key, dep)] = value
#             elif strings[ind].endswith("}"):
#                 #regex for object seq
#                 pass
#             elif strings[ind].strip().endswith("]"):
#                 #regex for array seq
#                 pass
#             elif strings[ind].strip().startswith(BLOCK_SEQ_SEPARATOR):
#                 #parsing object of sequence
#                 pass
#             elif strings[ind].strip().endswith(NAME_OBJECT_MATCHER):
#                 name = strings[ind].split(NAME_OBJECT_MATCHER)[0]
#                 ind += 1
#                 ans[name] = parse_obj(dep + 1)
#                 continue
#
#             ind += 1
#
#         return ans
#
#     def get_depth(s):
#         ans = 0
#         for c in s:
#             if c != ' ':
#                 break
#             ans += 1
#
#         if ans % 2 != 0:
#             raise ValueError
#         return ans // 2
#
#
#     def slice_string_with_depth(s, dep):
#         return s[dep * 2:]
#
#
#     print(parse_obj(0))
#     return 228


def dump(obj, fp):
    s = dumps(obj)

    fp.write(s)


def dumps(obj):
    def dump_complex(o):
        ans = ""
        tp = type(o)
        ans = yaml.dump(o)
        # if tp == dict or tp == tuple or tp == list:
        #     ans += yaml.dump(o)
        # else:
        #     # ans += f"{COMPLEX_OBJECT_NAME}{NAME_OBJECT_MATCHER}{TAB_LITERAL}"
        #     # fields = dir(o)
        #     # ans += f"{TYPE_FIELD_NAME}{NAME_VALUE_MATCHER}{re.search(CLASS_TYPE_REGEX, str(tp)).group(1)}\n"
        #     # for field in fields:
        #     #     if re.match(META_METHOD, field) is None:
        #     #         ans += f"{TAB_LITERAL}{field}{NAME_VALUE_MATCHER}" + dump_obj(o.__getattribute__(field)) + "\n"

        return ans

    s = dump_complex(obj)
    return s


def load(fp):
    return yaml.load(fp, Loader=yaml.FullLoader)


def loads(s):
    return yaml.load(s, Loader=yaml.FullLoader)
