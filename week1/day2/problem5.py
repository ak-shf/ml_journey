words = ["cat", "dog", "apple", "bat", "ball", "hi"]

#return a dic with key the length of the word and the value the words with that length 

word_len={}

for value in words:
    if not len(value) in word_len:
        word_len[len(value)]=[]
    word_len[len(value)].append(value)
print(word_len)
