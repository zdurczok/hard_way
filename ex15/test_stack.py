from stack import *

def test_push():
    colors = Stack()
    colors.push("Magenta")
    assert colors.count() == 1
    colors.push("Cyan")
    assert colors.count() == 2

def test_pop():
    colors = Stack()
    colors.push("Cadmium Red Light")
    colors.push("Hansa Yellow")
    assert colors.pop() == "Hansa Yellow"
    assert colors.pop() == "Cadmium Red Light"
    assert colors.pop() == None

def test_top():
    colors = Stack()
    colors.push("Gelb")
    assert colors.first() == "Gelb"
    colors.push("Rosarot")
    assert colors.first() == "Rosarot"
    colors.pop()
    colors.pop()
    assert colors.first() == None
