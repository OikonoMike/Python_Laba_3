class Stack:
    """Стек с поддержкой min() за O(1)"""

    def __init__(self):
        self._data = []
        self._min_stack = []

    def push(self, x: int) -> None:
        """Добавление элемента в стек"""
        if not isinstance(x, int):
            raise TypeError("Стек поддерживает только целые числа")
        self._data.append(x)
        if not self._min_stack or x <= self._min_stack[-1]:
            self._min_stack.append(x)

    def pop(self) -> int:
        """Удаление и возвращение верхнего элемента стека"""
        if self.is_empty():
            raise IndexError("нельзя вернуть pop из пустого стека")
        x = self._data.pop()
        if x == self._min_stack[-1]:
            self._min_stack.pop()
        return x

    def peek(self) -> int:
        """Возвращение верхнего элемента стека без удаления"""
        if self.is_empty():
            raise IndexError("нельзя вернуть peek из пустого стека")
        return self._data[-1]

    def min(self) -> int:
        """Минимальный элемент в стека"""
        if self.is_empty():
            raise IndexError("нельзя вернуть min из пустого стека")
        return self._min_stack[-1]

    def is_empty(self) -> bool:
        """Проверка на пустоту стека"""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в стеке"""
        return len(self._data)


class Queue:
    """Очередь на основе списка"""

    def __init__(self):
        self._data = []

    def enqueue(self, x: int) -> None:
        """Добавление элемента в конец очереди"""
        if not isinstance(x, int):
            raise TypeError("Очередь поддерживает только целые числа")
        self._data.append(x)

    def dequeue(self) -> int:
        """Удаление и возвращение первого элемента очереди"""
        if self.is_empty():
            raise IndexError("нельзя вернуть dequeue из пустой очереди")
        return self._data.pop(0)

    def front(self) -> int:
        """Возвращение первого элемента очереди без удаления"""
        if self.is_empty():
            raise IndexError("нельзя вернуть front из пустой очереди")
        return self._data[0]

    def is_empty(self) -> bool:
        """Проверка на пустоту очереди"""
        return len(self._data) == 0

    def __len__(self) -> int:
        """Количество элементов в очереди"""
        return len(self._data)
