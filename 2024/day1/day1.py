with open('data.txt') as infile:
    lines = infile.readlines()

lines = [l.strip() for l in lines]
set1 = [int(l[0]) for l in lines]
set2 = [int(l[-1]) for l in lines]

set1.sort()
set2.sort()
sum=[set2[i]-s1 for i,s1 in enumerate(set1)]

print(sum)
