text = "aB!c"
shift = 1

#shift the given lette sequence to the nest shifter letter sequence like abc become bcd

for v in text:
    if not v.isalpha():
        print(v,end='')
        continue
    ch=chr((ord(v.lower())-ord('a')+shift)%26 +ord('a'))
    if v.isupper():
        ch=ch.upper()
    print(ch,end="")