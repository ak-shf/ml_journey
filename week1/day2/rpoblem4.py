items = [1, 2, 6,3, 2, 4, 1, 5]

#jsut return after deleting the duplecates and preserve the order

unique=set(items)
print(unique)
output=[]
for value in items:
    if value in unique:
        output.append(value)
        unique.remove(value)
print(output)


# the more compact way is to check is the value in set then dont add
uniq=set()
rodered=[value for value in items if not (value in uniq or uniq.add(value))]
print(rodered)