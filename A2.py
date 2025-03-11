def custom_sort(strings):
    return sorted(strings, key=lambda x: (len(x), x.lower()))


words = ["apple", "banana", "cherry", "date", "fig", "grape","eat"]
sorted_words = custom_sort(words)
print(sorted_words)
