# Count Words in a Sentence
# Function count_words(sentence) returns total number of words in the input.

def count_word():
    count = 0
    sentence = "What is important is that what  and what is not, is not."
    words = sentence.split()  
    for word in words:
        
        if word == "is":
            count += 1
    print(f"is = {count}")

count_word()
