places = ['Japan', 'Italy', 'Iceland', 'New Zealand', 'Egypt']

print("Original order:", places)

print("Alphabetical:", sorted(places))
print("Still original order:", places)

print("Reverse alphabetical:", sorted(places, reverse=True))
print("Still original order:", places)

places.reverse()
print("Reversed order:", places)

places.reverse()
print("Back to original order:", places)

places.sort()
print("Sorted alphabetically:", places)

places.sort(reverse=True)
print("Sorted reverse-alphabetically:", places)