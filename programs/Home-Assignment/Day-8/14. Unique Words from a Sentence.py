# 14.	Unique Words from a Sentence
# o	Ask user for a sentence
# o	Convert it into a set of unique words using split() and set()


sentence = input("Enter a sentence: ")

words = set(sentence.split())

print("Unique words in the sentence are:")
print(words)
