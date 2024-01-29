def reverse_array(nums):
    return nums[::-1]

# Test cases


def test_reverse_array():
    # Test empty array
    assert reverse_array([]) == []

    # Test array with single element
    assert reverse_array([1]) == [1]

    # Test array with two elements
    assert reverse_array([1, 2]) == [2, 1]

    # Test array with multiple elements
    assert reverse_array([1, 2, 3, 4, 5]) == [5, 4, 3, 2, 1]

    # Test array with negative numbers
    assert reverse_array([-1, -2, -3, -4, -5]) == [-5, -4, -3, -2, -1]

    # Test array with mixed numbers
    assert reverse_array([1, -2, 3, -4, 5]) == [5, -4, 3, -2, 1]

    # Test with strings (assuming function can handle strings)
    assert reverse_array(["a", "b", "c"]) == ["c", "b", "a"]


print("All tests passed!")
