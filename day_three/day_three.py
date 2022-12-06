import sys

lower_case_offset = 96
upper_case_offset = 38

if len(sys.argv) < 2:
    raise Exception("Missing input file!")
else:
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    sum = 0
    
    for line in lines:
        line = line.strip()
        
        # 1. split up rucksack
        size_of_each_sack = len(line) // 2
        print(size_of_each_sack)
        first_rucksack = line[:size_of_each_sack]
        second_rucksack = line[size_of_each_sack:]
        print("first rucksack " + first_rucksack)
        print("second rucksack " + second_rucksack)
        
        # 2. search thru rucksack
        rucksack_dict = {}
        for n in first_rucksack:
            rucksack_dict[n] = 1
        for m in second_rucksack:
            if m in rucksack_dict.keys():
                print("The item found in both rucksacks is " + m)
                priority = ord(m)
                if priority >= 65 and priority <= 90:
                    priority -= upper_case_offset
                else:
                    priority -= lower_case_offset
                rucksack_dict.pop(m, None)
                print("The item found in both rucksacks is " + m + " with a value of " + str(priority))
                sum += priority
    
    print(f'The sum of the priorties of items that appear in both compartments is {sum}.')
    f.close()
