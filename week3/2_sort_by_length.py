def sort_by_len(strings):
    return sorted(strings, key=len)


strings = ["appleeeee", "banana", "cherry", "date", "yo"]
sorted_strings = sort_by_len(strings)
print(sorted_strings)
