from queue import *

def test_shift():
    colors = Queue()
    colors.shift("Magenta")
    assert colors.count() == 1
    colors.shift("Cyan")
    assert colors.count() == 2

def test_unshift():
    colors = Queue()
    colors.shift("Magenta")
    colors.shift("Cyan")
    colors.shift("Lila")
    assert colors.unshift() == "Magenta"
    assert colors.unshift() == "Cyan"
    assert colors.unshift() == "Lila"
    assert colors.unshift() == None

def test_first():
    colors = Queue()
    colors.shift("Lila")
    assert colors.first() == "Lila"
    colors.shift("Azorubine")
    assert colors.first() == "Lila"
    colors.shift("Azorubine")
    assert colors.first() == "Lila"

def test_last():
    colors = Queue()
    colors.shift("Lila")
    assert colors.last() == "Lila"
    colors.shift("Azorubine")
    assert colors.last() == "Azorubine"
    colors.shift("Cyan")
    assert colors.last() == "Cyan"

test_shift()
test_unshift()
test_first()
test_last()
