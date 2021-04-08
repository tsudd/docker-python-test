import toml
from serilizer_lib.serializer.serilization.proc_complex import serialize_obj, deserialize_obj

CONS = 222


def dumps(s):
    return toml.dumps(s)


def dump(s, fp):
    s = toml.dumps(s)
    fp.write(s)


def load(fp):
    return fp.load(fp)


def loads(s):
    return toml.loads(s)


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

    sum.__setattr__("nice", solve)
    sum.__setattr__("num", 228)
    # print(dumps(sum))
    # print(yaml.dump(sum))
    ass = {"cool": ["228", "nice"], "gogo": {"good": "boy", "nice": 229, "func": sum, "dont": {"lol": 20.9}}}
    b = serialize_obj(ass)
    assss = deserialize_obj(b)
    assss["gogo"]["func"](2, 2)
    pass
