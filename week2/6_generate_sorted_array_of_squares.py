def generate_sorted_array_of_squares(numbers):
    squares = []

    left = 0
    right = len(numbers) - 1

    while left <= right:
        if numbers[left]**2 < numbers[right]**2:
            squares.append(numbers[right]**2)
            right -= 1
        else:
            squares.append(numbers[left]**2)
            left += 1
    squares.reverse()
    return squares

# Test cases


def test_generate_sorted_array_of_squares():
    # Test case 1: Positive numbers only
    assert generate_sorted_array_of_squares([1, 2, 3, 4]) == [1, 4, 9, 16]

    # Test case 2: Mix of negative and positive numbers
    assert generate_sorted_array_of_squares([-9, -5, -2, 0, 3, 7]) == [0, 4, 9, 25, 49, 81]

    # Additional test cases
    # Single element
    assert generate_sorted_array_of_squares([5]) == [25]

    # All negative numbers
    assert generate_sorted_array_of_squares([-4, -3, -1]) == [1, 9, 16]

    # All positive numbers in decreasing order
    assert generate_sorted_array_of_squares([10, 5, 2]) == [4, 25, 100]

    # Large array
    large_array = [i for i in range(-10000, 10001)]
    large_array_result = [i**2 for i in range(10000, -1, -1)] * 2 + [0]
    assert generate_sorted_array_of_squares(large_array) == large_array_result


print("All tests passed!")
