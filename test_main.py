import pytest
from main import binary_search

def test_target_found_in_middle():
    arr = [1, 2, 3, 4, 5]
    target = 3
    assert binary_search(arr, target) == 2

def test_target_found_in_right_half():
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 6
    assert binary_search(arr, target) == 5

def test_target_found_in_right_half():
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 5
    assert binary_search(arr, target) == 4

def test_target_found_in_left_half():
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 1
    assert binary_search(arr, target) == 0

def test_target_found_in_left_half():
    arr = [1, 2, 3, 4, 5, 6, 7]
    target = 2
    assert binary_search(arr, target) == 1

def test_empty_array():
    arr = []
    target = 3
    assert binary_search(arr, target) == -1