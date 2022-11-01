from paramio.saveformatting import SaveFormatting


def test_saveformatting_1():
    assert "{test}".format_map(SaveFormatting(test="result")) == "result"


def test_saveformatting_2():
    assert "{test_2}".format_map(SaveFormatting(test="result")) == "{test_2}"
