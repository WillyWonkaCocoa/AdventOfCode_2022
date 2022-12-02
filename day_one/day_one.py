import sys
n = 3

if len(sys.argv) < 2:
    raise Exception("Missing input file!")
else:
    f = open(sys.argv[1], 'r')
    lines = f.readlines()
    total = 0
    highest = [] #make highest into n+1 sorted array for n highest calories

    for line in lines:
        if line.strip():
            total = total + int(line)
        else: #add n to sorted array, sort, then delete lowest one
            if len(highest) < n:
                highest.append(total)
            elif len(highest) == n:
                highest.append(total)
                highest.sort(reverse=True)
                highest = highest[:-1]
            total = 0
    
    print(f'The elf carrying the most calories is carrying {highest[0]} calories.')
    print(f'Highest {n} elfs are carrying {sum(highest)} calories in total.')
    f.close()
