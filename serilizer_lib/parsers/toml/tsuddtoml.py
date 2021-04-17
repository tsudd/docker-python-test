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
    replace_values(s, None, NULL_STRING)
    pp = toml.dumps(s)
    fp.write(pp)


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

def sum_two_elements(a=0, b=0):
    rez = a + b
    print_equation(a, b, rez)
    return rez


def print_equation(a, b, c):
    print(f"{a} + {b} = {c}")


def dd(a=2, b=3):
    c = a + b
    return c


def solve():
    par = JSONParser()
    fs = open("rez.json", "r")
    a = dd.__code__
    b = sum_two_elements.__globals__
    o = par.loads('{"niceNone": null, "goodnums": [22.6, 33, 2e5], "ohhyes": true, "uegay": false}')
    fs.close()
    pass
