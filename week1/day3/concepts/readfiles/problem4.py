#even line copy to new fiel even 
count=0
with open('largesample.txt','r') as f:
    with open('even.txt','w') as copyfile:
        for l in f:
            count+=1
            if (count %2)==0:

                copyfile.write(l)
