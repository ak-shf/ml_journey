#retun the top n count words in the sentence 

sentence = "Python is powerful. Python is simple, and Python is open source."
import re

from collections import Counter

k=2

words=re.findall(r'\b\w+\b',sentence.lower())
print(words)

# counts={w:words.count(w) for w in words }
# print(counts)
# #order is based on the first apperence on the list 

counts=Counter(words).most_common(k)
print(counts)
#one liner way for the aboue thing 
print([w for w, _ in Counter(words).most_common(k)])

type_dir={w:c for w,c in Counter(words).items()}
# print(dir)
sort=sorted(type_dir.items(),key= lambda x:x[1], reverse=True)
print(sort[:k])







