with open('5 Scientific Graphics/Country_Code_to_Continent_Mapping.csv', 'r') as f:
    data = f.readlines()
    continent = {}
    non_countries = ['ARB', 'CEB', 'CSS', 'EAP', 'EAR', 'EAS', 'ECA',
    'ECS', 'EMU', 'EUU', 'FCS', 'HIC', 'HPC', 'IBD', 'IBT', 'IDA',
    'IDB', 'IDX', 'LAC', 'LCN', 'LDC', 'LIC', 'LMC', 'LMY', 'LTE',
    'MEA', 'MIC', 'MNA', 'NAC', 'OED', 'OSS', 'PRE', 'PSS', 'PST',
    'SAS', 'SSA', 'SSF', 'SST', 'TEA', 'TEC', 'TLA', 'TMN', 'TSA',
    'TSS', 'UMC', 'WLD']

    for line in data[1:]:
        line = line[:-1].split(',')
        if line[1] in non_countries:
            continue
        if line[2] not in continent:
            continent[line[2]] = [ line[1] ]
        else:
            continent[line[2]].append(line[1])
    print(continent)