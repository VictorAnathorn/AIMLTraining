def get_intersection(numbers1, numbers2):
    intersection = []
    n1, n2 = 0, 0

    while n1 < len(numbers1) and n2 < len(numbers2):
        if numbers1[n1] == numbers2[n2]:
            if len(intersection) == 0 or intersection[-1] != numbers1[n1]:
                intersection.append(numbers1[n1])
            n1 += 1
            n2 += 1
        elif numbers1[n1] < numbers2[n2]:
            n1 += 1
        else:
            n2 += 1

    if len(intersection) > 0:
        return intersection
    return [-1]

# Test cases


def test_get_intersection():
    # Test case 1: Common elements present
    assert get_intersection([1, 2, 2, 6, 7], [2, 2, 7, 7]) == [2, 7]

    # Test case 2: No common elements
    assert get_intersection([5, 9, 11], [1, 4, 10, 12]) == [-1]

    # Additional test cases
    # Both arrays are empty
    assert get_intersection([], []) == [-1]

    # One array is empty
    assert get_intersection([], [1, 2, 3]) == [-1]

    # Common elements at the beginning
    assert get_intersection([1, 1, 2, 3], [1, 4, 5]) == [1]

    # Common elements at the end
    assert get_intersection([1, 3, 5], [2, 5, 6]) == [5]

    # Arrays with negative numbers
    assert get_intersection([-3, -2, -1, 0], [-1, 0, 1, 2]) == [-1, 0]


print("All tests passed!")
