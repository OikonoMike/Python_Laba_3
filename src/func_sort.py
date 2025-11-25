def bubble_sort(sp: list[int]) -> list[int]:
    """Пузырьковая сортировка"""
    for i in range(len(sp) - 1):
        for j in range(len(sp) - 1 - i):
            if sp[j] > sp[j + 1]:
                sp[j], sp[j + 1] = sp[j + 1], sp[j]
    return sp


def quick_sort(a: list[int]) -> list[int]:
    """Быстрая сортировка"""
    if len(a) <= 1:
        return a
    pivot = a[len(a) // 2]
    left = [x for x in a if x < pivot]
    middle = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def counting_sort(a: list[int]) -> list[int]:
    """Сортировка подсчетом"""
    if not a:
        return []
    min_val, max_val = min(a), max(a)
    range_of_values = max_val - min_val + 1
    count = [0] * range_of_values

    for num in a:
        count[num - min_val] += 1

    result = []
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)
    return result

