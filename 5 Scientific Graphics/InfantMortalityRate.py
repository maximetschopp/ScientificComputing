import numpy as np
import matplotlib.pyplot as plt


with open ('API_SH.DYN.MORT_DS2_en_csv_v2_76288.csv', 'r') as f:
    data = f.readlines()[4:]

    indices = data[0].split('","')
    indices[0] = indices[0][1:]
    indices[-1] = indices[-1][:-2]

    country_code_continent_lookup = {'North America': ['ABW', 'ATG', 'BHS', 'BLZ', 'BMU', 'BRB', 'CAN', 'CRI', 'CUB', 'CUW', 'DMA', 'DOM', 'GRD', 'GRL', 'GTM', 'HND', 'HTI', 'JAM', 'KNA', 'LCA', 'MAF', 'MEX', 'NIC', 'PAN', 'PRI', 'SLV', 'SXM', 'TCA', 'TTO', 'USA', 'VCT'], 'Asia': ['AFG', 'ARE', 'ARM', 'AZE', 'BGD', 'BHR', 'BRN', 'BTN', 'CHN', 'CYP', 'GEO', 'HKG', 'IDN', 'IND', 'IRN', 'IRQ', 'ISR', 'JOR', 'JPN', 'KAZ', 'KGZ', 'KHM', 'KOR', 'KWT', 'LAO', 'LBN', 'LKA', 'MAC', 'MDV', 'MMR', 'MNG', 'MYS', 'NPL', 'OMN', 'PAK', 'PHL', 'PRK', 'PSE', 'QAT', 'SAU', 'SGP', 'SYR', 'THA', 'TJK', 'TKM', 'TLS', 'TUR', 'UZB', 'VNM', 'YEM'], 'Africa': ['AGO', 'BDI', 'BEN', 'BFA', 'BWA', 'CAF', 'CIV', 'CMR', 'COD', 'COG', 'COM', 'CPV', 'DJI', 'DZA', 'EGY', 'ERI', 'ETH', 'GAB', 'GHA', 'GIN', 'GMB', 'GNB', 'GNQ', 'KEN', 'LBR', 'LBY', 'LSO', 'MAR', 'MDG', 'MLI', 'MOZ', 'MRT', 'MUS', 'MWI', 'NAM', 'NER', 'NGA', 'RWA', 'SDN', 'SEN', 'SLE', 'SOM', 'SSD', 'STP', 'SWZ', 'SYC', 'TCD', 'TGO', 'TUN', 'TZA', 'UGA', 'ZAF', 'ZMB', 'ZWE'], 'Europe': ['ALB', 'AND', 'AUT', 'BEL', 'BGR', 'BIH', 'BLR', 'CHE', 'CZE', 'DEU', 'DNK', 'ESP', 'EST', 'FIN', 'FRA', 'FRO', 'GBR', 'GRC', 'HRV', 'HUN', 'IRL', 'ISL', 'ITA', 'LIE', 'LTU', 'LUX', 'LVA', 'MCO', 'MDA', 'MKD', 'MLT', 'MNE', 'NLD', 'NOR', 'POL', 'PRT', 'ROU', 'RUS', 'SMR', 'SRB', 'SVK', 'SVN', 'SWE', 'UKR'], 'South America': ['ARG', 'BOL', 'BRA', 'CHL', 'COL', 'ECU', 'GUY', 'PER', 'PRY', 'SUR', 'URY', 'VEN'], 'Oceania': ['ASM', 'AUS', 'FJI', 'FSM', 'GUM', 'KIR', 'MHL', 'MNP', 'NCL', 'NRU', 'NZL', 'PLW', 'PNG', 'SLB', 'TON', 'TUV', 'VUT', 'WSM']}

    continent_raw = {
        'North America': [ np.zeros(2023-1960), np.zeros(2023-1960) ],
        'Asia': [ np.zeros(2023-1960), np.zeros(2023-1960) ],
        'Africa': [ np.zeros(2023-1960), np.zeros(2023-1960) ],
        'Europe': [ np.zeros(2023-1960), np.zeros(2023-1960) ],
        'South America': [ np.zeros(2023-1960), np.zeros(2023-1960) ],
        'Oceania': [ np.zeros(2023-1960), np.zeros(2023-1960) ]
    }
    # average infant mortality rate per continent for each year
    start = 1970
    end = 2023
    continent_processed = {
        'North America': np.zeros(2023-1960),
        'Asia': np.zeros(2023-1960),
        'Africa': np.zeros(2023-1960),
        'Europe': np.zeros(2023-1960),
        'South America': np.zeros(2023-1960),
        'Oceania': np.zeros(2023-1960)
    }

    for i in range(2, len(data)): # skip the indices and blank line
        line = data[i].split('","')
        line[-1] = line[-1][:-2]

        country_code = line[1]
        continent = None
        for key in country_code_continent_lookup:
            if country_code in country_code_continent_lookup[key]:
                continent = key
                break
        
        if not continent:
            continue

        # print(country_code, continent)

        for year in range(start, end):
            # Im lazy so we are gonna do scuffed version
            # every year isnt necessarily in the data for each country
            # therefore continent_raw is of form [ rate per year, number of countries per year]
            if line[indices.index(str(year))]:
                continent_raw[continent][0][year-start] += float(line[indices.index(str(year))])
                continent_raw[continent][1][year-start] += 1


        # now average the rates
    for key in continent_raw:
        for i in range(len(continent_raw[key][0])):
            if continent_raw[key][1][i] != 0:
                continent_processed[key][i] = continent_raw[key][0][i] / continent_raw[key][1][i]
            else:
                continent_processed[key][i] = 0

    # now plot with animation where we open and close the plot for every time step
    # and start with only plotting 1960, then 1960-1961, then 1960-1962, etc.
    first_time_step = 200 / 1000 # ms -> s
    time_step = 40 / 1000 # ms -> s
    for (i, year) in enumerate(range(start, end)):
        plt.plot(range(start, year), continent_processed['North America'][:i], label='North America')
        plt.plot(range(start , year), continent_processed['Asia'][:i], label='Asia')
        plt.plot(range(start , year), continent_processed['Africa'][:i], label='Africa')
        plt.plot(range(start , year), continent_processed['Europe'][:i], label='Europe')
        plt.plot(range(start , year), continent_processed['South America'][:i], label='South America')
        plt.plot(range(start , year), continent_processed['Oceania'][:i ], label='Oceania')
        plt.legend()
        plt.title('Infant Mortality Rate by Continent from 1960-2023')
        plt.xlabel('Year')
        plt.ylabel('Infant Mortality Rate')
        plt.show(block=False)
        plt.pause(first_time_step if i == 0 else time_step)
        plt.savefig(f'./InfantMortalityRate_{year}.png')
        plt.close()

    for key in continent_processed:
        plt.plot(range(start, end), continent_processed[key], label=key)
    plt.legend()
    plt.title('Infant Mortality Rate by Continent from 1960-2023')
    plt.xlabel('Year')
    plt.ylabel('Infant Mortality Rate')
    plt.show()