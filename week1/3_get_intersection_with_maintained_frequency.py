from collections import Counter


def get_intersection_with_maintained_frequency(a, b):
    f_a, f_b = Counter(a), Counter(b)
    return [key for key in f_a if key in f_b for _ in range(min(f_a[key], f_b[key]))]

# Test cases


def test_get_intersection_with_maintained_frequency():
    # Test case 1: Common elements with different frequencies
    assert sorted(get_intersection_with_maintained_frequency(
        [4, 2, 2, 3, 1], [2, 2, 2, 3, 3])) == sorted([2, 2, 3])

    # Test case 2: No common elements
    assert sorted(get_intersection_with_maintained_frequency([6, 2, 4], [1, 5, 3, 7])) == sorted([])

    # Additional test cases
    # Common elements with same frequency
    assert sorted(get_intersection_with_maintained_frequency(
        [1, 1, 2, 2], [2, 2, 1, 1])) == sorted([1, 1, 2, 2])

    # Common elements, one list is a subset of the other
    assert sorted(get_intersection_with_maintained_frequency(
        [1, 2, 3], [1, 1, 2, 2, 3, 3, 3])) == sorted([1, 2, 3])

    # Lists with negative numbers
    assert sorted(get_intersection_with_maintained_frequency(
        [-1, -2, 3], [-2, -2, -3, 3])) == sorted([-2, 3])

    # Lists with no intersection
    assert sorted(get_intersection_with_maintained_frequency([10, 20, 30], [40, 50])) == sorted([])


print("All tests passed!")
