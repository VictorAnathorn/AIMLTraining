def insert_element_at_position(nums, element, position):
    return nums[:position - 1] + [element] + nums[position - 1:]

# Test cases


def test_insert_element_at_position():
    # Test case 1
    assert insert_element_at_position([2, 4, 5, 6, -1], 3, 2) == [2, 3, 4, 5, 6]

    # Test case 2
    assert insert_element_at_position([70, 60, 50, -1], 40, 4) == [70, 60, 50, 40]

    # Additional test cases
    # Insert at the beginning
    assert insert_element_at_position([-1], 10, 1) == [10]

    # Insert at the end (excluding -1)
    assert insert_element_at_position([1, 2, 3, -1], 4, 4) == [1, 2, 3, 4]

    # Insert in the middle
    assert insert_element_at_position([1, 2, 4, 5, -1], 3, 3) == [1, 2, 3, 4, 5]


print("All tests passed!")
