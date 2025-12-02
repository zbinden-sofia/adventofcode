with open('day2/data.txt') as infile:
    line = infile.readlines()

lines = line[0].strip().split(',')
id_ranges = [range(int(l.split('-')[0]),int(l.split('-')[1])+1) for l in lines]

def get_num_invalid_IDs(id_range):
    num_invalid = 0
    sum_invalid = 0
    first_id = id_range[0]
    last_id = id_range[-1]

    id = first_id
    while id <= last_id:
        idstring = str(id)

        if len(idstring)%2 == 0:
            # get number to check
            id_half = idstring[0:len(idstring)//2]
            to_check = int(id_half + id_half)

            # check if the number is in the range
            if first_id <= to_check <= last_id:
                    num_invalid += 1
                    sum_invalid += to_check
                
            # forward to number afterwards
            id = (int(id_half)+1)*pow(10,len(id_half))
            continue


        id += 1
        
    return num_invalid, sum_invalid

num_invalid_ids = 0
sum_invalid_ids = 0
for id_range in id_ranges:
    num, sum = get_num_invalid_IDs(id_range)

    num_invalid_ids += num
    sum_invalid_ids += sum

print(f"{num_invalid_ids} invalid IDs found, summed up as {sum_invalid_ids}")