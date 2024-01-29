
def pair_sum_sorted_array(numbers, target):

    if len(numbers) < 2:
        return [-1, -1]

    left = 0
    right = len(numbers) - 1

    while left < right:
        s = numbers[left] + numbers[right]

        if s == target:
            return [left, right]

        elif s < target:
            left += 1
        else:
            right -= 1

    return [-1, -1]


def test_pair_sum_sorted_array():
    # Test case 1: Sorted array [1, 2, 3, 5, 10] with target 7, indices [1, 3] should sum up to 7
    assert pair_sum_sorted_array([1, 2, 3, 5, 10], 7) == [1, 3]

    # Test case 2: Sorted array [1, 2, 3, 5, 10] with target 13, indices [2, 4] should sum up to 13
    assert pair_sum_sorted_array([1, 2, 3, 5, 10], 13) == [2, 4]

    # Test case 3: Sorted array [1, 2, 3, 5, 10] with target 4, indices [0, 2] should sum up to 4
    assert pair_sum_sorted_array([1, 2, 3, 5, 10], 4) == [0, 2]

    # Test case 4: Sorted array [1, 2, 3, 5, 10] with target 20, no answer exists, should return [-1, -1]
    assert pair_sum_sorted_array([1, 2, 3, 5, 10], 20) == [-1, -1]

    # Test case 5: Sorted array [1, 2, 2, 5, 10] with target 4, indices [0, 2] should sum up to 4
    assert pair_sum_sorted_array([1, 2, 2, 5, 10], 4) == [1, 2]

    # Test case 6: Sorted array with negative numbers [-10, -5, 0, 2, 7] with target -15, indices [0, 4] should sum up to -15
    assert pair_sum_sorted_array([-10, -5, 0, 2, 7], -15) == [0, 1]

    # Test case 7: Sorted array with duplicate elements [1, 1, 2, 2, 3, 3, 4, 4] with target 5, indices [2, 3] should sum up to 5
    assert pair_sum_sorted_array([1, 1, 2, 2, 3, 3, 4, 4], 5) == [0, 7]

    print("All tests passed!")


test_pair_sum_sorted_array()
