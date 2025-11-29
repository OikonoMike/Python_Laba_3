def bubble_sort(sp: list[int]) -> list[int]:
    """Пузырьковая сортировка"""
    if not isinstance(sp, list):
        raise TypeError("Аргумент должен быть списком")
    if not sp:
        return []
    arr = sp[:]  # копия списка
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def quick_sort(sp: list[int]) -> list[int]:
    """Быстрая сортировка"""
    if not isinstance(sp, list):
        raise TypeError("Аргумент должен быть списком")
    if len(sp) <= 1:
        return sp[:]
    pivot = sp[len(sp) // 2]
    left = [x for x in sp if x < pivot]
    middle = [x for x in sp if x == pivot]
    right = [x for x in sp if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


def counting_sort(sp: list[int]) -> list[int]:
    """Сортировка подсчётом"""
    if not isinstance(sp, list):
        raise TypeError("Аргумент должен быть списком")
    if not sp:
        return []
    min_val = min(sp)
    max_val = max(sp)
    count = [0] * (max_val - min_val + 1)
    for num in sp:
        count[num - min_val] += 1
    result = []
    for i, freq in enumerate(count):
        result.extend([i + min_val] * freq)
    return result


def radix_sort(sp: list[int], base: int = 10) -> list[int]:
    """Поразрядная сортировка"""
    if not isinstance(sp, list):
        raise TypeError("Аргумент должен быть списком")
    if not sp:
        return []
    if any(x < 0 for x in sp):
        raise ValueError("radix_sort не поддерживает отрицательные числа")
    arr = sp[:]
    max_val = max(arr)
    exp = 1
    while max_val // exp > 0:
        buckets = [[] for _ in range(base)]
        for num in arr:
            digit = (num // exp) % base
            buckets[digit].append(num)
        arr = [x for bucket in buckets for x in bucket]
        exp *= base
    return arr


def bucket_sort(sp: list[float], buckets: int | None = None) -> list[float]:
    """Блочная сортировка для чисел в [0, 1)"""
    if not isinstance(sp, list):
        raise TypeError("Аргумент должен быть списком")
    if not sp:
        return []
    if any(x < 0.0 or x >= 1.0 for x in sp):
        raise ValueError("bucket_sort ожидает числа в диапазоне [0, 1)")
    n = len(sp)
    if buckets is None:
        buckets = n
    bucket_list = [[] for _ in range(buckets)]
    for x in sp:
        idx = min(int(x * buckets), buckets - 1)
        bucket_list[idx].append(x)
    for b in bucket_list:
        b.sort()  # разрешено для вёдер
    result = []
    for b in bucket_list:
        result.extend(b)
    return result


def _heapify(arr: list[int], n: int, i: int) -> None:
    """Вспомогательная функция для heap_sort: просеивание вниз"""
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        _heapify(arr, n, largest)


def heap_sort(sp: list[int]) -> list[int]:
    """Пирамидальная сортировка"""
    if not isinstance(sp, list):
        raise TypeError("Аргумент должен быть списком")
    if not sp:
        return []
    arr = sp[:]
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        _heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        _heapify(arr, i, 0)

    return arr
