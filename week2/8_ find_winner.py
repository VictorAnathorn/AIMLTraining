from collections import defaultdict


def find_winner(votes):
    counts = defaultdict(int)
    winner = votes[0]
    max_vote = 0
    for vote in votes:
        counts[vote] += 1
        if counts[vote] > max_vote or (counts[vote] == max_vote and vote < winner):
            max_vote = counts[vote]
            winner = vote
    return winner

# Test cases


def test_find_winner():
    # Test case 1: One candidate receives the most votes
    assert find_winner(["sam", "john", "jamie", "sam"]) == "sam"

    # Test case 2: Tie, return lexicographically smaller name
    assert find_winner(["sam", "john", "sam", "john"]) == "john"

    # Additional test cases
    # All votes for one candidate
    assert find_winner(["alice"] * 100) == "alice"

    # No votes (empty list)
    assert find_winner([]) == None  # or appropriate default behavior

    # Tie with multiple candidates
    assert find_winner(["bob", "bob", "alice", "alice", "charlie"]) == "alice"

    # Case sensitivity (assuming case matters)
    assert find_winner(["Bob", "bob", "Alice", "alice"]) == "Alice"


print("All tests passed!")
