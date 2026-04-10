#only print he lines that are having the word python 
import os


with open('sample.txt','r') as f:

    for line in f:
        if 'Python' in line:
            print(line)