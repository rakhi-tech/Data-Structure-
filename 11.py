


sentence = input("Enter a sentence: ")


words = sentence.split()


reversed_words = [word[::-1] for word in words]
result = " ".join(reversed_words)


print("Reversed sentence:", result)
