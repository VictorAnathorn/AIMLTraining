
def count_alphabets(s):
    return sum([1 for char in s if char.isalpha()])


def test_count_alphabets():
    # Test case 1: String contains both lower and upper case alphabets
    assert count_alphabets("#aBdj12C") == 5

    # Test case 2: String contains only special characters and digits
    assert count_alphabets("123 !@#$") == 0

    # Test case 3: Empty string, should return 0
    assert count_alphabets("") == 0

    # Test case 4: String contains spaces and special characters, but also alphabets
    assert count_alphabets("A*B c D") == 4

    # Test case 5: String contains only lower case alphabets
    assert count_alphabets("abcdefghijklmnopqrstuvwxyz") == 26

    # Test case 6: String contains only upper case alphabets
    assert count_alphabets("ABCDEFGHIJKLMNOPQRSTUVWXYZ") == 26

    # Test case 7: String contains a mix of alphabets and digits
    assert count_alphabets("Hello123World") == 10

    print("All tests passed!")


test_count_alphabets()
