def test_equality():
    assert "helo" != "hi"


def test_comparison():
    assert 6 > 5

def test_mem():
    gang = ["akshat", "Tushar"]
    assert "akshat" in gang
    assert "Akshay" not in gang

