
def uppercase_to_lowercase(s):
    return s.lower()


def test_uppercase_to_lowercase():
    # Test case 1: Mixed case string
    assert uppercase_to_lowercase("InTerView") == "interview"

    # Test case 2: All uppercase string
    assert uppercase_to_lowercase("KICKSTART") == "kickstart"

    # Test case 3: Empty string, should return an empty string
    assert uppercase_to_lowercase("") == ""

    # Test case 4: String with no uppercase characters
    assert uppercase_to_lowercase("lowercase") == "lowercase"

    # Test case 5: String with spaces, mixed case, and special characters
    assert uppercase_to_lowercase("HeLLo, WoRLD!") == "hello, world!"

    # Test case 6: String with numbers and symbols, no change to non-alphabetic characters
    assert uppercase_to_lowercase("1234!@#$%^") == "1234!@#$%^"

    print("All tests passed!")


test_uppercase_to_lowercase()
