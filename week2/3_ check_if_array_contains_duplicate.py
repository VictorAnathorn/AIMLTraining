def check_if_array_contains_duplicate(nums):
    seen = set()
    for n in nums:
        if n in seen:
            return True
        seen.add(n)
    return False

# Test cases


def test_check_if_array_contains_duplicate():
    # Test case 1: Array with duplicates
    assert check_if_array_contains_duplicate([10, 30, 10, 20]) == True

    # Test case 2: Array without duplicates
    assert check_if_array_contains_duplicate([5, 10, 15, 20]) == False

    # Additional test cases
    # Empty array
    assert check_if_array_contains_duplicate([]) == False

    # Array with single element
    assert check_if_array_contains_duplicate([10]) == False

    # Large array with no duplicates
    assert check_if_array_contains_duplicate(list(range(100000))) == False

    # Large array with a duplicate at the end
    nums = list(range(100000)) + [99999]
    assert check_if_array_contains_duplicate(nums) == True

    # Array with negative numbers and duplicates
    assert check_if_array_contains_duplicate([-1, -2, -3, -1]) == True


print("All tests passed!")
