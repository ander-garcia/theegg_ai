import pytest
from searcher import Searcher


def test_sort():
    tool = Searcher([4, 3, 2, 1])
    assert tool.sort() == [1, 2, 3, 4]
    tool = Searcher([3, 56, 21, 33, 874, 123, 66, 1000,
                     23, 45, 65, 56])
    assert tool.sort() == [3, 21, 23, 33, 45, 56, 56, 65, 66, 123, 874, 1000]


def test_binary_search():
    tool = Searcher([1, 2, 3, 4])
    assert tool.binary_search(3) == [2, 3]
    tool = Searcher([3, 21, 23, 33, 45, 56, 56, 65, 66, 123, 874, 1000])
    assert tool.binary_search(874) == [9, 3]


def test_secuential_search():
    tool = Searcher([1, 2, 3, 4])
    assert tool.secuential_search(3) == [2, 3]
    tool = Searcher([3, 21, 23, 33, 45, 56, 56, 65, 66, 123, 874, 1000])
    assert tool.secuential_search(874) == [9, 3]
