#return the numbers in the file and dis regard all others creat a list of all the numbers 
numbers=[]
with open('error_sample.txt','r') as f:
    for line in f:
        try:
            number=int(line.strip())
            numbers.append(number)

            
        except Exception as e:
            print(f'this is not to be printed  {line}  ')

        

print(numbers)