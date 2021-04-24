from serilizer_lib.parsers.json import tsuddjson
from serilizer_lib.parsers.json.exceptions import BadJSONException
from tests.test_config import DATA_DICT, JSON_FILE, DICT_RESULT, PARSED_DICT
import json


def test_simple_dict_dump():
    d = {"gooodNums": [22.34, 328, 228]}
    assert tsuddjson.dumps(d) == json.dumps(d)


def test_many_layers_dict_dump():
    d = {"TYPE":"function", "VALUE":{"__closure__":None, "__code__":{"TYPE":"code", "VALUE":{"__doc__":
            "code(argcount, posonlyargcount,  Not for the faint of heart.", "co_argcount":3,
            "co_cellvars":{"TYPE":"tuple", "VALUE":[]},
            "co_code":{"TYPE":"bytes", "VALUE":[116, 0, 124, 0, 155, 0, 100, 1, 124, 1, 155, 0, 100, 2, 124, 2, 155,
                                                0, 157, 5, 131, 1, 1, 0, 100, 0, 83, 0]}}}}}

    assert tsuddjson.dumps(d) == json.dumps(d)


def test_diff_types_dump():
    d = {"niceNone": None, "goodnums": [22.6, 33, 2e5], "ohhyes": True, "uegay": False}

    assert tsuddjson.dumps(d) == json.dumps(d)


def test_simple_dict_load():
    d = "{\"hi\": \"Hello pal!!!\", \"next phrases\": [\"Hi!\", \"Good morning\", \"ok\"]}"

    assert str(tsuddjson.loads(d)) == str(json.loads(d))


def test_many_layers_load():
    d = {"TYPE":"tuple", "VALUE":["a", "b", "rez"]}

    assert str(tsuddjson.loads(str(d))) == str(d)


def test_diff_types_load():
    d = {"niceNone": None, "goodnums": [22.6, 33, 2e5], "ohhyes": True, "uegay": False}

    assert str(tsuddjson.loads(str(d))) == str(d)


def test_exception():
    bad_string = "{\"hi\" Hello pal!!!\", \"next phrases\": [\"Hi!\", \"Good morning\", \"ok\"]}"

    try:
        rez = tsuddjson.loads(bad_string)
        assert 1 == 0
    except BadJSONException:
        assert 1 == 1
