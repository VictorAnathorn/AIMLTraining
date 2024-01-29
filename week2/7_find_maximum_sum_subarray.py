def find_maximum_sum_subarray(numbers):
    max_sum = current_sum = numbers[0]

    for number in numbers[1:]:
        current_sum = max(number, current_sum + number)
        max_sum = max(max_sum, current_sum)

    return max_sum

# Test cases


def test_find_maximum_sum_subarray():
    # Test case 1: Mixed positive and negative numbers
    assert find_maximum_sum_subarray([2, -6, 3, 4, -5]) == 7

    # Test case 2: All negative numbers
    assert find_maximum_sum_subarray([-7, -9, -3, -5]) == -3

    # Additional test cases
    # Single element (positive)
    assert find_maximum_sum_subarray([10]) == 10

    # Single element (negative)
    assert find_maximum_sum_subarray([-10]) == -10

    # Large array
    large_array = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    assert find_maximum_sum_subarray(large_array) == 6

    # All positive numbers
    assert find_maximum_sum_subarray([1, 2, 3, 4, 5]) == 15

    # All zero
    assert find_maximum_sum_subarray([0, 0, 0, 0]) == 0


print("All tests passed!")
