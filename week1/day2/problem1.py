#get the word count and the count of each of the words 

s = "Python is simple, yet powerful and simple."

#we have many was to count the frequency in the sentence 

words=s.split(" ")
#count of words
print(len(words))
#1 using Counter 
from collections import Counter 

print(Counter(words))

#2 using list comprehension with count list.count(current word)

print({w:words.count(w) for w in set(words)})

#3 using countOf in the operatiors

import operator as op 

print({word : op.countOf(words,word) for word in words })

