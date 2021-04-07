from lib.parsers.json import tsuddjson

DICT_RESULT = "{\'sosediOptions\': {\'marke\\\\\":tName\': \'Sosedi\', \'goodsURL\': \'https://sosedi.by/sales/\'," \
              " \'goodFields\': {\'pri    ce     \': True, \'priceBack\': \'priceBack\', \'sale\':" \
              " [22, 5.7, \'nice\', None]}}, \'greenOptions\': {\'ff\': 22.8," \
              " \'goodsURL\': \'https://www.green-market.by/shares\'," \
              " \'headers\': {\'accept-encoding\': \'gzip, deflate, br\'," \
              " \'x-requested-with\': \'XMLHttpRequest\'}, \'formData\': \'page={0}&cat=\'," \
              " \'goodHTMLSection\': {\'class\': \'stock-preview-item\'}}, \'damn\': \'wtf\'}"

JSON_FILE = """{
  "sosediOptions": {
    "marke\\\":tName": "Sosedi",
    "goodsURL": "https://sosedi.by/sales/",
    "goodFields": {
      "pri    ce     ": true,
      "priceBack": "priceBack",
      "sale": [22, 5.7, "nice", null]
    }
  },
  "greenOptions": {
    "ff": 22.8,
    "goodsURL": "https://www.green-market.by/shares",\
    "headers": {
      "accept-encoding": "gzip, deflate, br",
      "x-requested-with": "XMLHttpRequest"
    },
    "formData": "page={0}&cat=",
    "goodHTMLSection": {
      "class": "stock-preview-item"
    }
    },
  "damn": "wtf"
}"""

SERIALIZED_OBJECT = "[ { \"class\": \"tests.test_json.test_dumps.<locals>.TestClass\", " \
                    "\"fields\": {\"inst_attr\": { \"class\": \"tests.test_json.test_dumps.<locals>.TestClass\", " \
                    "\"fields\": {\"sum\": { \"class\": \"method\", \"fields\": { }}, " \
                    "\"test_number\": 228, \"write_hello\": { \"class\": \"method\", \"fields\": { }} }}, " \
                    "\"sum\": { \"class\": \"method\", \"fields\": { }}, \"test_number\": 228, " \
                    "\"write_hello\": { \"class\": \"method\", \"fields\": { }} }}, { \"class\": " \
                    "\"tests.test_json.test_dumps.<locals>.TestClass\", \"fields\": {\"sum\": " \
                    "{ \"class\": \"method\", \"fields\": { }}, \"test_number\": 228, " \
                    "\"write_hello\": { \"class\": \"method\", \"fields\": { }} }} ]"


def test_loads():
    assert str(tsuddjson.loads(JSON_FILE)) == DICT_RESULT


def test_dumps():

    class TestClass():
        test_number = 228

        def write_hello(self):
            print("Hello, this it test!")

        def sum(self, a, b):
            return a + b

    inst1 = TestClass()
    inst2 = TestClass()

    inst2.__setattr__("inst_attr", inst1)

    arr = [inst2, inst1]
    assert tsuddjson.dumps(arr) == SERIALIZED_OBJECT
    
    
    
    



