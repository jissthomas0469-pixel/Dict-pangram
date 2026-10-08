l=[]
sentence= input('please enter your sentence').lower()
for i in sentence:
    if i.isalpha() and i not in l:
        l.append(i)


if len(l)==26:
    print('it is a panagram')
else:
    print('it is not a panagram')