import pytomlpp as toml
from serilizer_lib.serializer.serilization.proc_complex import serialize_obj, deserialize_obj
from serilizer_lib.parser_factory.parser_objects.json.JSONParser import JSONParser
from serilizer_lib.parser_factory.parser_objects.yaml.YAMLParser import YAMLParser
from serilizer_lib.parser_factory.parser_objects.toml.TOMLParser import TOMLParser

from serilizer_lib.parsers.toml.toml_config import *

CONS = 222


def dumps(d: dict):
    replace_values(d, None, NULL_STRING)
    return toml.dumps(d)


def dump(s, fp):
    s = toml.dumps(s)
    fp.write(s)


def load(fp):
    result = fp.load(fp)
    replace_values(result, NULL_STRING, None)
    return result


def loads(s):
    result = toml.loads(s)
    replace_values(result, NULL_STRING, None)
    return result


def replace_values(d: dict, comp_obj=None, repl_obj=NULL_STRING):
    for name, o in d.items():
        if type(o) == dict:
            replace_values(o, comp_obj, repl_obj)
        else:
            typ = type(o)
            if typ == list or typ == tuple:
                for i in range(len(o)):
                    if type(o[i]) == dict:
                        replace_values(o, comp_obj, repl_obj)
                    elif o[i] == comp_obj:
                        o[i] = repl_obj
            elif o == comp_obj:
                d[name] = repl_obj


def print_snth(a):
    print("nice")
    b = a * 5
    return b


def sum(a=0, b=0):
    n = 229
    print(CONS)
    n += 327
    print(n)
    print_snth(a)
    return a + b


def solve():
    noce = 99

    # sum.__setattr__("nice", solve)
    # sum.__setattr__("num", 228)
    # # print(dumps(sum))
    # # print(yaml.dump(sum))
    ass = {"cool": ["228", "nice"], "gogo": {"good": "boy", "nice": 229, "func": sum, "dont": {"lol": 20.9}}}
    # b = serialize_obj(ass)

    par = TOMLParser()
    aa = par.dumps(ass)
    b = sum.__closure__
    print(b)
    n = serialize_obj(ass)
    assss = par.loads(aa)
    assss["gogo"]["func"](2, 2)
    pass
