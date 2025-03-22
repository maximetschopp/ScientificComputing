import csv

path = '/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/4 Nonsequential Data/geneticCode.txt'
with open(path, 'r') as f:
    table = list( csv.reader(f, delimiter=" ") )
    sorted_table = {}
    for i in range(len(table)):
        if table[i][1] not in sorted_table:
            sorted_table[table[i][1]] = []
        sorted_table[ table[i][1] ].append(table[i][0])

    print(sorted_table)
