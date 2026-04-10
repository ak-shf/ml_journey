# to check wether the file is empty or not


with open('empty.txt','r') as f:
    if len(f.read())==0:
        print('the file is empty ')
