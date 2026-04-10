#return the number only from the file and find the sum of them 
numbers=[]
with open('error_sample.txt','r') as f:
    for line in f:
        try:
            number=int(line.strip())
            numbers.append(number)
        except Exception as e:
            print('error')

print(numbers)