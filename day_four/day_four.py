import sys

partner_separator = ','
section_separator = '-'

if len(sys.argv) < 2:
    raise Exception("Missing input file!")
else:
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    counter = 0

    for line in lines:
        line.strip()
        first, second = line.split(partner_separator)
        first_begin, first_end = first.split(section_separator)
        second_begin, second_end = second.split(section_separator)
        
        first_begin = int(first_begin)
        first_end = int(first_end)
        second_begin = int(second_begin)
        second_end = int(second_end)
        
        if (first_end >= second_begin and first_begin <= second_end):
            counter += 1
        
    print(f'There are {counter} assignment pairs where ranges overlap.')
    f.close()




 

