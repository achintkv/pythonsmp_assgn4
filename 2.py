mystr=(input('Enter the string -'))
a=[]
for i in range(0,len(mystr),3):
    a.append(mystr[i:i+3])
b=set(a)
c=list(b)
print('The list of separated strings -',c)
d=''.join(c)
print('Required joined string -',d)
