# Count Words in a Sentence
# Function count_words(sentence) returns total number of words in the input.

def count_word():
    count = 0
    sentence = "What is important is that what is, is, and what is not, is not."
    for i in sentence : 
        if i == "is" :
            count = count + 1
    print(f" is = {count} ")
count_word()
            

