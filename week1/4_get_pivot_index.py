def get_pivot_index(numbers):
    left, right = 0, sum(numbers)

    for index in range(len(numbers)):
        if left == (right - numbers[index]):
            return index
        left += numbers[index]
        right -= numbers[index]

    return -1

# Test cases


def test_get_pivot_index():
    # Test case 1: Pivot index exists in the middle
    assert get_pivot_index([2, 3, 1, -1, 1, 1, 4]) == 2

    # Test case 2: No pivot index
    assert get_pivot_index([2, 3, 5]) == -1

    # Test case 3: Pivot index at the beginning
    assert get_pivot_index([0, 1, -1]) == 0

    # Additional test cases
    # Single element (pivot is the only index)
    assert get_pivot_index([10]) == 0

    # Pivot index at the end
    assert get_pivot_index([-1, 1, 0]) == 2

    # All elements are zero
    assert get_pivot_index([0, 0, 0, 0]) == 0

    # Large numbers with no pivot
    assert get_pivot_index([100000, -99999, 1, 2, 3, 4, 5]) == -1

    # Large numbers with a pivot
    assert get_pivot_index([100000, -99999, -1, 0]) == 2


print("All tests passed!")
