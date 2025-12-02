with open('day1/data.txt') as infile:
    lines = infile.readlines()

lines = [l.strip() for l in lines]
dials = [(True if l[0]=='R' else False, int(l[1:])) for l in lines]

def dial(num, dial):

    oldnum = num
    add = dial[1] if dial[0] else 100*(dial[1]//100+1)-dial[1]
    num += add

    if dial[0]: 
        point_zero = num//100
    elif oldnum == 0 or dial[1]%100 < oldnum:
        point_zero = dial[1]//100
    else:
        point_zero = dial[1]//100 + 1

    num %= 100
    return num, point_zero

num = 50
password1 = 0
password2 = 0

for d in dials:
    num, point_zero = dial(num,d)

    # part 1
    if num == 0:
        password1 += 1
    # part 2
    password2 += point_zero
    
print(f"Part 1: {password1}, part 2: {password2}")