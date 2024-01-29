
def length_of_last_word(sentence):
    words = sentence.split()
    if len(words) == 0:
        return 0
    return len(words[-1])


def test_length_of_last_word():
    # Test case 1: Multiple words in the sentence, last word is "Kickstart" with length 9
    assert length_of_last_word("Interview Kickstart") == 9

    # Test case 2: Multiple words with leading and trailing spaces, last word is "World" with length 5
    assert length_of_last_word(" Hello World  ") == 5

    # Test case 3: Empty sentence, should return 0
    assert length_of_last_word("") == 0

    # Test case 4: Single word sentence, last word is "hello" with length 5
    assert length_of_last_word("hello") == 5

    # Test case 5: Sentence with spaces and special characters, last word is "1234" with length 4
    assert length_of_last_word("Hello, WoRLD! 1234") == 4

    # Test case 6: Sentence with no words, should return 0
    assert length_of_last_word("    ") == 0

    # Test case 7: Sentence with mixed case, last word is "INTerViEw" with length 9
    assert length_of_last_word("This is a Test INTerViEw") == 9

    print("All tests passed!")


test_length_of_last_word()
