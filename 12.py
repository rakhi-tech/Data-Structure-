# Program to find longest and shortest word in a sentence


sentence = input("Enter a sentence: ")


words = sentence.split()
longest_word = max(words, key=len)
shortest_word = min(words, key=len)

print("Longest word:", longest_word)
print("Shortest word:", shortest_word)
