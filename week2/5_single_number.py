def single_number(arr):
    x = 0
    for n in arr:
        x = x ^ n
    return x

# Test cases


def test_single_number():
    # Test case 1: Unique number present in the middle
    assert single_number([2, 1, 2, 5, 1]) == 5

    # Test case 2: Unique number at the beginning
    assert single_number([7, 3, 3, 4, 4]) == 7

    # Test case 3: Unique number at the end
    assert single_number([6, 6, 9, 9, 11]) == 11

    # Additional test cases
    # Single element
    assert single_number([10]) == 10

    # Negative numbers
    assert single_number([-1, -1, -2]) == -2

    # Large array
    large_array = [i for i in range(10000)] * 2 + [12345]
    assert single_number(large_array) == 12345


print("All tests passed!")
