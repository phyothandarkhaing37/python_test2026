cities = ['Tokyo', 'Paris', 'New York', 'London', 'Sydney']

cities.append('Cairo')

cities.insert(1, 'Berlin')

del cities[0]

popped_city = cities.pop()

cities.remove('London')

print("Sorted:", sorted(cities))

cities.reverse()

cities.sort()

print("Number of cities:", len(cities))
print("Final List:", cities)