import pytest
from palabras import invertir_palabras

testdata = [
    (["aa ss", "qq ww"], ["ss aa", "ww qq"]),
    (["this is a test", "foobar", "all your base"],
     ["test a is this", "foobar", "base your all"])
]


@ pytest.mark.parametrize("frases,frases_invertidas", testdata)
def test_palabras(frases, frases_invertidas):
    result = invertir_palabras(frases)
    assert result == frases_invertidas
