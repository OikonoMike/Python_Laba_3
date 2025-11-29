from src.data_structure import Queue, Stack


# --------------------Stack--------------------
def test_stack_push_pop():
    s = Stack()
    s.push(5)
    s.push(10)
    assert s.pop() == 10
    assert s.pop() == 5


def test_stack_peek():
    s = Stack()
    s.push(42)
    assert s.peek() == 42


def test_stack_min():
    s = Stack()
    s.push(5)
    s.push(2)
    s.push(10)
    assert s.min() == 2
    s.pop()  # удаляем 10
    assert s.min() == 2
    s.pop()  # удаляем 2
    assert s.min() == 5


def test_stack_empty():
    s = Stack()
    assert s.is_empty() is True
    s.push(1)
    assert s.is_empty() is False


def test_stack_len():
    s = Stack()
    assert len(s) == 0
    s.push(1)
    s.push(2)
    assert len(s) == 2
    s.pop()
    assert len(s) == 1


def test_stack_min_with_duplicates():
    s = Stack()
    s.push(3)
    s.push(1)
    s.push(1)
    s.push(2)
    assert s.min() == 1
    s.pop()  # удаляем 2
    assert s.min() == 1
    s.pop()  # удаляем 1
    assert s.min() == 1
    s.pop()  # удаляем 1
    assert s.min() == 3


def test_stack_pop_empty_raises():
    s = Stack()
    try:
        s.pop()
        assert False, "Expected IndexError"
    except IndexError as e:
        assert str(e) == "нельзя вернуть pop из пустого стека"


def test_stack_peek_empty_raises():
    s = Stack()
    try:
        s.peek()
        assert False, "Expected IndexError"
    except IndexError as e:
        assert str(e) == "нельзя вернуть peek из пустого стека"


def test_stack_min_empty_raises():
    s = Stack()
    try:
        s.min()
        assert False, "Expected IndexError"
    except IndexError as e:
        assert str(e) == "нельзя вернуть min из пустого стека"


# --------------------Queue--------------------
def test_queue_enqueue_dequeue():
    q = Queue()
    q.enqueue(1)
    q.enqueue(2)
    assert q.dequeue() == 1
    assert q.front() == 2
    assert q.dequeue() == 2


def test_queue_empty():
    q = Queue()
    assert q.is_empty() is True
    q.enqueue(5)
    assert q.is_empty() is False


def test_queue_len():
    q = Queue()
    assert len(q) == 0
    q.enqueue(10)
    q.enqueue(20)
    assert len(q) == 2
    q.dequeue()
    assert len(q) == 1


def test_queue_single_element():
    q = Queue()
    q.enqueue(99)
    assert q.front() == 99
    assert q.dequeue() == 99


def test_queue_dequeue_empty_raises():
    q = Queue()
    try:
        q.dequeue()
        assert False, "Expected IndexError"
    except IndexError as e:
        assert str(e) == "нельзя вернуть dequeue из пустой очереди"


def test_queue_front_empty_raises():
    q = Queue()
    try:
        q.front()
        assert False, "Expected IndexError"
    except IndexError as e:
        assert str(e) == "нельзя вернуть front из пустой очереди"
