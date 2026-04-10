# count the number of lines 
count=0
with open('largesample.txt','r') as f:
    for _ in f:
        count+=1

print(count)