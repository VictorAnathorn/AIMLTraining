def reverse_words(s):
    return " ".join(s.split()[::-1])

# Test cases


def test_reverse_words():
    # Test case 1: Multiple words
    assert reverse_words(
        "best technical interview prep courses") == "courses prep interview technical best"

    # Test case 2: Single word
    assert reverse_words("kickstart") == "kickstart"

    # Additional test cases
    # String with leading and trailing spaces
    assert reverse_words("  hello world  ") == "world hello"

    # String with multiple spaces between words
    assert reverse_words("a   b c    d") == "d c b a"

    # Empty string
    assert reverse_words("") == ""

    # String with all spaces
    assert reverse_words("     ") == ""

    # String with punctuation
    assert reverse_words("Hello, world!") == "world! Hello,"


print("All tests passed!")
