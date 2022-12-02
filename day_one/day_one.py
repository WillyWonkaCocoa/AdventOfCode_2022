import sys

if len(sys.argv) < 2:
    raise Exception("Missing input file!")
else:
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    sum = 0
    highest = [] 

    for line in lines:
        if line.strip():
            sum = sum + int(line)
        else:
            if sum > highest:
                highest = sum
            sum = 0
            
    print(f'Highest calories is {highest}.')
    f.close()
