import sys

lower_case_offset = 96
upper_case_offset = 38
group_size = 3

if len(sys.argv) < 2:
    raise Exception("Missing input file!")
else:
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    sum = 0
    counter = 0
    rucksack_dict = {}
    
    for line in lines:
        line = line.strip()
        #keep track of group of three
        counter += 1
        
        if counter == 1:
        # add all contents to rucksack_dict
            for n in line:
                rucksack_dict[n] = 1

        elif counter > 1 :
        # compare against rucksack_dict
            temp_rucksack_dict = {}
            for m in line:
                if m in rucksack_dict.keys():
                    temp_rucksack_dict[m] = 1
            rucksack_dict = temp_rucksack_dict
            
            if counter == group_size:
                #calculate and add value
                for item in rucksack_dict.keys():
                    print("The item found in all " + str(group_size) + " rucksacks is " + item)
                    priority = ord(item)
                    if priority >= 65 and priority <= 90:
                        priority -= upper_case_offset
                    else:
                        priority -= lower_case_offset
                    print("The item found in both rucksacks is " + item + " with a value of " + str(priority))
                    sum += priority
                
                
                #reset counter, rucksack_dict
                counter = 0
                rucksack_dict = {}
    
    print(f'The sum of the priorties of items that appear in all {group_size} elf\'s racksack of each group is {sum}.')
    f.close()
