from src.func_sort import (bubble_sort, bucket_sort, counting_sort, heap_sort,
                           quick_sort, radix_sort)


# --------------------bubble_sort--------------------
def test_bubble_sort_normal():
    assert bubble_sort([3, 1, 2]) == [1, 2, 3]


def test_bubble_sort_empty():
    assert bubble_sort([]) == []


def test_bubble_sort_single():
    assert bubble_sort([42]) == [42]


def test_bubble_sort_duplicates():
    assert bubble_sort([5, 2, 5, 2, 8]) == [2, 2, 5, 5, 8]


# --------------------quick_sort--------------------
def test_quick_sort_normal():
    assert quick_sort([5, 2, 8, 1]) == [1, 2, 5, 8]


def test_quick_sort_empty():
    assert quick_sort([]) == []


def test_quick_sort_single():
    assert quick_sort([-7]) == [-7]


def test_quick_sort_many_duplicates():
    assert quick_sort([3, 3, 3, 3]) == [3, 3, 3, 3]


# --------------------counting_sort--------------------
def test_counting_sort_normal():
    assert counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]


def test_counting_sort_empty():
    assert counting_sort([]) == []


def test_counting_sort_single():
    assert counting_sort([100]) == [100]


def test_counting_sort_negative():
    assert counting_sort([-2, -1, 0, 1, 2]) == [-2, -1, 0, 1, 2]


# --------------------radix_sort--------------------
def test_radix_sort_normal():
    assert radix_sort([170, 45, 75, 90, 802, 24, 2, 66]) == [
        2,
        24,
        45,
        66,
        75,
        90,
        170,
        802,
    ]


def test_radix_sort_empty():
    assert radix_sort([]) == []


def test_radix_sort_single():
    assert radix_sort([123]) == [123]


def test_radix_sort_large_numbers():
    assert radix_sort([1000, 1, 9999, 10]) == [1, 10, 1000, 9999]


def test_radix_sort_negative_raises():
    try:
        radix_sort([1, -5, 3])
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "radix_sort не поддерживает отрицательные числа"


# --------------------bucket_sort--------------------
def test_bucket_sort_normal():
    result = bucket_sort([0.42, 0.32, 0.33, 0.52, 0.37, 0.47, 0.51])
    expected = [0.32, 0.33, 0.37, 0.42, 0.47, 0.51, 0.52]
    assert result == expected


def test_bucket_sort_empty():
    assert bucket_sort([]) == []


def test_bucket_sort_single():
    assert bucket_sort([0.5]) == [0.5]


def test_bucket_sort_many_elements():
    arr = [i / 100.0 for i in range(99, -1, -1)]  # [0.99, 0.98, ..., 0.0]
    assert bucket_sort(arr) == sorted(arr)


def test_bucket_sort_out_of_range_raises():
    try:
        bucket_sort([1.5])
        assert False, "Expected ValueError"
    except ValueError as e:
        assert str(e) == "bucket_sort ожидает числа в диапазоне [0, 1)"


# --------------------heap_sort--------------------
def test_heap_sort_normal():
    assert heap_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]


def test_heap_sort_empty():
    assert heap_sort([]) == []


def test_heap_sort_single():
    assert heap_sort([999]) == [999]


def test_heap_sort_reverse_sorted():
    assert heap_sort([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10]
