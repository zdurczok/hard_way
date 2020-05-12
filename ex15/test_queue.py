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

def test_first():
    colors = Queue()
    colors.shift("Lila")
    assert colors.first() == "Lila"
    colors.shift("Azorubine")
    assert colors.first() == "Azorubine"
    colors.shift("Cyan")
    assert colors.first() == "Cyan"
