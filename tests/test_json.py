from serilizer_lib.parsers.json import tsuddjson
from tests.test_config import DATA_DICT, JSON_FILE, DICT_RESULT, PARSED_DICT


def test_loads():
    assert str(tsuddjson.loads(JSON_FILE)) == DICT_RESULT


def test_dumps():
    assert tsuddjson.dumps(DATA_DICT) == str(PARSED_DICT)
