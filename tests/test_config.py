DICT_RESULT = "{\'sosediOptions\': {\'marke\\\\\":tName\': \'Sosedi\', \'goodsURL\': \'https://sosedi.by/sales/\'," \
              " \'goodFields\': {\'pri    ce     \': True, \'priceBack\': \'priceBack\', \'sale\': " \
              "[22, 5.7, \'nice\', None]}}, \'greenOptions\': {\'ff\': 22.8, \'goodsURL\': " \
              "\'https://www.green-market.by/shares\', \'headers\': {\'accept-encoding\': \'gzip, deflate, br\'," \
              " \'x-requested-with\': \'XMLHttpRequest\'}, " \
              "\'formData\': \'page={0}&cat=\', " \
              "\'goodHTMLSection\': {\'class\': \'stock-preview-item\'}}, \'damn\': \'wtf\'}"

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

DATA_DICT = {"cool": ["228", "nice"], "gogo": {"good": True, "nice": 229, "dont": {"lol": 20.9}}, "next": None}
PARSED_DICT = "{ \"cool\": [ \"228\", \"nice\" ], \"gogo\": { \"good\": true," \
                       " \"nice\": 229, \"dont\": { \"lol\": 20.9 } }, \"next\": null }"


def sum_two_elements(a=0, b=0):
    rez = a + b
    print_equation(a, b, rez)
    return rez


def print_equation(a, b, c):
    print(f"{a} + {b} = {c}")


def fib_nums(n):
    if n < 1:
        return 1
    return fib_nums(n - 1) + fib_nums(n - 2)
