def length(word):
    return len(word)


words = ["apple", "banana", "cherry", "date"]
sorted_words = sorted(words, key=length)
print(sorted_words)
