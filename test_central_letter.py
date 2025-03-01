from central_letter import central_letter

def test_central_letter():
    assert central_letter("variant") == "i"
    assert central_letter("andEkas") == "E"
    assert central_letter("Termos") == False
    assert central_letter("python") == False  # Even-length word
    assert central_letter("middle") == "d"  # Odd-length word
    assert central_letter("a") == "a"  # Single character case
    assert central_letter("") == False  # Empty string case
