from local_packages.serializers import tsuddjson

DICT_RESULT = "{\'sosediOptions\': {\'marke\\\\\":tName\': \'Sosedi\', \'goodsURL\': \'https://sosedi.by/sales/\'," \
              " \'goodFields\': {\'pri    ce     \': True, \'priceBack\': \'priceBack\', \'sale\':" \
              " [22, 5.7, \'nice\', None]}}, \'greenOptions\': {\'ff\': 22.8," \
              " \'goodsURL\': \'https://www.green-market.by/shares\', \'headers\': {\'accept-encoding\': \'gzip, deflate, br\'," \
              " \'x-requested-with\': \'XMLHttpRequest\'}, \'formData\': \'page={0}&cat=\'," \
              " \'goodHTMLSection\': {\'class\': \'stock-preview-item\'}}, \'damn\': \'wtf\'}"


def test_load():
    fp = open("example.json", "r")
    assert str(tsuddjson.load(fp)) == DICT_RESULT
    fp.close()


if __name__ == "__main__":
    test_load()
