with open('day2/data.txt') as infile:
    line = infile.readlines()

lines = line[0].strip().split(',')
id_ranges = [range(int(l.split('-')[0]),int(l.split('-')[1])+1) for l in lines]

def get_all_dividers(num):
    dividers = []

    for i in range(2,num+1):
        if num % i == 0:
            dividers.append(i)

    return dividers

def get_num_invalid_IDs(id_range):
    sum_invalid = 0
    first_id = id_range[0]
    last_id = id_range[-1]
    invalid_ids = []

    id = first_id
    while id <= last_id:
        idstring = str(id)

        for divider in get_all_dividers(len(idstring)):
            # get number to check
            id_part = idstring[0:len(idstring)//divider]
            to_check = int(id_part * divider)

            # check if the number is in the range
            if first_id <= to_check <= last_id:
                if to_check not in invalid_ids:
                    sum_invalid += to_check
                    invalid_ids.append(to_check)

        id += 1
        
    return sum_invalid

sum_invalid_ids = 0
for id_range in id_ranges:
    sum_invalid_ids += get_num_invalid_IDs(id_range)

print(f"There are invalid IDs found, summed up to {sum_invalid_ids}")
