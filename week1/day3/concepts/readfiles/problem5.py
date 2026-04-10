# calculate the number of words and the number of lines in the file
import re
finallist=[]
count=0
with open('largesample.txt','r') as f:
    
    line=f.readlines()

context="".join(line)

    
content=re.findall(r'\b[a-zA-Z]+\b',context)

print(line)
print(context)
   
print(f'the no of lines are {len(line)}')
print(f'the no of words are {len(content)}')