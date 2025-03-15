import csv
# S ~ R^2 T ^2 / a^2
# S / S_sun  = R/R_sun^2 * T/T_sun^4 * a/a_earth^-2

temp_sun = 5800.0
mass_earth = 1/320

with open("/Users/maximetschopp/Documents/University/FS 2025/Scientific Computing/ScientificComputing/4 Nonsequential Data/exoplanet.eu_catalog.csv", 'r') as f:
    t = list ( csv.reader(f) )

    ranking = [] # of form 'similarity_metric' 'name' 'mass_relative' 'daylight_strength_relative'
    name_index = t[0].index('# name')
    mass_index = t[0].index('mass')
    star_radius_index = t[0].index('star_radius')
    semi_major_axis_index = t[0].index('semi_major_axis')
    star_teff_index = t[0].index('star_teff')

    for i in range (1, len(t)): # skip first row
        star_radius_ratio = t[i][star_radius_index]
        star_temp = t[i][star_teff_index]
        semi_major_axis_ratio = t[i][semi_major_axis_index]
        mass_planet = t[i][mass_index]
        if not star_radius_ratio or not star_temp or not semi_major_axis_ratio or not mass_planet:
            continue
        daylight_strength_relative = (
            (float(star_radius_ratio) ** 2) *
            ((float(star_temp) / temp_sun) ** 4) *
            (float(semi_major_axis_ratio) ** -2)
        )
        mass_relative = float(mass_planet) / mass_earth
        similarity_metric = (mass_relative ** 2 + daylight_strength_relative ** 2)** 0.5

        ranking.append( [similarity_metric, t[i][name_index], mass_relative, daylight_strength_relative] )
    ranking.sort(key=lambda x: abs(x[0] - 1))
    
    # Print top 10 closest matches
    print("=" * 20)
    print("Top 10 most Earth-like exoplanets:")
        # Print header with fixed spacing
    print(f"{'Similarity':<12} {'Name':<30} {'Mass':<15} {'Daylight Strength'}")

    # Print top 10 results with fixed column widths
    for row in ranking[:10]:
        print(f"{row[0]:<12.5f} {row[1]:<30} {row[2]:<15.3f} {row[3]:.3f}")
