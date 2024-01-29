from collections import defaultdict


def majority_element(nums):

    threshold = len(nums) // 2

    frequency = defaultdict(int)

    for n in nums:
        frequency[n] += 1
        if frequency[n] >= threshold:
            return n

    return 0


def test_majority_element():
    # Test case 1: List with majority element 3
    assert majority_element([3, 3, 3, 2, 2, 2, 3]) == 3

    # Test case 2: List with majority element 2,
    assert majority_element([2, 2, 2, 3, 3, 3, 3]) == 2

    # Test case 3: List with majority element 5
    assert majority_element([1, 5, 5, 5, 2, 5, 5]) == 5

    # Test case 4: List with majority element 1
    assert majority_element([1, 1, 2, 2, 1, 1, 1]) == 1

    # Test case 5: List with negative numbers and majority element -5
    assert majority_element([-10, -10, -5, -5, -5, -10, -10]) == -5

    # Test case 6: List with single element
    assert majority_element([7]) == 7

    # Test case 7: List with two different elements, should return one of them
    assert majority_element([8, 9]) == 8

    # Test case 8: List with the same element repeated multiple times
    assert majority_element([3, 3, 3, 3, 3, 3, 3, 3, 3, 3]) == 3

    print("All tests passed!")


test_majority_element()
