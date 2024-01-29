
def find_first_occurrence(s, to_find):
    for index in range(len(s)):
        if s[index] == to_find:
            return index
    return -1


def test_find_first_occurrence():
    # Test case 1: Character 'e' is present at index 3
    assert find_first_occurrence("interview", "e") == 3

    # Test case 2: Character 'n' is not present in the string
    assert find_first_occurrence("kickstart", "n") == -1

    # Test case 3: Character 'a' is present at index 0
    assert find_first_occurrence("alphabet", "a") == 0

    # Test case 4: Character 'o' is present at index 4
    assert find_first_occurrence("programming", "o") == 2

    # Test case 5: Empty string, should return -1
    assert find_first_occurrence("", "x") == -1

    # Test case 6: String with only the character 'x'
    assert find_first_occurrence("xxxxx", "x") == 0

    # Test case 7: String with repeated characters, 'l' is present at index 2
    assert find_first_occurrence("hello world", "l") == 2

    print("All tests passed!")


test_find_first_occurrence()
