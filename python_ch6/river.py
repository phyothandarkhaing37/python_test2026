rivers = {
    'nile': 'egypt',
    'amazon': 'brazil',
    'mississippi': 'united states'
}

# 1. Print a sentence about each river
for river, country in rivers.items():
    print(f"The {river.title()} runs through {country.title()}.")

print("\nRivers included in the dictionary:")
# 2. Print the name of each river
for river in rivers.keys():
    print(river.title())

print("\nCountries included in the dictionary:")
# 3. Print the name of each country
for country in rivers.values():
    print(country.title())